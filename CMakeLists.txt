cmake_minimum_required(VERSION 2.8.3)
project(ros_weather)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  std_msgs
)


## Generate services in the 'srv' folder
add_service_files(DIRECTORY srv FILES Weather.srv)


## Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES std_msgs)



catkin_package(CATKIN_DEPENDS message_runtime std_msgs)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
