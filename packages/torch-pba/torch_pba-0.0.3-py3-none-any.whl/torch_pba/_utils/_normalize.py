

import numpy as np


def row_sum_normalize(A: np.ndarray) -> np.ndarray:
    
    """
    Parameters
    ----------
    A: np.ndarray
    
    Returns
    -------
    A_norm: np.ndarray
    """

    s = np.sum(A, axis=1)
    X, Y = np.meshgrid(s, s)
    return A / Y


def min_max_norm(a):
    return (a - a.min()) / (a.max() - a.min())