'''
Contains various filters used to blur/smoothen the image
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/eye.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25 #This is a homogeneous/average kernel thats why 1/25.
dst = cv2.filter2D(img, -1, kernel)

blur = cv2.blur(img,(5,5))  #It's the same as the homogeneous/average kernel

gblur = cv2.GaussianBlur(img,(5,5),0) #This is a gaussian blur

median = cv2.medianBlur(img,5)  #Good to remove salt and pepper noise

bilat = cv2.bilateralFilter(img,9,75,75) #This preserves the edges

titles = ['image','2D Convolution','blur','gaussian','median','bilateral']
images = [img,dst,blur,gblur,median,bilat]
for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()