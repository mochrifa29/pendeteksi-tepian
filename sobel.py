import cv2

g_1 = cv2.imread('sobel/anggur.jpg')
g_2 = cv2.imread('sobel/kucing.jpg')
g_3 = cv2.imread('sobel/orang.jpg')
g_4 = cv2.imread('sobel/pemandangan.jpg')


widht = 300
heigth = 300
dim = (widht, heigth)

gambar_1 = cv2.resize(g_1, dim, interpolation=cv2.INTER_LINEAR)
gambar_2 = cv2.resize(g_2, dim, interpolation=cv2.INTER_LINEAR)
gambar_3 = cv2.resize(g_3, dim, interpolation=cv2.INTER_LINEAR)
gambar_4 = cv2.resize(g_4, dim, interpolation=cv2.INTER_LINEAR)


Load1 = cv2.resize(g_1, dim, interpolation=cv2.INTER_LINEAR)
Load2 = cv2.resize(g_2, dim, interpolation=cv2.INTER_LINEAR)
Load3 = cv2.resize(g_3, dim, interpolation=cv2.INTER_LINEAR)
Load4 = cv2.resize(g_4, dim, interpolation=cv2.INTER_LINEAR)
# Sobel
edges_sobel1 = cv2.Sobel(Load1, cv2.CV_64F, 1, 0, ksize=1)
edges_sobel2 = cv2.Sobel(Load2, cv2.CV_64F, 1, 0, ksize=1)
edges_sobel3 = cv2.Sobel(Load3, cv2.CV_64F, 1, 0, ksize=1)
edges_sobel4 = cv2.Sobel(Load4, cv2.CV_64F, 1, 0, ksize=1)

cv2.imshow('anggur', gambar_1)
cv2.imshow('kucing', gambar_2)
cv2.imshow('orang', gambar_3)
cv2.imshow('alam', gambar_4)


cv2.imshow('sobel1', edges_sobel1)
cv2.imshow('sobel2', edges_sobel2)
cv2.imshow('sobel3', edges_sobel3)
cv2.imshow('sobel4', edges_sobel4)

cv2.waitKey()
cv2.destroyAllWindows()
