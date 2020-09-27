'''
image blending
we will blend half of the orange with half of the apple
'''
import cv2
import numpy as np

apple = cv2.imread('data/apple.jpg')
orange = cv2.imread('data/orange.jpg')

'''
Stacking them side by side: (not image blending)
'''
apple_orange = np.hstack((apple[:,:256] , orange[:, 256:])) #256 is half of the image

'''
Now using image pyramids we will blend the two images.
This requires 5 steps:
1. Load the two images
2. Find the Gaussian Pyramids for apple and orange - we will use level 6
3. From gaussian pyramids we find out laplacian pyramids
4. Now we join the left and right half of apple and orange
5.Reconstruct the original image from the above step 
'''
#generate gaussian pyramid for apple and orange:
apple_layer = apple.copy()
gp_apple = [apple_layer]
for i in range(6): #6 levels
    apple_layer = cv2.pyrDown(apple_layer)
    gp_apple.append(apple_layer)

orange_layer = orange.copy()
gp_orange = [orange_layer]
for i in range(6): #6 levels
    orange_layer = cv2.pyrDown(orange_layer)
    gp_orange.append(orange_layer)

#Generate laplacian pyramid for apple and orange
apple_copy = gp_apple[-1]
lp_apple = [apple_copy]
for i in range(5,0,-1): #6 levels
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_expanded)
    lp_apple.append(laplacian)

orange_copy = gp_orange[-1]
lp_orange = [orange_copy]
for i in range(5,0,-1): #6 levels
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)

#Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple,lp_orange):
    n += 1
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#Reconstruct time
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple orange',apple_orange)
cv2.imshow('apple orange blended',apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()