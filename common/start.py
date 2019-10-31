import logging

from appium import webdriver
import time
import yaml
import os


def start_server():
    logging.info('start appium')
    caps = get_desired_caps()
    port, bp, udid = caps['port'], caps['bp'], caps['desired_caps']['udid']
    cmd = os.popen('netstat -ano | findstr "%s" ' % port)
    msg = cmd.read()
    if "LISTENING" in msg:
        print("appium服务已经启动：%s" % msg)
    else:
        print("appium服务启动：%s" % msg)
        os.system("start /b appium -a 127.0.0.1 --session-override -p %s -bp %s -U %s" % (port, bp, udid))
        time.sleep(5)


def stop_server():
    os.system("start /b taskkill /F /t /IM node.exe")


def get_desired_caps():
    yml_path = os.path.join("../config/yozo_office_caps.yaml")
    f = open(yml_path, "r", encoding="utf-8")
    dev_info = f.read()
    f.close()
    info = yaml.load(dev_info, Loader=yaml.FullLoader)
    return info


if __name__ == "__main__":
    pass
