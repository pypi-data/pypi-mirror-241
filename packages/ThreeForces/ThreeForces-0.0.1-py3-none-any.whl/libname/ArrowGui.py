# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:14:20 2023

@author: herac
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

#import libraries
#visualisation library, arduino, maths, numerical
from vpython import *
import numpy as np
import math #from random 
#%matplotlib inline
import pyfirmata
import time

# Define a function to update the graph in real-time
def update_graph(curve_x,curve_y,curve_z,start_time,current_time,previous_time,force_x,force_y,force_z):
    current_time = time.time() - start_time
    delta_time = current_time - previous_time
    previous_time = current_time
    curve_x.plot(current_time,force_x)
    curve_y.plot(current_time,force_y)
    curve_z.plot(current_time,force_z)


def arrow3D(com,input1,input2,input3,input4):
    
    #arduino board connection
    board = pyfirmata.Arduino(com)
    it = pyfirmata.util.Iterator(board)
    it.start()
    
    #analog input A0,A1,A2,A3
    analog_input = board.get_pin(input1)
    analog_input1 = board.get_pin(input2)
    analog_input2 = board.get_pin(input3)
    analog_input3 = board.get_pin(input4)
    
    #OBJECTS WITH BACKGROUND VISUALISATION
    scene = canvas(width=1000, height=600, length = 1000, center=vector(0,0,0), range=3, background=color.white)
    sensor = box(pos=vector(0,0,0),axis=vector(1,0,0), length=3, height=0.3, width=3, shaftwidth=1, color = color.black)
    
    #create empty array for calibration
    force_x_array = []
    force_y_array = []
    force_z_array = []
    
    # Create the force graph
    my_graph = graph(width=600, height=400, title="Force vs Time", xtitle="Time / s", ytitle="Force / N")
    curve_x = gcurve(color=color.blue,label="Fx")
    curve_y = gcurve(color=color.red,label="Fy")
    curve_z = gcurve(color=color.orange,label="Fz")
    
    start_time = time.time()
    current_time = 0
    previous_time = 0
    initial_fx = 0
    
    while True:
        #analog read
        calibration_value = (5.0/1023)*450
        
        analog_value = analog_input.read()
        analog_value1 = analog_input1.read()
        analog_value2 = analog_input2.read()
        analog_value3 = analog_input3.read()
        
        if analog_value == None:
            analog_value=0
        else:
            analog_value = analog_value*calibration_value
            
        if analog_value1 == None:
            analog_value1=0
        else:
            analog_value1 = analog_value1*calibration_value
        
        if analog_value2 == None:
            analog_value2=0
        else:
             analog_value2 = analog_value2*calibration_value
        
        if analog_value3 == None:
            analog_value3=0
        else:
             analog_value3 = analog_value3*calibration_value
    
         
        #4channel to x,y,z conversion 
        FSRx=(analog_value-analog_value2)
        FSRy=(analog_value1-analog_value3)
        FSRz=(analog_value+analog_value1+analog_value2+analog_value3)
        #time.sleep(0.1)
        ### data from sensor
        force_x = FSRx
        force_y = FSRy
        force_z = FSRz
        
        #get first value from sensor
        force_x_array.append(force_x)
        force_y_array.append(force_y)
        force_z_array.append(force_z)
        #assign first value from sensor in the empty array
        initial_x = force_x_array[0]
        initial_y = force_y_array[0]
        initial_z = force_z_array[0]
       
        force_vector = vector(force_x,force_y,force_z)
        #print("Force vector = ", force_vector)
       
        #force magnitude calculation, r
        force = np.sqrt((force_x**2) + (force_y**2) + (force_z**2))
        #print("Total force = ", force, "Newtons")
       
        # angle with respect to the xy-plane normal at contact point, theta, phi
        angle = np.arccos(force_z / force)
        anglephi= np.arctan(force_y/np.abs(force_x))
        
        force_2 = vector(force,angle,anglephi)
        
        text_label = label(
            text="Fx = {:.3f} N\nFy = {:.3f} N\nFz = {:.3f} N\nθ = {:.3f} radians\nφ = {:.3f} radians".format(force_x, force_y, force_z, angle, anglephi),
            pos=vector(0, 0, 0), 
            xoffset=170, 
            yoffset=-170)
        text_label.box = False
        text_label.line = False
        
        # Update the force graph
        update_graph(curve_x,curve_y,curve_z,start_time,current_time,previous_time,force_x,force_y,force_z)
        
        # y-axis as the vertical
        # arrow scales like total force
        #arrow_vector = arrow(pos = vector(0,0,0), axis=vector((np.pi/4)-np.cos(anglephi), force, (np.pi/4)-np.cos(angle)))
       
        #arrow visualisation
        arrow_vector = arrow(pos = vector(0,0,0), axis=vector(force_x-initial_x,-(force_z-initial_z),force_y-initial_y ))
     
        sleep(0.00001)
        arrow_vector.visible = False
        
        