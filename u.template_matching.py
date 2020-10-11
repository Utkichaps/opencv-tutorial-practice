'''
Template matching is a way to find a smaller image in a larger image.
'''
import cv2
import numpy as np

img = cv2.imread('data/messi5.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('data/messi_face.jpg',0)
w,h = template.shape[::-1]

'''
Method to match the template.
The res matrix shows how "good" or "bad" the template has matched to different locations 
in the original image, since the template is moving over the image and checking how much 
they are matched in every location.
'''
res = cv2.matchTemplate(grayimg, template, cv2.TM_CCOEFF_NORMED) #This is a template matching method. There are many of them.
#print(res)

'''
Now our aim is to filter out all the "bad points". Hence we set a threshold of matching where
0.95 shows a 95% match of a point in our image with the template. You can play around with these
values and see how it works
'''
threshold = 0.95

loc = np.where(res >= threshold) #Higher threshold, higher accuracy
#print(loc)

for pt in zip(*loc[::-1]): #For loop is not really needed in this case as there is only one point
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()