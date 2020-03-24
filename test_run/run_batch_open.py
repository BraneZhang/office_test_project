import HTMLTestRunner
import os
import unittest
import time, logging
import sys


path = os.path.dirname(os.getcwd())
sys.path.append(path)
from common.device import Device

test_dir = '../test_case1'
report_dir = '../reports'
# test_dir = 'D:/PycharmProjects/office_test_project/test_case'
# report_dir = 'D:/PycharmProjects/office_test_project/reports'

# 需要跑的文件夹路径  e.g  dir_path = r'E:\MSfiles\MS2003files\xls'
dir_path = r'D:\MSfiles\MS2007files\docx'
test_dirs = ['test']
# 选取需要跑的模拟器
Device.dev = '127.0.0.1:62001'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_open_files1.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + 'Mobile_Office_Report.html'
with open(r'%s' % report_name, 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='YOZO_Mobile_Office_Report',
                                           description='yozo Android app test report')
    logging.info('start run test case...')
    runner.run(discover)


