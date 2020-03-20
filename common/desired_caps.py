import time

import yaml
import logging
import logging.config
import os

from appium import webdriver

# from test_run.run_batch_open import port, bootstrap, udid, ip, systemPort
from common.tool import Device

device = Device().get_dev()

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def get_desired_caps(devices='vivoX9'):
    with open('../config/yozo_office_caps1.yaml', 'r', encoding='utf-8') as file:
        devices_data = yaml.load(file, Loader=yaml.FullLoader)
    # print(f'devices_data:{devices_data}')
    device = ''
    for i in devices_data:
        # priant(i)
        if devices in i['desc']:
            device = i
    if device:
        return device
    else:
        logging.error('设备不在配置表中')


data = get_desired_caps(device)


def start_server():
    port, bootstrap, udid = data['port'], data['bp'], data['desired_caps']['udid']
    # os.system('adb connect %s' % udid)
    # logging.info('connect devices>>>>>>>>>>>>>')

    logging.info('start appium')
    # cmd = os.popen('netstat -ano | findstr "%s" ' % port)
    cmd = os.popen('netstat -ano | findstr "%s" ' % port)
    msg = cmd.read()
    if "LISTENING" in msg:
        print("appium服务已经启动：%s" % msg)
    else:
        print("appium服务启动：%s" % msg)
        os.system("start /b appium -a 127.0.0.1 --session-override -p %s -bp %s -U %s" % (port, bootstrap, udid))
        time.sleep(5)


def appium_desired():
    desired_caps = data['desired_caps']
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
    driver = webdriver.Remote('http://%s:%s/wd/hub' % (data['ip'], data['port']), desired_caps)
    driver.implicitly_wait(3)

    return driver


if __name__ == '__main__':
    data = get_desired_caps('yeshen01')
    print(data)
    print(type(data))
    print(data['desired_caps']['udid'])
    # print(data)

    # ss = ['A','B','C']
    # print(ss.index('C'))
