import tkinter as tk
from threading import Lock
from tkinter import filedialog

import cv2
import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image
from numpy import ndarray

from Part2.bin.core.constants import SHOW, FILE_PATH

lock = Lock()


def read_img(**kwargs):
    """
    Crea una semplice interfaccia in modo che l’utente possa scegliere dal filesystem
    un’immagine .bmp in toni di grigio;
    :return:
    """
    show = False
    if SHOW in kwargs:
        show = kwargs[SHOW]

    file_path = None
    if FILE_PATH in kwargs:
        file_path = kwargs[FILE_PATH]
    else:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()

    img = cv2.imread(file_path)

    if show:
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.show()

    return img


def read_from_standard_input():
    """
    Permette all’utente di scegliere:
    - un intero F che sarà l’ampiezza delle finestrelle (macro-blocchi) in cui si effettuare la DCT2;
    - un intero d compreso tra ZERO e (2F −2) che sar`a la soglia di taglio delle frequenze.
    :return:
    """
    f = int(input("Lunghezza dei macro-blocchi:"))
    d = int(input("Un intero compreso tra 0 e (2F − 2)"))
    while not d > 0 and d < (2 * f - 2):
        d = input("Un intero compreso tra 0 e (2F − 2)")

    return f, d


def splitting_img(img, f) -> list[ndarray]:
    """
    Suddivide l’immagine in blocchi quadrati f di pixel di dimensioni F×F partendo
    in alto a sinistra, scartando gli avanzi;
    :param f:
    :param img:
    :return:
    """
    row = img.shape[0] // f
    columns = img.shape[1] // f

    img = img[:f * row, :f * columns]
    print(img.shape)

    split_idx_columns = [x for x in range(f, img.shape[1], f)]
    split_idx_rows = [x for x in range(f, img.shape[0], f)]

    matrix_list: list[ndarray] = []

    hsplit_matrix = numpy.hsplit(img, split_idx_columns)
    for h in hsplit_matrix:
        vsplit_matrix = numpy.vsplit(h, split_idx_rows)
        for v in vsplit_matrix:
            matrix_list.append(v)

    return matrix_list


def img_reassemble(compressed_matrix_list: list[ndarray], f: int, length_matrix_rows: int) -> ndarray:
    """
    reassemble img from jpeg compression
    :param length_matrix_rows:
    :param compressed_matrix_list:
    :param f:
    :return:
    """

    # vertical reassemble
    v_reassemble: list[ndarray] = []
    j = 0

    v_reassemble.append(compressed_matrix_list[0])
    for i in range(1, len(compressed_matrix_list)):
        if i % (length_matrix_rows // f) == 0:
            j += 1
            v_reassemble.append(compressed_matrix_list[i])
            continue

        v_reassemble[j] = np.concatenate((v_reassemble[j], compressed_matrix_list[i]), axis=0)

    # horizontal reassemble
    reassemble: ndarray = v_reassemble[0]

    for i in range(1, len(v_reassemble)):
        reassemble = np.concatenate((reassemble, v_reassemble[i]), axis=1)

    return reassemble


def make_img_from_matrix(matrix: ndarray) -> Image:
    return Image.fromarray(matrix.astype(np.uint8))


def show_img(m1: Image, m2: Image):
    with lock:
        fig = plt.figure(figsize=(10, 7))

        # Adds a subplot at the 1st position
        fig.add_subplot(1, 2, 1)

        # showing image
        plt.imshow(m1, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')
        plt.title("Original")

        # Adds a subplot at the 2nd position
        fig.add_subplot(1, 2, 2)

        # showing image
        plt.imshow(m2, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')
        plt.title("Compressed")
        plt.show()
