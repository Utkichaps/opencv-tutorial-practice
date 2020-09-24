import cv2
import matplotlib.pyplot as plt

img = cv2.imread('data/lena.jpg')

'''
By default OpenCV reads images in BGR instead of RGB
so to display the image using a plotting lib, we convert
BGR to RGB
'''
img_fix = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_fix)
plt.show()