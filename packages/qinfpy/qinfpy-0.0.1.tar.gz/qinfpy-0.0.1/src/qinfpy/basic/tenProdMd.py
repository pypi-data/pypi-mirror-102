#tenProd(v1,v2)         :   Tensor product of two arrays 

import copy

__all__ = ['tenProd']

def tenProd(v1,v2):
    r"""Takes two arrays and returns their tensor product. The function
    just calls the Kronecker product from numpy.

    Parameters
    ----------
    v1 : numpy array
    
    v2 : numpy array
    
    Returns
    ----------
    mat : numpy array
          tensor product of the two inputs
    """
    mat = np.kron(v1,v2) 
    return mat

