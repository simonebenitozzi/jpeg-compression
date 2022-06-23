import cv2
import numpy as np

from scipy.fftpack import dctn, idctn

import math
import itertools

def img_partition(img, F):
    N = len(img)
    iterations = int(N/F)
    partitions_list = []

    for i in range(iterations):
        for j in range(iterations):
            partitions_list.append(img[i*F:i*F+F, j*F:j*F+F])

    return partitions_list

def img_reassemble(partitions, F, img_len):
    iterations = int(math.sqrt(len(partitions)))
    img = np.zeros((img_len-img_len%F, img_len-img_len%F))

    for i in range(iterations):
        for j in range(iterations):
            img[i*F:i*F+F, j*F:j*F+F] = partitions[i*iterations + j]
            
    return img



def main():
    img = cv2.imread("Immagini/shoe.bmp", 0)
    cv2.imshow("Original image", img)

    F = int(input("F: "))
    if F <= 0 or F > len(img):
        print("Invalid F input")
        return

    d = int(input("d: "))
    if d < 0 or d > 2*F-2:
        print("Invalid d input")
        return

    partitions = img_partition(img, F)
    new_partitions = []
    for f in partitions:
        c = dctn(f, norm="ortho")
        print(c)

        for k in range(len(c)):
            for l in range(len(c[k])):
                if k+l+2 >= d:
                    c[k][l] = 0

        ff = idctn(c, norm="ortho")
        ff[ff < 0] = 0
        ff[ff > 255] = 255

        new_partitions.append(ff.astype(int))
    
    new_img = img_reassemble(new_partitions, F, len(img))
    
    cv2.imshow("New Image", new_img)
    print(new_img)
    cv2.waitKey(0)
 



main()