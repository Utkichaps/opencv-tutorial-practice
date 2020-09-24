'''
Check if camera is working
'''
import cv2

cap = cv2.VideoCapture(0) #filename can be an argument. 0 or -1 for camera

'''
The following two lines are to save the video captured to a file
'''
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480)) #Used to save the file

while(cap.isOpened()):
	ret,frame = cap.read()
	if ret == True:
		#out.write(frame)	#To write it to file
		cv2.imshow('capture',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):	#Exits when you press q
			break
	else:
		break
cap.release()
#out.release()	#To stop the recording
cv2.destroyAllWindows()

