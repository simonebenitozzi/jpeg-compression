import os

from numpy import ndarray

from Part2.bin.Analyze.Analyze import Analyze
from Part2.bin.Compression.Compression import Compression
from Part2.bin.core.helper import read_img, img_reassemble, splitting_img, show_img, read_from_standard_input
from Part2.resources.constants import RESOURCES_DIRECTORY



def main():
    use_thread = True
    # get the path or directory
    if use_thread:
        folder_dir = RESOURCES_DIRECTORY
        for images in os.listdir(folder_dir):

            # check if the image end swith png or jpg or jpeg
            if images.endswith(".bmp"):
                thread = Analyze(os.path.join(folder_dir, images), 8, 1)
                thread.start()
    else:
        img = read_img()
        f, d = read_from_standard_input()
        matrix_list: list[ndarray] = splitting_img(img, f)
        c = Compression(matrix_list, d)
        matrix_compressed_list = c.start()
        reassemble = img_reassemble(matrix_compressed_list, f, img.shape[0])
        show_img(img, reassemble)


if __name__ == '__main__':
    main()
