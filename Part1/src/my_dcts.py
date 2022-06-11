import numpy as np
from matplotlib import pyplot as plt
from compute_D import compute_D

def my_dct1(f_vect):
    """executes 1-dimensional DCT

    Args:
        f_vect (array): 1-dimensional array of size N

    Returns:
        c_vect (array): result of DCT1
    """
    
    N = len(f_vect)
    D = compute_D(N)
    c_vect = np.inner(D, f_vect)

    return c_vect

def my_dct2(f_mat):
    """executes 2-dimensional DCT

    Args:
        f_mat (double matrix): square matrix of size N

    Returns:
        c_mat (double matrix): result of DCT2
    """

    N = len(f_mat)      #number of rows and columns (since it's a square matrix)
    D = compute_D(N)
    c_mat = f_mat

    # DCT1 for columns
    for j in range(N):
        c_mat[:,j] = np.dot(D, c_mat[:,j])

    # DCT1 for rows
    for j in range(N):
        c_mat[j,:] = np.transpose(np.dot(D, np.transpose(c_mat[j,:])))

    return c_mat

def my_idct1(c_vect):
    """executes 1-dimensional inverse-DCT

    Args:
        f_vect (array): 1-dimensional array of size N

    Returns:
        c_vect (array): result of i-DCT1
    """

    N = len(c_vect)
    D = compute_D(N)
    f_vect = np.transpose(D)*c_vect

    return f_vect

def my_idct2(c_mat):
    """executes 2-dimensional inverse-DCT

    Args:
        f_mat (double matrix): square matrix of size N

    Returns:
        c_mat (double matrix): result of i-DCT2
    """

    N = len(c_mat)      #number of rows and columns (since it's a square matrix)
    D = compute_D(N)
    f_mat = c_mat

    # iDCT1 for columns
    for j in range(N):
        f_mat[:,j] = np.dot(np.transpose(D), f_mat[:,j])

    # iDCT1 for rows
    for j in range(N):
        f_mat[j,:] = np.transpose(np.dot(np.transpose(D), np.transpose(f_mat[j,:])))

    return f_mat
