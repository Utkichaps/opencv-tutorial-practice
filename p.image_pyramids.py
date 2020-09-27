'''
Image pyramids:
Creating images of different resolutions.
Formal definition: Type of multiscale signal representation in
which a signal or an image is subject to repeated smoothing and sampling.
'''
import cv2
import numpy as np

img = cv2.imread('data/lena.jpg')
lr1 = cv2.pyrDown(img) #lower res
lr2 = cv2.pyrDown(lr1) #even lower res
hr = cv2.pyrUp(lr1) #higher res notice we are using lr1

'''
cv2.imshow('original image',img)
cv2.imshow('Pyrdown image',lr1)
cv2.imshow('Pyrdown2 image',lr2)
cv2.imshow('Pyrup image',hr)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#####################################################

layer = img.copy()
gp = [layer]  #Gaussian pyramid array
for i in range(5): #creating 5 res
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#####################################################
'''
A level in the Laplacian Pyramid is formed by the difference between 
that level in Gaussian Pyramid and expanded version of its upper level
in Gaussian pyramid
'''

lastimg = gp[-1] #last image of the image
cv2.imshow('upper level',layer)
lp = [lastimg] #laplacian pyramid

for i in range(5,0,-1):
     gaussian_extended = cv2.pyrUp(gp[i])
     laplacian = cv2.subtract(gp[i-1], gaussian_extended) #Images of laplacian pyramids
     cv2.imshow(str(i),laplacian)

cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()