#!/usr/bin/env python3
'''
    Line Following program for Picar-X:

    Pay attention to modify the reference value of the grayscale module 
    according to the practical usage scenarios.Use the following: 
        px.grayscale.reference = 1400 
    or
        px.set_grayscale_reference(1400)  

'''
from picarx_improved import Picarx
from time import sleep
import numpy as np

px = Picarx()
last_state = None
current_state = None
px_power = 10
offset = 20


def outHandle():
    global last_state, current_state
    if last_state == 'left':
        px.set_dir_servo_angle(-30)
        px.backward(10)
    elif last_state == 'right':
        px.set_dir_servo_angle(30)
        px.backward(10)
    while True:
        gm_val_list = px.get_grayscale_data()
        gm_state = px.get_line_status(gm_val_list)
        print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
        currentSta = gm_state
        if currentSta != last_state:
            break
    sleep(0.001)


if __name__=='__main__':
    reference = float(input("Enter gray scale reference value: "))
    px.set_grayscale_reference(reference)
    try:
        while True:
            gm_val_list = np.linalg.norm(np.array(px.get_grayscale_data()))
            
            gm_state = px.get_line_status(gm_val_list)
            print("gm_val_list: %s, %s"%(gm_val_list, gm_state))
            sleep(0.1)

            if gm_state != "stop":
                last_state = gm_state

            if gm_state == 'forward':
                px.set_dir_servo_angle(0)
                #px.forward(px_power) 
            elif gm_state == 'left':
                px.set_dir_servo_angle(offset)
                #px.forward(px_power) 
            elif gm_state == 'right':
                px.set_dir_servo_angle(-offset)
                #px.forward(px_power) 
            else:
                outHandle()
    finally:
        px.stop()


                
