#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os

import rospy

# imports the weather service
from ros_weather.srv import *

def weather_client(city, county, village, ishourly):

    rospy.wait_for_service('req_weather')

    try:
        # req_weather 서비스 생성
        requestWeater = rospy.ServiceProxy('req_weather', Weather)

        # 호출 1 번째 방법
        resp1 = requestWeater(city, county, village, ishourly)

        # 호출 2 번째 방법
        resp2 = requestWeater.call(WeatherRequest(city, county, village, ishourly))
        print(resp1.txt)
        print(resp2.txt)

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__ == "__main__":
    weather_client(u'경기', u'김포시', u'장기동', True)
