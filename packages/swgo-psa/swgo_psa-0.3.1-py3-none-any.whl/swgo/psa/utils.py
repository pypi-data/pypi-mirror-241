import numpy as np
import functools

__all__ = ["wrap_1d_nn"]


def wrap_1d_nn(func):
    """
    Decorator to wrap `func` - which acts on 1-d arrays and two scalar arguments - such that it works for 2-d arrays
    and either scalar or 1-d arguments.
    """

    @functools.wraps(func)
    def wrapper(x, a, b, **kwargs):
        x = np.asarray(x)
        squeeze = x.ndim == 1
        x = np.atleast_2d(x)
        a = np.atleast_1d(a)
        b = np.atleast_1d(b)

        n = x.shape[0]
        if n > 0:
            if len(a) == 1:
                a = np.broadcast_to(a, n)
            if len(b) == 1:
                b = np.broadcast_to(b, n)

        outputs = np.empty(n, float)
        for i in range(n):
            outputs[i] = func(x[i], a[i], b[i], **kwargs)

        return np.squeeze(outputs) if squeeze else outputs

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__

    return wrapper
