#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium import webdriver
import yaml
from time import ctime

with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

devices_list=['127.0.0.1:62001','127.0.0.1:62025']

def appium_desire(udid,port):
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=udid

    # desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    print('appium port: %s start run %s at %s' %(port,udid,ctime()))
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
    return driver

if __name__ == '__main__':
    appium_desire(devices_list[0],4723)
    appium_desire(devices_list[1],4725)