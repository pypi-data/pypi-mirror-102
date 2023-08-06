#tenProdSelf(mt,k)      :   Tensor product of array with itself k times

from .tenProdMd import tenProd

__all__ = ['tenProdSelf']

def tenProdSelf(mt,k):
    r"""Takes as input a numpy.ndarray mt and an integer k, returns
    the tensor product of the array with itself performed k times
    
    Parameters
    ----------
    mt : numpy.ndarray
    
    k : int
        
    Returns
    ----------
    mtTen : numpy.ndarray
            tensor product of mt with itself k times
    """
    if (k == 1):
        mtTen = mt
    
    else:
        mtTen = tenProd(mt,tenProdSelf(mt,k-1))
 
    return mtTen

