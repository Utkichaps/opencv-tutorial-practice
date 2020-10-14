'''
Hough transform is a technique used to detect any shape, if you
can represent it in a mathematical form. It can even detect the
shape if it is broken or distorted a bit. The algorithm is as follows:

1. Edge detection

2. Mapping of edge points to the Hough space and storage in the accumulator

3. Interpretation of the accumulator to yield lines of infinite length
(Done by thresholding and possibly other constraints)

4. Conversion of infinite lines to finite lines
'''

import cv2
import numpy as np

img = cv2.imread('data/sudoku.png')
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Using canny edge detector
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('edges',edges)

'''
2. Hough Lines method:
1st arg is the image
2nd arg is the row value is the distance resolution of the accumulator (usually 1)
3rd value is theta value which is angle resolution of the accumulator
4th arg is threshold
'''
lines = cv2.HoughLines(edges,1,np.pi/180, 200) # Image,row value

for line in lines:
    rho, theta = line[0] # rho is distance from (0,0), theta is angle
    a = np.cos(theta) # horizontal vector
    b = np.sin(theta) # vertical vector
    x0 = a * rho
    y0 = b * rho  # both of these gives the top left corner of the image

    # x1 is rounded off value of row x cos(theta) - 1000*sin(theta)
    x1 = int(x0 + 1000*(-b))

    # Similarly the rest is calculated
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)

    #Drawing the line:
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Hough Lines',img)

'''
2.5 Probabilistic Hough Lines Method
1st arg is the image
2nd arg is the row value is the distance resolution of the accumulator (usually 1)
3rd value is theta value which is angle resolution of the accumulator
4th arg is threshold
5th arg is minlinelength (Lines shorter than this will be rejected)
'''
lines2 = cv2.HoughLinesP(edges, 1, np.pi/180, 200, minLineLength=100, maxLineGap=10)

for line in lines2:
    x1,y1,x2,y2 = line[0]
    cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('Hough Lines P',img2)


k = cv2.waitKey(0)
cv2.destroyAllWindows()