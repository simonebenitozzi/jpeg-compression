from numpy import ndarray

from Part2.bin.Compression.Compression import Compression
from Part2.bin.core.helper import read_img, read_from_standard_input, splitting_img, img_reassemble


def main():
    img = read_img(True)
    f, d = read_from_standard_input()
    matrix_list: list[ndarray] = splitting_img(img, f)
    c = Compression(matrix_list, d)
    matrix_compressed_list = c.start()
    reassemble = img_reassemble(matrix_compressed_list, f, img.shape[0])


if __name__ == '__main__':
    main()
