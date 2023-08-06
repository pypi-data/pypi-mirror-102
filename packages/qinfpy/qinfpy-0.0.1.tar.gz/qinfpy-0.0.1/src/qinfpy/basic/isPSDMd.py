#isPSD(mt)              :   Checks whether matrix is PSD or not

import numpy as np

__all__ = ['isPSD']

def isPSD(mt, tol = 1e-12, flag = False):
    r"""Takes a matrix, returns True if is Positive Semi-definite, otherwise
    returns False

    Parameters
    ----------
    mt : numpy.ndarray

    tol : float
          Optional, default value 1e-12

    flag : bool
           Optional, Returns eigenvalues and of mt if True

    Returns
    ----------
    When flag is False, returns pos, else returns (pos, val, vec)

    pos : bool
          True if mt is positive semi-definite up to some numerical tolerance; 
          False otherwise

    val : numpy.ndarray
          Eigenvalues of mt

    vec : numpy.ndarray
          Eigenvectors of mt

    """
    #Square Matrix
    (row, col) = np.shape(mt)
    sqr = row == col
    if not sqr:
        return False

    #Hermitian
    mtDag = mt.conj().T
    diff = mt - mtDag
    herm = np.linalg.norm(diff) < 10*tol
    if not herm:
        return False

    #Positivity
    mt2 = (mt + mt.conj().T)/2.
    val, vec = np.linalg.eigh(mt2)
    pos = all(val.real > -tol) & all(val.imag > -tol)
    
    if flag:
        return (pos, val, vec)
    else:
        return pos

