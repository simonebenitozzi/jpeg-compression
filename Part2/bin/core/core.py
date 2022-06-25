import os

from numpy import ndarray

from Part2.bin.Analyze.Analyze import Analyze
from Part2.bin.Compression.Compression import Compression
from Part2.bin.GUI.GUI import GUI
from Part2.bin.core.helper import read_img, img_reassemble, splitting_img, show_img, read_from_standard_input
from Part2.resources.constants import RESOURCES_DIRECTORY



def main():
    use_thread = False
    # get the path or directory
    if use_thread:
        folder_dir = RESOURCES_DIRECTORY
        for images in os.listdir(folder_dir):

            # check if the image end swith png or jpg or jpeg
            if images.endswith(".bmp"):
                thread = Analyze(os.path.join(folder_dir, images), 8, 1)
                thread.start()
    else:
        app = GUI()
        app.mainloop()


if __name__ == '__main__':
    main()
