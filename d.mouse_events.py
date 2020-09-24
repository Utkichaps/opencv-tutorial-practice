'''
Left click shows you coordinates of image
right click shows you the value of colour at that specific clicked point

'''
import cv2

#All available events:
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

#callback function:
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        stri = str(x) + ',' + str(y)
        frame = cv2.putText(img,stri,(x,y),cv2.FONT_HERSHEY_COMPLEX,
                            1,(255,124,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        strXY = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strXY, (x,y), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
        cv2.imshow('image',img)

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('data/lena.jpg')

cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()