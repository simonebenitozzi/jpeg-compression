import numpy as np
np.set_printoptions(linewidth=200)

from scipy.fftpack import dctn, dct
from my_dcts import my_dct2

test_vector = np.array([231, 32, 233, 161, 24, 71, 140, 245])
test_matrix = np.array([[231, 32, 233, 161, 24, 71, 140, 245], 
                        [247, 40, 248, 245, 124, 204, 36, 107],
                        [234, 202, 245, 167, 9, 217, 239, 173],
                        [193, 190, 100, 167, 43, 180, 8, 70],
                        [11, 24, 210, 177, 81, 243, 8, 112],
                        [97, 195, 203, 47, 125, 114, 165, 181],
                        [193, 70, 174, 167, 41, 30, 127, 245],
                        [87, 149, 57, 192, 65, 129, 178, 228]
                        ]).astype(np.float32)

expected_dct = np.array([4.01e+02, 6.60e+00, 1.09e+02, -1.12e+02, 6.54e+01, 1.21e+02, 1.16e+02, 2.88e+01])

print(dct(test_vector, norm="ortho") / expected_dct) # Expected all ~1
print(dctn(test_matrix.copy(), norm="ortho") / my_dct2(test_matrix.copy())) # Expected all ~1
