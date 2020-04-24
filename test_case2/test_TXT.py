#!/user/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.common_fun import Common
from data import data_info

index_share_list = data_info.index_share_list


@ddt
class TestTXT(StartEnd):

    def open_TXT_file(self):
        """
        打开PDF文件，若打开的是损坏的文件，关闭重新打开其他PDF文件
        :return:
        """
        hp = HomePageView(self.driver)
        hp.open_random_file('.txt')
        time.sleep(2)

        # 显示文档名称
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_txt_title_name').text
        self.assertTrue('.txt' in file_title, '未显示TXT文档名称')

    # @unittest.skip('skip test_TXT_rotate')
    def test_TXT_rotate(self):
        """
        TXT横竖屏模式切换
        :return: None
        """
        logging.info('==========test_TXT_rotate==========')
        self.open_TXT_file()

        # 横竖屏切换
        logging.info('==========横竖屏切换==========')
        hp = HomePageView(self.driver)
        hp.screen_rotate('LANDSCAPE')
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_txt_title_name').text
        self.assertTrue('.txt' in file_title, '竖屏切换横屏模式未显示TXT文档名称')

        hp.screen_rotate('PORTRAIT')
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_txt_title_name').text
        self.assertTrue('.txt' in file_title, '横屏切换竖屏模式未显示TXT文档名称')

        logging.info('==========close file and validate==========')
        # 点击'x'关闭文档
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
        time.sleep(2)
        # 验证文档已关闭
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_txt_title_name')
        except NoSuchElementException:
            self.assertTrue(True, '点击"X"TXT未关闭')
        else:
            self.assertTrue(False, '点击"X"TXT未关闭')

    # @unittest.skip('skip test_TXT_fitToScreen')
    def test_TXT_fitToScreen(self):
        """
        适应屏幕模式、分页模式-复制（较大文件不会出现全选）
        :return:
        """
        logging.info('==========test_TXT_fitToScreen==========')
        self.open_TXT_file()

        # 验证默认进入适应屏幕模式
        logging.info('==========验证默认进入适应屏幕模式==========')
        page_mode = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_page_model')
        mode_state = page_mode.get_attribute('selected')
        self.assertEqual(mode_state, 'true', '打开TXT文档未默认设置适应屏幕模式')
        size_dic = self.driver.get_window_size()
        TouchAction(self.driver).long_press(
            x=int(size_dic.get('width') * 0.5), y=int(size_dic.get('height') * 0.5)).release().perform()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/text_selected_button_copy')
        except NoSuchElementException:
            self.assertTrue(False, '适应屏幕模式页面长按未出现复制菜单')
        else:
            self.assertTrue(True)

        # 进入分页模式
        logging.info('==========进入分页模式==========')
        page_mode.click()
        time.sleep(2)
        self.driver.keyevent(4)
        mode_state = page_mode.get_attribute('selected')
        self.assertEqual(mode_state, 'false', '未关闭TXT适应屏幕模式')
        size_dic = self.driver.get_window_size()
        TouchAction(self.driver).long_press(
            x=int(size_dic.get('width') * 0.5), y=int(size_dic.get('height') * 0.5)).release().perform()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/text_selected_button_copy')
        except NoSuchElementException:
            self.assertTrue(False, '分页模式页面长按未出现复制菜单')
        else:
            self.assertTrue(True)

    # @unittest.skip('skip test_TXT_print')
    def test_TXT_print(self):
        """
        TXT打印
        :return:None
        """
        logging.info('==========test_TXT_print==========')
        self.open_TXT_file()

        # 打印-保存为PDF
        logging.info('==========打印-保存为PDF==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_print').click()
        ele = WebDriverWait(self.driver, 300).until(
            lambda x: x.find_element(By.ID, 'com.android.printspooler:id/destination_spinner'))
        ele.click()
        self.driver.find_element(By.XPATH, '//*[@text="保存为 PDF"]').click()
        time.sleep(3)
        # 选中与未选中效果验证
        logging.info('==========选中与未选中效果验证==========')
        print_page = self.driver.find_element(By.ID, 'com.android.printspooler:id/page_content')
        page_state = print_page.get_attribute('selected')
        self.assertEqual(page_state, 'true', 'TXT首页未被选中')

        # 若只有一页则无法取消
        page_num = self.driver.find_element(By.ID, 'com.android.printspooler:id/page_number').text
        if page_num != '1 / 1':
            print_page.click()
            page_state = print_page.get_attribute('selected')
            self.assertEqual(page_state, 'false', 'TXT首页取消选中失败')

        # 返回关闭
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    # @unittest.skip('skip test_TXT_fileInfo')
    def test_TXT_fileInfo(self):
        """
        TXT文档信息
        :return:None
        """
        logging.info('==========test_TXT_fileInfo==========')
        self.open_TXT_file()
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_txt_title_name').text

        logging.info('==========查看文档信息==========')
        # 打开文档信息
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_info').click()
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text
        file_type = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text
        file_loc = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        file_size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        file_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text
        # 验证信息
        logging.info('==========验证信息==========')
        self.assertEqual(file_title, file_name + '.' + file_type, '文件名错误')
        self.assertTrue(file_title in file_loc, '文件位置错误')
        self.assertNotEqual(file_size, ' ', '文件大小为空')
        self.assertNotEqual(file_time, ' ', '上次修改时间为空')

        # 返回关闭
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    # @unittest.skip('skip test_TXT_changeFrontSize')
    def test_TXT_changeFrontSize(self):
        """
        增大/减小字号
        :return:
        """
        logging.info('==========test_TXT_changeFrontSize==========')
        self.open_TXT_file()

        # 增大字号
        logging.info('==========增大字号==========')
        flag = False
        while not flag:
            self.driver.find_element(By.ID, 'com.yozo.office:id/tab_font_increase').click()
            try:
                self.driver.find_element(By.XPATH, '//*[contains(@text,已是最大字号)]')
            except NoSuchElementException:
                pass
            else:
                flag = True

        # 减小字号
        logging.info('==========减小字号==========')
        flag = False
        while not flag:
            self.driver.find_element(By.ID, 'com.yozo.office:id/tab_font_decrease').click()
            try:
                self.driver.find_element(By.XPATH, '//*[contains(@text,已是最小字号)]')
            except NoSuchElementException:
                pass
            else:
                flag = True

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    # @unittest.skip('skip test_TXT_fullscreen')
    def test_TXT_fullscreen(self):
        logging.info('==========test_PDF_fullscreen==========')
        self.open_TXT_file()

        # 向上滑动页面进入全屏模式
        logging.info('==========向上滑动页面进入全屏模式==========')
        common = Common(self.driver)
        common.swipeUp()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/bottom')
        except NoSuchElementException:
            self.assertTrue(True)
        else:
            self.assertTrue(False, '未进入全屏模式')

        # 点击屏幕退出全屏
        logging.info('==========点击屏幕退出全屏==========')
        size_dic = self.driver.get_window_size()
        TouchAction(self.driver).tap(x=int(size_dic.get('width') * 0.5), y=int(size_dic.get('height') * 0.5)).perform()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/bottom')
        except NoSuchElementException:
            self.assertTrue(False, '未退出全屏模式')
        else:
            self.assertTrue(True)

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    # @unittest.skip('skip test_TXT_percentage')
    def test_TXT_percentage(self):
        logging.info('==========test_TXT_percentage==========')
        self.open_TXT_file()

        # 向上滑动页面显示百分比
        logging.info('==========向上滑动页面显示百分比==========')
        common = Common(self.driver)
        common.swipeUp()

        # 验证百分比显示
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozotxt_document_percent')
        except NoSuchElementException:
            self.assertTrue(False, '向上滑动TXT文档未显示百分比')
        else:
            self.assertTrue(True)

        # 退出全屏
        size_dic = self.driver.get_window_size()
        TouchAction(self.driver).tap(x=int(size_dic.get('width') * 0.5), y=int(size_dic.get('height') * 0.5)).perform()

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()