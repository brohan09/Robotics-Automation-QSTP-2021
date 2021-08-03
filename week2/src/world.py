#! /usr/bin/python3.8

import rospy
from std_msgs.msg import String

rospy.init_node("world")

pub2 = rospy.Publisher("world",String)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub2.publish("world !")
    rate.sleep()
