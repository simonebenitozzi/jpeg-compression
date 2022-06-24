import os

from Part2.bin.Analyze.Analyze import Analyze
from Part2.resources.constants import RESOURCES_DIRECTORY


def main():
    # get the path or directory
    folder_dir = RESOURCES_DIRECTORY
    for images in os.listdir(folder_dir):

        # check if the image end swith png or jpg or jpeg
        if images.endswith(".bmp"):
            thread = Analyze(os.path.join(folder_dir, images))
            thread.start()

    # img = read_img(SHOW=False, FILE_PATH=os.path.join(folder_dir, images))
    # f, d = 8, 8  # read_from_standard_input()
    # matrix_list: list[ndarray] = splitting_img(img, f)
    # c = Compression(matrix_list, d)
    # matrix_compressed_list = c.start()
    # reassemble = img_reassemble(matrix_compressed_list, f, img.shape[0])
    # show_img(img, reassemble)


if __name__ == '__main__':
    main()
