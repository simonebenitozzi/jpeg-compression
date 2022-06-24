from numpy import ndarray

from Part2.bin.core.helper import read_img, read_from_standard_input, splitting_img

img = read_img(True)
f, d = read_from_standard_input()
matrix_list: list[ndarray] = splitting_img(img, f)