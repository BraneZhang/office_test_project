#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from businessView.pgView import PGView
from businessView.ssView import SSView
from businessView.wpView import WPView
from common.myunit import StartEnd
from common.tool import read_csv
from data.data_info import wp_templates
ss_path = '../data/SS_Online_Templates.csv'
wp_path = '../data/WP_Online_Templates.csv'
pg_path = '../data/PG_Online_Templates.csv'
wp_list = read_csv(wp_path)
ss_list = read_csv(ss_path)
pg_list = read_csv(pg_path)

@ddt
class TestOpenAllTemplates(StartEnd):

    @unittest.skip('skip test_wp_all_templates')
    # @data(*wp_list)
    def test_wp_all_templates(self, temp_file='灰色扁平化简约个人简历模板'):  # 对所有在线模板进行开档
        logging.info('==========test_wp_all_templates==========')
        hp = HomePageView(self.driver)
        # hp.login_on_needed()
        hp.create_file_preoption('wp')

        logging.info('=======search option======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchTv').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et').set_text(temp_file)
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchv').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % temp_file), 'cannot find specified file!!!')

        logging.info('=======open option======')
        bottom_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/rv')
        bottom_ele.find_element(By.XPATH, '//*[@text="%s"]' % temp_file).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        self.assertTrue(hp.is_not_visible('//*[@text="请稍等..."]'), '卡在请稍等界面')
        self.assertTrue(hp.is_not_visible('//*[contains(@text,"正在打开")]'), '卡在正在打开界面')
        self.assertTrue(hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                        '关闭按钮未显示')  # 关闭按钮显示
        button_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text
        self.assertTrue(button_name1 == '编辑', '编辑按键未显示')
        file_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        self.assertTrue(file_name1 != '', '文档标题未显示')

    @unittest.skip('skip test_ss_all_templates')
    # @data(*ss_list)
    def test_ss_all_templates(self, temp_file):  # 对所有在线模板进行开档
        logging.info('==========test_ss_all_templates==========')
        hp = HomePageView(self.driver)
        # hp.login_on_needed()
        hp.create_file_preoption('ss')

        logging.info('=======search option======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchTv').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et').set_text(temp_file)
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchv').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % temp_file), 'cannot find specified file!!!')

        logging.info('=======open option======')
        bottom_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/rv')
        bottom_ele.find_element(By.XPATH, '//*[@text="%s"]' % temp_file).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        self.assertTrue(hp.is_not_visible('//*[@text="请稍等..."]'), '卡在请稍等界面')
        self.assertTrue(hp.is_not_visible('//*[contains(@text,"正在打开")]'), '卡在正在打开界面')
        self.assertTrue(hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                        '关闭按钮未显示')  # 关闭按钮显示
        button_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text
        self.assertTrue(button_name1 == '编辑', '编辑按键未显示')
        file_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        self.assertTrue(file_name1 != '', '文档标题未显示')

    # @unittest.skip('skip test_pg_all_templates')
    # @data(*pg_list[1300:1301])
    def test_pg_all_templates(self, temp_file='小型商业广告传单'):  # 对所有在线模板进行开档
        logging.info('==========test_pg_all_templates==========')
        hp = HomePageView(self.driver)
        # hp.login_on_needed()
        hp.create_file_preoption('pg')

        logging.info('=======search option======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchTv').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et').set_text(temp_file)
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchv').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % temp_file), 'cannot find specified file!!!')

        logging.info('=======open option======')
        bottom_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/rv')
        bottom_ele.find_element(By.XPATH, '//*[@text="%s"]' % temp_file).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        self.assertTrue(hp.is_not_visible('//*[@text="请稍等..."]',180), '卡在请稍等界面')
        self.assertTrue(hp.is_not_visible('//*[contains(@text,"正在打开")]'), '卡在正在打开界面')
        self.assertTrue(hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                        '关闭按钮未显示')  # 关闭按钮显示
        button_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_button').text
        self.assertTrue(button_name1 == '编辑', '编辑按键未显示')
        file_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        self.assertTrue(file_name1 != '', '文档标题未显示')

