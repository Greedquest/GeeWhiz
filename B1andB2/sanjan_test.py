
#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

#reading the image 

image = cv2.imread('samplepic.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#plotting the image
plt.imshow(image)