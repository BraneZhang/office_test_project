#!/user/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from data import data_info
from common.common_fun import Common

index_share_list = data_info.index_share_list


@ddt
class TestPDF(StartEnd):

    def open_PDF_file(self):
        """
        打开PDF文件，若打开的是损坏的文件，关闭重新打开其他PDF文件
        :return:
        """
        flag = False
        while not flag:
            hp = HomePageView(self.driver)
            hp.open_random_file('.pdf')
            time.sleep(2)
            try:
                self.driver.find_element(By.XPATH, '//*[@content-desc="载入 PDF 时发生错误。"]')
            except NoSuchElementException:
                flag = True
                # 显示文档名称
                file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_pdf_title_name').text
                self.assertTrue('.pdf' in file_title, '未显示PDF文档名称')
            else:
                logging.info('该PDF文档错误，不能正常打开')
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
                self.driver.keyevent(4)

    # @unittest.skip('skip test_PDF_rotate')
    def test_PDF_rotate(self):
        """
        PDF横竖屏模式切换
        :return: None
        """
        logging.info('==========test_PDF_Rotate==========')
        self.open_PDF_file()

        logging.info('==========rotate screen==========')
        # 横竖屏切换
        hp = HomePageView(self.driver)
        hp.screen_rotate('LANDSCAPE')
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_pdf_title_name').text
        self.assertTrue('.pdf' in file_title, '竖屏切换横屏模式未显示PDF文档名称')

        hp.screen_rotate('PORTRAIT')
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_pdf_title_name').text
        self.assertTrue('.pdf' in file_title, '横屏切换竖屏模式未显示PDF文档名称')

        logging.info('==========close file and validate==========')
        # 点击'x'关闭文档
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
        time.sleep(2)
        # 验证文档已关闭
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_pdf_title_name')
        except NoSuchElementException:
            self.assertTrue(True, '点击"X"PDF未关闭')
        else:
            self.assertTrue(False, '点击"X"PDF未关闭')

    # @unittest.skip('skip test_PDF_thumbnail')
    def test_PDF_thumbnail(self):
        """
        PDF缩略图，目前只做到验证缩略图数量不为0
        :return: None
        """
        logging.info('==========test_PDF_Thumbnail==========')
        self.open_PDF_file()
        # 打开缩略图
        self.driver.find_element(By.ID, 'com.yozo.office:id/rl_thumbnail_bg').click()
        time.sleep(3)

        # 当前只可验证缩略图数量与页码数相同
        thumbnail_list = self.driver.find_elements(By.XPATH, '//*[contains(@content-desc, "页码") ]')
        self.assertTrue(len(thumbnail_list) > 0, '缩略图数量为0或为损坏的文件')
        # 点击'x'关闭文档
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    @unittest.skip('TODO')
    @data(*index_share_list)
    def test_PDF_share(self, way='more'):
        logging.info('==========test_PDF_share==========')
        self.open_PDF_file()

        # 查看文件大小
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_info').click()
        file_size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        size_list = file_size.split(' ')

        # 分享
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_%s_share' % way).click()
        if way == 'more':
            self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_shareitem')[0].click()
        if size_list[1] == 'MB':
            pass
        # 需要账号支持

    # @unittest.skip('skip test_PDF_print')
    def test_PDF_print(self):
        logging.info('==========test_PDF_print==========')
        self.open_PDF_file()

        # 打印-保存为PDF
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_print').click()
        ele = WebDriverWait(self.driver, 60).until(
            lambda x: x.find_element(By.ID, 'com.android.printspooler:id/destination_spinner'))
        ele.click()
        self.driver.find_element(By.XPATH, '//*[@text="保存为 PDF"]').click()
        time.sleep(3)
        # 选中与未选中效果验证
        print_page = self.driver.find_element(By.ID, 'com.android.printspooler:id/page_content')
        page_state = print_page.get_attribute('selected')
        self.assertEqual(page_state, 'true', 'PDF首页未被选中')

        page_num = self.driver.find_element(By.ID, 'com.android.printspooler:id/page_number').text
        if page_num != '1 / 1':
            print_page.click()
            page_state = print_page.get_attribute('selected')
            self.assertEqual(page_state, 'false', 'PDF首页取消选中失败')

        # 返回关闭
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    # @unittest.skip('skip test_PDF_fileInfo')
    def test_PDF_fileInfo(self):
        logging.info('==========test_PDF_info==========')
        self.open_PDF_file()

        # 打开文档信息
        file_title = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_pdf_title_name').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_info').click()
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text
        file_type = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text
        file_loc = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        file_size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        file_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text
        # 验证信息
        self.assertEqual(file_title, file_name+'.'+file_type, '文件名错误')
        self.assertTrue(file_title in file_loc, '文件位置错误')
        self.assertNotEqual(file_size, ' ', '文件大小为空')
        self.assertNotEqual(file_time, ' ', '上次修改时间为空')

        # 返回关闭
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

    # @unittest.skip('skip test_PDF_fullscreen')
    def test_PDF_fullscreen(self):
        logging.info('==========test_PDF_fullscreen==========')
        self.open_PDF_file()

        # 向上滑动页面进入全屏模式
        common = Common(self.driver)
        common.swipeUp()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/bottom')
        except NoSuchElementException:
            self.assertTrue(True)
        else:
            self.assertTrue(False, '未进入全屏模式')

        # 点击屏幕退出全屏
        size_dic = self.driver.get_window_size()
        TouchAction(self.driver).tap(x=int(size_dic.get('width') * 0.5), y=int(size_dic.get('height') * 0.5)).perform()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/bottom')
        except NoSuchElementException:
            self.assertTrue(False, '未退出全屏模式')
        else:
            self.assertTrue(True)

        # 缩略图不可进入全屏
        self.driver.find_element(By.ID, 'com.yozo.office:id/tab_thumbnail').click()
        common.swipeUp()
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/bottom')
        except NoSuchElementException:
            self.assertTrue(False, '缩略图展开模式，进入全屏模式')

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
