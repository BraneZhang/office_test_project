#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.common_fun import Common


class OpenView(Common):

    def close_file(self):
        logging.info('======close_file=====')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()  # 关闭功能

    def open_file(self, file_name):
        logging.info('======open_file_%s=====' % file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()  # 点击搜索功能
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(file_name)  # 输入搜索内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % file_name).click()  # 打开对应文件

    def check_open_status(self, file_name):
        logging.info('======test_open_status_%s=====' % file_name)
        try:
            # 查找指定元素判断是否加载成功
            self.find_element(By.XPATH, "//*[@resource-id='com.yozo.office:id/yozo_ui_option_group_button']")
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
            self.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
        except NoSuchElementException:
            logging.error(file_name + 'open fail!')
            self.getScreenShot(file_name + 'open fail')
            return False
        else:
            logging.info(file_name + 'open success!')
            return True
