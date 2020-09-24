'''
Program to put trackbar
'''
import numpy as np
import cv2

def nothing(x): #x is current pos of trackbar
    print(x)

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image') #placeholder for images and trackbars

#Creating 3 trackbars:
cv2.createTrackbar('B','image',0,255,nothing)  #0 is initial value, 255 is final value, nothing is the callback function
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch = '0:OFF | 1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
b = 0

while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF #esc key
    if k == 27:
        break

    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()