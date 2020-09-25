'''
Segmentation technique used to separate an object
from its background by using a threshold.
'''
import cv2
import numpy as np

img = cv2.imread('data/gradient.png')

#Binary thresholding:
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)    #second arg is threshold value which is a pixel value

#Binary Inverse thresholding
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

#Thresh trunk. Keeps same colour pixels after threshold
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

#Thresh to 0
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)


cv2.imshow('image',img)
cv2.imshow('threshold',th1)
cv2.imshow('threshold2',th2)
cv2.imshow('threshold3',th3)
cv2.imshow('threshold4',th4)

cv2.waitKey(0)
cv2.destroyAllWindows()