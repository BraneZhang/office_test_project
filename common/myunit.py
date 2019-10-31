import os
import unittest
from common.desired_caps import appium_desired
import logging
import warnings

from common.start import start_server, stop_server, get_desired_caps


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info('=====setUpClass=====')
        # 忽略ResourceWarning警告类型
        warnings.simplefilter("ignore", ResourceWarning)
        start_server()

    @classmethod
    def tearDownClass(cls):
        logging.info('=====tearDownClass=====')
        stop_server()

    def setUp(self):
        logging.info('=====setUp====')
        # os.system('adb shell pm clear com.tencent.mobileqq')
        # os.system('adb shell pm clear com.tencent.mm')
        # os.system('adb shell pm clear com.vivo.email')
        # os.system('adb shell pm clear com.alibaba.android.rimet')
        dev = get_desired_caps()['desired_caps']['udid']
        os.system('adb -s %s shell am force-stop com.tencent.mobileqq' % dev)
        os.system('adb -s %s shell am force-stop com.tencent.mm' % dev)
        os.system('adb -s %s shell am force-stop com.vivo.email' % dev)
        os.system('adb -s %s shell am force-stop com.alibaba.android.rimet' % dev)
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        self.driver.close_app()
