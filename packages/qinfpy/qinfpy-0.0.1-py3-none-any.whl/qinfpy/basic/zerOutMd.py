#zerOut(mt)             :   Removes small entries in array

import copy
import numpy as np

__all__ = ['zerOut']

def zerOut(array, tol = 1e-15):
    r"""Takes as input an array and tolerance, copies it, in this copy, 
    nulls out real and complex part of each entry smaller than the tolerance,
    returns the copy.

    Parameters
    ----------
    array : numpy.ndarray

    tol : float
          Optional, 1e-15 by default
    
    Returns
    ----------
    arr : numpy.ndarray
          Identical to input array, except each entry smaller than tol is set
          to zero
    """
    arr = copy.deepcopy(array)
    for index, val in np.ndenumerate(arr):
        if (np.abs(val.real) < tol):
            arr[index] = (arr[index] - arr[index].conj())/2.
        if (np.abs(val.imag) < tol):
            arr[index] = (arr[index] + arr[index].conj())/2.
    return arr

