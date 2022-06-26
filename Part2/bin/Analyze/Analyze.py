import os
import re
from threading import Thread

from numpy import ndarray

from Part2.bin.Compression.Compression import Compression
from Part2.bin.core.helper import read_img, show_img, img_reassemble, splitting_img
from Part2.resources.constants import RESULTS_DIRECTORY


class Analyze(Thread):
    def __init__(self, file_path, f: int, d: int):
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

        # find name
        txt = re.findall("\w+\.bmp$", self.__file_path)[0]
        name, extension = txt.split(".")

        name = name + "x" + str(self.__f) + "x" + str(self.__d) + ".png"
        print(name)
        show_img(img, reassemble, NAME=os.path.join(RESULTS_DIRECTORY, name))
