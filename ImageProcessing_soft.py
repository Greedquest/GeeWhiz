import cv2
import numpy as np
import DataCollation.Semantic_Class as SC
import B3.dial
import B3.light_switch
import B3.silver_switch
import B3.voltmeter
# import B3.light_switch
import B1andB2.functions_1
import B3.seven_seg

def subscript_np_array(box, arr):
    return np.array([x[box[0]:box[0] + box[2]] for x in arr[box[1]:box[1] + box[3]]])

dict_of_stuff = {
    'seven segment display' : (lambda b,np_img : create_disp(subscript_np_array(b,np_img))),
    'voltmeter' : (lambda b,np_img : create_voltmeter(subscript_np_array(b,np_img))),
    'silver switch' : (lambda b,np_img : create_silver(subscript_np_array(b,np_img))),
    'dial' : (lambda b,np_img : create_dial(subscript_np_array(b,np_img))),
    'three state' : (lambda b,np_img : create_threestate(subscript_np_array(b,np_img))),
    'small light' : (lambda b,np_img : create_light(subscript_np_array(b, np_img), "s")),
    'green light' : (lambda b,np_img : create_light(subscript_np_array(b, np_img), "g")),
    'red light' : (lambda b,np_img : create_light(subscript_np_array(b, np_img), "r"))
}

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
    "light": lambda so : B3.light_switch.get_button_state(so.np, np.array(so.cal_on), np.array(so.cal_off)),
    "volt": lambda so: B3.voltmeter.get_voltmeter_angle(so.np),
    "silver": lambda so: B3.silver_switch.get_switch_state(so.np),
    "dial": lambda so: B3.dial.get_angle(so.np),
}

dial_dic = {
    'cont' : ((-180,180),(-10,10)),
}

def create_disp(pixels):
    r = SC.LCDDisplay('7seg_disp')
    r.measure_func = lambda so : B3.seven_seg.seven_seg_disp(so.np)
    return r

def create_silver(pixels):
    r = SC.Discrete('silver_switch')
    r.measure_func = lambda so : B3.silver_switch.get_switch_state(so.np)
    return r

def create_dial(pixels,typeof_dial='cont'):
    range_d,val_d = dial_dic[typeof_dial]
    r = SC.ContinuousDial(typeof_dial + ' dial',range_d[0],range_d[1],val_d[0],val_d[1])
    r.measure_func = lambda so : B3.dial.get_angle(so.np)
    return r

def create_threestate(pixels):
    r = SC.Discrete('threestate',valueMap={-45.0:'left',0.0:'middle',45.0:'right'})
    r.measure_func = lambda so : B3.dial.get_angle(so.np)[0]
    return r

def create_voltmeter(pixels,range_d=(-30,30),val_d=(0,15)):
    r = SC.ContinuousDial('voltmeter',range_d[0],range_d[1],val_d[0],val_d[1])
    r.measure_func = lambda so : B3.voltmeter.get_voltmeter_angle(so.np)
    return r

def create_light(pixels, typeof_light):
    r = SC.Discrete(typeof_light + ' light')
    r.measure_func = lambda so : B3.light_switch.get_button_state(so.np, np.array(so.cal_on), np.array(so.cal_off))

    
    r.cal_on = cals_dict[typeof_light]["on"]
    r.cal_off = cals_dict[typeof_light]["off"]
    return r    

def create_placeholder(pixels):
    r = SC.Discrete("light")
    return r


def get_so_list(img_colour):
    SOs = []
    # main list of all semantic objects

    boxes = B1andB2.functions_1.cv2_to_box(img_colour)

    # print(boxes)
    boxes = boxes[0:-1]
    # print(np.array(boxes)[...,1])
    # box_means = np.mean(box_arr[...,:2],axis=1)
    # boxes = sorted(boxes,key = lambda x:x[0])
    # print(boxes)

    np_img = np.asarray(img_colour)

    # print(np.shape(np_img))

    ## GET BOX TYPES FROM EMAIL
    # is this seriously what you're doing.... - B.
    # box_types is a dictionary e.g {1 (box number): "type"}
    box_types = {1:'text display', 2:'seven segment display', 3:'voltmeter', 4:'silver switch', 5:'dial', 6:'three state', 7:'small light', 8:'red light', 9:'green light'}


    for i, b in enumerate(boxes):
        print ("enumerate", i)
        print(box_types[i+1])
        
        try:
            box_type = box_types[i+1]
            SOs.append(dict_of_stuff[box_type](b,np_img))
        except:
            pass
        print("SO length", len(SOs))
        # match the correct creation function to box
        # return a variable that speciies the type of input enclosed
        # make a dictionary of all the create_typeofinput
        # type = types[i]
        # SOs.append(function_dict[type](zoomed_in_img))
        # zoomed in image by calling subscript_np_array(b,np_img)
        try:
            SOs[-1].box = b
        except:
            pass
        # except IndexError:
        # pixels = subscript_np_array(b,np_img)
        # SOs.append(create_placeholder(pixels))

    # update_so_values(SOs,img_colour)
    print(len(SOs))
    return SOs

def update_so_values(SOs,img_colour):

    for so in SOs:
        so.np = subscript_np_array(so.box,img_colour)
        try:
            so.value = so.measure_func(so)
        except:
            print('couldn\'t update SO: ' + so.meaning)
    

if __name__ == '__main__':
    img = cv2.imread('samplepic_cropped.png',1)
    SOs = get_so_list(img)
    update_so_values(SOs,img)

    for so in SOs:
        print(so.meaning)
        print(so.value)
        print(so.box)
        print('\n')


