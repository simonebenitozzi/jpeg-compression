from numpy import ndarray

from Part2.bin.Compression.Compression import Compression
from Part2.bin.core.helper import read_img, splitting_img, img_reassemble, show_img


def execute(file_path, f, d):
    img = read_img(FILE_PATH=file_path, SHOW=True)
    matrix_list: list[ndarray] = splitting_img(img, f)
    c = Compression(matrix_list, d)
    matrix_compressed_list = c.start()
    reassemble = img_reassemble(matrix_compressed_list, f, img.shape[0])
    show_img(img, reassemble)
