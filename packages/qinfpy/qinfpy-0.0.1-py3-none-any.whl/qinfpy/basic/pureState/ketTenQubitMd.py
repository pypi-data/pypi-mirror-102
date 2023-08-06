#ketTenQubit(i,n)       :   n-qubit state with |1> at i-th tensor and |0> elswhere

import numpy as np

from ..tenProdSelfMd import tenProdSelf
from ..tenProdMd import tenProd

__all__ = ['ketTenQubit']

def ketTenQubit(i,n):
    r"""Takes as input an integer representing a position 'i'
    and another integer representing the number of tensor products 'n'.
    Returns an n-qubit state(numpy.ndarray of length :math:'2^n') with i-th 
    qubit |1> and rest |0>.
    
    Parameters
    ----------
    i : int
        index where ket should be |1>

    n : int
        the number of tensor products
        
    Returns
    ----------
    vec : numpy.ndarray
          A 1-d numpy.ndarray representing an n-qubit state
    
    Notes
    ----------
    The input argument 'ten' should be greater than 1
    """
    
    err1 = 'position of qubit greater or equal to tensor products in ketTenQubit'

    if (i >= n):
        raise ValueError(err1)
    
    zero = np.array([1.,0.])
    one = np.array([0.,1.])
    
    if (i == 0):
        block1 = one
        block2 = tenProdSelf(zero, n-1)

    elif (i == n - 1):
        block1 = tenProdSelf(zero, n-1)
        block2 = one
    
    else:
        block1 = ketTenQubit(i,i+1)
        block2 = tenProdSelf(zero,n-i-1)
    
    vec = tenProd(block1, block2)
    return vec

