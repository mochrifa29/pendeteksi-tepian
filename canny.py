import cv2
import numpy as np

g_1 = cv2.imread('canny/anggur.jpg')
g_2 = cv2.imread('canny/kucing.jpg')
g_3 = cv2.imread('canny/orang.jpg')
g_4 = cv2.imread('canny/pemandangan.jpg')

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
# Canny
edges_canny1 = cv2.Canny(Load1, 40, 30)
edges_canny2 = cv2.Canny(Load2, 90, 80)
edges_canny3 = cv2.Canny(Load3, 90, 80)
edges_canny4 = cv2.Canny(Load4, 90, 80)

cv2.imshow('anggur', gambar_1)
cv2.imshow('kucing', gambar_2)
cv2.imshow('orang', gambar_3)
cv2.imshow('alam', gambar_4)


cv2.imshow('Canny1', edges_canny1)
cv2.imshow('Canny2', edges_canny2)
cv2.imshow('Canny3', edges_canny3)
cv2.imshow('Canny4', edges_canny4)


cv2.waitKey()
cv2.destroyAllWindows()
