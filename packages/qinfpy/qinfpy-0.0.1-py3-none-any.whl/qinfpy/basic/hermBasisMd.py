#hermBasis(n)           :   Takes integer n, returns n^2-1 traceless, Hermitian basis

import numpy as np

__all__ = ['hermBasis']

def __getW(j,n):
    r"""Takes as input 2 integers j, n (expects 1<= j <= n-1) and returns
    a diagonal operator constructed recursively. 
    Helper Function for hermBasis(n)
    
    Parameters
    ----------
    j : int
        index for diagonal operator
    
    n : int
        dimension of diagonal operator

    Returns
    ----------
    returns : numpy.ndarray
              A diagonal matrix operator, constructed recursively. It is the 
              w matrix of Sec. 2.3 in the 'Generalized Bloch Vector and the 
              Eigenvalues of a Density Matrix' paper by Ozols and Mancinska
    """
    if (j >= n-1):
        raise ValueError('Invalid indices')
    
    if (j == 0 ):
        mat = np.zeros(shape=(n,n))
        mat[0,0] = 1.
        mat[1,1] = -1.
        return mat
    else:
        mat = np.zeros(shape=(n,n))
        mat[j,j] = j+1.
        mat[j+1,j+1] = -(j+1.)
        m1 = __getW(j-1, n)*np.sqrt(j*(j+1)/2.)
        return (m1 + mat)*np.sqrt(2./((j+1.)*(j+2.))) 


def hermBasis(n):
    r"""Takes as input a integer n and generates n^2 - 1, traceless,
    hermitian, orthogonal, norm 2 matrices 
    
    Parameters
    ----------
    n : int
        Dimension of space

    Returns
    ----------
    basis : list of numpy.ndarrays
            A list of length n^2 - 1, traceless, hermitian, orthogonal, norm 2 
            basis operators. They are the :math:'\lambda' matrix of Sec. 2.3 
            in the 'Generalized Bloch Vector and the Eigenvalues of a 
            Density Matrix' paper by Ozols and Mancinska
    """
    basis = []
    for i in xrange(0, n-1):
        basis += [__getW(i,n)]
    for j in xrange(0,n-1):
        for k in xrange(j+1,n):
            mat = np.zeros(shape=(n,n))
            mat[k,j] = 1.
            u = mat + mat.T
            v = 1j*(mat - mat.T)
            basis += [u]
            basis += [v]
    return basis
