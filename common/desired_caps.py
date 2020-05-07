import time

import yaml
import logging
import logging.config
import os

from appium import webdriver

from appium_sync.check_port import release_port
from common.device import Device
from common.tool import get_project_path

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

data = {}


def get_desired_caps(devices='127.0.0.1:62001'):
    with open('../config/yozo_office_caps.yaml', 'r', encoding='utf-8') as file:
        devices_data = yaml.load(file, Loader=yaml.FullLoader)
    for i in devices_data:
        if devices == i['desc']:
            return i
    logging.error('设备不在配置表中')
    return {}


def stop_server():
    # data = get_desired_caps(device)
    port = data['port']
    release_port(port)


def start_server():
    global data
    device = Device.dev
    data = get_desired_caps(device)
    Device.data = data
    # print(f'data:{data}')
    port, bootstrap, udid = data['port'], data['bp'], data['desired_caps']['udid']
    Device.udid = udid

    # 连接设备
    # logging.info('adb connect device')
    # os.system('adb devices')
    # time.sleep(3)
    # os.system('adb connect %s' % udid)

    # 释放端口
    release_port(port)

    logging.info('start appium')
    # cmd = os.popen('netstat -ano | findstr "%s" ' % port)
    # msg = cmd.read()
    # if "LISTENING" in msg:
    #     print("appium服务已经启动：%s" % msg)
    # else:
    # print("appium服务启动：%s" % msg)
    os.system("start /b appium -a 127.0.0.1 --session-override -p %s -bp %s -U %s" % (port, bootstrap, udid))
    time.sleep(5)


def appium_desired():
    # data = get_desired_caps(device)
    # desired_caps = data['desired_caps']
    # desired_caps['systemPort'] = systemPort
    # 使用adb shell input 代替Yosemite输入  ?ime_method=ADBIME
    # from airtest.core.api import *
    # text("hello")
    # 第二种写法：init_device("Android", ime_method="ADBIME")
    # auto_setup(__file__, devices=["Android:///"+"%s?ime_method=ADBIME" % data['desired_caps']['udid']])
    # desired_caps['platformName']=data['platformName']
    # desired_caps['platformVersion']=data['platformVersion']
    # desired_caps['deviceName']=data['deviceName']

    # #app属性 值为绝对路径，如果有appActivity和appPackage则不需要此属性
    # base_dir = os.path.dirname(os.path.dirname(__file__)) #项目绝对路径
    # app_path = os.path.join(base_dir, 'app', data['appname'])
    # desired_caps['app']=app_path

    # desired_caps['appPackage']=data['appPackage']
    # desired_caps['appActivity']=data['appActivity']
    # desired_caps['noReset']=data['noReset']

    # desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    # desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote('http://%s:%s/wd/hub' % (data['ip'], data['port']), data['desired_caps'])
    driver.implicitly_wait(3)

    return driver
