#doLinComb(...)         :   Takes array of numbers and matrices, constructs linear combination

import numpy as np

__all__ = ['doLinComb']

def doLinComb(num, mats):
    r"""Takes in a 1-d numpy.ndarray of numbers, and a list of matrices
    and returns a linear combination of the matrices.
    
    Parameters
    ----------
    num : numpy.ndarray

    mats : A list of numpy.ndarrays

    Returns
    ----------
    rho : numpy.ndarray
          Multiplies each number in num with corresponding matrix in mats and
          constructs a linear combination
    """
    if (len(num) != len(mats)):
        raise ValueError('Length of number vector and number of matrices unequal')
        
    (da, da) = mats[0].shape
    rho = 1j*np.zeros(shape = (da, da))
    for i in xrange(len(num)):
        rho += mats[i]*num[i]
    return rho

