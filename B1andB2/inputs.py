import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('samplepic_cropped.png')



plt.imshow(image, cmap='gray')

edges = cv2.Canny(image,100,200)
plt.imshow(edges, cmap='gray')

# edge detection - get binary image

# fill in boxes?

