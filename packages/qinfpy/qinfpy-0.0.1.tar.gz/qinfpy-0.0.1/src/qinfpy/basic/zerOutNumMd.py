#zerOutNum(num)          :   Removes small parts of a number

import copy
import numpy as np

__all__ = ['zerOutNum']

def zerOutNum(num, tol = 1e-15):
    r"""Takes as input a number and tolerance, copies it, in this copy 
    nulls out real and complex parts smaller than the tolerance, and returns
    the copy.
    
    Parameters
    ----------
    num : complex

    tol : float
          Optional, 1e-15 by default
    
    Returns
    ----------
    val : same type as num
    """
    val = copy.deepcopy(num)
    if (np.abs(val.real) < tol):
        val = (val - val.conj())/2.
    if (np.abs(val.imag) < tol):
        val = (val + val.conj())/2.
    return val

