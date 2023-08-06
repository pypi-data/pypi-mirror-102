#stanBra(size, index)   :   bra of given 'size' with 1 at index position

import numpy as np

__all__ = ['stanBra']

def stanBra(size, index):
    r"""Takes size and index and returns a row vector of the given size and 1 
    at the given index
    
    Parameters
    ----------
    size : int
    
    index : int
    
    Returns
    ----------
    vec : numpy.ndarray 
          shape (1,size) with 1 at 'index' position 0 elsewhere
    """
    vec = np.eye(1,size,index) 
    return vec

