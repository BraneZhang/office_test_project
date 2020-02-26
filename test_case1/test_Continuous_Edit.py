#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import time
import unittest

from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from businessView.ssView import SSView
from common.myunit import StartEnd


class TestContinuousEdit(StartEnd):

    # @unittest.skip('skip test_ss_new_edit_save')
    def test_ss_new_edit_save(self):
        os.system('adb shell rm -rf /storage/emulated/0/ss_new_edit_save.xls')
        logging.info('==========test_ss_new_edit_save==========')
        ss = SSView(self.driver)
        ss.create_file('ss', 978, 1754)  # 基于夜神模拟器修改

        ss.save_new_file('ss_new_edit_save', 'local')
        self.assertTrue(ss.get_toast_message('保存成功'))

        time.sleep(1)
        # x, y, width, height = ss.cell_location() #模拟器该功能无用直接给定数据
        # self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_cancel').click()
        x, y, width, height = 94, 258, 197, 46
        start_time = time.time()
        last_time = 0

        # while last_time < 2 * 60 * 60:
        while last_time < 60 * 60:
            for i in range(10):
                ss.tap(x + width * 0.5, y + height * (i + 0.5))
                ss.cell_edit()
                self.driver.keyevent(32)
                if i == 9:
                    ss.swipe(x + width, y, x, y)
            end_time = time.time()
            last_time = end_time - start_time
            logging.info('last_time>>>>>>>>%s' % last_time)

        ss.show_sheet()
        self.driver.find_element(By.XPATH, '//*[@text="工作表2"]').click()
        start_time = time.time()
        last_time1 = 0
        while last_time1 < 60 * 60:
            for i in range(10):
                ss.tap(x + width * 0.5, y + height * (i + 0.5))
                ss.cell_edit()
                self.driver.keyevent(32)
                if i == 9:
                    ss.swipe(x + width, y, x, y)
            end_time = time.time()
            last_time1 = end_time - start_time
            logging.info('last_time1>>>>>>>>%s' % last_time1)

        self.driver.find_element(By.XPATH, '//*[@text="工作表3"]').click()
        start_time = time.time()
        last_time2 = 0
        while last_time2 < 60 * 60:
            for i in range(10):
                ss.tap(x + width * 0.5, y + height * (i + 0.5))
                ss.cell_edit()
                self.driver.keyevent(32)
                if i == 9:
                    ss.swipe(x + width, y, x, y)
            end_time = time.time()
            last_time2 = end_time - start_time
            logging.info('last_time2>>>>>>>>%s' % last_time2)

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_back').click()
        ss.save_file()
        self.assertTrue(ss.get_toast_message('保存成功'))

        ss.group_button_click('文件')
        ss.swipe_options()
        ss.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_file_info').click()
        size1 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()

        search_result = ss.search_file('ss_new_edit_save.xls')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = ss.open_file('ss_new_edit_save.xls')
        self.assertEqual(open_result, True, '打开失败')
        ss.group_button_click('文件')
        ss.swipe_options()
        ss.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_file_info').click()
        size2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        self.assertTrue(size1 == size2, '文件内容丢失')

    # @unittest.skip('skip test_wp_new_edit_save')
    def test_wp_new_edit_save(self):
        os.system('adb shell rm -rf /storage/emulated/0/wp_new_edit_save.doc')
        logging.info('==========test_wp_new_edit_save==========')
        hp = HomePageView(self.driver)
        hp.create_file('wp', 978, 1754)  # 基于夜神模拟器修改

        hp.save_new_file('wp_new_edit_save', 'local')
        self.assertTrue(hp.get_toast_message('保存成功'))

        # 编辑
        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_scale_motion_helper_layout_id').click()  # 进入编辑状态
        start_time = time.time()
        last_time = 0

        while last_time < 2 * 60 * 60:
            # while last_time < 1 * 60:
            for i in range(100):
                logging.info('>>>>>>>>No.%s' % i)
                self.driver.keyevent(32)
            end_time = time.time()
            last_time = end_time - start_time
            logging.info('last_time>>>>>>>>%s' % last_time)
        else:
            hp.save_file()
            self.assertTrue(hp.get_toast_message('保存成功'))
        hp.group_button_click('文件')
        hp.swipe_options()
        hp.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_file_info').click()
        size1 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()

        search_result = hp.search_file('wp_new_edit_save.doc')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = hp.open_file('wp_new_edit_save.doc')
        self.assertEqual(open_result, True, '打开失败')
        hp.group_button_click('文件')
        hp.swipe_options()
        hp.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_file_info').click()
        size2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        self.assertTrue(size1 == size2, '文件内容丢失')
