'''
We look at image gradient:
A direction change in intensity or colour in an image.
'''
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('data/messi5.jpg',0) #Try with sudoku.png also

'''
laplacian gradient:
'''
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3) #The datatype is 64 bit float,kernel size
lap = np.uint8(np.absolute(lap))  #Converting it back to 8bit

'''
Sobel
'''
sobelX = cv2.Sobel(img, cv2.CV_64F,1,0)  #dx=1,dy=0 means we are using sobelx method
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1) #using sobely method

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_comb = cv2.bitwise_or(sobelX,sobelY)

'''
Canny:
threshold 1 and 2 is for the hysteris step. (Can be better visualized by trackbar)

'''
canny = cv2.Canny(img,100,200)

titles = ['image','laplacian','SobelX','SobelY','Sobel Combined','Canny']
images = [img,lap,sobelX,sobelY,sobel_comb,canny]
for i in range(len(titles)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
