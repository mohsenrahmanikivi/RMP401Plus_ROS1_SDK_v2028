#!/usr/bin/env python3
import rospy
from segway_msgs.srv import ros_enable_chassis_rotate_cmd
from segway_msgs.srv import ros_set_chassis_enable_cmd
from geometry_msgs.msg import Twist


import time


def enable_chassis_rotate(data):
    rospy.wait_for_service("ros_enable_chassis_rotate_cmd_srv")
    try:
        ch = rospy.ServiceProxy(
            "ros_enable_chassis_rotate_cmd_srv", ros_enable_chassis_rotate_cmd
        )
        ret = ch(True)
        print(ret)
    except:
        pass


def enable_chassis(data):
    rospy.wait_for_service("ros_set_chassis_enable_cmd_srv")
    try:
        ch = rospy.ServiceProxy(
            "ros_set_chassis_enable_cmd_srv", ros_set_chassis_enable_cmd
        )
        ret = ch(True)
        print(ret)
    except:
        pass


def pub_speed_msg(data):
    global speed_pub
    msg = Twist()
    msg.linear.x = 0
    msg.angular.z = 0
    speed_pub.publish(msg)


rospy.init_node("waypoints_tracker", anonymous=True)

speed_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

timer = rospy.Timer(rospy.Duration(0.005), pub_speed_msg)
enable_chassis_rotate([])
# enable_chassis([])
rospy.spin()
