#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


import multiprocessing
import yaml
import logging.config
# import logging.
from appium import webdriver
from time import ctime


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

from appium_sync.testSearch import testSearch
from appium_sync.test_batch_files_open import openFiles

with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def appium_desired(udid, port, sysPort, files):

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid
    desired_caps['systemPort'] = sysPort

    # desired_caps['app']=data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    print('appium port:%s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    # return driver

    # k = testSearch(driver)
    open = openFiles(driver)
    # k.test_search()
    open.test_bat_open_files(files, udid)
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
