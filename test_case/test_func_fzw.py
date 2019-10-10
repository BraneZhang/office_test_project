#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import random
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.loginView import LoginView
from businessView.openView import OpenView
from businessView.pgView import PGView
from businessView.ssView import SSView
from businessView.wpView import WPView
from common.myunit import StartEnd


share_list = ['wp_wx', 'wp_qq', 'wp_ding', 'wp_mail', 'ss_wx', 'ss_qq', 'ss_ding',
              'ss_mail', 'pg_wx', 'pg_qq', 'pg_ding', 'pg_mail']
wps = ['wp', 'ss', 'pg']
ps = ['ss', 'pg']
wp = ['wp', 'pg']
ws = ['wp', 'ss']
search_dict = {'wp': 'docx', 'ss': 'xlsx', 'pg': 'pptx'}
switch_list = ['无切换', '平滑淡出', '从全黑淡出', '切出', '从全黑切出', '溶解', '向下擦除', '向左擦除', '向右擦除',
               '向上擦除', '扇形展开', '从下抽出', '从左抽出', '从右抽出', '从上抽出', '从左下抽出', '从左上抽出',
               '从右下抽出', '从右上抽出', '盒状收缩', '盒状展开', '1根轮辐', '2根轮辐', '3根轮辐', '4根轮辐', '8根轮辐',
               '上下收缩', '上下展开', '左右收缩', '左右展开', '左下展开', '左上展开', '右下展开', '右上展开', '圆形',
               '菱形', '加号', '新闻快报', '向下推出', '向左推出', '向右推出', '向上推出', '向下插入', '向左插入',
               '向右插入', '向上插入', '向左下插入', '向左上插入', '向右下插入', '向右上插入', '水平百叶窗',
               '垂直百叶窗', '横向棋盘式', '纵向棋盘式', '水平梳理', '垂直梳理', '水平线条', '垂直线条', '随机']
csv_file = '../data/account.csv'
folder_list = ['手机', '我的文档', 'Download', 'QQ', '微信']
index_share_list = ['qq', 'wechat', 'email', 'more']


@ddt
class TestFunc1(StartEnd):
    @unittest.skip('skip test_close_file')
    @data(*wps)
    def test_close_file(self, file_type):
        """
        关闭功能（X）
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_close_file==========')
        ov = OpenView(self.driver)
        ov.open_random_file(search_dict[file_type])
        ov.close_file()
        self.assertTrue(ov.check_close_file())

    @unittest.skip('skip test_share_newFile')
    @data(*share_list)
    def test_share_newFile(self, share_info):
        """
        新建文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_share_newFile==========')
        file_type = share_info.split('_')[0]
        share_type = share_info.split('_')[1]

        logging.info('==========create and save new File==========')
        cv = CreateView(self.driver)
        cv.create_file(file_type)
        cv.save_new_file('%s%s分享' % (file_type, share_type), 'local')
        time.sleep(1)
        cv.cover_file(True)
        self.assertTrue(cv.get_toast_message('保存成功'))

        logging.info('==========share new File==========')
        gv = GeneralView(self.driver)
        gv.share_file(file_type, share_type)

    @unittest.skip('skip test_share_editFile')
    @data(*share_list)
    def test_share_editFile(self, share_info):
        """
        编辑文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_share_newFile==========')
        file_type = share_info.split('_')[0]
        share_type = share_info.split('_')[1]

        logging.info('==========edit and save File==========')
        ov = OpenView(self.driver)
        ov.open_random_file(search_dict[file_type])

        gv = GeneralView(self.driver)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        gv.group_button_click('插入')
        gv.insert_shape(file_type, 1)

        cv = CreateView(self.driver)
        cv.save_file()
        self.assertTrue(cv.get_toast_message('保存成功'))

        logging.info('==========share new File==========')
        gv = GeneralView(self.driver)
        gv.share_file(file_type, share_type)

    @unittest.skip('skip test_file_info')
    @data(*wps)
    def test_file_info(self, file_type):
        """
        文档信息
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_share_newFile==========')
        ov = OpenView(self.driver)
        ov.open_random_file("行列复制.%s" % search_dict[file_type])

        logging.info('==========show file info==========')
        gv = GeneralView(self.driver)
        gv.wait_loading()
        gv.file_info(file_type)
