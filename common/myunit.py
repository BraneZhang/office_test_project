import unittest
from appium.webdriver.connectiontype import ConnectionType

from common.desired_caps import start_server, appium_desired, stop_server
import logging
import warnings

from common.device import Device


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
        self.driver.set_network_connection(ConnectionType.WIFI_ONLY)


    def tearDown(self):
        logging.info('====tearDown====')
        self.driver.close_app()
