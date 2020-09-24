'''
Adds text at particular location on video
'''
import cv2

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.putText(frame,"This is some random text",(10,50),cv2.FONT_HERSHEY_COMPLEX,
                    1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
