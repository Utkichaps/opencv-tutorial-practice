'''
Contours:
Curve joining all the continuous points that lie on a boundary which have the
same colour or intensity.
- Good for shape analysis
- Object detection and recognition
'''
import numpy as np
import cv2

img = cv2.imread('data/opencv-logo-whiteback.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray,127,255,0) #Calculating thresholds

'''
Getting the contours
'contours' is a list of all the contours in the image. Each is a numpy array of (x,y) coordinates
of boundary points of the object.
'hierarchy' is an optional parameter that gives image topology
'''
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Its a mode and method

#Thus len of contours will be:
print("No of contours = " + str(len(contours)))
print(contours[0])  #First contour

'''
Drawing the contours
Putting -1 as contour index will draw all the contours
You can put 0 for first, 1 for second and so on
'''
cv2.drawContours(img, contours, -1,(0,255,0),3)  # -1 means it'll draw all the contours

cv2.imshow('image',img)
cv2.imshow('image gray',imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()