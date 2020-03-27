import HTMLTestRunner
import os
import unittest
import time
import logging
import sys

from common.device import Device

path = os.path.dirname(os.getcwd())
sys.path.append(path)

test_dir = '../test_case1'
report_dir = '../reports'

Device.dev = 'GWY0217805003862'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_Continuous_Edit.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + 'Mobile_Office_Report.html'
with open(r'%s' % report_name, 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='YOZO_Mobile_Office_Report',
                                           description='yozo Android app test report')
    logging.info('start run test case...')
    runner.run(discover)
