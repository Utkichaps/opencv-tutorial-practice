'''
Detecting basic geometric shapes
'''
import cv2

img = cv2.imread('data/shapes.jpg')

#Convert to grayscale
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Find out the threshold
_, thresh = cv2.threshold(imgGrey,240,255,cv2.THRESH_BINARY)

#Find out the contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#Iterating over all the contours:
for contour in contours:
    '''
    Approx poly approximates a polygonal curve according to some precision.
    The second parameter is epsilon which specifies parameter accuracy
    arcLength calcs the curve length of contour 
    Both the True parameters are for it being a closed shape
    '''
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),5) #Draw parameters on original image. Index is 0 as only 1 contour
    x = approx.ravel()[0]  # x coordinate
    y = approx.ravel()[1]  # y coordinate of the image
    if len(approx) == 3: #Then it is a triangle
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

    elif len(approx) == 4: #square or rectangle
        x, y, w, h = cv2.boundingRect(approx)
        # We use aspect ratio to include error (noise) which may come from bounding rect function

        aspectRatio = float(w)/h #Typecasting needed to get decimal
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        else:
            cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

    elif len(approx) == 5: #Pentagon
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

    elif len(approx) == 10: #Star
        cv2.putText(img,"Star",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

cv2.imshow('shapes',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
