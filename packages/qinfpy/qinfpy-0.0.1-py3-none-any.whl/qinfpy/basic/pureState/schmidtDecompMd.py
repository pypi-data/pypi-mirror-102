#schmidtDecomp(...)   :   Gives Schmidt decomposition over spaces of given dimension

import numpy as np

__all__ = ['schmidtDecomp']

def schmidtDecomp(psi,da,db):
    r"""Takes an input a vector, and dimensions :math:'da' and :math:'db'
    of the two spaces over whose tensor product the vector is defined.
    Returns the Schmidt decomposition of the vector.
   
    Parameters
    ----------
    psi : numpy.ndarray
          1-d complex vector
    
    da : int
         Dimension of space 1

    db : int
         Dimension of space 2
        
    Returns
    ----------
    comp : numpy.ndarray
           A vector with components that are the Schmidt coefficients of the 
           input psi

    U : numpy.ndarray
        Matrix with :math:'k^{th}' Schmidt vector on space 1 written as U[:,k]

    V : numpy.ndarray
        Matrix with :math:'k^{th}' Schmidt vector on space 2 written as V[:,k]
    """
    try:
        mat = psi.reshape(da,db)
    except:
        raise ValueError('Shape of psi and da*db do not seem compatible')
        return None
    U, D, V = np.linalg.svd(mat, full_matrices=True)
    return (D,U,V.T)

