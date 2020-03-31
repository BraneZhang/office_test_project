#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from time import ctime

def appium_start(host,port,udid):
    '''启动appium server'''
    bootstrap_port = str(port + 1)
    # cmd = 'start /b appium -a ' + host + ' --session-override -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port) + ' -U '+ udid

    print('%s at %s' %(cmd,ctime()))
    subprocess.Popen(cmd, shell=True,stdout=open('../logs/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = '127.0.0.1'
    for i in range(2):
        port = 4723 + 2 * i
        appium_start(host, port)