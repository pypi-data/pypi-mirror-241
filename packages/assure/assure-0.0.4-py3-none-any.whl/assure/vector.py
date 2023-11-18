__all__ = [
    'vector',
    'vectors',
    'harmonize',
]

import numpy as np

def vector(o):
    if not hasattr(o, 'ndim'):
        raise TypeError
    if o.ndim != 1:
        o = o.squeeze()
    if o.ndim == 1:
        return o
    raise TypeError


def vectors(o):
    """
        vectors: plural vectors

        rank two arrays, of shape (n, N), for variable n and shared N.
    """
    if isinstance(o, (list, tuple)):
        return np.stack([vector(p) for p in o])
    if hasattr(o, 'ndim'):
        if o.ndim == 1:
            return o[None, ...]
        if o.ndim == 2:
            return o
        if o.ndim > 2:
            raise TypeError
    raise TypeError


def harmonize(*args):
    """
        a = np.arange(1024)
        b = np.arange(2048)
        c = np.arange(4096)
        d = np.arange(4097)

        [x.shape for x in harmonize(a,b,c)]
        [(1, 1024), (2, 1024), (4, 1024)]

        [x.shape for x in harmonize(a,b,c,d)]
        ValueError
    """
    dims = set(a.shape[-1] for a in args)
    dim = min(dims)
    return [a.ravel().reshape((-1, dim)) for a in args]

