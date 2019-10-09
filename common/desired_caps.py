import xlrd
import yaml
import logging
import logging.config
import os

from appium import webdriver

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    with open('../config/yozo_office_caps.yaml', 'r', encoding='utf-8') as file:
    # with open('../config/wx_read_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        print(data)
    desired_caps = data['desired_caps']
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
    # print( os.path.dirname(os.path.dirname(__file__)))
    appium_desired()
    # with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    #     data = yaml.load(file)
    #
    # base_dir=os.path.dirname(os.path.dirname(__file__))
    # print(os.path.dirname(__file__))
    # print(base_dir)
    #
    # app_path=os.path.join(base_dir,'app',data['appname'])
    # print(app_path)
