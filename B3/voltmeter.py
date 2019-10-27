"""
INPUT --> cropped image array of voltmeter
OUTPUT --> angle (degrees) from the vertical (+ve clockwise)

assumes:
- voltmeter dial is red
- angles are confined to ±90
"""
import numpy as np
import cv2
import os


def get_voltmeter_angle(raw_dial):
    size = np.shape(raw_dial)
    f = 200/size[1]
    dsize = (int( size[1]*f ),int( size[0]*f ))
    raw_dial = cv2.resize(raw_dial, dsize)

    raw_dial[:,:,2] = raw_dial[:,:,2]*1.1

    # cv2.imshow('f',raw_dial)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    hsv_dial = cv2.cvtColor(raw_dial,cv2.COLOR_BGR2HSV)
    # print(np.shape(hsv_dial))

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv_dial,lower_red,upper_red)

    # cv2.imshow('r',mask1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv_dial,lower_red,upper_red)

    # cv2.imshow('r',mask1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    mask = mask1+mask2
    # mask = cv2.bitwise_not(mask)

    arrow = cv2.bitwise_and(raw_dial,raw_dial,mask=mask)

    # cv2.imshow('r',arrow)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    b,g,r = cv2.split(arrow)

    try:
        kernel = np.ones((3,3),np.uint8)
        r = cv2.normalize(r,r,0,255,cv2.NORM_MINMAX)
        r = cv2.erode(r,kernel,iterations=1)
        r = cv2.dilate(r,kernel,iterations=1)
        r = cv2.threshold(r,220,255,cv2.THRESH_BINARY)[1]

    # cv2.imshow('r',r)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

        coords = np.stack(r.nonzero(),axis=1)
        line = cv2.fitLine(coords,cv2.DIST_L2,0,0.01,0.01)

    except:
        b,g,r = cv2.split(arrow)
        coords = np.stack(r.nonzero(),axis=1)
        line = cv2.fitLine(coords,cv2.DIST_L2,0,0.01,0.01)

    theta = np.arctan(line[1]/line[0])*180/np.pi

    #don't question it
    theta = -theta
    # print(theta)
    return theta

    # cv2.imshow('im',arrow)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



if __name__ == '__main__':
    for filename in os.listdir('images/voltmeter'):
        raw = cv2.imread('images/voltmeter/'+filename,cv2.IMREAD_COLOR)
        print(filename)
        print(get_voltmeter_angle(raw))
        print('\n')


