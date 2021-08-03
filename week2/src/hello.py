#! /usr/bin/python3.8

import rospy
from std_msgs.msg import String

rospy.init_node("hello")

pub1 = rospy.Publisher("hello", String)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub1.publish("Hello")
    rate.sleep()

