#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

#reading the image 

#img = cv2.imread('samplepic.png', 0)
#img_colour = cv2.imread('samplepic.png', 1)
#img = cv2.imread('samplepic_cropped.png', 0)
#img_colour = cv2.imread('samplepic_cropped.png', 1)
img = cv2.imread('newimage2.png', 0)
img_colour = cv2.imread('newimage2.png', 1)

## 1. Edge detection
blurred = cv2.blur(img,(5,5))
edges = cv2.Canny(blurred,50,200)

## 2. Dilation then erode
kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(edges,kernel,iterations = 2)
erode = cv2.erode(dilation,kernel,iterations = 1)

## 3. Fill 

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

## 4. Add rectangles

# convert the grayscale image to binary image
ret,thresh = cv2.threshold(im_out,127,255,0)
 
# find contours in the binary image
contours, heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
count = 1
rectangle_coords = []
for c in contours:
    
    # adding rectangles
    x,y,w,h = cv2.boundingRect(c)
    if (w/h < 0.3 or w/h > 3) or w < 15 or h < 15:
        pass
    else:
        top_l, top_r, bot_l, bot_r = int(x-0.1*w), int(x+w*1.1), int(y-0.1*h), int(y+h*1.1)
        rectangle_coords.append((x, y, w, h))
        cv2.rectangle(img_colour,(top_l,bot_l),(top_r,bot_r),(0,255,0),2)
        cv2.putText(img_colour, str(count), (x - 10, y - 10),
		    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)

        roi = img_colour[bot_l:bot_r, top_l:top_r] 
        cv2.imwrite("roi%d.jpg" % count , roi)
        count = count+1

        '''
        # calculate moments for each contour
        M = cv2.moments(c)
    
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
        cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        '''

        # display the image
        cv2.imshow("Image", img_colour)
        cv2.waitKey(0)
cv2.imwrite("image_with_boxes.jpg", img_colour)   
print("rectangle_coords: ", rectangle_coords)
   


## 5. Display images


cv2.imshow("sample_image", img)
cv2.imshow("sample_image_with_edge_detection (100,200)", edges)
#cv2.imshow("sample_image_with_edge_detection (120, 200)", edges_120_200)
#cv2.imshow("sample_image_with_edge_detection (100, 220)", edges_100_220)
#cv2.imshow("sample_image_with_edge_detection dilation (100, 220)", dilation)
cv2.imshow("sample_image_with_edge_detection erode (100, 220)", erode)
#cv2.imshow("sample_image_with_edge_detection erode (100, 220)", img2)





cv2.waitKey(0)

cv2.destroyAllWindows()