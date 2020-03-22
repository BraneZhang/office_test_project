#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from appium import webdriver
import yaml
from time import ctime
import multiprocessing

with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as file:
    # with open('../config/yozo_office_caps1.yaml','r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def appium_desired(udid, port):

    #连接设备
    os.system('adb connect %s' % udid)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid

    # desired_caps['app']=data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    print('appium port:%s start run %s at %s' % (port, udid, ctime()))
    # os.system("start /b appium -a 127.0.0.1 --session-override -p %s -bp %s -U %s" % (port, str(port + 1), udid))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


# 构建desired进程租
desired_process = []

# 加载desied进程
for i in range(len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))
    desired_process.append(desired)

if __name__ == '__main__':
    print(data)
    # 启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
