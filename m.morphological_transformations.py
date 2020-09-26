'''
This prg contains some morphological transformations
Morphological transformations are simple operations based on the image shape.
They are mostly performed on binary images.
Better to run the code and see how it is
'''
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('data/smarties.png',0)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3), np.uint8) # 3 x 3 kernel of 1s
'''
Dilation transformation:
To remove those small white dots in the mask of the balls
'''
dilation = cv2.dilate(mask, kernel, iterations=2)  #i no of iterations applies the kernel i number of times

'''
Erosion transformation:
Erodes the image
'''
erosion = cv2.erode(mask,kernel, iterations=1)

'''
Opening transformation:
It is erosion followed by dilation      
'''
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

'''
Closing transformation:
dilation then erosion
'''
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

'''
A few more:
grad - difference between erosion and dilation 
tophat - difference between image and opening of image
'''
grad = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

titles = ['image','mask','dilation','erosion','opening','closing','gradient','tophat']
images = [img,mask,dilation,erosion,opening,closing,grad,tophat]

for i in range(len(titles)):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
