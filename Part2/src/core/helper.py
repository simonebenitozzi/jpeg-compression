import tkinter as tk
from tkinter import filedialog
import os

import numpy
import numpy as np
from numpy import asarray
from scipy import misc

from PIL import Image
import matplotlib.pyplot as plt


def read_img(show=False):
    '''
    Creare una semplice interfaccia in modo che l’utente possa scegliere dal filesystem
un’immagine .bmp in toni di grigio;
    :param show:
    :return:
    '''
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
    '''
     permettere all’utente di scegliere:
 un intero F che sar`a l’ampiezza delle finestrelle (macro-blocchi) in cui si
effettuer`a la DCT2;
 un intero d compreso tra 0 e (2F −2) che sar`a la soglia di taglio delle frequenze
(vedi sotto).
    :return:
    '''
    f = int(input("Lunghezza dei macro-blocchi:"))
    d = int(input("Un intero compreso tra 0 e (2F − 2)"))
    while not d > 0 and d < (2 * f - 2):
        d = input("Un intero compreso tra 0 e (2F − 2)")

    return f, d


def splitting_img(img, f):
    '''
     suddividere l’immagine in blocchi quadrati f di pixel di dimensioni F×F partendo
    in alto a sinistra, scartando gli avanzi;
    :param img:
    :return:
    '''

    split_idx = [x for x in range(f, img.shape[0], f)]
    hsplit_matrix = numpy.hsplit(img, split_idx)
    for m in hsplit_matrix:
        vsplit_matrix = numpy.vsplit(m, split_idx)


