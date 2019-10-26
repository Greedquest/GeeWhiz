import numpy as np
import cv2
from matplotlib import pyplot as plt
import json
import os


with open('calibration.json','r') as json_file:
    calibration = json.load(json_file)


def get_button_state(raw_switch,cal_on,cal_off):
    size = np.shape(raw_switch)
    f = 100/size[1]
    dsize = (int( size[1]*f ),int( size[0]*f ))
    raw_switch = cv2.resize(raw_switch,dsize)

    raw_switch = cv2.normalize(raw_switch, raw_switch,0,255,cv2.NORM_MINMAX)

    switch = cv2.medianBlur(raw_switch,5)
    gswitch = cv2.cvtColor(switch,cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gswitch,cv2.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))

    blank = np.zeros((dsize[1],dsize[0]),np.uint8)
    for i in circles[0,:]:
        cv2.circle(blank,(i[0],i[1]),i[2],1,-1)

    masked = cv2.bitwise_and(raw_switch, raw_switch, mask=blank)
    b,g,r = cv2.split(masked)
    mean_r = np.mean(r)
    mean_g = np.mean(g)
    mean_b = np.mean(b)

    out = (mean_r/mean_g,mean_b/mean_g)

    d_on = np.linalg.norm(out-cal_on)
    d_off = np.linalg.norm(out-cal_off)

    print('Out: {}'.format(out))
    if d_off > d_on:
        print('ON!')
    else:
        print('OFF!')
    print('Don {}\nDoff {}'.format(d_on,d_off) )
    print('\n')

    return d_off > d_on


    '''
    raw_switch_on = cv2.resize(raw_switch_on,(200,200))
    raw_switch_off = cv2.resize(raw_switch_off,(200,200))

    switch_on = np.copy(raw_switch_on)
    switch_off = np.copy(raw_switch_off)

    switch_on=cv2.blur(switch_on,(10,10))
    switch_on = cv2.Canny(switch_on,100,200)
    switch_on = cv2.dilate(switch_on,np.ones((10,10),np.uint8),iterations=1)
    contours_on, hierarchy_on = cv2.findContours(switch_on, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(raw_switch_on,contours_on,0,(255,0,0),3)
    print(np.mean(switch_on))

    print(np.mean(switch_off))

    cv2.imshow("On",raw_switch_on)
    # cv2.imshow("Off",switch_off)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

if __name__ == '__main__':
    # change light_switch_states_ to r/g depending on button
    cal_on = np.array(calibration['light_switch_states_s']['on'])
    cal_off = np.array(calibration['light_switch_states_s']['off'])
    # change images/ red/blue depending on button
    button = 'small'
    for filename in os.listdir('images/'+button):
        raw_switch = cv2.imread('images/'+button+'/'+filename,cv2.IMREAD_COLOR)
        print(filename)
        get_button_state(raw_switch,cal_on,cal_off)
