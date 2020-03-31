#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium_sync.multi_appium import appium_start
from appium_sync.multi_devices_sync import *
from appium_sync.check_port import *
from time import sleep
import multiprocessing




dir_path = r'E:\MSfiles\MS2007files\docx'
dirs_list = [
    ['10000-10999'],
    ['30000-30999'],
    ['20000-20999']
             ]
devices_list = [
    '127.0.0.1:62025',
    '127.0.0.1:62001',
    '127.0.0.1:62026'
                ]


def start_appium_action(host, port, udid):
    '''检测端口是否被占用，如果没有被占用则启动appium服务'''
    # if check_port(host, port):
    #     appium_start(host, port)
    #     return True
    # else:
    #     print('appium %s start failed!' % port)
    #     return False
    if not check_port(port):
        release_port(port)
    appium_start(host, port, udid)


def need_run_dirs(test_dirs, udid):
    """获取需要进行测试的文档的文件名称"""
    suffix_path = []
    path_list = []
    for i in test_dirs:
        sub_dir_path = os.path.join(dir_path, i)
        path_list.append(sub_dir_path)
        os.system('adb -s %s shell rm -rf /mnt/shell/emulated/0/%s' % (udid, i))
        os.system('adb -s %s push %s /mnt/shell/emulated/0' % (udid, sub_dir_path))

        print(sub_dir_path)
        for root, dirs, files in os.walk(sub_dir_path):
            for file in files:
                suffix_path.append(i + '/' + file)
    return suffix_path


def start_devices_action(udid, port, sysPort, test_dirs):
    '''先检测appium服务是否启动成功，启动成功则再启动App,否则释放端口'''
    host = '127.0.0.1'
    # if start_appium_action(host, port):
    #     appium_desired(udid, port)
    # else:
    #     release_port(port)
    file_list = need_run_dirs(test_dirs, udid)
    appium_desired(udid, port, sysPort, file_list)


def appium_start_sync():
    '''并发启动appium服务'''
    print('====appium_start_sync=====')

    # 构建appium进程组
    appium_process = []

    # 加载appium进程
    for i in range(len(devices_list)):
        host = '127.0.0.1'
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=start_appium_action, args=(host, port, devices_list[i]))
        appium_process.append(appium)

    # 启动appium服务
    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    sleep(5)


def devices_start_sync():
    '''并发启动设备'''
    print('===devices_start_sync===')

    # 定义desired进程组
    desired_process = []

    # 加载desired进程
    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        sysPort = 8201 + i
        desired = multiprocessing.Process(target=start_devices_action,
                                          args=(devices_list[i], port, sysPort, dirs_list[i]))
        desired_process.append(desired)

    # 并发启动App
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


if __name__ == '__main__':
    appium_start_sync()
    devices_start_sync()
