'''
This is a small project that will help us in lane detection.
In this program we will use a picture of a road to see the steps.
In the next program we will use a video
'''
import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('data/road.png')

#For matplotlib converting to rgb
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

'''
Now we have to define a region of interest. i.e. the lane in which our
vehicle is travelling. This will be in the shape of a triangle.
'''

print(img.shape)
height = img.shape[0]
width = img.shape[1]

'''
The region to be captured in our image is the road. For the image we have, 
the road ends at height/2 + 250 (trail and error) and that becomes the middle point.
'''
region_of_interest_vertices = [
    (0,height), #bottom left corner
    (width/2, height/2 + 250), #Middle point of the triangle
    (width, height)   #Bottom right corner
]

def region_of_interest(img, vertices):
    #define a blank matrix that matches the dimensions of our image
    mask = np.zeros_like(img)

    match_mask_color = 255 #Black
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

'''
Now we have to use edge detection to find out where the lanes (edges) are.
We do the canny edge detection before finding region of interest so that the
region itself isnt classified as an edge
'''
test_mask = region_of_interest(img, np.array([region_of_interest_vertices], np.int32))

gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

canny_image = cv2.Canny(gray_image, 100, 200)

masked_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

'''
Now to draw the lines on the image using hough line transform.
Play around with the parameter values to get better results.
'''
lines = cv2.HoughLinesP(masked_image, rho=6, theta=np.pi/60,
                        threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)

def draw_lines(img, lines):
    img = np.copy(img)
    line_image = np.zeros_like(img, dtype=np.uint8) #Blank image
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0),4) #Draw the lines on the blank image

    #Merge the line image with actual image
    img = cv2.addWeighted(img, 0.8, line_image, 1, 0.0)
    return img

image_with_lines = draw_lines(img, lines)

titles = ["Image","Test Mask", "Canny image", "Masked image", "Final image"]
images = [img,test_mask,canny_image,masked_image,image_with_lines]

for i in range(len(titles)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
