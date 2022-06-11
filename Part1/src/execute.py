import numpy as np
np.set_printoptions(linewidth=200)

import pandas as pd
import time
import math

from my_dcts import my_dct2, my_idct2
from scipy.fftpack import dctn, idctn

def f(x, y):
    return np.sign(x-0.5) * np.sign(y-0.5)



times_df = pd.DataFrame(columns=["N", "my_dct2", "scipy_dct2", "my_idct2", "scipy_idct2"])

for N in [8, 16, 32, 64, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000]:

    ### --- DCT 2D --- ###

    f_mat = np.zeros((N, N))

    for j in range(1, N+1):
        for ell in range(1, N+1):    
            x_val = (2*j-1) / (2*N)
            y_val = (2*ell-1) / (2*N)
            f_mat[j-1, ell-1] = f(x_val, y_val)

    t = time.time()
    c_mat = my_dct2(np.copy(f_mat));
    my_dct2_time = time.time() - t

    t = time.time()
    c_mat_scipy = dctn(np.copy(f_mat), norm="ortho")
    scipy_dct2_time = time.time() - t

    ### --- inverse-DCT 2D --- ###

    param = 0.5

    c_mat_reduced = np.copy(c_mat)
    c_mat_reduced[math.ceil(N*param):, math.ceil(N*param):] = 0

    t = time.time()
    f_mat_reduced = my_idct2(c_mat_reduced)
    my_idct2_time = time.time() - t

    c_mat_scipy_reduced = np.copy(c_mat_scipy)
    c_mat_scipy_reduced[math.ceil(N*param):, math.ceil(N*param):] = 0

    t = time.time()
    f_mat_scipy_reduced = idctn(c_mat_scipy_reduced, norm="ortho")
    scipy_idct2_time = time.time() - t


    ### --- logging --- ###
    times_df.loc[len(times_df)] = [N, my_dct2_time, scipy_dct2_time, my_idct2_time, scipy_idct2_time]


print(times_df)
times_df.to_csv("data/times.csv", index=False)