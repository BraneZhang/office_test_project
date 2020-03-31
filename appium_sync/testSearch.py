#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from selenium.webdriver.common.by import By


class testSearch(object):

    def __init__(self, driver):
        self.driver = driver

    def test_search(self):
        logging.info('test')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys('.docx')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()