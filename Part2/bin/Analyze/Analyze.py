import os
from threading import Thread

from numpy import ndarray

from Part2.bin.Compression.Compression import Compression
from Part2.bin.core.helper import read_img, show_img, img_reassemble, splitting_img


class Analyze(Thread):
    def __init__(self, file_path, f:int, d:int):
        super().__init__()
        self.__file_path = file_path
        self.__f = f
        self.__d = d

    def run(self) -> None:
        img = read_img(SHOW=False, FILE_PATH=os.path.join(self.__file_path))
        matrix_list: list[ndarray] = splitting_img(img, self.__f)
        c = Compression(matrix_list, self.__d)
        matrix_compressed_list = c.start()
        reassemble = img_reassemble(matrix_compressed_list, self.__f, img.shape[0])
        show_img(img, reassemble)
