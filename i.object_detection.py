'''
Object detection using HSV colour space.
1. Detecting specific color balls (Commented)
2. Detecting specific colours from video camera
By changing the different bars on the trackbar, You can filter out different colours
'''
import cv2
import numpy as np

def nothing(x):
    pass

#To use video:
cap = cv2.VideoCapture(0)

#Use of trackbar to figure out lower and upper bounds of hue,saturation,value
cv2.namedWindow('Tracking')
cv2.createTrackbar("LH",'Tracking',0,255,nothing)
cv2.createTrackbar("UH",'Tracking',255,255,nothing)
cv2.createTrackbar("LS",'Tracking',0,255,nothing)
cv2.createTrackbar("US",'Tracking',255,255,nothing)
cv2.createTrackbar("LV",'Tracking',0,255,nothing)
cv2.createTrackbar("UV",'Tracking',255,255,nothing)

while True:
    #frame = cv2.imread('data/smarties.png')

    #For video:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    '''
    We will actually use the trackbar to figure out the lower and
    upper bounds of the colours
    '''
    l_h = cv2.getTrackbarPos("LH",'Tracking')
    u_h = cv2.getTrackbarPos("UH", 'Tracking')

    l_v = cv2.getTrackbarPos("LV", 'Tracking')
    u_v = cv2.getTrackbarPos("UV", 'Tracking')

    l_s = cv2.getTrackbarPos("LS", 'Tracking')
    u_s = cv2.getTrackbarPos("US", 'Tracking')

    #l_b = np.array([110,50,50]) #Lower colour range of blue
    #u_b = np.array([130,255,255]) #Upper limit for blue colour

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b) #Getting blue colour only using range


    res = cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 27:       #Esc key
        break

#For video:
cap.release()

cv2.destroyAllWindows()
