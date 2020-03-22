import HTMLTestRunner
import os
import unittest
import time, logging
import sys


path = os.path.dirname(os.getcwd())
sys.path.append(path)

test_dir = '../test_case1'
report_dir = '../reports'
# test_dir = 'D:/PycharmProjects/office_test_project/test_case'
# report_dir = 'D:/PycharmProjects/office_test_project/reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_Open_All_Templates.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + 'Mobile_Office_Report.html'
with open(r'%s' % report_name, 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='YOZO_Mobile_Office_Report',
                                           description='yozo Android app test report',retry=1)
    logging.info('start run test case...')
    runner.run(discover)
