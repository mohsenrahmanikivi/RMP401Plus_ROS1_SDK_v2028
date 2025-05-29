#!/bin/bash

source /opt/ros/noetic/setup.bash 

rm -rf build devel 

catkin_make -DCATKIN_WHITELIST_PACKAGES='segway_msgs'
catkin_make -DCATKIN_WHITELIST_PACKAGES='segwayrmp'