'''
matplotlib can be used to show the different images generated in a better
format and in a more concise manner
'''
import cv2
from matplotlib import pyplot as plt

imgl = cv2.imread('data/lena.jpg')

#OpenCV reads it in BGR format always
#cv2.imshow('image',imgl)

#For matplotlib we need to convert it to RGB
imgl = cv2.cvtColor(imgl,cv2.COLOR_BGR2RGB)

plt.imshow(imgl)
#plt.xticks([]), plt.yticks([]) #If empty params, it hides the ticks
plt.show()


########################################################################################
'''
Using the thresholding program
'''
img = cv2.imread('data/gradient.png',0)

_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


titles = ['original','binary','binary_inv','trunc','tozero','tozero_inv']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1)    #2 rows, 3 columns, index
    plt.imshow(images[i], 'gray')   #displayes in grayscale
    plt.title(titles[i])
    #plt.xticks([]),plt.yticks([])

plt.show()
