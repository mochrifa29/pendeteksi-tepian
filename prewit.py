import cv2
import numpy as np

g_1 = cv2.imread('prewiit/anggur.jpg')
g_2 = cv2.imread('prewiit/kucing.jpg')
g_3 = cv2.imread('prewiit/orang.jpg')
g_4 = cv2.imread('prewiit/pemandangan.jpg')
widht = 300
heigth = 300
dim = (widht, heigth)

gambar_1 = cv2.resize(g_1, dim, interpolation=cv2.INTER_LINEAR)
gambar_2 = cv2.resize(g_2, dim, interpolation=cv2.INTER_LINEAR)
gambar_3 = cv2.resize(g_3, dim, interpolation=cv2.INTER_LINEAR)
gambar_4 = cv2.resize(g_4, dim, interpolation=cv2.INTER_LINEAR)

Load1 = cv2.resize(gambar_1, dim, interpolation=cv2.INTER_LINEAR)
Load2 = cv2.resize(gambar_2, dim, interpolation=cv2.INTER_LINEAR)
Load3 = cv2.resize(gambar_3, dim, interpolation=cv2.INTER_LINEAR)
Load4 = cv2.resize(gambar_4, dim, interpolation=cv2.INTER_LINEAR)


# Prewit
kernelX_1 = np.array(
    [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]
)

kernelX_2 = np.array(
    [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]
)

kernelX_3 = np.array(
    [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]
)

kernelX_4 = np.array(
    [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]
)

edges_prewitt1 = cv2.filter2D(Load1, -1, kernelX_1)
edges_prewitt2 = cv2.filter2D(Load2, -1, kernelX_2)
edges_prewitt3 = cv2.filter2D(Load3, -1, kernelX_3)
edges_prewitt4 = cv2.filter2D(Load4, -1, kernelX_4)

cv2.imshow('anggur', gambar_1)
cv2.imshow('kucing', gambar_2)
cv2.imshow('orang', gambar_3)
cv2.imshow('alam', gambar_4)


cv2.imshow('prewitt1', edges_prewitt1)
cv2.imshow('prewitt2', edges_prewitt2)
cv2.imshow('prewitt3', edges_prewitt3)
cv2.imshow('prewitt4', edges_prewitt4)

cv2.waitKey()
cv2.destroyAllWindows()
