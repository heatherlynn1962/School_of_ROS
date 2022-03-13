#!/usr/bin/env python

"""
    Calculates the density of a cylinder based upon values
    from subscribed topics. The weight is then published to
    the topic /weight.
    
    Author: Heather Brewer
    Date: 3/14/2022
"""



import rospy
from std_msgs.msg import Float64

from math import pi

# These are global varibles 
radius_squared = 0
height = 0
density = 0

radius_squared_found = False
height_found = False
density_found = False



def radius_squared_callback(data):
    global radius_squared
    global radius_squared_found
    radius_squared = data.data 
    radius_squared_found = True
    
def height_callback(data):
    global height
    global height_found
    height = data.data 
    height_found = True

def density_callback(data):
    global density
    global density_found
    density = data.data 
    density_found = True

def calculate():
    if  radius_squared_found and height_found and density_found:
        weight = pi * radius_squared * height * density
        pub.publish(weight)      

rospy.init_node("weight_calc")
rospy.Subscriber("/radius_squared", Float64, radius_squared_callback)
rospy.Subscriber("/height", Float64, height_callback)
rospy.Subscriber("/density", Float64, density_callback)
pub = rospy.Publisher("/weight", Float64, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1)
