import jax
from jax import numpy as np
from typing import Any, Optional, Tuple, Callable

def get_cg_fn(loss_and_grad_fn, hess_fn, l2=0.0):
    """Return standard conjugate gradient function, using lstsq to solve the linear system in case of ill-conditioning.

    Args:
        grad_fn: function returning loss and gradient.
        hess_fn: Hessian function.
        l2: L2 regularization strength.

    Returns:
        function: conjugate gradient function.
    """
    def cg_fn(params, *args):
        """Conjugate gradient function using lstsq to solve the linear system in case of ill-conditioning.

        Args:
            params: model parameters.
            *args: arguments to pass to loss and gradient function.

        Returns:
            tuple: loss, conjugate gradient, gradient norm.
        """
        loss, grad = loss_and_grad_fn(params, *args) 
        hess = hess_fn(params, *args)
        loss += 0.5 * l2 * np.sum(params ** 2)
        grad += l2 * params
        hess += l2 * np.eye(hess.shape[0])
        return np.mean(loss), jax.vmap(np.linalg.lstsq, in_axes=(0, 0))(hess, grad)[0], np.max(np.linalg.norm(grad, axis=-1))
    return cg_fn

def clip_inv_prod(eps, grad, u, v):
    """Clip eigenvalues and compute inverse product.
    
    Args:
        eps: clipping values.
        grad: gradient.
        u: eigenvalues.
        v: eigenvectors.
        
    Returns:
        np.ndarray: inverse product.
    """
    inv_hess = v @ np.diag(1 / np.maximum(u, eps)) @ v.T
    next_cg = inv_hess @ grad
    return next_cg

eigh =  jax.jit(np.linalg.eigh)
clip_inv_prod = jax.jit(jax.vmap(clip_inv_prod, in_axes=(0, None, None, None)))

def get_clipped_cg_fn(loss_fn, grad_fn, hess_fn, start_clip=1e-1, stop_clip=1e-4, num_clip=10, l2=0.0):
    """Return conjugate gradient function with eigenvalue clipping in case of ill-conditioning.
    Eigenvalues are clipped between start_clip and stop_clip, with num_clip values in between,
    with the clipped inverse product computed using the eigendecomposition of the Hessian.
    The conjugate gradient is then computed as the minimum of the clipped inverse products and the
    standard conjugate gradient.

    Args:
        loss_fn: loss function.
        grad_fn: gradient function.
        hess_fn: Hessian function.
        start_clip: starting clipping value.
        stop_clip: stopping clipping value.
        num_clip: number of clipping values.
        l2: L2 regularization strength.

    Returns:
        function: conjugate gradient function.
    """

    # compute clipping values
    eps = np.logspace(
        np.log(start_clip), np.log(stop_clip), num_clip, base=np.exp(1)
    )

    # define vectorizing helper functions
    def cp(params, grad, hess):
        """Compute conjugate gradient using clipped inverse product.
        
        Args:
            params: model parameters.
            grad: gradient.
            hess: Hessian.
            
        Returns:
            tuple: gradient, Hessian, updated parameters, conjugate gradient.
        """
        grad += l2 * params
        hess += l2 * np.eye(hess.shape[0])
        u, v = eigh(hess)
        cg = clip_inv_prod(eps, grad, u, v).T
        return grad, hess, params[:, None] - cg, cg
    
    def gl(losses, cg, params, grad):
        """Compute loss, conjugate gradient and gradient norm.

        Args:
            losses: losses.
            cg: conjugate gradient.
            params: model parameters.
            grad: gradient.

        Returns:
            tuple: losses, conjugate gradient, gradient norm.
        """
        min_idx = np.argmin(losses + 0.5 * l2 * np.sum((params[:, None] - cg) ** 2, axis=0), axis=0)
        return losses[min_idx], cg[:, min_idx], np.linalg.norm(grad)

    # vectorize helper functions
    cp = jax.jit(jax.vmap(cp, in_axes=(0, 0, 0)))
    gl = jax.jit(jax.vmap(gl, in_axes=(0, 0, 0, 0)))

    def cg_fn(params, *args):
        """Conjugate gradient function using clipped inverse product.

        Args:
            params: model parameters.
            *args: arguments to pass to loss and gradient function.

        Returns:
            tuple: loss, conjugate gradient, gradient norm.
        """
        _, grad = grad_fn(params, *args) 
        hess = hess_fn(params, *args)
        grad, hess, updated_params, cg = cp(params, grad, hess)
        losses = loss_fn(updated_params, *args) 
        losses, cg, grad_norm = gl(losses, cg, params, grad)
        return np.mean(losses), cg, np.max(grad_norm)
    return cg_fn


def fit(
        loss_fn: Callable, 
        model_fn: Callable,
        model_params: dict, 
        group_data: Tuple[dict],
        lr: Optional[float] = 1.0,
        maxit: Optional[int] = 1_000, 
        tol: Optional[float] = 1e-8, 
        verbose: Optional[int] = 0, 
        print_every: Optional[int] = 50, 
        save_every: Optional[int] = 50,
        save_dir: Optional[str] = None,
        mapped_loss_and_dir_fn = None,
        group_weights=None,
        keep_history=False
) -> Tuple[dict, float]:
    """Fit a model to data using directional descent with the given loss and direction functions.

    Args:
        loss_fn: loss function.
        model_fn: model function.
        model_params: model parameters.
        group_data: tuple of group covariates, group outcomes and group number of observations.
        maxit: maximum number of iterations.
        tol: tolerance for convergence.
        verbose: verbosity level (0: silent, 1: standard prints, 2: debug prints).
        print_every: print every n iterations.
        save_every: save model every n iterations.
        save_dir: directory to save model.
        lr: learning rate.
        mapped_loss_and_dir_fn: mapped loss and direction function, if None, will be compiled from loss function.
        group_weights: weights for each group.
        keep_history: whether to keep history of model parameters, loss and gradient norm.

    Returns:
        tuple: model parameters, gradient norm.
    """
    if mapped_loss_and_dir_fn is None:
        from elrpy.losses import get_wrapped_loss
        from elrpy.utils import get_mean_fn, get_mapped_fn
        print("Gradient functions not provided, these will be recompiled...")
        num_groups = len(group_data[0])
        loss_fn = get_wrapped_loss(loss_fn, model_fn, num_groups)
        if group_weights is None:
            mapped_loss_fn = get_mapped_fn(jax.jit(jax.vmap(loss_fn, in_axes=(0, None, None, None))))
            grad_fn = jax.jit(jax.vmap(jax.value_and_grad(get_mean_fn(loss_fn)), in_axes=(0, None, None, None)))
            hess_fn = jax.jit(jax.vmap(jax.hessian(get_mean_fn(loss_fn)), in_axes=(0, None, None, None)))
        else:
            mapped_loss_fn = get_mapped_fn(jax.jit(jax.vmap(loss_fn, in_axes=(0, None, None, None, 0))))
            grad_fn = jax.jit(jax.vmap(jax.value_and_grad(get_mean_fn(loss_fn)), in_axes=(0, None, None, None, 0)))
            hess_fn = jax.jit(jax.vmap(jax.hessian(get_mean_fn(loss_fn)), in_axes=(0, None, None, None, 0)))
        mapped_loss_and_grad_fn = get_mapped_fn(grad_fn)
        mapped_hess_fn = get_mapped_fn(hess_fn)
        mapped_loss_and_dir_fn = get_clipped_cg_fn(mapped_loss_fn, mapped_loss_and_grad_fn, mapped_hess_fn)

    if group_weights is not None:
        group_data = (group_data[0], group_data[1], group_data[2], group_weights)

    if keep_history:
        history = []

    for i in range(maxit):
        out = mapped_loss_and_dir_fn(model_params, group_data)
        if len(out) == 2:
            loss, grad = out
            grad_norm = np.linalg.norm(grad, axis=-1)
        elif len(out) == 3:
            loss, grad, grad_norm = out
        else:
            raise ValueError("Unexpected number of outputs from mapped loss and gradient function.")

        if np.any(np.isnan(grad)):
            print("NaN gradient update, aborting...")
            break
        
        if i % print_every == 0 and verbose == 2:
            print(i, "\t", loss, "\t", grad_norm)
        if np.all(grad_norm < tol) and verbose > 0:
            print("Converged!")
            if verbose == 2:
                print(i, loss, grad_norm)
            break

        model_params -= (grad_norm >= tol) * lr * grad
        if keep_history:
            history.append((model_params, loss, grad_norm))
        if i % save_every == 0 and save_dir is not None:
            np.savez(f"{save_dir}/model.npz", model_params=model_params, grad_norm=grad_norm, i=i)

    if grad_norm > tol and verbose > 0:
        print(f"Failed to converge, gradient norm is {grad_norm}.")
    if save_dir is not None:
        np.savez(f"{save_dir}/model.npz", model_params=model_params, grad_norm=grad_norm, i=i)
    
    return (model_params, grad_norm, history) if keep_history else (model_params, grad_norm)


