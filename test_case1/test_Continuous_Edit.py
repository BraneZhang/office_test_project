#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import time
import unittest
import random
import hashlib


from selenium.webdriver.common.by import By
from businessView.homePageView import HomePageView
from businessView.ssView import SSView
from common.myunit import StartEnd
from common.device import Device
udid = Device.dev
path = os.getcwd()


class TestContinuousEdit(StartEnd):
    @staticmethod
    def hash_file(self, filename):
        """该函数返回传入文件的SHA-1哈希值"""

        # 创建一个哈希对象
        h = hashlib.sha1()

        # 以二进制读取模式打开一个文件
        with open(filename, 'rb') as file:
            # 循环直到文件结束
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)

        # 返回摘要的十六进制表示
        return h.hexdigest()

    @unittest.skip('skip test_ss_new_edit_save')
    def test_ss_new_edit_save(self):
        os.system('adb shell rm -rf /storage/emulated/0/ss_new_edit_save.xls')
        logging.info('==========test_ss_new_edit_save==========')
        ss = SSView(self.driver)
        ss.create_file('ss', 921, 1560)  # 基于夜神模拟器修改

        ss.save_new_file('ss_new_edit_save', 'local')
        self.assertTrue(ss.get_toast_message('保存成功'))

        time.sleep(1)
        x, y, width, height = ss.cell_location() #模拟器该功能无用直接给定数据
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_cancel').click()
        # x, y, width, height = 94, 258, 197, 46
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
            for i in range(100000):
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

    @unittest.skip('skip test_wp_new_edit_save')
    def test_wp_new_edit_save(self):
        os.system('adb shell rm -rf /storage/emulated/0/wp_new_edit_save.doc')
        logging.info('==========test_wp_new_edit_save==========')
        hp = HomePageView(self.driver)
        hp.create_file('wp', 921, 1560)

        hp.save_new_file('wp_new_edit_save', 'local')
        self.assertTrue(hp.get_toast_message('保存成功'))
        # 编辑
        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_scale_motion_helper_layout_id').click()  # 进入编辑状态
        start_time = time.time()

        words_count_path = '//*[@text="字符数（不含空格）"]/../android.widget.LinearLayout/android.widget.TextView'
        count = 0
        while count < 86400:
            logging.info('>>>>>>>>No.%d' % (count + 1))
            self.driver.keyevent(32)
            last_time = time.time() - start_time
            logging.info('last_time>>>>>>>>%s' % last_time)
            count += 1
        else:
            hp.group_button_click('查看')
            hp.swipe_options()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_count').click()
            words_count_before_save = self.driver.find_element(By.XPATH, words_count_path).text
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
            self.assertTrue(hp.get_toast_message('保存成功'))
            self.driver.keyevent(4)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()

        search_result = hp.search_file('wp_new_edit_save.doc')
        self.assertTrue(search_result is True, '搜索失败')
        open_result = hp.open_file('wp_new_edit_save.doc')
        self.assertEqual(open_result, True, '打开失败')
        hp.group_button_click('查看')
        hp.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_count').click()
        words_count = self.driver.find_element(By.XPATH, words_count_path).text
        self.assertTrue(int(words_count_before_save) == int(words_count) == count, '文件内容丢失')

    @unittest.skip('skip test_wp_edit_save')
    def test_wp_edit_save(self):
        logging.info('==========test_wp_edit_save==========')
        hp = HomePageView(self.driver)
        random_num = random.randint(0, 1)
        if random_num == 0:
            hp.open_random_file('.doc')
        else:
            hp.open_random_file('.docx')
        time.sleep(3)

        # 查看文件名
        hp.group_button_click('文件')
        hp.swipe_options()
        hp.swipe_options()
        self.driver.find_element(By.XPATH, '//*[@text="文档信息"]').click()
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text
        file_type = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text
        self.driver.keyevent(4)

        words_count_path = '//*[@text="字符数（不含空格）"]/../android.widget.LinearLayout/android.widget.TextView'
        hp.group_button_click('查看')
        hp.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_count').click()
        words_count_before_edit = self.driver.find_element(By.XPATH, words_count_path).text

        # 编辑
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()  # 进入编辑状态
        start_time = time.time()
        count = 0
        while count < 86400:  # 约需要20h
            logging.info('>>>>>>>>No.%d' % (count + 1))
            self.driver.keyevent(32)
            last_time = time.time() - start_time
            logging.info('last_time>>>>>>>>%s' % last_time)
            count += 1
        else:
            hp.group_button_click('查看')
            hp.swipe_options()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_count').click()
            words_count_after_edit = self.driver.find_element(By.XPATH, words_count_path).text
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
            self.assertTrue(hp.get_toast_message('保存成功'))
            self.driver.keyevent(4)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_back').click()

        self.assertEqual(int(words_count_before_edit)+count, int(words_count_after_edit),  '文件编辑失败，编辑后字符数不正确')
        search_result = hp.search_file('%s.%s' % (file_name, file_type))
        self.assertTrue(search_result is True, '搜索失败')
        open_result = hp.open_file('%s.%s' % (file_name, file_type))
        self.assertEqual(open_result, True, '打开失败')
        hp.group_button_click('查看')
        hp.swipe_options()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_count').click()
        words_count = self.driver.find_element(By.XPATH, words_count_path).text
        self.assertTrue(int(words_count) == count, '文件内容丢失')

    # @unittest.skip('skip test_ss_edit_save')
    def test_ss_edit_save(self):
        logging.info('==========test_ss_edit_save==========')
        hp = HomePageView(self.driver)
        file_name = '0247201.xls'
        hp.open_random_file(file_name)

        # 查看文件名
        hp.group_button_click('文件')
        hp.swipe_options()
        hp.swipe_options()
        self.driver.find_element(By.XPATH, '//*[@text="文档信息"]').click()
        file_loc = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        self.driver.keyevent(4)

        # 复制手机中文件至本地并获取原文件hash
        os.system('adb -s %s pull %s %s' % (udid, file_loc, path))
        file_hash = self.hash_file(self, path+'\\'+file_name)
        os.rename(path+'\\'+file_name, path+'\\'+'temp')

        # 编辑
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()  # 进入编辑状态
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_edit_container').click()
        start_time = time.time()
        count = 0
        while count < 85000:  # 约需要20h
            logging.info('>>>>>>>>No.%d' % (count + 1))
            self.driver.keyevent(32)
            last_time = time.time() - start_time
            logging.info('last_time>>>>>>>>%s' % last_time)
            count += 1
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
            self.assertTrue(hp.get_toast_message('保存成功'))
            self.driver.keyevent(4)
            self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_back').click()

        # 重新复制文件并获取新的hash值
        os.system('adb -s %s pull %s %s' % (udid, file_loc, path))
        file_hash_new = self.hash_file(self, path+'\\'+file_name)

        # 验证两次哈希值不同
        self.assertNotEqual(file_hash, file_hash_new, '两次Hash一直表示文件内容为修改，即保存失败！')

        # 修改文件名
        os.replace(path + '\\' + 'temp', path + '\\' + file_name)
        os.system('adb -s %s push %s %s' % (udid, path+'\\'+file_name, file_loc))
        # 删除本地文件
        os.remove(path + '\\' + file_name)

