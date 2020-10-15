'''
This is the same code as the previous program except that
it has been put into a new function called process and we
will now use a video and continuously detect the lanes.
'''
import cv2
import matplotlib.pylab as plt
import numpy as np

def region_of_interest(img, vertices):
    #define a blank matrix that matches the dimensions of our image
    mask = np.zeros_like(img)

    match_mask_color = 255 #Black
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    img = np.copy(img)
    line_image = np.zeros_like(img, dtype=np.uint8) #Blank image
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0),4) #Draw the lines on the blank image
    # Merge the line image with actual image
    img = cv2.addWeighted(img, 0.8, line_image, 1, 0.0)
    return img

#img = cv2.imread('data/road.png')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Processes each frame (same code as prev program)
def process(img):
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]


    region_of_interest_vertices = [
        (0,height), #bottom left corner
        (width/2, height/2 + 250), #Middle point of the triangle
        (width, height)   #Bottom right corner
    ]

    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    masked_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    #Play around with these values to get better lane detection results
    lines = cv2.HoughLinesP(masked_image, rho=2, theta=np.pi/60,
                            threshold=50,lines=np.array([]),minLineLength=40,maxLineGap=100)

    if lines is None:
        image_with_lines = img
    else:                 #This else statement is so that the program doesn't give an error if no lines are detected
        image_with_lines = draw_lines(img, lines)
    return image_with_lines

cap = cv2.VideoCapture("data/lane_test1.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #Exit at q
        break


cap.release()
cv2.destroyAllWindows()