import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image
from numpy import asarray, ndarray


def read_img(show=False):
    """
    Crea una semplice interfaccia in modo che l’utente possa scegliere dal filesystem
    un’immagine .bmp in toni di grigio;
    :param show:
    :return:
    """
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    if show:
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.show()

    # convert image to numpy array
    data = asarray(img)
    print(type(data))

    # summarize shape

    print(data.shape)

    return data


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
    x = img.shape[0] // f
    print(f"Immagine con scarto di {img.shape[0] % f}, divisione: {x}")
    img = img[:f * x, :f * x]
    print(img.shape)

    split_idx = [x for x in range(f, img.shape[0], f)]
    print(f"Original: \n {img} \n")

    matrix_list: list[ndarray] = []

    hsplit_matrix = numpy.hsplit(img, split_idx)
    for h in hsplit_matrix:
        print("--------------------------------")
        print(f"hsplit: \n {h} \n")
        vsplit_matrix = numpy.vsplit(h, split_idx)
        for v in vsplit_matrix:
            print(f"vsplit: \n {v} \n")
            matrix_list.append(v)

    return matrix_list


def img_reassemble(compressed_matrix_list, f):
    """
    reassemble img from jpeg compression
    :param compressed_matrix_list:
    :param f:
    :return:
    """

    # vertical reassemble
    v_reassemble = []
    j = 0

    v_reassemble[j] = compressed_matrix_list[0]
    for i in range(1, len(compressed_matrix_list)):
        if i % f == 0:
            j += 1
            v_reassemble[j] = compressed_matrix_list[i]
            continue
            
        v_reassemble[j] = np.vstack((v_reassemble[j], compressed_matrix_list[i]))


    # horizontal reassemble
    reassemble = v_reassemble[0]

    for i in range(1, len(v_reassemble)):
        reassemble = np.hstack((v_reassemble, v_reassemble[i]))

    return reassemble



    
