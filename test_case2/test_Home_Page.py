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
            self.assertTrue(hp.get_message(delete_from_last))
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
        hp.click_element(*first_temp)
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
        hp.click_element(*first_temp)
        time.sleep(1)

        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*temp_download)
        hp.click_element(*return1)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        time.sleep(2)
        hp.click_element(*mytemplate)
        self.assertTrue(hp.get_message(dns_fail))
        time.sleep(2)
        hp.click_element(*my_download)
        hp.click_element(*batch_manage)
        hp.click_element(*delete_temp)
        self.assertTrue(hp.get_message(select_temp))
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
        hp.click_element(*first_temp)
        time.sleep(1)

        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*temp_download)
        hp.click_element(*return1)
        hp.click_element(*mytemplate)
        hp.click_element(*my_download)
        hp.click_element(*batch_manage)
        hp.click_element(*delete_temp)
        self.assertTrue(hp.get_message(select_temp))
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
        hp.click_element(*first_temp)

        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*subscribe)
        hp.click_element(*return1)
        hp.click_element(*mytemplate)
        hp.click_element(*batch_manage)
        hp.click_element(*unsubscribe)
        self.assertTrue(hp.get_message(select_temp))
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
        hp.click_element(*first_temp)

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
    def test_last_create_template_search(self, file_index='last_pg'):  # 最近_新建_模板搜索
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
        hp.create_file_preoption(file_type, x_create, y_create)
        while not hp.get_message(no_more_data):
            if hp.get_message(change):
                temp_name1 = hp.find_element(*first_temp_name).text
                hp.click_element(*change)
                time.sleep(1)
                temp_name2 = hp.find_element(*first_temp_name).text
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
        hp.create_file_preoption(file_type, x_create, y_create)
        while not hp.get_message(no_more_data):
            hp.swipe_options('//androidx.recyclerview.widget.RecyclerView')

        hp.click_element(*first_temp)
        time.sleep(1)
        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*apply)

        if not hp.is_visible(*mode_switch, 60):
            raise
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
        hp.click_element(*first_temp)
        hp.click_element(*apply)
        if not hp.is_visible(*mode_switch, 60):
            raise
        hp.click_element(*mode_switch)
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
        hp.click_element(*first_temp)
        time.sleep(1)
        temp_name = hp.find_element(*temp_title).text
        hp.click_element(*apply)
        if not hp.is_visible(*mode_switch, 60):
            raise
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
        hp.click_element(*first_temp)
        hp.click_element(*apply)
        if not hp.is_visible(*mode_switch, 60):
            raise
        hp.click_element(*mode_switch)
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
        hp.click_element(*upload)
        hp.click_element(*upload_save)
        self.assertTrue(hp.get_message(upload_success))

    @unittest.skip('test_last_nonet_upload02')
    def test_last_nonet_upload02(self):  # 最近_未联网_上传
        logging.info('==========test_last_nonet_upload==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
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
        hp.click_element(*upload)
        hp.click_element(*upload_save)
        self.assertTrue(hp.get_message(upload_fail))

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
        hp.click_element(*upload)
        self.assertTrue(hp.get_message(no_wifi))

    @unittest.skip('test_last_unlogin_upload')
    def test_last_unlogin_upload(self):  # 最近_联网/未联网未登录本机文档上传
        logging.info('==========test_last_unlogin_upload==========')
        hp = HomePageView(self.driver)
        if hp.check_login_status():
            hp.logout_action()
        hp.jump_to_index('last')
        hp.file_more_info(0)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_message(login_first))
        time.sleep(2)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(hp.get_message(login_first))

    @unittest.skip('test_last_multi_select_file')
    def test_last_multi_select_file(self):  # 文档多选_删除
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.file_more_info(0)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[0].click()
        num1 = hp.find_element(*selected_num).text
        self.assertTrue(int(num1) == 1)

        hp.click_element(*select_all)
        num2 = hp.find_element(*selected_num).text
        self.assertTrue(int(num2) >= 1)
        hp.click_element(*multi_upload)
        self.assertTrue(hp.get_message(cloud_exist))
        time.sleep(2)
        hp.click_element(*cancel_all)
        num3 = hp.find_element(*selected_num).text
        self.assertTrue(int(num3) == 0)
        hp.click_element(*multi_delete)
        self.assertTrue(hp.get_message(select_file_first))
        time.sleep(2)
        hp.click_element(*multi_upload)
        self.assertTrue(hp.get_message(select_file_first))
        hp.find_elements(*item)[0].click()
        hp.click_element(*multi_delete)
        self.assertFalse(hp.get_message(delete_from_last))

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
        hp.click_element(*download)
        # 判定
        self.assertTrue(hp.get_message(download_success))

    @unittest.skip('test_last_cloud_logo')
    def test_last_cloud_logo(self):  # 最近_云文档标识小云朵
        logging.info('==========test_last_cloud_logo==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.find_element(*cloud_logo)

    # ======2020_04_21====== #
    @unittest.skip('test_search')
    @data(*act_index1)
    def test_search(self, index='star'):  # 最近/打开/标星_搜索
        logging.info('==========test_account_logo==========')
        hp = HomePageView(self.driver)
        # hp.login_needed()
        hp.jump_to_index(index)
        hp.click_element(*search)

        # 搜索存在的文件
        hp.find_element(*search_input).send_keys('欢迎使用永中Office.pdf')
        hp.click_element(*search_start)
        # 判定是否搜索到
        hp.find_elements(*item)

        # 搜索不存在的文件
        hp.find_element(*search_input).send_keys('***')
        hp.click_element(*search_start)
        # 判定是否搜索到
        self.assertTrue(hp.get_message(search_no_result))

        # 清空搜索关键词
        hp.click_element(*search_keyword_clear)
        self.assertTrue(hp.get_message(search_tips))
        # 无关键词搜索
        hp.click_element(*search_start)
        # 判定是否搜索到
        hp.find_elements(*item)

    @unittest.skip('test_account_logo')
    @data(*act_index)
    def test_account_logo(self, index='star'):  # 最近/打开/云文档/标星_头像
        logging.info('==========test_account_logo==========')
        hp = HomePageView(self.driver)
        # hp.login_needed()
        hp.jump_to_index(index)
        hp.click_element(*account_logo)
        # 判定是否跳转
        self.assertTrue(hp.get_message(about_yozo))

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
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.hide_keyboard()
        hp.click_element(*account_edit)
        username = hp.find_element(*nickname2).text
        self.assertTrue(username != "")
        hp.find_element(*nickname2).click()
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(nickname_not_change))
        name_time = hp.getTime("%Y%m%d%H%M%S")
        hp.find_element(*nickname_edit).send_keys(name_time)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(info_modified_success))
        name_now = hp.find_element(*nickname2).text
        self.assertTrue(name_time == name_now)
        account1 = hp.find_element(*account).text
        self.assertTrue(account1 == '139****5564')
        email = hp.find_element(*account_email).text
        self.assertTrue(email == 'branezhang@163.com')
        hp.click_element(*account_email)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(please_enter_email))
        hp.find_element(*enter_email).send_keys('3451')
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(incorrect_email_format))
        time.sleep(2)
        hp.find_element(*enter_email).send_keys('345126454@qq.com')
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(please_enter_verfycode))
        time.sleep(2)
        hp.find_element(*enter_email_verfycode).send_keys('3451')
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_message(email_verfycode_wrong))

    @unittest.skip('test_my_nonet_logout_convert_tool')
    def test_my_nonet_logout_convert_tool(self):  # 我的_非登录_未联网_转换工具
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)

        hp.click_element(*convert_tools)
        eles = hp.find_element(*convert_item)
        for i in eles:
            i.click()
            self.assertTrue(hp.get_message(check_net))
            time.sleep(3)

    @unittest.skip('test_my_logout_convert_tool')
    def test_my_logout_convert_tool(self):  # 我的_非登录_联网_转换工具
        logging.info('==========test_my_logout_convert_tool==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        if hp.check_login_status():
            hp.logout_action()
            hp.jump_to_index('my')
        hp.click_element(*convert_tools)
        eles = hp.find_element(*convert_item)
        for i in eles:
            i.click()
            self.assertTrue(hp.get_message(login4more_functions))
            time.sleep(2)

    @unittest.skip('test_cloud_auto_upload_folder')
    def test_cloud_auto_upload_folder(self):  # 云文档_自动上传
        logging.info('==========test_cloud_nonet_search==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        folder_name = hp.find_elements(*item)[0].text
        self.assertTrue(folder_name == '自动上传')

    @unittest.skip('test_cloud_nonet_search')
    def test_cloud_nonet_search(self):  # 云文档_未联网_搜索
        hp = HomePageView(self.driver)
        hp.login_needed()
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.jump_to_index('cloud')
        hp.click_element(*search)
        hp.click_element(*search_start)
        self.assertFalse(hp.get_message(item))

    # ======2020_04_20====== #
    @unittest.skip('test_my_logout')
    def test_my_logout(self):  # 退出登录
        logging.info('==========test_my_about==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.swipe_ele(about_yozo,convert_tools)
        hp.click_element(*logout)
        hp.click_element(*pop_cancel)
        hp.click_element(*logout)
        hp.click_element(*pop_confirm)
        hp.find_element(*mytemplate)
        self.driver.find_element(*recycle)

    @unittest.skip('test_my_about')
    def test_my_about(self):  # 关于永中
        logging.info('==========test_my_about==========')
        hp = HomePageView(self.driver)
        hp.jump_to_index('my')
        hp.click_element(*about_yozo)
        hp.click_element(*version)
        addr = hp.find_element(*yozo_web).text
        email = hp.find_element(*yozo_email).text
        phone = hp.find_element(*yozo_phone).text
        self.assertListEqual([addr, email, phone], ['www.yozosoft.com', 'mobile@yozosoft.com', '400-050-5206'])
        hp.click_element(*share2others)
        hp.find_element(*download_QR)

    @unittest.skip('test_my_nonet_recycle')
    def test_my_nonet_recycle(self):  # 回收站_未联网
        logging.info('==========test_my_nonet_recycle==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.click_element(*recycle)
        self.assertTrue(hp.get_message(net_exception))

    @unittest.skip('test_my_recycle_restore')
    def test_my_recycle_restore(self):  # 回收站_联网_还原
        logging.info('==========test_my_nonet_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.click_element(*cloud_add_folder)
        folder_name = '0000'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        time.sleep(1)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[index].click()
        hp.find_elements(*item)[1].click()
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
        hp.jump_to_index('my')
        hp.click_element(*recycle)
        index = hp.identify_file_index()
        hp.find_elements(*item)[index].click()
        self.assertTrue(hp.find_element(*selected_num).text == '1')
        hp.click_element(*select_all)
        hp.click_element(*cancel_all)
        hp.click_element(*multi_cancel)
        file_name = hp.find_elements(*item_title)[index].text
        hp.find_elements(*item)[index].click()
        hp.click_element(*recycle_revert)
        self.assertTrue(hp.get_message(already_revert))
        hp.find_elements(*item)[index - 1].click()
        hp.click_element(*recycle_delete)
        hp.click_element(*pop_confirm)
        self.assertTrue(hp.get_message(already_delete))
        hp.click_element(*return4)
        hp.jump_to_index('cloud')
        self.assertTrue(hp.get_toast_message('%s' % file_name))

    @unittest.skip('test_my_recycle_empty')
    def test_my_recycle_empty(self):  # 回收站_联网_清空
        logging.info('==========test_my_nonet_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.click_element(*cloud_add_folder)
        folder_name = '0000'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[index].click()
        hp.find_elements(*item)[1].click()
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
        hp.jump_to_index('my')
        hp.click_element(*recycle)
        hp.click_element(*recycle_clear)
        hp.click_element(*pop_cancel)
        index = hp.identify_file_index()
        hp.find_elements(*item_title)[index - 1].click()
        self.assertTrue(hp.get_message(cannot_open))
        hp.find_elements(*item_title)[index].click()
        time.sleep(3)
        hp.click_element(*close)
        hp.click_element(*recycle_clear)
        hp.click_element(*pop_confirm)
        self.assertTrue(hp.get_message(already_clear))

    @unittest.skip('test_my_nonet_feedback_history')
    def test_my_nonet_feedback_history(self):  # 意见反馈_联网_历史反馈记录
        logging.info('==========test_my_nonet_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.click_element(*feedback)
        hp.click_element(*feedback_history)
        self.assertTrue(hp.get_message(dns_fail))

        hp.click_element(*return1)

    @unittest.skip('test_my_feedback_history')
    def test_my_feedback_history(self):  # 意见反馈_联网_历史反馈记录
        logging.info('==========test_my_feedback_history==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*feedback)
        hp.click_element(*feedback_history)
        while not hp.get_message(no_more_data):
            hp.swipe_options('//*[@resource-id="com.yozo.office:id/rv"]')
        hp.click_element(*return1)

    @unittest.skip('test_my_nonet_feedback')
    def test_my_nonet_feedback(self):  # 意见反馈_未联网_反馈分类
        logging.info('==========test_my_nonet_feedback==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.click_element(*feedback)
        
        hp.find_element(*feedback_content).send_keys('aaaaa')
        hp.find_element(*feedback_contact).send_keys('13915575564')
        hp.swipe_ele(feedback_contact,feedback_content)
        hp.click_element(*feedback_submit)
        self.assertTrue(hp.get_message(no_wifi))
        hp.click_element(*return1)
        hp.click_element(*sys_setting)
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        hp.click_element(*feedback)
        hp.find_element(*feedback_content).send_keys('aaaaa')
        hp.find_element(*feedback_contact).send_keys('13915575564')
        hp.swipe_ele(feedback_contact, feedback_content)
        hp.click_element(*feedback_submit)
        self.assertTrue(hp.get_message(dns_fail))
        hp.click_element(*return1)
        hp.click_element(*sys_setting)
        hp.wifi_trans('开启')

    @unittest.skip('test_my_feedback')
    def test_my_feedback(self):  # 意见反馈_联网_反馈分类
        logging.info('==========test_my_feedback==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*feedback)
        hp.swipe_ele(feedback_contact, feedback_content)
        hp.click_element(*feedback_submit)
        self.assertTrue(hp.get_message(enter_feedback_content))
        no_input = 0
        input_str = ''
        while no_input < 30:
            input_str += 'AAAAAAAAAA'
            no_input += 1
        hp.find_element(*feedback_content).send_keys(input_str)
        content = hp.find_element(*feedback_content).text
        self.assertTrue(len(content) == 200, '反馈不等于200个字')
        hp.swipe_ele(feedback_contact, feedback_content)
        hp.click_element(*feedback_submit)
        self.assertTrue(hp.get_message(enter_feedback_contact))
        time.sleep(2)
        hp.find_element(*feedback_contact).send_keys('11111')
        hp.swipe_ele(feedback_contact, feedback_content)
        hp.click_element(*feedback_submit)
        self.assertTrue(hp.get_message(contact_wrong))
        hp.find_element(*feedback_contact).send_keys('13915575564')
        hp.swipe_ele(feedback_contact, feedback_content)
        hp.click_element(*feedback_submit)
        self.assertTrue(hp.get_message(feedback_submit_success))

    @unittest.skip('test_my_nonet_template_subscribe_download')
    def test_my_nonet_template_subscribe_download(self):  # 我的模板_未联网_收藏/下载
        logging.info('==========test_my_nonet_template_subscribe_download==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*my_template)
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        hp.click_element(*temp_download)
        hp.click_element(*return1)
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        hp.click_element(*my_download)
        hp.click_element(*my_subscribe)
        self.assertTrue(hp.get_message(dns_fail))
        hp.click_element(*my_download)
        hp.click_element(*batch_manage)
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        hp.click_element(*delete_temp)
        hp.click_element(*pop_confirm)

    @unittest.skip('test_my_template_subscribe_download')
    def test_my_template_subscribe_download(self):  # 我的模板_联网_收藏/下载
        logging.info('==========test_my_template_subscribe_download==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*my_template)
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        time.sleep(1)
        file_name = hp.find_element(*temp_title).text
        hp.click_element(*subscribe)
        self.assertTrue(hp.get_message(already_unsubscribe))
        hp.click_element(*apply)
        hp.click_element(*close)
        time.sleep(1)
        self.assertFalse(hp.get_element_result('//*[@text="%s"]' % file_name))
        hp.click_element(*my_download)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % file_name).click()
        hp.click_element(*subscribe)
        self.assertTrue(hp.get_message(already_subscribe))
        hp.click_element(*apply)
        hp.click_element(*close)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % file_name).click()
        hp.click_element(*temp_download)
        hp.click_element(*pop_confirm)
        time.sleep(1)
        # self.assertFalse(hp.get_element_result('//*[@text="%s"]'%file_name))
        hp.click_element(*my_subscribe)
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file_name))

    @unittest.skip('test_my_template_handle')
    def test_my_template_handle(self):  # 我的模板_批量管理
        logging.info('==========test_my_template==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*my_template)
        hp.click_element(*feedback_history)
        hp.click_element(*delete_temp)
        self.assertTrue(hp.get_message(select_temp))
        hp.click_element(*my_download)
        hp.click_element(*delete_temp)
        self.assertTrue(hp.get_message(select_temp))
        hp.click_element(*my_subscribe)
        self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')[
            0].click()
        hp.click_element(*delete_temp)
        hp.click_element(*pop_cancel)
        hp.click_element(*delete_temp)
        hp.click_element(*pop_confirm)

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
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*sys_setting)
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
        hp.click_element(*save_confirm)
        self.assertTrue(hp.get_toast_message('上传失败'))

        hp.file_more_info(0)
        hp.mark_star()
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
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
        self.assertTrue(hp.get_message(no_wifi))

        hp.file_more_info(0)
        hp.mark_star()

    @unittest.skip('test_cloud_nonet_multi_select_download02')
    def test_cloud_nonet_multi_select_download02(self):  # 云文档_未联网_云文档操作_多选_下载
        logging.info('==========test_cloud_nonet_multi_select_download02==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
        hp.wifi_trans('关闭')
        hp.click_element(*return1)
        hp.jump_to_index('cloud')
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        index = hp.identify_file_index()
        hp.file_more_info(index)
        hp.click_element(*multi_select)
        hp.find_elements(*item)[index].click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_toast_message('文件下载失败'))

        hp.click_element(*multi_cancel)
        hp.jump_to_index('my')
        hp.click_element(*sys_setting)
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
        hp.click_element(*multi_select)
        hp.find_elements(*item)[index].click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        self.assertTrue(hp.get_message(no_wifi))
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
        hp.click_element(*multi_select)
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
        hp.click_element(*multi_select)
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
        hp.click_element(*multi_select)
        hp.find_elements(*item)[6].click()
        hp.find_elements(*item)[7].click()
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*delete)
        hp.click_element(*pop_cancel)
        hp.file_more_info(7)
        hp.click_element(*delete)
        name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_show_title').text
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('网络连接异常'))

    @unittest.skip('test_cloud_file_delete')
    def test_cloud_file_delete(self):  # 云文档_联网_云文档操作_删除
        logging.info('==========test_cloud_file_delete==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')
        hp.file_more_info(7)

        logging.info('==========delete operation==========')
        hp.click_element(*delete)
        hp.click_element(*pop_cancel)
        hp.file_more_info(7)
        hp.click_element(*delete)
        name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_show_title').text
        hp.click_element(*pop_confirm2)
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

        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.hide_keyboard()
            hp.find_element(*cloud_folder_name).send_keys(folder_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        folder_name = '01234567890123456789012345678901234567890'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '0000'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
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

        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.hide_keyboard()
            hp.find_element(*cloud_folder_name).send_keys(folder_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        folder_name = '01234567890123456789012345678901234567890'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*sys_setting)
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
        self.assertTrue(hp.get_message(no_wifi))

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
        hp.click_element(*delete)
        hp.click_element(*pop_cancel)
        hp.file_more_info(2)
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
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
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('网络连接异常'))

        hp.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()

        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            self.driver.hide_keyboard()
            hp.find_element(*cloud_folder_name).send_keys(folder_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)

        folder_name = '01234567890123456789012345678901234567890'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*cloud_add_folder)
        # 验证弹出框的内容
        hp.find_element(*temp_title)
        hp.find_element(*cloud_folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true')
        hp.click_element(*pop_cancel)

        hp.click_element(*cloud_add_folder)
        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            hp.find_element(*cloud_folder_name).send_keys(folder_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)
        folder_name = '01234567890123456789012345678901234567890'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '0000'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*multi_select)
        hp.find_elements(*item)[0].click()
        hp.find_elements(*item)[1].click()
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_choose_file_cancel').click()
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_choose_file_ok').click()
        self.driver.find_element(By.XPATH, '//*[@text="保存"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消上传"]').click()
        hp.file_more_info(1)
        hp.click_element(*multi_select)
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
        hp.click_element(*multi_select)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        hp.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text.strip()
        hp.click_element(*multi_select)
        self.driver.find_element(By.XPATH, '//*[@text="已选择"]')
        self.driver.find_element(By.XPATH, '//*[@text="0"]')
        self.driver.find_element(By.XPATH, '//*[@text="个文件"]')

        hp.click_element(*select_all)
        self.assertTrue(hp.get_element_result('//*[@text="取消全选"]'))
        num = int(hp.find_element(*selected_num).text)
        self.assertTrue(num != 0)
        hp.click_element(*delete)
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
        hp.click_element(*pop_cancel)
        hp.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()
        hp.find_element(*cloud_folder_name).set_text(newName)
        hp.click_element(*pop_confirm2)
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
        hp.find_element(*cloud_folder_name).send_keys('1111')
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*account_logo)
        hp.jump_to_index('star')
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % file_name))
        hp.jump_to_index('alldoc')
        hp.select_file_type('all')
        hp.file_more_info(1)
        file_name = hp.mark_star()
        self.assertFalse(hp.get_element_result('//*[@resource-id="com.yozo.office:id/iv_star"]'))
        hp.click_element(*account_logo)
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
        hp.click_element(*multi_select)
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
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*multi_select)
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
        hp.click_element(*multi_cancel)
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
        hp.click_element(*multi_select)
        eles = hp.find_elements(*item)
        name1 = eles[6].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        name2 = eles[7].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        names_del = [name1, name2]
        eles[6].click()
        eles[7].click()
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*multi_select)
        num2 = hp.find_element(*selected_num).text
        self.assertTrue(int(num2) == 0)

        hp.find_elements(*item)[5].click()
        hp.find_elements(*item)[6].click()
        hp.find_elements(*item)[7].click()
        num2 = hp.find_element(*selected_num).text
        self.assertTrue(int(num2) == 3)

        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        num = hp.find_element(*selected_num).text
        self.assertTrue(int(num) != 0)

        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        num1 = hp.find_element(*selected_num).text
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
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
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
        hp.click_element(*cloud_add_folder)
        folder_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')
        hp.file_more_info(2)
        hp.click_element(*delete)
        hp.click_element(*pop_cancel)
        hp.file_more_info(2)
        hp.click_element(*delete)
        hp.click_element(*pop_confirm2)
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

        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('原文件名和新文件名一样，无需重命名'))

        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            hp.find_element(*cloud_folder_name).send_keys(folder_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)
        folder_name = '01234567890123456789012345678901234567890'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '自动上传'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('文件名已存在'))

        hp.file_more_info(3)
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()
        folder_name = hp.getTime('%Y%m%d%H%M%S')
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), 'folder rename fail')

    @unittest.skip('skip test_cloud_folder_options')
    @data(*options)
    def test_cloud_folder_options(self, option='移动'):  # 云文档_联网_文件夹操作_移动
        logging.info('==========test_cloud_folder_options==========')
        hp = HomePageView(self.driver)
        hp.login_needed()
        hp.jump_to_index('cloud')

        hp.click_element(*cloud_add_folder)
        folder_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')
        hp.file_more_info(2)

        logging.info('==========move action==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()
        hp.find_elements(*item)[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        self.assertTrue(hp.get_toast_message('目标文件夹与源文件相同。'))

        hp.click_element(*account_logo)
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
        hp.click_element(*cloud_add_folder)
        # 验证弹出框的内容
        hp.find_element(*temp_title)
        hp.find_element(*cloud_folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true')
        hp.click_element(*pop_cancel)

        hp.click_element(*cloud_add_folder)
        spec_char = ['/', '\\', ':', '?', '<', '>', '|']
        for i in spec_char:
            folder_name = i
            hp.find_element(*cloud_folder_name).send_keys(folder_name)
            hp.click_element(*pop_confirm2)
            self.assertTrue(hp.get_toast_message('请不要包含特殊字符'))
            time.sleep(2)
        folder_name = '01234567890123456789012345678901234567890'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_toast_message('不得大于40个字符'))

        folder_name = '0000'
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')

        hp.click_element(*cloud_add_folder)
        hp.find_element(*cloud_folder_name).send_keys(folder_name)
        hp.click_element(*pop_confirm2)
        self.assertTrue(hp.get_element_result('//*[@text="%s(1)"]' % folder_name), '文件夹新建失败')

        e1 = hp.find_elements(*item)[1]
        e1.find_element(By.ID, 'com.yozo.office:id/lay_more').click()
        hp.delete_file()
        time.sleep(1)
        e1 = hp.find_elements(*item)[1]
        e1.find_element(By.ID, 'com.yozo.office:id/lay_more').click()
        hp.delete_file()
