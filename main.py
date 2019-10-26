import cv2
import numpy as np
import DataCollation.Semantic_Class as SC
import B3.light_switch

def subscript_np_array(box, arr):
    return np.array([x[box[0][1]:box[0][1] + box[1][1]] for x in arr[box[0][0]:box[0][0] + box[1][0]]])

list_of_stuff = [
    (lambda box : create_light(subscript_np_array(b, np_img), "g"))
]

cals_dict = {
    "g" : {
    "on" : [0.00,0.95],
    "off" : [0.17,0.84]
    },
    "r" : {
    "on" : [2.66,0.68],
    "off" : [5.18,0.79]
    },
    "s" : {
    "on" : [1.06,1.04],
    "off" : [1.38,0.74]
    }
}

measure_func_dict = {
    "light": lambda so : B3.light_switch.get_button_state(so.np, np.array(so.cal_on), np.array(so.cal_off))
}

def create_light(pixels, type):
    r = SC.Discrete("light")
    r.np = pixels
    r.cal_on = cals_dict[type]["on"]
    r.cal_off = cals_dict[type]["off"]
    return r    

SOs = []
# main list of all semantic objects

img_blcwht = cv2.imread('samplepic_cropped.png', 0)
img_colour = cv2.imread('samplepic_cropped.png', 1)

boxes = [((25,57),(98,105))]

np_img = np.asarray(img_colour)

for i,b in enumerate(boxes):
    SOs.append(list_of_stuff[i](b))

while True:

    for so in SOs:
        so.value = measure_func_dict[so.meaning](so)
    
    break