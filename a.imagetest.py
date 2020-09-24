import cv2
import matplotlib.pyplot as plt
img = cv2.imread('data/lena.jpg')
img_fix = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_fix)
plt.show()