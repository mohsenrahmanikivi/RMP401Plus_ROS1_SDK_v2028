cmake_minimum_required(VERSION 3.0.2)
project(rospy_package)

find_package(catkin REQUIRED COMPONENTS
  rosmsg
  rospy
  nav_msgs
  geometry_msgs
)

catkin_python_setup()