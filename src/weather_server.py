#!/usr/bin/env python
NAME = 'weather_server'

from ros_weather.srv import *
import skweather as wh
import rospy

def req_weather(req):
    print("request : %s, %s, %s, %s" % (req.city, req.county, req.village, req.ishourly))
    return wh.requestCurrentWeather(req.city, req.county, req.village, req.ishourly)

def weather_server():
    rospy.init_node(NAME)
    s = rospy.Service('req_weather', Weather, req_weather)

    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    weather_server()
