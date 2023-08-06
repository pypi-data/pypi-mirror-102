#dualMat(mts)           :   Takes list of matrices, computes their dual.

import numpy as np

__all__ = ['dualMat']

def dualMat(mts, lid = False):
    r"""Takes as input a list of matrices, an optional argument stating if
        the matrices are linearly independent and returns a list of matrices
        dual (under Frobenius Norm) to the input list of matrices

    Parameters
    ----------
    mts : list of numpy.ndarrays
          A list of matrices
    
    lid : bool 
          Optional, False by default. If True assumes matrices are 
          linearly independent
    
    Returns
    ----------
    mts : list of numpy.ndarrays
          The dual matrices(under Frobenius Norm) to the set of input matrices. 
          If matrices are linearly independent, it uses regular inverse 
          otherwise uses(less numerically accurate) pseudo-inverse.
    """
    vc = []
    #Each matrix is a ket, place it as a bra making a row of vecRows matrix
    for mt in mts:
        (d,d) = mt.shape
        vcR = np.ndarray.flatten(mt).conj()
        vc += [np.array([vcR])]
    vecRows =  np.vstack(vc)
    #Construct matrix with dual vectors as its columns
    if lid:
        try:
            dualVecCols = np.linalg.inv(vecRows)
        except:
            raise Exception('Cannot find dual matrices')
    else:
        try:
            dualVecCols = np.linalg.pinv(vecRows)
        except:
            raise Exception('Cannot find dual matrices')

    (row, col) = dualVecCols.shape
    mts = []
    #Reshape the columns as matrices of same size as input
    for i in xrange(col):
        mt = dualVecCols[:,i].reshape(d,d)
        mts += [zerOut(mt, tol = 1e-15)]
    return mts

