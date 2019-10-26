# import the necessary packages
from PIL import Image

import importlib.util
import pytesseract
import argparse
import cv2
import os

# Checking pytesseract import
#print(pytesseract.__dict__)

### PART 1

args = {"image": "ocr_test_image1.png", "preprocess": "tresh"}

### PART 2
# load the example image and convert it to grayscale
image = cv2.imread(args["image"], 1)
gray = cv2.imread(args["image"], 0)

'''
#cv2.imshow("image", image)
#cv2.imshow("image grey", gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
#filename = "{}.png".format(os.getpid())
cv2.imwrite("preprocessed_ocr_image", gray)
'''

### PART 3

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(image)
#os.remove("preprocessed_ocr_image")
print(text)
 
# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)