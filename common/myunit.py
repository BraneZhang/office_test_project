import unittest
from common.desired_caps import appium_desired
import logging

from common.start import start_server, stop_server


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info('=====setUpClass=====')
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
