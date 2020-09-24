import cv2

img = cv2.imread('data/messi5.jpg')
img2 = cv2.imread('data/opencv-logo.png')

print(img.shape)  #(rows,columns,channels)
print(img.size)   # tot no of pixels
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#################################################

#Region of interest:

ball = img[280:340 , 330:390]   #Range of the ball in messi.jpg
img[273:333, 100:160] = ball    #Placing ball in different part of image
#cv2.imshow('image',img)

#################################################

#Adding images:

#Need to resize the images so that their dimensions match
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#dstimg = cv2.add(img, img2)

#Can also use addWeighted() i.e. transparancy percentage

dstimage = cv2.addWeighted(img,0.9,img2,0.1,0)
cv2.imshow('image2',dstimage)

#################################################

cv2.waitKey(0)
cv2.destroyAllWindows()