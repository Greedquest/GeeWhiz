import numpy as np
import cv2
import json
import os

raw_dial = cv2.imread('images/dial_cont/left1.jpg')

def get_angle(raw_dial,offset=0):
    size = np.shape(raw_dial)
    f = 100/size[1]
    dsize = (int( size[1]*f ),int( size[0]*f ))
    raw_dial = cv2.resize(raw_dial,dsize)

    raw_dial = cv2.normalize(raw_dial, raw_dial,0,255,cv2.NORM_MINMAX)

    dial = cv2.medianBlur(raw_dial,5)
    gdial = cv2.cvtColor(raw_dial,cv2.COLOR_BGR2GRAY)
    gdial = cv2.Canny(gdial,150,200)

    circles = cv2.HoughCircles(gdial,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)

    blank = np.zeros((dsize[1],dsize[0]),np.uint8)
    try:
        circles = np.uint16(np.around(circles))

        i = circles[0,0]
        centre = (i[0],i[1])
    except:
        centre = (dsize[1]//2,dsize[0]//2)
        i = [0,0,dsize[0]//3]

    cv2.circle(blank,centre,int(i[2]*0.8),1,-1)

    masked = cv2.bitwise_and(raw_dial, raw_dial, mask=blank)

    # cv2.imshow('im',masked)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    masked = cv2.cvtColor(masked,cv2.COLOR_BGR2GRAY)
    masked = cv2.normalize(masked,masked,0,255,cv2.NORM_MINMAX)
    _,masked = cv2.threshold(masked,200,255,cv2.THRESH_BINARY)

    kern = np.ones((3,3),np.uint8)
    masked = cv2.erode(masked,kern,iterations=2)

    coords = np.stack(masked.nonzero(),axis=1)

    line = cv2.fitLine(coords,cv2.DIST_L2,0,0.01,0.01)
    # print(line)
    theta = np.arctan(line[1]/line[0])*180/np.pi

    masked = cv2.dilate(masked,kern,iterations=1)

    cv2.circle(masked,centre,1,127,5)

    sticker = masked.nonzero()
    s_centre = np.mean(sticker,axis=1)
    s_centre = np.array((s_centre[1],s_centre[0]))

    if abs(line[0])>abs(line[1]):
        change = s_centre[1]>centre[1]

    else:
        if theta < 0:
            change = s_centre[0] < centre[0]
        else:
            change = s_centre[0] > centre[0]

    if change:
        if theta > 0:
            theta -= 180
        else:
            theta += 180

    print(theta)
    return theta

    # cv2.circle(masked,(int(s_centre[0]),int(s_centre[1])),1,127,5)

    # diff = s_centre-centre
    # diff = np.array((-diff[1],diff[0]))
    # theta = np.arctan(diff[1]/diff[0])*180/np.pi

    # print(theta)

    # cv2.imshow('img',masked)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



if __name__ == '__main__':
    # change images/ red/blue depending on button
    for filename in os.listdir('images/dial_test'):
        # if '3861' not in filename:
            # continue
        raw_switch = cv2.imread('images/dial_test/'+filename,cv2.IMREAD_COLOR)
        print(filename)
        get_angle(raw_switch)
