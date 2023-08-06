#isRightDim(mt,da,db)   :   Checks whether mt is square shape with dim = da.db

import numpy as np

__all__ = ['isRightDim']

def isRightDim(mt, da, db):
    r"""Given a numpy.ndarray and two integers da, db returns True if the numpy
    array has shape (d,d) where d = da*db, otherwise returns False.

    Parameters
    ----------
    mt : numpy.ndarray

    da : int

    db : int
    
    Returns
    ----------
    dimCheck : bool
               True if matrix is a da*db square matrix, False otherwise.
    """
    d = da*db
    dimCheck = np.shape(mt) == (d,d)
    return dimCheck    


