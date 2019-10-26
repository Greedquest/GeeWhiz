#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

#reading the image 

#img = cv2.imread('samplepic.png', 0)
img = cv2.imread('samplepic_cropped.png', 0)

edges_100_200 = cv2.Canny(img,100,200)
#edges_120_200 = cv2.Canny(img,120,200)
#edges_100_220 = cv2.Canny(img,120,200)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(edges_100_200,kernel,iterations = 2)

erode = cv2.erode(dilation,kernel,iterations = 1)

### Fill start ###

erode_inversed = cv2.bitwise_not(erode)
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
 
th, im_th = cv2.threshold(erode_inversed, 220, 255, cv2.THRESH_BINARY_INV)
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv

# im_out is the filled in white on black image

### Fill end ###

### Center detection ###
 
# convert the image to grayscale
 
# convert the grayscale image to binary image
ret,thresh = cv2.threshold(im_out,127,255,0)
 
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

### Center detection end ###


cv2.imshow("sample_image", img)
cv2.imshow("sample_image_with_edge_detection (100,200)", edges_100_200)
#cv2.imshow("sample_image_with_edge_detection (120, 200)", edges_120_200)
#cv2.imshow("sample_image_with_edge_detection (100, 220)", edges_100_220)
#cv2.imshow("sample_image_with_edge_detection dilation (100, 220)", dilation)
cv2.imshow("sample_image_with_edge_detection erode (100, 220)", erode)
#cv2.imshow("sample_image_with_edge_detection erode (100, 220)", img2)





cv2.waitKey(0)

cv2.destroyAllWindows()
