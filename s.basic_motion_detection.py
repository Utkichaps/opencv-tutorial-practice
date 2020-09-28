import cv2
import numpy as np

cap = cv2.VideoCapture('data/vtest.avi')

ret, frame1 = cap.read() #Reading 1st frame
ret, frame2 = cap.read() #Reading 2nd frame

while cap.isOpened():

    diff = cv2.absdiff(frame1,frame2)  #Gets the abs difference of both the frames
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)  #We are using grayscale to find the contours

    blur = cv2.GaussianBlur(gray,(5,5),0)  #Eliminating noise
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)    #Getting threshold for clean difference
    dilated = cv2.dilate(thresh, None, iterations=3)    #Eliminating weak threshold lines

    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)  #Will give the coordinates of the rectangle

        #Removing moving objects which may not be human. i.e, less than a partcular area
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame1, (x,y), (x+w,y+h),(0,255,0),2)

        #Now to put some text if any movement is observed
        cv2.putText(frame1, "Status: {}".format('Movement'), (10,20),cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,0,255),3)

    #cv2.drawContours(frame1, contours, -1, (0,255,0),2) #This will show outline of all the moving objects

    cv2.imshow("feed",frame1)

    frame1 = frame2     #Assigning frame2 value
    ret, frame2 = cap.read()  #Reading new frame

    if cv2.waitKey(40) == 27:  #Esc
        break

cv2.destroyAllWindows()
cap.release()