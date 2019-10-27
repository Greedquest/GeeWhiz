"""
INPUT --> cropped image array of silver switch
OUTPUT --> boolean TRUE when up?

assumes:
- on state ~ off state rotated by 180 degrees
- switch is vertical
- (circular switch) (not really required though)
"""
# Classification of state of knob (on/off) switch
# correlate against reference images - to be made

import numpy as np
import cv2
import matplotlib.pyplot as plt
import json
import os

# preprocess images to a standard form
def preprocess(image):
    
    # resize to x = 100 pixels, keeping aspect ratio
    size = np.shape(image)
    f = 200/size[1]
    dsize = (int( size[1]*f ),int( size[0]*f ))
    image = cv2.resize(image, dsize)
    
    # normalise
    image = cv2.normalize(image, image,0,255,cv2.NORM_MINMAX)
    
    #blur
    image_blur = cv2.medianBlur(image,13)
    # cv2.imshow('k',image_blur)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

     
    #circle finding


    blank = np.zeros((dsize[1],dsize[0]),np.uint8)
    try:
        circles = cv2.HoughCircles(image_blur,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        circles = np.uint16(np.around(circles))

        i = circles[0,0]
        centre = (i[0],i[1])
    except:
        centre = (dsize[1]//2,dsize[0]//2)
        i = [centre[0],centre[1],dsize[0]//3]

    
    cv2.circle(blank,centre,i[2],1,-1)   


    masked = cv2.bitwise_and(image, image, mask=blank)  #using a circular mask
    # cv2.imshow('k',masked)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    #coordinates of crop (based on circle)
    bot_l = i[0] - i[2]
    bot_r = i[0] + i[2]
    top_l = i[1] - i[2]
    top_r = i[1] + i[2]
        
    # crop to just the circle
    roi = masked[top_l:top_r, bot_l:bot_r] 
    
    #resize to 100*100
    new_size = (100,100)
    resized_image = cv2.resize(roi, new_size)
    
    # threshold to binary 
    ret, final_image = cv2.threshold(resized_image,45,255,cv2.THRESH_BINARY_INV)
    
    return final_image

# correlate two (preprocessed) images
def correlate(image1, image2):
    
    #flatten into an array
    image1 = np.array(image1)
    image1 = image1.flatten()
    image2 = np.array(image2)
    image2 = image2.flatten()
    
    return np.sum(abs(image2-image1))

# difference of two images
def difference(image1, image2):
    
    #flatten into an array
    image1 = np.array(image1)
    image1 = image1.flatten()
    image2 = np.array(image2)
    image2 = image2.flatten()
    
    
    return np.sum(abs(image2-image1))

# import raw images as grayscale
# knob_up_raw = cv2.imread('knob_up.png', 0)
# knob_down_raw = cv2.imread('knob_down.png', 0)
# test_raw = cv2.imread('knob_up.png', 0)

# process images
# processed_up = preprocess(knob_up_raw)
# processed_down = preprocess(knob_down_raw)
# processed_test = preprocess(test_raw)





'''
# correlate test image
up_diff = difference(processed_test, processed_up)
down_diff = difference(processed_test, processed_down)
print(up_diff, down_diff)

if down_diff > up_diff:
    print('test = up')
else:
    print('test = down')
'''

def get_switch_state(raw_switch):
    raw_switch = preprocess(raw_switch)
    flipped = np.flip(np.flip(raw_switch,0),1)

    combo = np.logical_and(flipped,raw_switch)
    xor = np.logical_xor(combo,raw_switch).astype(np.uint8)*255
    vals = np.nonzero(xor)[0]
    mean = np.mean(vals)

    if mean < np.shape(xor)[0]/2:
        # print('down')
        return 0
    else:
        # print('up')
        return 1


if __name__ == '__main__':

    for filename in os.listdir('images/silver_switch/'):
        print(filename)
        raw_switch = cv2.imread('images/silver_switch/'+filename,0)
        get_switch_state(raw_switch)

