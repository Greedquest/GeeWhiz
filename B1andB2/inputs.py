import cv2 
import numpy as np
import matplotlib.pyplot as plt

#image = cv2.imread('samplepic_cropped.png')



#plt.imshow(image, cmap='gray')

#edges = cv2.Canny(image,100,200)
#plt.imshow(edges, cmap='gray')


# read image through command line
img = cv2.imread('samplepic_cropped.png')
 
# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,127,255,0)
 
# find contours in the binary image
contours, heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
   # calculate moments for each contour
   M = cv2.moments(c)
 
   # calculate x,y coordinate of center
   cX = int(M["m10"] / M["m00"])
   cY = int(M["m01"] / M["m00"])
   cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
   cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
   # display the image
   cv2.imshow("Image", img)
   cv2.waitKey(0)

