#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

#reading the image 

img = cv2.imread('samplepic.png', 0)
edges = cv2.Canny(img,100,200)
#plotting the image
plt.imshow(img)

cv2.imshow("sample_image", img)
cv2.imshow("sample_image_with_edge_detection", edges)

cv2.waitKey(0)

cv2.destroyAllWindows()


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()