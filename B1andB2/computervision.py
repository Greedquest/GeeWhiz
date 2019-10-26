import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('samplepic.png', cv.IMREAD_COLOR)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
