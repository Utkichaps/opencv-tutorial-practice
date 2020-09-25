'''
Same as thresholding but with dynamic value for the threshold.
It is calculated for the smaller regions.
'''
import cv2
import numpy as np

img = cv2.imread('data/sudoku.png',0)   #0 is for grayscale

_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

'''
Mean thresholding:
Threshold value is mean of blocksize x blocksize [5th param] minus c [6th param]
'''
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11, 2)

'''
Guassian Thresholding
'''
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11, 2)

cv2.imshow('image',img)
cv2.imshow('threshold',th1)
cv2.imshow('threshold2',th2)
cv2.imshow('threshold3',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()