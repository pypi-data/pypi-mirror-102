#indexToKet(i,j,d1,d2)  :   Index (i,j) to ket |ij>

import numpy as np

__all__ = ['indexToKet']

def indexToKet(i,j,d1,d2):
    r""" Takes as input indices (i,j) that represent a ket |ij> over a 
    d1 (tensor) d2 dimensional Hilbert space and returns a 1-d numpy.ndarray 
    representing this ket
    
    Parameters
    ----------
    i  : int 
         state in space 1
    
    j  : int 
         state in space 2
    
    d1 : int 
         dimension of space 1
    
    d2 : int
         dimension of space 2
    
    Returns
    ----------
    vec : numpy.ndarray
          shape (1, d1*d2) vector representing |ij>
    """
    index = d2*i + j
    dim = d1*d2
    vec = np.eye(1,dim,index) 
    
    return vec

