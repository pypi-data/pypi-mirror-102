#getLog(mt)             :   Returns the natural log of the matrix.

import numpy as np
from .isPSDMd import isPSD

__all__ = ['getLog']

def getLog(M, eps=1e-15):
    r"""Takes as input a matrix M and returns the natural log of M.
    
    Parameters
    ----------
    M : numpy.ndarray
        2-d array representing a hermitian matrix
    
    eps : float
          Optional with defaul 1e-15, sets tolerance for the smallest eigenvalue
        
    Returns
    ----------
    lgMt : numpy.ndarray
           log of the input array
    
    Notes
    ----------
    Scales by eps, all eigenvalues between their actual value and 1.0, 
    if any of the eigenvalue is smaller than eps
    """
    try : 
        (psd, val, vec) = isPSD(M,eps,flag=True)
    except :
        raise ValueError('Input matrix is not square and hermitian')

    if psd == False:
        raise ValueError('Eigenvalues of input matrix not sufficiently positive')
    
    n = len(val)
    
    #If any of the eigenvalues is smaller than eps, then rescale the spectrum
    #to make all eigenvalues at least eps, this prevents log from complaining
    
    if np.any(val<eps):
        val = (1-eps)*val + eps*1. 
    
    lgMt = np.dot(np.log(val)*vec,vec.conj().T)
    return lgMt

