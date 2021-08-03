#! /usr/bin/python3.8

import rospy

from std_msgs.msg import String


class hello:
    m1 = ""
    m2 = ""
    
#    hw = m1 + m2

    def __init__(self):

        self.pub = rospy.Publisher("helloWorld" , String)

        self.sub1 = rospy.Subscriber("hello" , String , self.callback1)
        self.sub2 = rospy.Subscriber("world" , String , self.callback2)


    def callback1(self,msg):
        self.m1 = msg.data


    def callback2(self,msg):
        self.m2 = msg.data

    def p(self):
        self.pub.publish(self.m1 + ' ' + self.m2)


obj = hello()


rospy.init_node('helloWorld')

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    obj.p()
    rate.sleep()

