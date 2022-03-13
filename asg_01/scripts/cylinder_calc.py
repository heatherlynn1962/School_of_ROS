#!/usr/bin/env python
from pickle import FALSE
import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

from math import pi

radius = 0
radius_squared = 0
height = 0
weight = 0

radius_found = False
radius_squared_found = False
height_found = False
weight_found = False

def radius_callback(data):
    global radius
    global radius_found
    radius = data.data 
    radius_found = True

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

def weight_callback(data):
    global weight
    global weight_found
    weight = data.data 
    weight_found = True   

def calculate():
    if radius_found and radius_squared_found and height_found and weight_found:
        msg = Cylinder()
        msg.volume = pi * radius_squared * height
        msg.surface_area = 2 * pi * (radius * height + radius_squared)
        msg.weight = weight
        pub.publish(msg)


rospy.init_node("cylinder_calc")
rospy.Subscriber("/radius", Float64, radius_callback)
rospy.Subscriber("/radius_squared", Float64, radius_squared_callback)
rospy.Subscriber("/height", Float64, height_callback)
rospy.Subscriber("/weight", Float64, weight_callback)
pub = rospy.Publisher("/cylinder", Cylinder, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1)
