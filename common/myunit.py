import unittest
from common.desired_caps import start_server, appium_desired, stop_server
import logging
import warnings



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
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        self.driver.close_app()
