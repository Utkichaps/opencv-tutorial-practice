'''
Left click allows you to draw line between clicked points
right click opens a new window which shows the colour of the point in image clicked
'''
import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255),-1) #-1 fills the color
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-2],points[-1],(255,255,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        cv2.circle(img,(x,y),3,(0,255,255),-1)

        mycolorimage = np.zeros((512,512,3), np.uint8)
        mycolorimage[:] = [blue,green,red]
        cv2.imshow('color',mycolorimage)

img = cv2.imread('data/lena.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()