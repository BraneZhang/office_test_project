#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import random
import time
import unittest

from appium.webdriver.connectiontype import ConnectionType
from ddt import ddt, data, unpack, file_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from businessView.elementRepo import *
from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from data import data_info
from common.common_fun import Common
from data.data_info import *

screenshot_file = '../screenshots/'
options = ['移动', '复制']
act_index = ['last', 'alldoc', 'star', 'cloud']
act_index1 = ['last', 'alldoc', 'star']
x_create = 926
y_create = 1669


@ddt
class TestHomePage(StartEnd):

    # ======2020_05_07====== #

    # @unittest.skip('test_nonet_upload')
    def test_multi_files_upload(self, index_type='alldoc'):  # 上传大于20个
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
            rand_option = random.choice(type_list)
            hp.click_element(*rand_option)
            # hp.select_file_type('all')
        hp.file_more_info(0)
        hp.click_element(*multi_select)
        hp.click_element(*multi_upload)
        self.assertTrue(hp.get_message(select_file_first))
        hp.click_element(*select_all)
        hp.click_element(*multi_upload)
        self.assertTrue(hp.get_message(great20))
        hp.file_more_info(0)
        hp.click_element(*multi_select)
        eles = hp.find_elements(*item)
        for i in eles:
            i.click()
        hp.click_element(*multi_upload)
        hp.click_element(*upload_save)
        hp.click_element(*pop_confirm2)
        hp.click_element(*pop_cancel)
        self.assertTrue(hp.get_message(cancelled))

    # @unittest.skip('test_nonet_upload')
    def test_nonet_upload(self, index_type='alldoc'):  # 未联网-登录上传
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
        hp.wifi_trans('开启')
        hp.click_element(*return1)
        hp.jump_to_index(index_type)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        if index_type == 'alldoc':
            hp.select_file_type('all')
        hp.file_more_info(0)
        hp.click_element(*upload)
        self.assertTrue(hp.get_message(no_wifi))
        self.driver.keyevent(4)
        hp.click_element(*return2)
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')
        hp.file_more_info(0)
        hp.click_element(*upload)
        # hp.click_element(*upload_save)
        # hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(upload_fail))
        hp.click_element(*pop_confirm2)
        hp.click_element(*return2)
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
        hp.wifi_trans('开启')

    # @unittest.skip('test_unlogin_upload')
    def test_unlogin_upload(self, index_type='alldoc'):  # 联网/未联网-未登录上传
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')
        hp.file_more_info(0)
        hp.click_element(*upload)
        self.assertTrue(hp.get_message(login_first))
        time.sleep(2)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(0)
        hp.click_element(*upload)
        self.assertTrue(hp.get_message(login_first))

    # @unittest.skip('test_multi_files_copy')
    def test_multi_files_copy(self, index_type='alldoc'):  # 多选移动文件
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')
        hp = HomePageView(self.driver)
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')

        hp.file_more_info(0)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[0].click()
        hp.find_elements(*item)[1].click()
        hp.click_element(*multi_copy)
        hp.find_elements(*item)[0].click()
        hp.click_element(*new_folder)
        hp.find_element(*folder_name).send_keys('1111')
        hp.click_element(*pop_confirm2)
        time.sleep(2)
        hp.find_elements(*item)[0].click()
        hp.click_element(*paste)
        # if hp.get_message(cover_tips):
        #     rand_option = random.choice([skip, cover, keep])
        #     hp.click_element(*rand_option)
        self.assertTrue(hp.get_message(option_success))
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')

    # @unittest.skip('test_multi_files_move')
    def test_multi_files_move(self, index_type='alldoc'):  # 多选移动文件
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')
        hp = HomePageView(self.driver)
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')

        hp.file_more_info(0)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[0].click()
        hp.find_elements(*item)[1].click()
        hp.click_element(*multi_move)
        hp.find_elements(*item)[0].click()
        time.sleep(1)
        hp.click_element(*new_folder)
        hp.find_element(*folder_name).send_keys('1111')
        hp.click_element(*pop_confirm2)
        hp.find_elements(*item)[0].click()
        hp.click_element(*paste)
        if hp.get_message(cover_tips):
            rand_option = random.choice([skip, cover, keep])
            hp.click_element(*rand_option)
        self.assertTrue(hp.get_message(option_success))
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')

    # @unittest.skip('test_last_multi_select_file')
    def test_multi_select_file(self, index_type='last'):  # 文档多选
        hp = HomePageView(self.driver)
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')
        hp.file_more_info(0)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[0].click()
        num1 = hp.find_element(*selected_num).text
        self.assertTrue(int(num1) == 1)
        hp.click_element(*select_all)
        num2 = hp.find_element(*selected_num).text
        self.assertTrue(int(num2) >= 1)
        hp.click_element(*select_all)
        num3 = hp.find_element(*selected_num).text
        self.assertTrue(int(num3) == 0)
        hp.click_element(*multi_cancel)

    # @unittest.skip('test_file_delete')
    # @data(*index_list)
    def test_file_delete(self, index_type='alldoc'):  # 文档删除
        hp = HomePageView(self.driver)

        if index_type == 'alldoc':
            hp.jump_to_index(index_type)
            hp.select_file_type('all')
        elif index_type == 'last':
            hp.jump_to_index('alldoc')
            hp.select_file_type('all')
            hp.file_more_info(0)
            hp.find_elements(*item)[0].click()
            time.sleep(2)
            hp.click_element(*close)
            hp.click_element(*return2)
            hp.jump_to_index(index_type)

        logging.info('==========delete operation==========')
        hp.file_more_info(0)
        hp.click_element(*delete)
        hp.click_element(*pop_cancel)
        hp.file_more_info(0)
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
        if index_type == 'last':
            self.assertTrue(hp.get_toast_message('此操作只是将文件从最近列表中删除'))
        else:
            self.assertTrue(hp.get_toast_message('操作成功'))

    # ======2020_05_06====== #

    # @unittest.skip('test_file_move')
    # @data(*index_list)
    def test_file_move(self, index_type='alldoc'):  # 移动文件
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')
        hp = HomePageView(self.driver)
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')
        hp.file_more_info(0)

        location = hp.find_element(*file_location).text
        fileName = location[location.rindex('/') + 1:]
        logging.info('=========copy_file==========')
        hp.click_element(*move)
        hp.find_elements(*item)[0].click()
        time.sleep(1)
        hp.click_element(*new_folder)
        hp.find_element(*folder_name).send_keys('1111')
        hp.click_element(*pop_confirm2)
        hp.find_elements(*item)[0].click()
        hp.click_element(*paste)
        self.assertTrue(hp.get_toast_message('操作成功'))
        msg = os.system('adb shell ls /storage/emulated/0/0000/1111/%s' % fileName)
        self.assertTrue(msg == 0, 'move fail')
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')

    # @unittest.skip('test_file_copy')
    # @data(*index_list)
    def test_file_copy(self, index_type='alldoc'):  # 复制文件
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')
        hp = HomePageView(self.driver)
        hp.jump_to_index(index_type)
        if index_type == 'alldoc':
            hp.select_file_type('all')
        hp.file_more_info(0)

        location = hp.find_element(*file_location).text
        fileName = location[location.rindex('/') + 1:]
        logging.info('=========copy_file==========')
        hp.click_element(*copy)
        self.driver.find_element(By.ID, 'com.yozo.office:id/file_item').click()
        time.sleep(1)
        hp.find_elements(*item)[1].click()
        time.sleep(1)
        hp.click_element(*new_folder)
        hp.find_element(*folder_name).send_keys('1111')
        hp.click_element(*pop_confirm2)
        hp.find_elements(*item)[1].click()
        hp.click_element(*paste)
        self.assertTrue(hp.get_toast_message('操作成功'))
        msg = os.system('adb shell ls /storage/emulated/0/0000/1111/%s' % fileName)
        self.assertTrue(msg == 0, 'copy fail')
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')

    @unittest.skip('test_file_rename')
    @data(*index_list)
    def test_file_rename(self, index_type='alldoc'):  # 文档重命名
        hp = HomePageView(self.driver)
        if hp.check_login_status():
            hp.logout_action()
        if index_type == 'alldoc':
            hp.jump_to_index('alldoc')
            hp.select_file_type('all')
        hp.file_more_info(0)
        self.driver.hide_keyboard()
        suffix = hp.find_element(*file_type).text.strip()
        hp.click_element(*rename)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))
        time.sleep(2)

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            file_name = i
            self.driver.hide_keyboard()
            hp.find_element(*rename_edit).send_keys(file_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        file_name = '01234567890123456789012345678901234567890'
        hp.find_element(*rename_edit).send_keys(file_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        file_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        hp.find_element(*rename_edit).send_keys(file_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % (file_name + '.' + suffix)))

    @unittest.skip('test_alldoc_file_info')
    @data(*index_list)
    def test_file_info(self, index_type='alldoc'):  # 打开_文档信息
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        time.sleep(1)
        hp.file_more_info(0)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text
        file_type = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text
        file_size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        file_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text
        file_location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        self.assertFalse(file_name == '-')
        self.assertFalse(file_type == '-')
        self.assertFalse(file_size == '-')
        self.assertFalse(file_time == '-')
        self.assertFalse(file_location == '-')

    @unittest.skip('test_create_template')
    @data(*index_wps)
    def test_create_template(self, file_index='alldoc_wp'):  # 最近/打开_新建_在线模板
        hp = HomePageView(self.driver)
        index_type = file_index.split('_')[0]
        file_type = file_index.split('_')[1]
        hp.jump_to_index(index_type)
        hp.create_file_preoption(file_type, x_create, y_create)
        # 新建模板
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        # self.driver.find_element(By.XPATH,
        #                          '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]').click()
        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*apply)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
        hp.click_element(*mode_switch)
        time.sleep(1)
        ele.screenshot('../screenshots/temp_create.png')
        hp.click_element(*mode_switch)
        if file_type == 'wp':
            hp.tap(200, 350)
        elif file_type == 'ss':
            hp.group_button_click('签批')
            hp.swipe(400, 1000, 800, 1000)
        else:
            ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
            self.driver.find_element(By.XPATH,
                                     '//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.View[1]').click()
            hp.tap(670, 2004)
        self.driver.keyevent(30)
        hp.click_element(*mode_switch)
        time.sleep(1)
        ele.screenshot('../screenshots/temp_edit.png')
        hp.click_element(*save)
        hp.click_element(*save_local)
        hp.click_element(*save_confirm)
        hp.cover_file(True)
        hp.click_element(*close)
        hp.click_element(*apply)
        hp.click_element(*mode_switch)
        ele.screenshot('../screenshots/temp_recreate.png')
        time.sleep(1)
        result1 = hp.compare_pic('temp_create.png', 'temp_recreate.png')
        result2 = hp.compare_pic('temp_edit.png', 'temp_recreate.png')
        self.assertEqual(result1, 0.0, '模板被修改')
        self.assertNotEqual(result2, 0.0)

    @unittest.skip('test_nonet_create_mytemplate_download')
    @data(*index_wps)
    def test_nonet_create_mytemplate_download(self, file_index='alldoc_wp'):  # 未联网_新建_我的模板_下载
        hp = HomePageView(self.driver)
        hp.login_needed()
        index_type = file_index.split('_')[0]
        file_type = file_index.split('_')[1]
        hp.jump_to_index(index_type)
        hp.create_file_preoption(file_type, x_create, y_create)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        time.sleep(1)

        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*download)
        hp.click_element(*return1)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        time.sleep(2)
        hp.click_element(*mytemplate)
        self.assertTrue(hp.get_toast_message('服务器DNS解析失败,请检查您的网络'))
        time.sleep(2)
        hp.click_element(*my_download)
        hp.click_element(*batch_manage)
        hp.click_element(*delete_temp)
        self.assertTrue(hp.get_toast_message('请选择要编辑的模板'))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % temp_name).click()
        hp.click_element(*delete_temp)
        hp.click_element(*pop_confirm)
        self.assertFalse(hp.get_toast_message(temp_name))
        hp.click_element(*finish)
        self.assertTrue(hp.get_toast_message('暂无模板'))

    @unittest.skip('test_create_mytemplate_download')
    @data(*index_wps)
    def test_create_mytemplate_download(self, file_index='alldoc_wp'):  # 新建_我的模板_下载
        hp = HomePageView(self.driver)
        hp.login_needed()
        index_type = file_index.split('_')[0]
        file_type = file_index.split('_')[1]
        hp.jump_to_index(index_type)
        hp.create_file_preoption(file_type, x_create, y_create)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        time.sleep(1)

        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*download)
        hp.click_element(*return1)
        hp.click_element(*mytemplate)
        hp.click_element(*my_download)
        hp.click_element(*batch_manage)
        hp.click_element(*delete_temp)
        self.assertTrue(hp.get_toast_message('请选择要编辑的模板'))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % temp_name).click()
        hp.click_element(*delete_temp)
        hp.click_element(*pop_confirm)
        self.assertFalse(hp.get_toast_message(temp_name))

    @unittest.skip('test_create_mytemplate_subscribe')
    @data(*index_wps)
    def test_create_mytemplate_subscribe(self, file_index='alldoc_wp'):  # 新建_我的模板_收藏
        hp = HomePageView(self.driver)
        hp.login_needed()
        index_type = file_index.split('_')[0]
        file_type = file_index.split('_')[1]
        hp.jump_to_index(index_type)
        hp.create_file_preoption(file_type, x_create, y_create)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()

        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*subscribe)
        hp.click_element(*return1)
        hp.click_element(*mytemplate)
        hp.click_element(*batch_manage)
        hp.click_element(*unsubscribe)
        self.assertTrue(hp.get_toast_message('请选择要编辑的模板'))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % temp_name).click()
        hp.click_element(*unsubscribe)
        hp.click_element(*pop_confirm)
        self.assertFalse(hp.get_toast_message(temp_name))

    @unittest.skip('skip test_create_unlogin_mytemplate')
    @data(*index_wps)
    def test_create_unlogin_mytemplate(self, file_index='alldoc_wp'):  # 打开/云文档/标星_新建_联网/未联网未登录情况下我的模板
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        index_type = file_index.split('_')[0]
        hp.jump_to_index(index_type)
        file_type = file_index.split('_')[1]
        hp.create_file_preoption(file_type, x_create, y_create)
        hp.click_element(*mytemplate)
        self.assertTrue(hp.get_toast_message('其他登录方式'))
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.click_element(*login_cancel)
        hp.click_element(*mytemplate)
        self.assertTrue(hp.get_toast_message('其他登录方式'))

    @unittest.skip('skip test_nonet_create_mytemplate')
    @data(*index_wps)
    def test_nonet_create_mytemplate(self, file_index='alldoc_wp'):  # 打开/云文档/标星_新建_未联网登录情况下我的模板收藏
        hp = HomePageView(self.driver)
        hp.login_needed()
        index_type = file_index.split('_')[0]
        hp.jump_to_index(index_type)
        file_type = file_index.split('_')[1]
        hp.create_file_preoption(file_type, x_create, y_create)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.click_element(*mytemplate)
        self.assertTrue(hp.get_message(dns_fail))
        hp.click_element(*batch_manage)
        hp.click_element(*unsubscribe)

        self.assertTrue(hp.get_message(select_temp))

    # ======2020_04_30====== #
    @unittest.skip('skip test_alldoc_common_use_add')
    def test_alldoc_common_use_add(self):  # 打开_常用位置_上移下移移除
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.click_element(*add_folder)
        hp.click_element(*add2common)
        self.assertTrue(hp.get_message(select_folder2add))
        folder1 = hp.find_elements(*item)[0]
        folder1_name = folder1.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        folder1.find_element(By.ID, 'com.yozo.office:id/lay_check').click()
        hp.swipe_options('//androidx.recyclerview.widget.RecyclerView')
        folder2 = hp.find_elements(*item)[1]
        folder2_name = folder2.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        folder2.find_element(By.ID, 'com.yozo.office:id/lay_check').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_add').click()
        hp.swipe_options('//*[@resource-id="com.yozo.office:id/lv_floder_list"]')
        hp.swipe_options('//*[@resource-id="com.yozo.office:id/lv_floder_list"]')
        ele = self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder1_name)
        x = ele.location['x']
        y = ele.location['y']
        hp.long_press(x, y)
        hp.click_element(*move_down)
        ele = self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder1_name)
        x = ele.location['x']
        y = ele.location['y']
        hp.long_press(x, y)
        hp.click_element(*move_up)
        ele = self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder1_name)
        x = ele.location['x']
        y = ele.location['y']
        hp.long_press(x, y)
        hp.click_element(*remove)
        ele = self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder2_name)
        x = ele.location['x']
        y = ele.location['y']
        hp.long_press(x, y)
        hp.click_element(*remove)

    # @unittest.skip('skip test_alldoc_sort_file')
    def test_alldoc_sort_file(self):  # “打开”文档按条件排序
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
        sort_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in type_list:
            hp.select_file_type(i)
            for m in sort_list:
                for n in order_list:
                    hp.sort_files(m, n)

    @unittest.skip('skip test_alldoc_unlogin_cloud')
    def test_alldoc_unlogin_cloud(self):
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('alldoc')

        self.assertTrue(hp.get_message(unlogin_cloud))
        hp.click_element(*cloud)
        self.assertTrue(hp.get_message(login_button))

    # ======2020_04_23====== #

    @unittest.skip('test_last_file_list_refresh')
    def test_last_file_list_refresh(self):  # 最近开档列表刷新
        hp = HomePageView(self.driver)
        eles = hp.find_elements(*item)
        file_name = eles[-1].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        eles[-1].click()
        time.sleep(2)
        hp.click_element(*close)
        time.sleep(1)
        first_file = hp.find_elements(*item_title)[0].text
        self.assertEqual(file_name, first_file, '列表未刷新')

    @unittest.skip('test_last_nonet_create_blank_file')
    @data(*wps)
    def test_last_nonet_create_blank_file(self, file_type='ss'):
        logging.info('==========test_create_blank_file==========')
        hp = HomePageView(self.driver)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.create_file_preoption(file_type, x_create, y_create)
        hp.click_element(*create_nonet_blank)
        self.assertTrue(hp.get_message(net4more_temp))
        file_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        hp.save_new_file(file_name, 'local')
        hp.click_element(*close)
        hp.click_element(*return1)
        time.sleep(1)
        hp.find_elements(*item)[0].click()
        time.sleep(2)
        hp.click_element(*close)

    @unittest.skip('test_last_nonet_create_blank_file')
    @data(*wps)
    def test_last_create_subscribe_nologin(self, file_type='ss'):  # 最近_未登录_新建_收藏在线模板
        logging.info('==========test_create_blank_file==========')
        hp = HomePageView(self.driver)
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('last')
        hp.create_file_preoption(file_type, x_create, y_create)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()

        hp.click_element(*subscribe)
        self.assertTrue(hp.get_message(login_first1))

    @unittest.skip('test_create_blank_file')
    @data(*index_wps)
    def test_create_blank_file(self, file_index='last_pg'):
        logging.info('==========test_create_blank_file==========')
        hp = HomePageView(self.driver)
        index_type = file_index.split('_')[0]
        file_type = file_index.split('_')[1]
        hp.jump_to_index(index_type)
        hp.create_file_preoption(file_type, x_create, y_create)
        hp.click_element(*create_blank)
        file_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        hp.save_new_file(file_name, 'local')
        hp.click_element(*close)
        hp.click_element(*return1)
        time.sleep(1)
        hp.find_elements(*item)[0].click()
        time.sleep(2)
        hp.click_element(*close)

    @unittest.skip('test_last_create_template_search')
    @data(*template_search)
    def test_last_create_template_search(self,  file_index='last_pg'):  # 最近_新建_模板搜索
        logging.info('==========test_last_create_temp_change==========')
        hp = HomePageView(self.driver)

        # 新建模板
        index_type = file_index.split('_')[0]
        file_type = file_index.split('_')[1]
        hp.jump_to_index(index_type)
        hp.create_file_preoption(file_type, x_create, y_create)

        hp.click_element(*temp_search)
        keywords = search_template_dict[file_type]

        # 不存在的模板
        hp.find_element(*temp_search_input).send_keys('****')
        hp.click_element(*temp_search_start)
        time.sleep(1)
        self.assertTrue(hp.get_message(no_related_temp))

        # 存在模板搜索
        for i in keywords:
            hp.find_element(*temp_search_input).send_keys(i)
            hp.click_element(*temp_search_start)
            time.sleep(1)
            self.assertFalse(hp.get_message(no_related_temp), '模板名或分类搜索失败')

        logging.info('======历史记录显示======')
        hp.find_element(*temp_search_input).clear()
        results = list(map(lambda e: hp.get_element_result('//*[@text="%s"]' % e), keywords))
        print(False in results)
        self.assertFalse(False in results)

        logging.info('======历史记录选取======')
        record_ele = hp.find_element(*search_history)
        record_ele.find_elements(By.XPATH, '//android.widget.TextView')[0].click()
        select_record = record_ele.find_elements(By.XPATH, '//android.widget.TextView')[0].text
        edit_content = hp.find_element(*temp_search_input).text
        self.assertTrue(select_record == edit_content, '历史记录选取错误')

        logging.info('======历史记录删除======')
        hp.find_element(*temp_search_input).clear()
        hp.click_element(*clear_history)
        clear_result = record_ele.find_elements(By.XPATH, '//android.widget.TextView')
        print(len(clear_result))
        self.assertTrue(len(clear_result) == 0, '历史记录删除失败')

    @unittest.skip('test_last_create_temp_change')
    # @data(*wps)
    def test_last_create_temp_change(self, file_type='ss'):  # 最近/打开_新建_在线模板换一批
        logging.info('==========test_last_create_temp_change==========')
        hp = HomePageView(self.driver)
        # 新建模板
        hp.create_file_preoption(file_type, 925, 2055)
        while not hp.get_toast_message('没有更多数据'):
            if hp.get_toast_message('换一换'):
                temp_name1 = self.driver.find_element(By.ID, 'com.yozo.office:id/tpTitle1').text
                self.driver.find_element(By.ID, 'com.yozo.office:id/changeTv').click()
                time.sleep(1)
                temp_name2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tpTitle1').text
                self.assertFalse(temp_name1 == temp_name2)
            # ele = self.driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
            ele = '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]'
            loc = hp.get_swipe_xy(ele)
            self.driver.swipe(loc[1], loc[5], loc[1], loc[3])

    @unittest.skip('test_last_create_templ_hot')
    @data(*wps)
    def test_last_create_templ_hot(self, file_type='ss'):  # 最近/打开_新建_在线模板最热下载
        logging.info('==========test_last_create_templ_hot==========')
        hp = HomePageView(self.driver)
        # 新建模板
        hp.create_file_preoption(file_type, 925, 2055)
        while not hp.get_toast_message('没有更多数据'):
            hp.swipe_options('//androidx.recyclerview.widget.RecyclerView')

        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        time.sleep(1)
        temp_name = self.driver.find_element(By.ID, 'com.yozo.office:id/title').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        if not hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_mode"]', 60):
            raise
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        time.sleep(1)
        ele.screenshot('../screenshots/temp_create.png')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        if file_type == 'wp':
            hp.tap(200, 350)
        elif file_type == 'ss':
            hp.group_button_click('签批')
            hp.swipe(400, 1000, 800, 1000)
        else:
            ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
            self.driver.find_element(By.XPATH,
                                     '//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.View[1]').click()
            hp.tap(670, 2004)
        self.driver.keyevent(30)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        time.sleep(1)
        ele.screenshot('../screenshots/temp_edit.png')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        hp.cover_file(True)
        hp.click_element(*close)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        if not hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_mode"]', 60):
            raise
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        time.sleep(1)
        ele.screenshot('../screenshots/temp_recreate.png')
        result1 = hp.compare_pic('temp_create.png', 'temp_recreate.png')
        # self.assertEqual(result1, 0.0, '模板被修改')
        if file_type == 'wp':
            self.assertEqual(result1, 0.0, '模板被修改')
        else:
            self.assertLessEqual(result1, 500, '模板被修改')

    @unittest.skip('test_last_create_temp_recommend')
    @data(*wps)
    def test_last_create_temp_recommend(self, file_type='pg'):  # 最近/打开_新建_在线模板今日推荐
        hp = HomePageView(self.driver)
        # 新建模板
        hp.create_file_preoption(file_type, 925, 2055)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        time.sleep(1)
        temp_name = self.driver.find_element(By.ID, 'com.yozo.office:id/title').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        if not hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_mode"]', 60):
            raise
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        time.sleep(1)
        ele.screenshot('../screenshots/temp_create.png')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        if file_type == 'wp':
            hp.tap(200, 350)
        elif file_type == 'ss':
            hp.group_button_click('签批')
            hp.swipe(400, 1000, 800, 1000)
        else:
            ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
            self.driver.find_element(By.XPATH,
                                     '//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.View[1]').click()
            hp.tap(670, 2004)
        self.driver.keyevent(30)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        time.sleep(1)
        ele.screenshot('../screenshots/temp_edit.png')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        hp.cover_file(True)
        hp.click_element(*close)
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        if not hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_mode"]', 60):
            raise
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        time.sleep(1)
        ele.screenshot('../screenshots/temp_recreate.png')
        result1 = hp.compare_pic('temp_create.png', 'temp_recreate.png')
        # self.assertEqual(result1, 0.0, '模板被修改')
        if file_type == 'wp':
            self.assertEqual(result1, 0.0, '模板被修改')
        else:
            self.assertLessEqual(result1, 500, '模板被修改')

    # ======2020_04_22====== #
    @unittest.skip('test_last_nonet_share')
    @data(*index_share_list)
    def test_last_nonet_share(self, way='qq'):  # 最近_未联网_分享到_微信/QQ/邮箱
        logging.info('==========test_last_nonet_share==========')
        hp = HomePageView(self.driver)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_%s_share' % way).click()
        if way == 'more':
            self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_shareitem')[0].click()
        self.assertTrue(hp.get_element_result('//*[contains(@text,分享失败)]'))

    @unittest.skip('test_last_upload_file')
    def test_last_upload_file(self):  # 最近_上传
        logging.info('==========test_last_upload_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        time.sleep(1)
        hp.find_elements(*item)[0].click()
        time.sleep(2)
        hp.click_element(*close)
        self.driver.keyevent(4)
        hp.jump_to_index('last')
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        self.assertTrue(hp.get_toast_message('上传成功'))

    @unittest.skip('test_last_nonet_upload02')
    def test_last_nonet_upload02(self):  # 最近_未联网_上传
        logging.info('==========test_last_nonet_upload==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.XPATH, '//*[@text="系统设置"]').click()
        hp.wifi_trans('关闭')
        self.driver.keyevent(4)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.find_elements(*item)[0].click()
        time.sleep(2)
        hp.click_element(*close)
        self.driver.keyevent(4)
        hp.jump_to_index('last')
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        self.assertTrue(hp.get_toast_message('上传失败'))

    @unittest.skip('test_last_nonet_upload')
    def test_last_nonet_upload(self):  # 最近_未联网_上传
        logging.info('==========test_last_nonet_upload==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.find_elements(*item)[0].click()
        time.sleep(2)
        hp.click_element(*close)
        self.driver.keyevent(4)
        hp.jump_to_index('last')
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_toast_message('当前为非wifi环境，无法进行文件传输\n如需更改设置请到我的->系统设置中进行更改'))

    @unittest.skip('test_last_unlogin_upload')
    def test_last_unlogin_upload(self):  # 最近_联网/未联网未登录本机文档上传
        logging.info('==========test_last_unlogin_upload==========')
        hp = HomePageView(self.driver)
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('last')
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_toast_message('请先登录账号'))
        time.sleep(2)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_toast_message('请先登录账号'))

    @unittest.skip('test_last_multi_select_file')
    def test_last_multi_select_file(self):  # 文档多选_删除
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[0].click()
        num1 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num1) == 1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        num2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num2) >= 1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_check_bottom_upload').click()
        self.assertTrue(hp.get_toast_message('文件已存在于云文档'))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@text="取消全选"]').click()
        num3 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num3) == 0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_check_bottom_del').click()
        self.assertTrue(hp.get_toast_message('请先选择文件'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_check_bottom_upload').click()
        self.assertTrue(hp.get_toast_message('请先选择文件'))
        hp.find_elements(*item)[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_check_bottom_del').click()
        self.assertFalse(hp.get_toast_message('此操作只是将文件从最近列表中删除'))

    @unittest.skip('test_last_file_download')
    def test_last_file_download(self):  # 最近_云文档下载
        logging.info('==========test_last_cloud_logo==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        index = hp.identify_file_index()
        hp.find_elements(*item)[index].click()
        time.sleep(2)
        hp.click_element(*close)
        hp.jump_to_index('last')
        hp.file_more_info(0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filework_pop_download').click()
        # 判定
        self.assertTrue(hp.get_toast_message('文件下载成功,已保存至/storage/emulated/0/yozoCloud文件夹'))

    @unittest.skip('test_last_cloud_logo')
    def test_last_cloud_logo(self):  # 最近_云文档标识小云朵
        logging.info('==========test_last_cloud_logo==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_from')

    # ======2020_04_21====== #
    @unittest.skip('test_search')
    @data(*act_index1)
    def test_search(self, index='star'):  # 最近/打开/标星_搜索
        logging.info('==========test_account_logo==========')
        hp = HomePageView(self.driver)
        # hp.login_needed()
        hp.jump_to_index(index)
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()

        # 搜索存在的文件
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys('欢迎使用永中Office.pdf')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
        # 判定是否搜索到
        hp.find_elements(*item)

        # 搜索不存在的文件
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys('***')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
        # 判定是否搜索到
        self.assertTrue(hp.get_toast_message('没有找到相关文档'))

        # 无关键词搜索
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
        # 判定是否搜索到
        hp.find_elements(*item)

    @unittest.skip('test_account_logo')
    @data(*act_index)
    def test_account_logo(self, index='star'):  # 最近/打开/云文档/标星_头像
        logging.info('==========test_account_logo==========')
        hp = HomePageView(self.driver)
        # hp.login_needed()
        hp.jump_to_index(index)
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        # 判定是否跳转
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_util')

    @unittest.skip('test_last_file_info')
    def test_last_file_info(self):  # 最近_文档信息
        logging.info('==========test_last_file_info==========')
        hp = HomePageView(self.driver)
        time.sleep(1)
        hp.file_more_info(0)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text
        file_type = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text
        file_size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
        file_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text
        file_location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        self.assertFalse(file_name == '-')
        self.assertFalse(file_type == '-')
        self.assertFalse(file_size == '-')
        self.assertFalse(file_time == '-')
        self.assertFalse(file_location == '-')

    @unittest.skip('test_my_login_info')
    def test_my_login_info(self):  # 我的_登录_个人信息
        logging.info('==========test_my_login_info==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_useredit').click()
        username = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').text
        self.assertTrue(username != "")
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('昵称未修改'))
        name_time = hp.getTime("%Y%m%d%H%M%S")
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newname').send_keys(name_time)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('用户信息修改成功'))
        name_now = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').text
        self.assertTrue(name_time == name_now)
        account = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfochange_username').text
        self.assertTrue(account == '139****5564')
        email = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_email').text
        self.assertTrue(email == 'branezhang@163.com')
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_email').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('请输入邮箱'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newemai').send_keys('3451')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('请输入验证码'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('输入的邮箱格式有误'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newemai').send_keys('345126454@qq.com')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_code').send_keys('3451')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('邮箱验证码错误'))

    @unittest.skip('test_my_nonet_logout_convert_tool')
    def test_my_nonet_logout_convert_tool(self):  # 我的_非登录_未联网_转换工具
        logging.info('==========test_my_nonet_logout_convert_tool==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_util').click()
        eles = self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_convert_tools_item')
        for i in eles:
            i.click()
            self.assertTrue(hp.get_toast_message('无法连接网络,请检查网络连接'))
            time.sleep(3)

    @unittest.skip('test_my_logout_convert_tool')
    def test_my_logout_convert_tool(self):  # 我的_非登录_联网_转换工具
        logging.info('==========test_my_logout_convert_tool==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_util').click()
        eles = self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_convert_tools_item')
        for i in eles:
            i.click()
            self.assertTrue(hp.get_toast_message('解锁更多功能，请先登录！'))
            time.sleep(2)

    @unittest.skip('test_cloud_auto_upload_folder')
    def test_cloud_auto_upload_folder(self):  # 云文档_自动上传
        logging.info('==========test_cloud_nonet_search==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.assertTrue(hp.get_element_result('//*[@text="自动上传"]'))

    @unittest.skip('test_cloud_nonet_search')
    def test_cloud_nonet_search(self):  # 云文档_未联网_搜索
        logging.info('==========test_cloud_nonet_search==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
        self.assertFalse(hp.get_element_result('//*[@resource-id="com.yozo.office:id/file_item"]'))

    # ======2020_04_20====== #
    @unittest.skip('test_my_logout')
    def test_my_logout(self):  # 退出登录
        logging.info('==========test_my_about==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login')

    @unittest.skip('test_my_about')
    def test_my_about(self):  # 关于永中
        logging.info('==========test_my_about==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_about').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_version')
        addr = self.driver.find_element(By.ID, 'com.yozo.office:id/_phone_web').text
        email = self.driver.find_element(By.ID, 'com.yozo.office:id/_phone_email').text
        phone = self.driver.find_element(By.ID, 'com.yozo.office:id/_phone_phone').text
        self.assertListEqual([addr, email, phone], ['www.yozosoft.com', 'mobile@yozosoft.com', '400-050-5206'])

    @unittest.skip('test_my_nonet_recycle')
    def test_my_nonet_recycle(self):  # 回收站_未联网
        logging.info('==========test_my_nonet_recycle==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.assertFalse(hp.get_element_result('//*[@text="回收站"]'))
        hp.login_from_my('13915575564', 'zhang199412')
        hp.jump_to_index('my')
        self.assertTrue(hp.get_element_result('//*[@text="回收站"]'))
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        self.assertTrue(hp.get_toast_message('网络异常'))

    @unittest.skip('test_my_recycle_restore')
    def test_my_recycle_restore(self):  # 回收站_联网_还原
        logging.info('==========test_my_nonet_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        folder_name = '0000'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        time.sleep(1)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[index].click()
        hp.find_elements(*item)[1].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        index = hp.identify_file_index()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/lay_check')[index].click()
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text == '1')
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消全选"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_chanel').click()
        file_name = hp.find_elements(*item_title)[index].text
        self.driver.find_elements(By.ID, 'com.yozo.office:id/lay_check')[index].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_recycle_revert').click()
        self.assertTrue(hp.get_toast_message('已还原'))
        self.driver.find_elements(By.ID, 'com.yozo.office:id/lay_check')[index - 1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_recycle_delete').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        self.assertTrue(hp.get_toast_message('已删除'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_back').click()
        hp.jump_to_index('cloud')
        self.assertTrue(hp.get_toast_message('%s' % file_name))

    @unittest.skip('test_my_recycle_empty')
    def test_my_recycle_empty(self):  # 回收站_联网_清空
        logging.info('==========test_my_nonet_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        folder_name = '0000'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        index = hp.identify_file_index()
        hp.file_more_info(index)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[index].click()
        hp.find_elements(*item)[1].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_clear_all').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        index = hp.identify_file_index()
        hp.find_elements(*item_title)[index - 1].click()
        self.assertTrue(hp.get_toast_message('已删除的文件夹无法打开'))
        hp.find_elements(*item_title)[index].click()
        time.sleep(3)
        hp.click_element(*close)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_clear_all').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        self.assertTrue(hp.get_toast_message('已清空'))

    @unittest.skip('test_my_nonet_feedback_history')
    def test_my_nonet_feedback_history(self):  # 意见反馈_联网_历史反馈记录
        logging.info('==========test_my_nonet_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/end').click()
        self.assertTrue(hp.get_toast_message('服务器DNS解析失败,请检查您的网络'))

        hp.click_element(*return1)

    @unittest.skip('test_my_feedback_history')
    def test_my_feedback_history(self):  # 意见反馈_联网_历史反馈记录
        logging.info('==========test_my_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/end').click()
        while not hp.get_toast_message('没有更多数据'):
            hp.swipe_options('//*[@resource-id="com.yozo.office:id/rv"]')
        hp.click_element(*return1)

    @unittest.skip('test_my_nonet_feedback')
    def test_my_nonet_feedback(self):  # 意见反馈_未联网_反馈分类
        logging.info('==========test_my_nonet_feedback==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/contentEt').send_keys('aaaaa')
        self.driver.find_element(By.ID, 'com.yozo.office:id/contactEt').send_keys('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        self.assertTrue(hp.get_toast_message('当前为非wifi环境，无法进行文件传输\n如需更改设置请到我的->系统设置中进行更改'))
        hp.click_element(*return1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/contentEt').send_keys('aaaaa')
        self.driver.find_element(By.ID, 'com.yozo.office:id/contactEt').send_keys('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        self.assertTrue(hp.get_toast_message('服务器DNS解析失败,请检查您的网络'))
        hp.click_element(*return1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('开启')

    @unittest.skip('test_my_feedback')
    def test_my_feedback(self):  # 意见反馈_联网_反馈分类
        logging.info('==========test_my_feedback==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.assertFalse(hp.get_element_result('//*[@text="意见反馈"]'))
        hp.login_from_my('13915575564', 'zhang199412')
        hp.jump_to_index('my')
        self.assertTrue(hp.get_element_result('//*[@text="意见反馈"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        self.assertTrue(hp.get_toast_message('请填写反馈内容'))
        no_input = 0
        input_str = ''
        while no_input < 30:
            input_str += 'AAAAAAAAAA'
            no_input += 1
        self.driver.find_element(By.ID, 'com.yozo.office:id/contentEt').send_keys(input_str)
        content = self.driver.find_element(By.ID, 'com.yozo.office:id/contentEt').text
        self.assertTrue(len(content) == 200, '反馈不等于200个字')
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        # self.assertTrue(hp.get_toast_message('请填写联系方式'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/contactEt').send_keys('11111')
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        self.assertTrue(hp.get_toast_message('联系方式不正确'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/contactEt').send_keys('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        self.assertTrue(hp.get_toast_message('提交成功'))

    @unittest.skip('test_my_sys_setting')
    def test_my_sys_setting(self):  # 系统设置,功能验证在云文档下载上传中有体现
        logging.info('==========test_my_sys_setting==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.assertFalse(hp.get_element_result('//*[@text="系统设置"]'))
        hp.login_from_my('13915575564', 'zhang199412')
        hp.jump_to_index('my')
        self.assertTrue(hp.get_element_result('//*[@text="系统设置"]'))

    @unittest.skip('test_my_nonet_template_subscribe_download')
    def test_my_nonet_template_subscribe_download(self):  # 我的模板_未联网_收藏/下载
        logging.info('==========test_my_nonet_template_subscribe_download==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/mouldSec').click()
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/download').click()
        hp.click_element(*return1)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvRight').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvLeft').click()
        self.assertTrue(hp.get_toast_message('服务器DNS解析失败,请检查您的网络'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvRight').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/end').click()
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btnTv').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()

    @unittest.skip('test_my_template_subscribe_download')
    def test_my_template_subscribe_download(self):  # 我的模板_联网_收藏/下载
        logging.info('==========test_my_template_subscribe_download==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/mouldSec').click()
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        time.sleep(1)
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/title').text
        hp.click_element(*subscribe)
        self.assertTrue(hp.get_toast_message('已取消收藏'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        hp.click_element(*close)
        time.sleep(1)
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % file_name))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvRight').click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % file_name).click()
        hp.click_element(*subscribe)
        self.assertTrue(hp.get_toast_message('已收藏'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        hp.click_element(*close)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % file_name).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/download').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        time.sleep(1)
        # self.assertFalse(hp.get_element_result('//*[@text="%s"]'%file_name))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvLeft').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file_name))

    @unittest.skip('test_my_template_handle')
    def test_my_template_handle(self):  # 我的模板_批量管理
        logging.info('==========test_my_template==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.assertFalse(hp.get_element_result('//*[@text="我的模板"]'))
        hp.login_from_my('13915575564', 'zhang199412')
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/mouldSec').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/end').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btnTv').click()
        self.assertTrue(hp.get_toast_message('请选择要编辑的模板'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvRight').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btnTv').click()
        self.assertTrue(hp.get_toast_message('请选择要编辑的模板'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tvLeft').click()
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btnTv').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btnTv').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()

    @unittest.skip('test_my_nonet_register')
    def test_my_nonet_register(self):  # 注册和登录_未联网_注册账号
        logging.info('==========test_my_nonet_register==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_unlogin').click()
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_register').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_toast_message('请输入手机号'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('1111')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_toast_message('请输入密码'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_password').send_keys('1111')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_toast_message('请重新输入密码,必须包含字母和数字,且密码长度为6到12位'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_password').send_keys('1111abcd')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_toast_message('请先仔细阅读并勾选同意永中Office的《隐私政策》和《服务条款》'))
        self.driver.switch_to_alert().accept()
        self.driver.find_element(By.ID, 'com.yozo.office:id/checkbox_privacy').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_toast_message('请输入正确的手机号'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_toast_message('请输入验证码'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('请输入图片验证码'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_figure_code').send_keys('abcd')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_my_nonet_login_SMS')
    def test_my_nonet_login_SMS(self):  # 注册和登录_未联网_短信密码登录
        logging.info('==========test_my_nonet_login_SMS==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_unlogin').click()
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_register').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login_verfiy').click()
        self.assertTrue(hp.get_toast_message('请输入手机号'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('1111')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('手机号的格式有误'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_my_nonet_forget_pwd')
    def test_my_nonet_forget_pwd(self):  # 注册和登录_未联网_忘记密码
        logging.info('==========test_my_nonet_forget_pwd==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_unlogin').click()
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_findpwd').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('请输入手机号'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('1111')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('输入的账号格式有误'))
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_verifycode').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    # ======2020_04_17====== #
    @unittest.skip('test_my_nonet_login')
    def test_my_nonet_login(self):  # 注册和登录_联网_账号登录
        logging.info('==========test_my_nonet_login==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_unlogin').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('请输入账号'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('11111')  # 输入手机号
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('请输入密码'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_pwd').send_keys('sdfsadf')  # 输入密码
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('手机号的格式有误'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('13915575564')  # 输入手机号
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('登录失败：网络连接异常'))

    @unittest.skip('test_star_nonet_upload_file02')
    def test_star_nonet_upload_file02(self):  # 标星_未联网_上传
        logging.info('==========test_star_nonet_upload_file02==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        hp.jump_to_index('star')
        if hp.get_element_result('//*[@text="重要文件，珍藏在这里"]'):
            hp.jump_to_index('alldoc')
            hp.select_file_type('all')
            hp.file_more_info(0)
            file = hp.mark_star()
            self.assertTrue(hp.check_mark_satr(file))
            self.driver.keyevent(4)
            hp.jump_to_index('star')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        time.sleep(2)
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        self.assertTrue(hp.get_toast_message('上传失败'))

        hp.file_more_info(0)
        hp.mark_star()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('开启')

    @unittest.skip('test_star_nonet_upload_file')
    def test_star_nonet_upload_file(self):  # 标星_未联网_上传
        logging.info('==========test_star_upload_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('star')
        if hp.get_element_result('//*[@text="重要文件，珍藏在这里"]'):
            hp.jump_to_index('alldoc')
            hp.select_file_type('all')
            hp.file_more_info(0)
            file = hp.mark_star()
            self.assertTrue(hp.check_mark_satr(file))
            self.driver.keyevent(4)
            hp.jump_to_index('star')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_toast_message('当前为非wifi环境，无法进行文件传输\n如需更改设置请到我的->系统设置中进行更改'))

        hp.file_more_info(0)
        hp.mark_star()

    @unittest.skip('test_cloud_nonet_multi_select_download02')
    def test_cloud_nonet_multi_select_download02(self):  # 云文档_未联网_云文档操作_多选_下载
        logging.info('==========test_cloud_nonet_multi_select_download02==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[index].click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_toast_message('文件下载失败'))

        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_chanel').click()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('开启')

    @unittest.skip('test_cloud_nonet_multi_select_download')
    def test_cloud_nonet_multi_select_download(self):  # 云文档_未联网_云文档操作_多选_下载
        logging.info('==========test_cloud_nonet_multi_select_download==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[index].click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_toast_message('当前为非wifi环境，无法进行文件传输\n如需更改设置请到我的->系统设置中进行更改'))
        time.sleep(3)
        hp.find_elements(*item)[index - 1].click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_toast_message('当前操作不支持文件夹'))

    # ======2020_04_10====== #
    @unittest.skip('test_cloud_nonet_multi_select_share')
    def test_cloud_nonet_multi_select_share(self):  # 云文档_未联网_云文档操作_多选_分享
        logging.info('==========test_cloud_nonet_multi_select_share==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        file_index = hp.identify_file_index()
        hp.file_more_info(file_index)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[2].click()
        hp.find_elements(*item)[6].click()
        hp.find_elements(*item)[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="分享"]').click()
        self.assertTrue(hp.get_toast_message('当前操作不支持文件夹'))
        hp.find_elements(*item)[2].click()
        self.driver.find_element(By.XPATH, '//*[@text="分享"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_shareitem')[0].click()
        self.assertTrue(hp.get_element_result('//*[contains(@text,分享失败)]'))

    @unittest.skip('test_cloud_nonet_multi_select_options')
    @data(*options)
    def test_cloud_nonet_multi_select_options(self, option='移动'):  # 云文档_未联网_云文档操作_多选_复制/移动
        logging.info('==========test_cloud_nonet_multi_select_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(6)

        logging.info('==========copy operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[6].click()
        hp.find_elements(*item)[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_cloud_nonet_multi_select_delete')
    def test_cloud_nonet_multi_select_delete(self):  # 云文档_未联网_云文档操作_多选_删除
        logging.info('==========test_cloud_nonet_multi_select_delete==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(7)

        logging.info('==========delete operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[6].click()
        hp.find_elements(*item)[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_cloud_nonet_file_delete')
    def test_cloud_nonet_file_delete(self):  # 云文档_未联网_云文档操作_删除
        logging.info('==========test_cloud_nonet_file_delete==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(7)

        logging.info('==========delete operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        hp.file_more_info(7)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_show_title').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_cloud_file_delete')
    def test_cloud_file_delete(self):  # 云文档_联网_云文档操作_删除
        logging.info('==========test_cloud_file_delete==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)

        logging.info('==========delete operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        hp.file_more_info(7)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_show_title').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertFalse(hp.get_toast_message(name))

    @unittest.skip('test_cloud_nonet_file_rename')
    def test_cloud_nonet_file_rename(self):  # 云文档_未联网_云文档操作_重命名
        logging.info('==========test_cloud_nonet_file_rename==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)

        hp.file_more_info(7)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.hide_keyboard()
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        folder_name = '01234567890123456789012345678901234567890'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '0000'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_cloud_file_rename')
    def test_cloud_file_rename(self):  # 云文档_联网_云文档操作_重命名
        logging.info('==========test_cloud_file_rename==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')

        hp.file_more_info(7)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.hide_keyboard()
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        folder_name = '01234567890123456789012345678901234567890'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % (folder_name + '.' + suffix)))

    @unittest.skip('test_cloud_nonet_file_options')
    @data(*options)
    def test_cloud_nonet_file_options(self, option='移动'):  # 云文档_未联网_云文档操作_复制
        logging.info('==========test_cloud_nonet_file_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(7)

        logging.info('==========copy action==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_cloud_nonet_download_file02')
    def test_cloud_nonet_download_file02(self):  # 云文档_未联网_云文档操作_下载
        logging.info('==========test_cloud_nonet_download_file02==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_toast_message('文件下载失败'))

    @unittest.skip('test_cloud_nonet_download_file')
    def test_cloud_nonet_download_file(self):  # 云文档_未联网_云文档操作_下载
        logging.info('==========test_cloud_nonet_download_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_toast_message('当前为非wifi环境，无法进行文件传输\n如需更改设置请到我的->系统设置中进行更改'))

    @unittest.skip('test_cloud_nonet_share')
    @data(*index_share_list)
    def test_cloud_nonet_share(self, way='more'):  # 云文档_未联网_分享到_微信/QQ/邮箱
        logging.info('==========test_cloud_nonet_share==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        file_index = hp.identify_file_index()
        hp.file_more_info(file_index)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_%s_share' % way).click()
        if way == 'more':
            self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_shareitem')[0].click()
        self.assertTrue(hp.get_element_result('//*[contains(@text,分享失败)]'))

    @unittest.skip('test_cloud_nonet_delete_folder')
    def test_cloud_nonet_delete_folder(self):  # 云文档_未联网_文件夹操作_删除
        logging.info('==========test_cloud_nonet_delete_folder==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

        time.sleep(2)

    @unittest.skip('test_cloud_nonet_rename_folder')
    def test_cloud_nonet_rename_folder(self):  # 云文档_未联网_文件夹操作_重命名
        logging.info('==========test_cloud_nonet_rename_folder==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()

        folder_name = '自动上传'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.hide_keyboard()
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        folder_name = '01234567890123456789012345678901234567890'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        time.sleep(2)

    @unittest.skip('skip test_cloud_folder_options')
    @data(*options)
    def test_cloud_nonet_folder_options(self, option='复制'):  # 云文档_未联网_文件夹操作_移动
        logging.info('==========test_cloud_nonet_folder_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.file_more_info(2)

        logging.info('==========move action==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('网络连接异常'))

        time.sleep(2)

    @unittest.skip('test_cloud_nonet_create_folder')
    def test_cloud_nonet_create_folder(self):  # 云文档_未联网_新建文件夹
        logging.info('==========test_cloud_nonet_create_folder==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        # time.sleep(2)
        # self.driver.find_element(By.ID,'com.yozo.office:id/ll_head_net')
        # 新建按钮
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        # 验证弹出框的内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/title')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)
        folder_name = '01234567890123456789012345678901234567890'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '0000'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        results = hp.get_toast_message('新建文件夹失败')
        self.assertTrue(results)

        time.sleep(2)

    @unittest.skip('test_cloud_unlogin')
    def test_cloud_unlogin(self):  # 云文档_未登录
        logging.info('==========test_cloud_unlogin==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_view')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_cloud_title_text')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_logo').click()
        self.assertTrue(hp.get_element_result('//*[@text="请输入手机号"]'))

    # ======2020_04_09====== #
    @unittest.skip('test_my_login')
    def test_my_login(self):  # 注册和登录_联网_账号登录
        logging.info('==========test_my_login==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_unlogin').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('请输入账号'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('11111')  # 输入手机号
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('请输入密码'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_pwd').send_keys('sdfsadf')  # 输入密码
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('手机号的格式有误'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').send_keys('13915575564')  # 输入手机号
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        self.assertTrue(hp.get_toast_message('登录失败：用户名或密码错误'))
        self.assertTrue(hp.get_element_result('//*[@text="请输入密码"]'))
        graph_code = True
        while graph_code:
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_pwd').send_keys('sdfsadf')  # 输入密码
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
            if hp.get_element_result('//*[@text="请输入图形验证"]'):
                graph_code = False
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_figure_code').send_keys('45ds')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()
        self.assertTrue(hp.get_toast_message('登录失败：次数过多，请转手机号验证码登录'))
        self.assertTrue(hp.get_element_result('//*[@text="请输入验证码"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_pwd_sms').send_keys('461145')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_login').click()
        self.assertTrue(hp.get_toast_message('登录失败：用户名或密码错误'))

    @unittest.skip('test_star_file_info')
    def test_star_file_info(self):  # 文档信息显示
        logging.info('==========test_star_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        self.driver.keyevent(4)
        hp.jump_to_index('star')
        hp.file_more_info(1)
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        self.assertTrue(filename != '-')
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        self.assertTrue(suffix != '-')
        size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text.strip()
        self.assertTrue(size != '-')
        chang_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text.strip()
        self.assertTrue(chang_time != '-')
        path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text.strip()
        self.assertTrue(path != '-')
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('test_star_share_back')
    def test_star_share_back(self):  # “标星”中的分享的返回键
        logging.info('==========test_star_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('star')
        if len(hp.find_elements(*item)) == 0:
            hp.jump_to_index('alldoc')
            hp.select_file_type('ss')
            hp.file_more_info(1)
            file = hp.mark_star()
            self.assertTrue(hp.check_mark_satr(file))
            self.driver.keyevent(4)
            hp.jump_to_index('star')
        hp.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))
        hp.mark_star()

    @unittest.skip('test_star_show_no_file')
    def test_star_show_no_file(self):
        logging.info('==========test_star_show_no_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('star')
        if hp.find_elements(*item):
            length = len(hp.find_elements(*item))
            for i in range(length):
                hp.file_more_info(0)
                hp.mark_star()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_view"]'))

    @unittest.skip('test_star_multi_select02')
    def test_star_multi_select02(self):
        logging.info('==========test_star_multi_select02==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file = hp.mark_star()
        hp.file_more_info(2)
        file = hp.mark_star()
        hp.file_more_info(3)
        file = hp.mark_star()
        self.driver.keyevent(4)
        hp.jump_to_index('star')
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[0].click()
        hp.find_elements(*item)[1].click()
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_choose_file_cancel').click()
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_choose_file_ok').click()
        self.driver.find_element(By.XPATH, '//*[@text="保存"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消上传"]').click()
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        hp.find_elements(*item)[1].click()
        hp.find_elements(*item)[0].click()
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="确认"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="保存"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="上传成功"]'))
        self.driver.find_element(By.XPATH, '//*[@text="确定"]').click()
        hp.file_more_info(1)
        file = hp.mark_star()
        hp.file_more_info(2)
        file = hp.mark_star()
        hp.file_more_info(0)
        file = hp.mark_star()

    @unittest.skip('test_star_multi_select')
    def test_star_multi_select(self):  # “标星”全选操作
        logging.info('==========test_star_multi_select==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        self.driver.keyevent(4)
        hp.jump_to_index('star')
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        hp.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text.strip()
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="已选择"]')
        self.driver.find_element(By.XPATH, '//*[@text="0"]')
        self.driver.find_element(By.XPATH, '//*[@text="个文件"]')

        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.assertTrue(hp.get_toast_message('操作成功'))
        msg = os.system('adb shell ls %s' % location)
        self.assertTrue(msg == 1, 'delete fail')

    @unittest.skip('test_star_delete_file')
    def test_star_delete_file(self):
        logging.info('==========test_star_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('wp')
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        self.driver.keyevent(4)
        hp.jump_to_index('star')
        hp.file_more_info(1)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text.strip()
        name = filename + '.' + suffix
        hp.delete_file()
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name), 'delete fail')
        msg = os.system('adb shell ls %s' % location)
        self.assertTrue(msg == 1, 'delete fail')

    @unittest.skip('test_star_rename_file')
    def test_star_rename_file(self):
        logging.info('==========test_star_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file = hp.mark_star()
        # self.assertTrue(hp.check_mark_satr(file))
        self.driver.keyevent(4)
        hp.jump_to_index('star')
        hp.file_more_info(1)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').set_text(newName)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('操作成功'))
        hp.file_more_info(1)
        hp.mark_star()

    @unittest.skip('test_star_file_options')
    @data(*options)
    def test_star_file_options(self, option='移动'):  # 标星复制文件
        logging.info('==========test_star_file_options==========')
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('ss')
        hp.file_more_info(1)
        file = hp.mark_star()
        self.driver.keyevent(4)
        hp.jump_to_index('star')
        hp.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        logging.info('=========copy_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/framelayout_cover').click()
        time.sleep(1)
        hp.find_elements(*item)[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/framelayout_cover').click()
        time.sleep(1)
        hp.find_elements(*item)[1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_new_file').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys('1111')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/framelayout_cover')[1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        if option == '复制':
            self.assertTrue(hp.get_toast_message('操作成功'))
        else:
            self.assertTrue(hp.get_toast_message('移动操作成功'))
        msg = os.system('adb shell ls /storage/emulated/0/0000/1111/%s' % fileName)
        self.assertTrue(msg == 0, 'copy fail')
        os.system('adb shell rm -rf /storage/emulated/0/0000/1111')
        hp.file_more_info(1)
        file = hp.mark_star()

    @unittest.skip('test_star_upload_file')
    def test_star_upload_file(self):  # 标星_联网_上传
        logging.info('==========test_star_upload_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('star')
        if len(hp.find_elements(*item)) == 0:
            hp.jump_to_index('alldoc')
            hp.select_file_type('ss')
            hp.file_more_info(1)
            file = hp.mark_star()
            self.assertTrue(hp.check_mark_satr(file))
            self.driver.keyevent(4)
            hp.jump_to_index('star')
        hp.file_more_info(0)
        check = hp.upload_file('标星上传')
        self.assertTrue(check, 'upload fail')
        hp.file_more_info(0)
        hp.mark_star()
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('test_star_mark_on_off')
    def test_star_mark_on_off(self):  # 标星_标星/取消标星
        logging.info('==========test_star_mark_on_off==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('last')
        hp.file_more_info(1)
        file_name = hp.mark_star()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_star"]'))
        hp.jump_to_index('star')
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file_name))
        hp.jump_to_index('last')
        hp.file_more_info(1)
        file_name = hp.mark_star()
        self.assertFalse(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_star"]'))
        hp.jump_to_index('star')
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % file_name))
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file_name = hp.mark_star()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_star"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        hp.jump_to_index('star')
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file_name))
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file_name = hp.mark_star()
        self.assertFalse(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_star"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        hp.jump_to_index('star')
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % file_name))

    @unittest.skip('test_star_search')
    def test_star_search(self):  # 标星_搜索
        logging.info('==========test_star_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('star')

        search_file = 'abcdef.pptx'
        result = hp.search_file(search_file)
        self.assertFalse(result)
        self.assertTrue((hp.get_element_result('//*[@text="没有找到相关文档"]')))
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_content_clear').click()
        search_file = '欢迎使用永中Office.docx'
        result = hp.search_file1(search_file)
        self.assertTrue(result)

    @unittest.skip('test_star_sort')
    def test_star_sort(self):  # 标星条件排序
        logging.info('==========test_star_sort==========')
        hp = HomePageView(self.driver)
        # hp.login_needed()
        hp.jump_to_index('star')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)
        # hp.jump_to_index('my')
        # hp.logout_action()

    @unittest.skip('test_cloud_search')
    def test_cloud_search(self):  # 云文档_联网_搜索
        logging.info('==========test_cloud_search==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.create_file('wp')
        hp.save_new_file('localSearch', 'local')
        hp.close_file()
        hp.click_element(*return1)
        hp.create_file('pg')
        hp.save_new_file('cloudSearch', 'cloud')
        hp.close_file()
        time.sleep(0.5)
        hp.click_element(*return1)
        hp.jump_to_index('cloud')
        results = hp.search_file('cloudSearch.ppt')
        self.assertTrue(results == True)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_back').click()
        results = hp.search_file('localSearch.doc')
        self.assertTrue(results == False)

    # ======2020_04_08====== #
    @unittest.skip('skip test_cloud_select_all_download')
    def test_cloud_select_all_download(self):  # 云文档_联网_云文档操作_多选_下载
        logging.info('==========test_cloud_select_all_download==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)

        logging.info('==========download operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        ele6 = hp.find_elements(*item)[6]
        ele7 = hp.find_elements(*item)[7]
        name6 = ele6.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        name7 = ele7.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        ele6.click()
        ele7.click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        is_displayed = WebDriverWait(self.driver, 120).until(
            lambda driver: self.driver.find_element(By.XPATH, '//*[@text="下载成功"]').is_displayed())
        # hp.get_element_result('//*[@text="下载成功"]')
        self.assertTrue(is_displayed)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        msg = os.system('adb shell ls /storage/emulated/0/yozoCloud/%s' % name6)
        self.assertTrue(msg == 0, '文件不存在')
        msg = os.system('adb shell ls /storage/emulated/0/yozoCloud/%s' % name7)
        self.assertTrue(msg == 0, '文件不存在')

    @unittest.skip('skip test_cloud_select_all_copy')
    @data(*options)
    def test_cloud_multi_select_options(self, option='复制'):  # 云文档中多选移动复制
        logging.info('==========test_cloud_select_all_copy==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)

        logging.info('==========copy operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        ele6 = hp.find_elements(*item)[6]
        ele7 = hp.find_elements(*item)[7]
        name6 = ele6.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        name7 = ele7.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        ele6.click()
        ele7.click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        time.sleep(2)
        option_folder = hp.find_elements(*item)[0]
        folder_name = option_folder.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        option_folder.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('操作成功'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_chanel').click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder_name).click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % name6)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % name7)

    @unittest.skip('skip test_cloud_select_all_delete')
    def test_cloud_multi_select_delete(self):  # 云文档_联网_云文档操作_多选_删除
        logging.info('==========test_cloud_select_all_delete==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)

        logging.info('==========delete operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        eles = hp.find_elements(*item)
        name1 = eles[6].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        name2 = eles[7].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        names_del = [name1, name2]
        eles[6].click()
        eles[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        eles1 = hp.find_elements(*item_title)
        names = list(map(lambda x: x.text, eles1))
        a = set(names_del) <= set(names)  # 前一个集合是否是后一个集合的子集
        self.assertFalse(a)

    @unittest.skip('skip test_cloud_select_all')
    def test_cloud_multi_select(self):  # 云文档_云文档操作_多选_全选
        logging.info('==========test_cloud_multi_select==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)

        logging.info('==========select_all operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        num2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num2) == 0)

        hp.find_elements(*item)[5].click()
        hp.find_elements(*item)[6].click()
        hp.find_elements(*item)[7].click()
        num2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num2) == 3)

        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        num = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num) != 0)

        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        num1 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num1) == 0)

    @unittest.skip('skip test_cloud_file_options02')
    @data(*options)
    def test_cloud_file_options02(self, option='复制'):  # 云文档_联网_云文档操作_复制
        logging.info('==========test_cloud_file_options02==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        file = filename + '.' + suffix

        logging.info('==========copy action==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        copy_folder_ele = hp.find_elements(*item)[0]
        copy_folder_name = copy_folder_ele.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        copy_folder_ele.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_new_file').click()
        folder_name = hp.getTime('%Y%m%d%H%M%S')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder_name).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('操作成功'))
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % copy_folder_name).click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder_name).click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file))

    @unittest.skip('skip test_cloud_file_options')
    @data(*options)
    def test_cloud_file_options(self, option='复制'):  # 云文档_联网_云文档操作_复制
        logging.info('==========test_cloud_file_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        file = filename + '.' + suffix

        logging.info('==========copy action==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        copy_folder_ele = hp.find_elements(*item)[0]
        copy_folder_name = copy_folder_ele.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        copy_folder_ele.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('操作成功'))
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % copy_folder_name).click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file))

    @unittest.skip('skip test_cloud_download_file')
    def test_cloud_download_file(self):  # 云文档_联网_云文档操作_下载
        logging.info('==========test_cloud_download_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        index = hp.identify_file_index()
        hp.file_more_info(index)
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        file = filename + '.' + suffix
        check = hp.download_file()
        self.assertTrue(check, 'download fail')
        msg = os.system('adb shell ls /storage/emulated/0/yozoCloud/%s' % file)
        self.assertTrue(msg == 0, '文件不存在')

    @unittest.skip('skip test_cloud_file_info')
    def test_cloud_file_info(self):  # 云文档_文档信息
        logging.info('==========test_cloud_file_info==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        self.assertTrue(filename != '-')
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        self.assertTrue(suffix != '-')
        size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text.strip()
        self.assertTrue(size != '-')
        chang_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text.strip()
        self.assertTrue(chang_time != '-')
        path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text.strip()
        self.assertTrue(path == '云文档/')

    @unittest.skip('skip test_cloud_delete_folder')
    def test_cloud_delete_folder(self):  # 云文档_联网_文件夹操作_删除
        logging.info('==========test_cloud_delete_folder==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        folder_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('操作成功'))
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % folder_name), 'delete fail')

    @unittest.skip('skip test_cloud_rename_folder')
    def test_cloud_rename_folder(self):  # 云文档_联网_文件夹操作_重命名
        logging.info('==========test_cloud_rename_folder==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(3)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)
        folder_name = '01234567890123456789012345678901234567890'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '自动上传'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('文件名已存在'))

        hp.file_more_info(3)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()
        folder_name = hp.getTime('%Y%m%d%H%M%S')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), 'folder rename fail')

    @unittest.skip('skip test_cloud_folder_options')
    @data(*options)
    def test_cloud_folder_options(self, option='移动'):  # 云文档_联网_文件夹操作_移动
        logging.info('==========test_cloud_folder_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        folder_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')
        hp.file_more_info(2)

        logging.info('==========move action==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        hp.find_elements(*item)[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('目标文件夹与源文件相同。'))

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        move_folder_ele = hp.find_elements(*item)[1]
        move_folder = move_folder_ele.find_element(By.ID, 'com.yozo.office:id/tv_title').text
        move_folder_ele.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('操作成功'))

        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % move_folder).click()
        result1 = hp.get_element_result('//*[@text="%s"]' % folder_name)
        self.assertTrue(result1, '操作失败')

    @unittest.skip('skip test_cloud_sort')
    def test_cloud_sort(self):  # 云文档_排序
        logging.info('==========test_cloud_sort==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_cloud_create_folder')
    def test_cloud_create_folder(self):  # 云文档_未联网_新建文件夹
        logging.info('==========test_cloud_create_folder==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')

        # 新建按钮
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        # 验证弹出框的内容
        self.driver.find_element(By.ID, 'com.yozo.office:id/title')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true')
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
            self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)
        folder_name = '01234567890123456789012345678901234567890'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '0000'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(hp.get_element_result('//*[@text="%s(1)"]' % folder_name), '文件夹新建失败')

        e1 = hp.find_elements(*item)[1]
        e1.find_element(By.ID, 'com.yozo.office:id/lay_more').click()
        hp.delete_file()
        time.sleep(1)
        e1 = hp.find_elements(*item)[1]
        e1.find_element(By.ID, 'com.yozo.office:id/lay_more').click()
        hp.delete_file()

    """
    # ======add 2020_01_02=====

    @unittest.skip('skip test_my2_recycle_options')
    def test_my2_recycle_options(self):
        logging.info('==========test_my2_recycle_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        if not hp.is_not_visible('//*[@text="数据加载中.."]'):
            logging.error('回收站加载过长')
            return False
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_file_list_item_check').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        num = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num) != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()

    @unittest.skip('skip test_my2_recycle_restore')
    def test_my2_recycle_restore(self):
        logging.info('==========test_my2_recycle_restore==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        result1 = hp.recycle_files_delete(*(0,))
        self.assertTrue(result1 == True)
        result2 = hp.recycle_files_revert(*(0,))
        self.assertTrue(result2 == True)
        result3 = hp.recycle_files_clear()
        self.assertTrue(result3 == True)

    @unittest.skip('skip test_alldoc_cloud_click_unlogin')
    def test_alldoc_cloud_click_unlogin(self):
        logging.info('==========test_alldoc_cloud_click_unlogin==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('alldoc')
        self.assertTrue(hp.get_element_result('//*[@text="登录送1G空间"]'))
        self.driver.find_element(By.XPATH, '//*[@text="云文档"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_alldoc_cloud_click_login')
    def test_alldoc_cloud_click_login(self):
        logging.info('==========test_alldoc_cloud_click_unlogin==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        self.assertTrue(hp.get_element_result('//*[contains(@text,"已用")]'))
        self.driver.find_element(By.XPATH, '//*[@text="云文档"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="自动上传"]'))
    
    # ======before 2020_01_02========
    @unittest.skip('skip test_template_category')
    @data(*wps)
    def test_my2_template_zoom_apply(self, file_type='ss'):  # 模板类别
        logging.info('==========test_template_category==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('last')
        hp.create_file_preoption(file_type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tpImg1').click()
        result = hp.is_visible('//*[@resource-id="com.yozo.office:id/tpImg"]')
        self.assertTrue(result, '模板预览失败')
        # self.driver.find_element(By.ID, 'com.yozo.office:id/tpImg').click()
        # time.sleep(1)
        # self.driver.save_screenshot(screenshot_file + 'origin.png')
        # hp.zoom_in() #放大失败
        # self.driver.save_screenshot(screenshot_file + 'zoom_in.png')
        # result1 = hp.compare_pic('origin.png', 'zoom_in.png')
        # self.assertNotEqual(result1, 0.0, '放大失败')
        self.driver.find_element(By.ID, 'com.yozo.office:id/applyTv').click()
        self.assertTrue(hp.is_not_visible('//*[@text="请稍等..."]'))
        self.assertTrue(hp.is_not_visible('//*[contains(@text,"正在打开")]'))
        self.assertTrue(hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_title_text_view"]'))

    @unittest.skip('skip test_template_category')
    @data(*wps)
    def test_my2_template_category(self, file_type='pg'):  # 模板类别
        logging.info('==========test_template_category==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('last')
        hp.create_file_preoption(file_type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/category1').click()
        time.sleep(1)
        template_type = templates_dict[file_type]
        for i in template_type:
            ele = self.driver.find_element(By.XPATH, '//*[@text="%s"]' % i)
            ele.click()
            status = ele.get_attribute('selected')
            self.assertTrue(status == 'true')
            time.sleep(1)
            eles = self.driver.find_elements(By.XPATH,
                                             '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
            self.assertTrue(len(eles) != 0)
        hp.click_element(*return1)
        fresh_before = self.driver.find_element(By.ID, 'com.yozo.office:id/tpTitle1').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/changeTv').click()
        fresh_after = self.driver.find_element(By.ID, 'com.yozo.office:id/tpTitle1').text
        self.assertFalse(fresh_before == fresh_after)

    @unittest.skip('skip test_my2_templates_options')
    @data(*way_list)
    def test_my2_templates_options(self, way='下载'):
        logging.info('==========test_my2_templates_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        for i in ['ss', 'wp', 'pg']:
            result = hp.templates_access(i, *[way])
            self.assertTrue(result, '%s%s失败' % (i, way))
        self.assertTrue(hp.templates_preview(way), '模板为空')
        self.assertTrue(hp.templates_delete(), '删除成功')
        self.driver.find_element(By.XPATH, '//*[@text="完成"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="批量管理"]'))
        hp.click_element(*return1)
        self.assertTrue(hp.get_element_result('//*[@text="我的模板"]'))

    @unittest.skip('skip test_alldoc_copy_file')
    def test_alldoc_copy_file(self):  # “打开”复制文件
        logging.info('==========test_alldoc_copy_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = hp.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_delete_file')
    def test_alldoc_delete_file(self):
        logging.info('==========test_alldoc_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.sort_files('name', 'up')
        hp.file_more_info(1)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        name = filename + '.' + suffix
        hp.delete_file()
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name), 'delete fail')
        # file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        # index_e = file_path.rindex('/') + 1
        # name = file_path[index_e:]
        # hp.delete_file()
        # self.driver.keyevent(4)
        # self.assertFalse(hp.search_file(name))

    @unittest.skip('skip test_alldoc_download_copy_file')
    def test_alldoc_download_copy_file(self):
        logging.info('==========test_alldoc_download_copy_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(7)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = hp.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_download_delete_file')
    def test_alldoc_download_delete_file(self):
        logging.info('==========test_alldoc_download_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        hp.delete_file()
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_alldoc_download_file_info')
    def test_alldoc_download_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_download_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_download_mark_star')
    def test_alldoc_download_mark_star(self):
        logging.info('==========test_alldoc_download_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_download_move_file')
    def test_alldoc_download_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_download_move_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        check = hp.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_download_rename_file')
    def test_alldoc_download_rename_file(self):
        logging.info('==========test_alldoc_download_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        check = hp.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_download_search_file')
    def test_alldoc_download_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_download_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = hp.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_download_select_all')
    def test_alldoc_download_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_download_select_all==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_alldoc_download_select_all1')
    def test_alldoc_download_select_all1(self):
        logging.info('==========test_alldoc_download_select_all1==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(2)
        name_list = hp.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(hp.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_alldoc_download_share')
    @data(*index_share_list)
    def test_alldoc_download_share(self, way):
        logging.info('==========test_alldoc_download_share==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(7)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_download_share_back')
    def test_alldoc_download_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_download_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_download_sort_file')
    def test_alldoc_download_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_download_sort_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)

    @unittest.skip('skip test_alldoc_download_upload_file')
    def test_alldoc_download_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_download_upload_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.open_local_folder('Download')
        self.assertTrue(hp.check_open_folder('Download'), 'open fail')
        hp.file_more_info(7)
        check = hp.upload_file('Download上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_alldoc_file_info')
    def test_alldoc_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        self.assertTrue(filename != '-')
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        self.assertTrue(suffix != '-')
        size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text.strip()
        self.assertTrue(size != '-')
        chang_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text.strip()
        self.assertTrue(chang_time != '-')
        path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text.strip()
        self.assertTrue(path != '-')

    @unittest.skip('skip test_alldoc_local_folder')
    @data(*folder_list)
    def test_alldoc_local_folder(self, folder='TIM'):  # 测试本地文档打开
        logging.info('==========test_alldoc_local_folder==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder(folder)
        self.assertTrue(hp.check_open_folder(folder), 'open fail')

    @unittest.skip('skip test_alldoc_mark_star')
    def test_alldoc_mark_star(self):
        logging.info('==========test_alldoc_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_mobile_copy_file')
    def test_alldoc_mobile_copy_file(self):
        logging.info('==========test_alldoc_mobile_copy_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = hp.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_mobile_delete_file')
    def test_alldoc_mobile_delete_file(self):
        logging.info('==========test_alldoc_mobile_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        hp.find_elements(*item)[0].click()
        hp.file_more_info(1)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        hp.delete_file()
        # self.driver.keyevent(4)
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_alldoc_mobile_file_info')
    def test_alldoc_mobile_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_mobile_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        for i in range(10):
            hp.swipeUp()
        hp.file_more_info(1)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_mobile_mark_star')
    def test_alldoc_mobile_mark_star(self):
        logging.info('==========test_alldoc_mobile_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(8)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_mobile_move_file')
    def test_alldoc_mobile_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_mobile_move_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        check = hp.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_mobile_rename_file')
    def test_alldoc_mobile_rename_file(self):
        logging.info('==========test_alldoc_mobile_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        for i in range(10):
            hp.swipeUp()
        hp.file_more_info(1)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        check = hp.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_mobile_search_file')
    def test_alldoc_mobile_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_mobile_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = hp.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_mobile_select_all')
    def test_alldoc_mobile_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_mobile_select_all==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_alldoc_mobile_select_all1')
    def test_alldoc_mobile_select_all1(self):
        logging.info('==========test_alldoc_mobile_select_all1==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        name_list = hp.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(hp.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_alldoc_mobile_share')
    @data(*index_share_list)
    def test_alldoc_mobile_share(self, way):
        logging.info('==========test_alldoc_mobile_share==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_mobile_share_back')
    def test_alldoc_mobile_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_mobile_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_mobile_sort_file')
    def test_alldoc_mobile_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_mobile_sort_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)

    @unittest.skip('skip test_alldoc_mobile_upload_file')
    def test_alldoc_mobile_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_mobile_upload_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.open_local_folder('手机')
        self.assertTrue(hp.check_open_folder('手机'), 'open fail')
        while not hp.find_elements(*item_title)[0].text.endswith(
                ('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt')):
            hp.swipeUp()
        hp.file_more_info(8)
        check = hp.upload_file('手机上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_alldoc_move_file')
    def test_alldoc_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_move_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        check = hp.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_myfile_copy_file')
    def test_alldoc_myfile_copy_file(self):
        logging.info('==========test_alldoc_myfile_copy_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = hp.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_myfile_delete_file')
    def test_alldoc_myfile_delete_file(self):
        logging.info('==========test_alldoc_myfile_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        hp.delete_file()
        # self.driver.keyevent(4)
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_alldoc_myfile_file_info')
    def test_alldoc_myfile_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_myfile_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_myfile_mark_star')
    def test_alldoc_myfile_mark_star(self):
        logging.info('==========test_alldoc_myfile_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_myfile_move_file')
    def test_alldoc_myfile_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_myfile_move_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        check = hp.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_myfile_rename_file')
    def test_alldoc_myfile_rename_file(self):
        logging.info('==========test_alldoc_myfile_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        check = hp.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_myfile_search_file')
    def test_alldoc_myfile_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_myfile_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = hp.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_myfile_select_all')
    def test_alldoc_myfile_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_myfile_select_all==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_alldoc_myfile_select_all1')
    def test_alldoc_myfile_select_all1(self):
        logging.info('==========test_alldoc_myfile_select_all1==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(2)
        name_list = hp.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(hp.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_alldoc_myfile_share')
    @data(*index_share_list)
    def test_alldoc_myfile_share(self, way):
        logging.info('==========test_alldoc_myfile_share==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(7)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_myfile_share_back')
    def test_alldoc_myfile_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_myfile_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_myfile_sort_file')
    def test_alldoc_myfile_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_myfile_sort_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)

    @unittest.skip('skip test_alldoc_myfile_upload_file')
    def test_alldoc_myfile_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_myfile_upload_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.open_local_folder('我的文档')
        self.assertTrue(hp.check_open_folder('我的文档'), 'open fail')
        hp.file_more_info(7)
        check = hp.upload_file('我的文档上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_alldoc_qq_copy_file')
    def test_alldoc_qq_copy_file(self):
        logging.info('==========test_alldoc_qq_copy_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        check = hp.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_qq_delete_file')
    def test_alldoc_qq_delete_file(self):
        logging.info('==========test_alldoc_qq_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        hp.delete_file()
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_alldoc_qq_file_info')
    def test_alldoc_qq_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_qq_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_qq_mark_star')
    def test_alldoc_qq_mark_star(self):
        logging.info('==========test_alldoc_qq_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_qq_move_file')
    def test_alldoc_qq_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_qq_move_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        check = hp.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_qq_rename_file')
    def test_alldoc_qq_rename_file(self):
        logging.info('==========test_alldoc_qq_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        check = hp.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_qq_search_file')
    def test_alldoc_qq_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_qq_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = hp.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_qq_select_all')
    def test_alldoc_qq_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_qq_select_all==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_alldoc_qq_select_all1')
    def test_alldoc_qq_select_all1(self):
        logging.info('==========test_alldoc_qq_select_all1==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(2)
        name_list = hp.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(hp.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_alldoc_qq_share')
    @data(*index_share_list)
    def test_alldoc_qq_share(self, way):
        logging.info('==========test_alldoc_qq_share==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(7)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_qq_share_back')
    def test_alldoc_qq_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_qq_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_qq_sort_file')
    def test_alldoc_qq_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_qq_sort_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)

    @unittest.skip('skip test_alldoc_qq_upload_file')
    def test_alldoc_qq_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_qq_upload_file==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('alldoc')
        hp.open_local_folder('QQ')
        self.assertTrue(hp.check_open_folder('QQ'), 'open fail')
        hp.file_more_info(7)
        check = hp.upload_file('QQ上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_alldoc_rename_file')
    def test_alldoc_rename_file(self):
        logging.info('==========test_alldoc_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        check = hp.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_scroll')
    def test_alldoc_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_alldoc_scroll==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        first_name = hp.find_elements(*item_title)[0].text
        hp.swipeUp()
        second_name = hp.find_elements(*item_title)[0].text
        self.assertTrue(first_name != second_name)

    @unittest.skip('skip test_alldoc_search_file')
    def test_alldoc_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        search_file = '欢迎使用永中Office.pptx'
        result = hp.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_select_all')
    def test_alldoc_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_select_all==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_alldoc_select_all1')
    def test_alldoc_select_all1(self):
        logging.info('==========test_alldoc_select_all1==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        name_list = hp.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(hp.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_alldoc_share')
    @data(*index_share_list)
    def test_alldoc_share(self, way):
        logging.info('==========test_alldoc_share==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_share_back')
    def test_alldoc_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_show_file')
    def test_alldoc_show_file(self):  # 点击文件类型
        logging.info('==========test_alldoc_show_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')

        type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
        for i in type_list:
            hp.select_file_type(i)
            self.assertTrue(hp.check_select_file_type(i), 'filter fail')
            self.driver.keyevent(4)

    @unittest.skip('skip test_alldoc_sort_file')
    def test_alldoc_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_sort_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)

    @unittest.skip('skip test_alldoc_type_back')
    def test_alldoc_type_back(self):  # “打开”文档类型中的返回键
        logging.info('==========test_alldoc_type_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('pdf')

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_main_title"]'))

    @unittest.skip('skip test_alldoc_upload_file')
    def test_alldoc_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_upload_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        check = hp.upload_file('打开上传')
        if check == None:
            hp.jump_to_index('alldoc')
            hp.select_file_type('all')
            hp.file_more_info(1)
            check = hp.upload_file('打开上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_alldoc_wechat_copy_file')
    def test_alldoc_wechat_copy_file(self):
        logging.info('==========test_alldoc_wechat_copy_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = hp.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_wechat_delete_file')
    def test_alldoc_wechat_delete_file(self):
        logging.info('==========test_alldoc_wechat_delete_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        hp.delete_file()
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_alldoc_wechat_file_info')
    def test_alldoc_wechat_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_wechat_file_info==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_wechat_mark_star')
    def test_alldoc_wechat_mark_star(self):
        logging.info('==========test_alldoc_wechat_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(2)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_wechat_move_file')
    def test_alldoc_wechat_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_wechat_move_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        check = hp.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_wechat_rename_file')
    def test_alldoc_wechat_rename_file(self):
        logging.info('==========test_alldoc_wechat_rename_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        newName = 'rename' + hp.getTime('%Y%m%d%H%M%S')
        check = hp.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_wechat_search_file')
    def test_alldoc_wechat_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_wechat_search_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = hp.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_wechat_select_all')
    def test_alldoc_wechat_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_wechat_select_all==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_alldoc_wechat_select_all1')
    def test_alldoc_wechat_select_all1(self):
        logging.info('==========test_alldoc_wechat_select_all1==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        name_list = hp.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(hp.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_alldoc_wechat_share')
    @data(*index_share_list)
    def test_alldoc_wechat_share(self, way):
        logging.info('==========test_alldoc_wechat_share==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_wechat_share_back')
    def test_alldoc_wechat_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_wechat_share_back==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_wechat_sort_file')
    def test_alldoc_wechat_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_wechat_sort_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                hp.sort_files(i, j)

    @unittest.skip('skip test_alldoc_wechat_upload_file')
    def test_alldoc_wechat_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_wechat_upload_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('alldoc')
        hp.open_local_folder('微信')
        self.assertTrue(hp.check_open_folder('微信'), 'open fail')
        hp.file_more_info(2)
        check = hp.upload_file('微信上传')
        if check == None:
            hp.jump_to_index('alldoc')
            hp.open_local_folder('微信')
            self.assertTrue(hp.check_open_folder('微信'), 'open fail')
            hp.file_more_info(7)
            check = hp.upload_file('微信上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_head_logo_show')
    def test_head_logo_show(self):  # 头像显示
        logging.info('==========test_head_logo_show==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('last')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        hp.jump_to_index('alldoc')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        hp.jump_to_index('cloud')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        hp.jump_to_index('star')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        hp.jump_to_index('my')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon')
        self.assertTrue(ele != None)
        hp.login_from_my('13915575564', 'zhang199412')
        hp.jump_to_index('my')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_userinfo')
        self.assertTrue(ele != None)
        hp.logout_action()

    @unittest.skip('skip test_last_delete_file')
    def test_last_delete_file(self):  # “最近”删除文件
        logging.info('==========test_last_delete_file==========')
        hp = HomePageView(self.driver)
        hp.file_more_info(1)
        self.assertTrue(hp.delete_last_file())

    @unittest.skip('skip test_last_mark_star')
    def test_last_mark_star(self):  # 最近中的标星操作
        logging.info('==========test_last_mark_star==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('last')
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertTrue(hp.check_mark_satr(file))
        hp.file_more_info(1)
        file = hp.mark_star()
        self.assertFalse(hp.check_mark_satr(file))

    @unittest.skip('skip test_last_scroll')
    def test_last_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_last_scroll==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        first_name = hp.find_elements(*item_title)[0].text
        ele = '//*[@resource-id="com.yozo.office:id/list_lastfile"]'
        hp.swipe_options(ele)
        second_name = hp.find_elements(*item_title)[0].text
        self.assertTrue(first_name != second_name)

    @unittest.skip('skip test_last_select_all')
    def test_last_select_all(self):  # “最近”全选操作
        logging.info('==========test_last_select_all==========')
        hp = HomePageView(self.driver)
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_last_select_all1')
    def test_last_select_all1(self):  # “最近”全选操作
        logging.info('==========test_last_select_all1==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消全选"]').click()
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num == 0)
        # self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        hp.find_elements(*item)[0].click()
        hp.find_elements(*item)[1].click()
        hp.find_elements(*item)[2].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        time.sleep(1)
        self.assertTrue(hp.get_toast_message('此操作只是将文件从最近列表中删除'))

    @unittest.skip('skip test_share_from_index')
    @data(*index_share_list)
    def test_last_share(self, way):  # “最近”中的分享
        logging.info('==========test_last_share==========')
        hp = HomePageView(self.driver)
        hp.file_more_info(1)
        hp.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_last_share_back')
    def test_last_share_back(self):  # “最近”中的分享的返回键
        logging.info('==========test_last_share_back==========')
        hp = HomePageView(self.driver)
        hp.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_last_show_cloud_file')
    def test_last_show_cloud_file(self):  # 登录时显示云文件
        logging.info('==========test_last_show_cloud_file==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        hp.login_needed()
        hp.jump_to_index('last')
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/tv_from"]'))
        hp.jump_to_index('my')
        hp.logout_action()

    @unittest.skip('skip test_last_show_open_file')
    def test_last_show_open_file(self):  # “最近”中显示已打开的文件
        logging.info('==========test_last_show_open_file==========')
        hp = HomePageView(self.driver)
        file_name = '欢迎使用永中Office.xlsx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        hp.close_file()
        self.driver.press_keycode(4)
        file_ele = '//*[@text="%s"]' % file_name
        self.assertTrue(hp.get_element_result(file_ele))

    @unittest.skip('skip test_last_unlogin_show')
    def test_last_unlogin_show(self):  # 未登录时显示3个内置文件（初次安装）
        logging.info('==========test_last_unlogin_show==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('my')
        exist_files = ['欢迎使用永中Office.docx', '欢迎使用永中Office.pptx', '欢迎使用永中Office.pdf']
        for i in exist_files:
            file_ele = '//*[@text="%s"]' % i
            self.assertTrue(hp.get_element_result(file_ele), '文档不存在')

    @unittest.skip('skip test_my1_about_yozo')
    def test_my1_about_yozo(self):
        logging.info('==========test_my1_about_yozo==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        self.driver.find_element(By.XPATH, '//*[@text="关于YOZO"]').click()
        version_no = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_version').text
        self.assertTrue(version_no != '-')
        web_addr = self.driver.find_element(By.ID, 'com.yozo.office:id/_phone_web').text
        self.assertTrue(web_addr == 'www.yozosoft.com')
        mail_addr = self.driver.find_element(By.ID, 'com.yozo.office:id/_phone_email').text
        self.assertTrue(mail_addr == 'mobile@yozosoft.com')
        phone = self.driver.find_element(By.ID, 'com.yozo.office:id/_phone_phone').text
        self.assertTrue(phone == '400-050-5206')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="关于YOZO"]'))

    @unittest.skip('skip test_my1_head_unlog')
    def test_my1_head_unlog(self):
        logging.info('==========test_my1_head_unlog==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.assertTrue(hp.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_my2_about_head_login')
    def test_my2_head_login(self):  # 已登陆头像功能
        logging.info('==========test_my2_about_head_login==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        username = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_username').text
        self.assertTrue(username != "")
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_userinfo').click()
        self.assertTrue(hp.get_element_result('//*[@text="拍照"]'))
        self.assertTrue(hp.get_element_result('//*[@text="从相册中选取"]'))
        self.assertTrue(hp.get_element_result('//*[@text="取消"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancle').click()

    @unittest.skip('skip test_my2_login_way')
    def test_my2_login_way(self):  # 登录操作
        logging.info('==========test_my2_login_way==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('my')
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_findpwd').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/et_account"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/et_pwd"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/btn_verifycode"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/btn_true"]'))
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_wechat').click()
        self.driver.keyevent(4)
        time.sleep(0.5)
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_register').click()
        self.assertTrue(hp.get_element_result('//*[@text="短信登录"]'))

    @unittest.skip('skip test_my2_logout')
    def test_my2_logout(self):  # 退出登录
        logging.info('==========test_my2_logout==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.swipe_options('//android.widget.ScrollView')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        self.assertTrue(hp.get_element_result('//*[@text="是否退出登录？"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        self.assertTrue(hp.get_element_result('//*[@text="退出登录"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        self.assertTrue(hp.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_my2_sign_up')
    def test_my2_sign_up(self):  # 注册
        logging.info('==========test_my2_login_way==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_register').click()
        self.assertTrue(hp.get_element_result('//*[@text="注册"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').set_text('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_password').set_text('zhang199412')
        self.driver.find_element(By.ID, 'com.yozo.office:id/checkbox_privacy').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/tv_pwd_login2"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/et_figure_code"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/et_pwd"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/btn_verifycode"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/btn_register"]'))
        self.assertTrue(hp.get_element_result('//*[@resource-id="com.yozo.office:id/tv_pwd_login2"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="《隐私政策》"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()
        self.assertTrue(hp.get_element_result('//*[@text="关于YOZO"]'))

    @unittest.skip('skip test_my2_sys_setting')
    def test_my2_sys_setting(self):  # 系统设置
        logging.info('==========test_my2_sys_setting==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        hp.wifi_trans('关闭')
        hp.wifi_trans('开启')
        hp.click_element(*return1)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_element_result('//*[contains(@text,"当前为非wifi环境")]'), '未捕捉到toast')
        

    @unittest.skip('skip test_my_login_fail')
    def test_my_login_fail(self):
        logging.info('==========test_my_login_fail==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('my')
        data = hp.get_csv_data(csv_file, 5)

        hp.login_from_my(data[0], data[1])
        self.assertTrue(hp.get_element_result('//*[@text="忘记密码?"]'), msg='login success')

    @unittest.skip('skip test_login_success')
    def test_my_login_success(self):
        logging.info('==========test_login_success==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('my')
        data = hp.get_csv_data(csv_file, 4)

        hp.login_from_my(data[0], data[1])
        time.sleep(1)
        hp.jump_to_index('my')
        self.assertTrue(hp.check_login_status(), msg='login fail')

        hp.logout_action()

    @unittest.skip('skip test_search_icon_show')
    def test_search_icon_show(self):  # 搜索键显示
        logging.info('==========test_search_icon_show==========')
        hp = HomePageView(self.driver)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
        hp.jump_to_index('alldoc')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
        hp.jump_to_index('star')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
    """
