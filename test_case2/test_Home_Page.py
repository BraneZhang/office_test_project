#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import time
import unittest

from appium.webdriver.connectiontype import ConnectionType
from ddt import ddt, data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from data import data_info

csv_file = data_info.csv_file
folder_list = data_info.folder_list
index_share_list = data_info.index_share_list
index_share_list1 = data_info.index_share_list1
way_list = data_info.way_list
wps = data_info.wps
search_template_dict = data_info.search_template_dict
templates_dict = data_info.templates_dict
screenshot_file = '../screenshots/'


@ddt
class TestHomePage(StartEnd):

    @unittest.skip('skip test_hp_template_category')
    @data(*wps)
    def test_hp_my2_template_zoom_apply(self, file_type='ss'):  # 模板类别
        logging.info('==========test_hp_template_category==========')
        hp = HomePageView(self.driver)
        hp.login_on_needed()
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

    @unittest.skip('skip test_hp_template_category')
    @data(*wps)
    def test_hp_my2_template_category(self, file_type='pg'):  # 模板类别
        logging.info('==========test_hp_template_category==========')
        hp = HomePageView(self.driver)
        hp.login_on_needed()
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
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()
        fresh_before = self.driver.find_element(By.ID, 'com.yozo.office:id/tpTitle1').text
        self.driver.find_element(By.ID, 'com.yozo.office:id/changeTv').click()
        fresh_after = self.driver.find_element(By.ID, 'com.yozo.office:id/tpTitle1').text
        self.assertFalse(fresh_before == fresh_after)

    @unittest.skip('skip test_template_search')
    @data(*wps)
    def test_hp_my2_template_search(self, file_type='wp'):
        logging.info('==========test_hp_create_blank_file==========')
        hp = HomePageView(self.driver)
        hp.login_on_needed()
        hp.jump_to_index('last')
        hp.create_file_preoption(file_type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/searchTv').click()
        keywords = search_template_dict[file_type]

        logging.info('======模板名或分类搜索======')
        for i in keywords:
            self.driver.find_element(By.ID, 'com.yozo.office:id/et').set_text(i)
            self.driver.find_element(By.ID, 'com.yozo.office:id/searchv').click()
            self.assertFalse(hp.get_toast_message('没有找到相关模板'), '模板名或分类搜索失败')

        logging.info('======历史记录显示======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et').clear()
        results = list(map(lambda e: hp.get_element_result('//*[@text="%s"]' % e), keywords))
        print(False in results)
        self.assertFalse(False in results)

        logging.info('======历史记录选取======')
        record_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/flowHistory')
        record_ele.find_elements(By.XPATH, '//android.widget.TextView')[0].click()
        select_record = record_ele.find_elements(By.XPATH, '//android.widget.TextView')[0].text
        edit_content = self.driver.find_element(By.ID, 'com.yozo.office:id/et').text
        self.assertTrue(select_record == edit_content, '历史记录选取错误')

        logging.info('======历史记录删除======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et').clear()
        self.driver.find_element(By.ID, 'com.yozo.office:id/trash').click()
        clear_result = record_ele.find_elements(By.XPATH, '//android.widget.TextView')
        print(len(clear_result))
        self.assertTrue(len(clear_result) == 0, '历史记录删除失败')

    @unittest.skip('skip test_hp_create_blank_file')
    @data(*wps)
    def test_hp_create_blank_file(self, file_type='wp'):
        logging.info('==========test_hp_create_blank_file==========')
        hp = HomePageView(self.driver)
        hp.create_file(file_type)
        self.assertTrue(hp.get_element_result('//*[contains(@text, "新建空白")]'))

    @unittest.skip('skip test_hp_my2_templates_options')
    @data(*way_list)
    def test_hp_my2_templates_options(self, way='下载'):
        logging.info('==========test_hp_my2_templates_options==========')
        hp = HomePageView(self.driver)
        hp.login_on_needed()
        for i in ['ss', 'wp', 'pg']:
            result = hp.templates_access(i, *[way])
            self.assertTrue(result, '%s%s失败' % (i, way))
        self.assertTrue(hp.templates_preview(way), '模板为空')
        self.assertTrue(hp.templates_delete(), '删除成功')
        self.driver.find_element(By.XPATH, '//*[@text="完成"]').click()
        self.assertTrue(hp.get_element_result('//*[@text="批量管理"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()
        self.assertTrue(hp.get_element_result('//*[@text="我的模板"]'))

    @unittest.skip('skip test_hp_alldoc_copy_file')
    def test_hp_alldoc_copy_file(self):  # “打开”复制文件
        logging.info('==========test_hp_alldoc_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = gv.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_hp_alldoc_delete_file')
    def test_hp_alldoc_delete_file(self):
        logging.info('==========test_hp_alldoc_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.sort_files('name', 'up')
        gv.file_more_info(1)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        name = filename + '.' + suffix
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name), 'delete fail')
        # file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        # index_e = file_path.rindex('/') + 1
        # name = file_path[index_e:]
        # gv.delete_file()
        # self.driver.keyevent(4)
        # self.assertFalse(gv.search_file(name))

    @unittest.skip('skip test_hp_alldoc_download_copy_file')
    def test_hp_alldoc_download_copy_file(self):
        logging.info('==========test_hp_alldoc_download_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = gv.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_hp_alldoc_download_delete_file')
    def test_hp_alldoc_download_delete_file(self):
        logging.info('==========test_hp_alldoc_download_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_hp_alldoc_download_file_info')
    def test_hp_alldoc_download_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_alldoc_download_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_download_mark_star')
    def test_hp_alldoc_download_mark_star(self):
        logging.info('==========test_hp_alldoc_download_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_alldoc_download_move_file')
    def test_hp_alldoc_download_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_alldoc_download_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_hp_alldoc_download_rename_file')
    def test_hp_alldoc_download_rename_file(self):
        logging.info('==========test_hp_alldoc_download_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_hp_alldoc_download_search_file')
    def test_hp_alldoc_download_search_file(self):  # 搜索功能
        logging.info('==========test_hp_alldoc_download_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_alldoc_download_select_all')
    def test_hp_alldoc_download_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_alldoc_download_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_alldoc_download_select_all1')
    def test_hp_alldoc_download_select_all1(self):
        logging.info('==========test_hp_alldoc_download_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_hp_alldoc_download_share')
    @data(*index_share_list)
    def test_hp_alldoc_download_share(self, way):
        logging.info('==========test_hp_alldoc_download_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_alldoc_download_share_back')
    def test_hp_alldoc_download_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_hp_alldoc_download_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_download_sort_file')
    def test_hp_alldoc_download_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_alldoc_download_sort_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_hp_alldoc_download_upload_file')
    def test_hp_alldoc_download_upload_file(self):  # 上传文件
        logging.info('==========test_hp_alldoc_download_upload_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file('Download上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_alldoc_file_info')
    def test_hp_alldoc_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_alldoc_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
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

    @unittest.skip('skip test_hp_alldoc_local_folder')
    @data(*folder_list)
    def test_hp_alldoc_local_folder(self, folder):  # 测试本地文档打开
        logging.info('==========test_hp_alldoc_local_folder==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder(folder)
        self.assertTrue(gv.check_open_folder(folder), 'open fail')

    @unittest.skip('skip test_hp_alldoc_mark_star')
    def test_hp_alldoc_mark_star(self):
        logging.info('==========test_hp_alldoc_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_alldoc_mobile_copy_file')
    def test_hp_alldoc_mobile_copy_file(self):
        logging.info('==========test_hp_alldoc_mobile_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = gv.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_hp_alldoc_mobile_delete_file')
    def test_hp_alldoc_mobile_delete_file(self):
        logging.info('==========test_hp_alldoc_mobile_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0].click()
        gv.file_more_info(1)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        # self.driver.keyevent(4)
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_hp_alldoc_mobile_file_info')
    def test_hp_alldoc_mobile_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_alldoc_mobile_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_mobile_mark_star')
    def test_hp_alldoc_mobile_mark_star(self):
        logging.info('==========test_hp_alldoc_mobile_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_alldoc_mobile_move_file')
    def test_hp_alldoc_mobile_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_alldoc_mobile_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_hp_alldoc_mobile_rename_file')
    def test_hp_alldoc_mobile_rename_file(self):
        logging.info('==========test_hp_alldoc_mobile_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_hp_alldoc_mobile_search_file')
    def test_hp_alldoc_mobile_search_file(self):  # 搜索功能
        logging.info('==========test_hp_alldoc_mobile_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_alldoc_mobile_select_all')
    def test_hp_alldoc_mobile_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_alldoc_mobile_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_alldoc_mobile_select_all1')
    def test_hp_alldoc_mobile_select_all1(self):
        logging.info('==========test_hp_alldoc_mobile_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        name_list = gv.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_hp_alldoc_mobile_share')
    @data(*index_share_list)
    def test_hp_alldoc_mobile_share(self, way):
        logging.info('==========test_hp_alldoc_mobile_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_alldoc_mobile_share_back')
    def test_hp_alldoc_mobile_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_hp_alldoc_mobile_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_mobile_sort_file')
    def test_hp_alldoc_mobile_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_alldoc_mobile_sort_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_hp_alldoc_mobile_upload_file')
    def test_hp_alldoc_mobile_upload_file(self):  # 上传文件
        logging.info('==========test_hp_alldoc_mobile_upload_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(7)
        check = gv.upload_file('手机上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_alldoc_move_file')
    def test_hp_alldoc_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_alldoc_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_hp_alldoc_myfile_copy_file')
    def test_hp_alldoc_myfile_copy_file(self):
        logging.info('==========test_hp_alldoc_myfile_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = gv.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_hp_alldoc_myfile_delete_file')
    def test_hp_alldoc_myfile_delete_file(self):
        logging.info('==========test_hp_alldoc_myfile_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        # self.driver.keyevent(4)
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_hp_alldoc_myfile_file_info')
    def test_hp_alldoc_myfile_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_alldoc_myfile_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_myfile_mark_star')
    def test_hp_alldoc_myfile_mark_star(self):
        logging.info('==========test_hp_alldoc_myfile_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_alldoc_myfile_move_file')
    def test_hp_alldoc_myfile_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_alldoc_myfile_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_hp_alldoc_myfile_rename_file')
    def test_hp_alldoc_myfile_rename_file(self):
        logging.info('==========test_hp_alldoc_myfile_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_hp_alldoc_myfile_search_file')
    def test_hp_alldoc_myfile_search_file(self):  # 搜索功能
        logging.info('==========test_hp_alldoc_myfile_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_alldoc_myfile_select_all')
    def test_hp_alldoc_myfile_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_alldoc_myfile_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_alldoc_myfile_select_all1')
    def test_hp_alldoc_myfile_select_all1(self):
        logging.info('==========test_hp_alldoc_myfile_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_hp_alldoc_myfile_share')
    @data(*index_share_list)
    def test_hp_alldoc_myfile_share(self, way):
        logging.info('==========test_hp_alldoc_myfile_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_alldoc_myfile_share_back')
    def test_hp_alldoc_myfile_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_hp_alldoc_myfile_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_myfile_sort_file')
    def test_hp_alldoc_myfile_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_alldoc_myfile_sort_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_hp_alldoc_myfile_upload_file')
    def test_hp_alldoc_myfile_upload_file(self):  # 上传文件
        logging.info('==========test_hp_alldoc_myfile_upload_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file('我的文档上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_alldoc_qq_copy_file')
    def test_hp_alldoc_qq_copy_file(self):
        logging.info('==========test_hp_alldoc_qq_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_hp_alldoc_qq_delete_file')
    def test_hp_alldoc_qq_delete_file(self):
        logging.info('==========test_hp_alldoc_qq_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_hp_alldoc_qq_file_info')
    def test_hp_alldoc_qq_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_alldoc_qq_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_qq_mark_star')
    def test_hp_alldoc_qq_mark_star(self):
        logging.info('==========test_hp_alldoc_qq_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_alldoc_qq_move_file')
    def test_hp_alldoc_qq_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_alldoc_qq_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_hp_alldoc_qq_rename_file')
    def test_hp_alldoc_qq_rename_file(self):
        logging.info('==========test_hp_alldoc_qq_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_hp_alldoc_qq_search_file')
    def test_hp_alldoc_qq_search_file(self):  # 搜索功能
        logging.info('==========test_hp_alldoc_qq_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_alldoc_qq_select_all')
    def test_hp_alldoc_qq_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_alldoc_qq_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_alldoc_qq_select_all1')
    def test_hp_alldoc_qq_select_all1(self):
        logging.info('==========test_hp_alldoc_qq_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_hp_alldoc_qq_share')
    @data(*index_share_list)
    def test_hp_alldoc_qq_share(self, way):
        logging.info('==========test_hp_alldoc_qq_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_alldoc_qq_share_back')
    def test_hp_alldoc_qq_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_hp_alldoc_qq_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_qq_sort_file')
    def test_hp_alldoc_qq_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_alldoc_qq_sort_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_hp_alldoc_qq_upload_file')
    def test_hp_alldoc_qq_upload_file(self):  # 上传文件
        logging.info('==========test_hp_alldoc_qq_upload_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file('QQ上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_alldoc_rename_file')
    def test_hp_alldoc_rename_file(self):
        logging.info('==========test_hp_alldoc_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_hp_alldoc_scroll')
    def test_hp_alldoc_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_hp_alldoc_scroll==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        first_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        gv.swipeUp()
        second_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        self.assertTrue(first_name != second_name)

    @unittest.skip('skip test_hp_alldoc_search_file')
    def test_hp_alldoc_search_file(self):  # 搜索功能
        logging.info('==========test_hp_alldoc_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_alldoc_select_all')
    def test_hp_alldoc_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_alldoc_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_alldoc_select_all1')
    def test_hp_alldoc_select_all1(self):
        logging.info('==========test_hp_alldoc_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.sort_files('name', 'up')
        gv.file_more_info(1)
        name_list = gv.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(gv.search_file(i))
            self.driver.keyevent(4)

    @unittest.skip('skip test_hp_alldoc_share')
    @data(*index_share_list)
    def test_hp_alldoc_share(self, way):
        logging.info('==========test_hp_alldoc_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_alldoc_share_back')
    def test_hp_alldoc_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_hp_alldoc_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_show_file')
    def test_hp_alldoc_show_file(self):  # 点击文件类型
        logging.info('==========test_hp_alldoc_show_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')

        type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
        for i in type_list:
            gv.select_file_type(i)
            self.assertTrue(gv.check_select_file_type(i), 'filter fail')
            self.driver.keyevent(4)

    @unittest.skip('skip test_hp_alldoc_sort_file')
    def test_hp_alldoc_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_alldoc_sort_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_hp_alldoc_type_back')
    def test_hp_alldoc_type_back(self):  # “打开”文档类型中的返回键
        logging.info('==========test_hp_alldoc_type_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('pdf')

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/iv_main_title"]'))

    @unittest.skip('skip test_hp_alldoc_upload_file')
    def test_hp_alldoc_upload_file(self):  # 上传文件
        logging.info('==========test_hp_alldoc_upload_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.upload_file('打开上传')
        if check == None:
            gv.jump_to_index('alldoc')
            gv.select_file_type('all')
            gv.file_more_info(1)
            check = gv.upload_file('打开上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_alldoc_wechat_copy_file')
    def test_hp_alldoc_wechat_copy_file(self):
        logging.info('==========test_hp_alldoc_wechat_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = gv.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_hp_alldoc_wechat_delete_file')
    def test_hp_alldoc_wechat_delete_file(self):
        logging.info('==========test_hp_alldoc_wechat_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_hp_alldoc_wechat_file_info')
    def test_hp_alldoc_wechat_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_alldoc_wechat_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_wechat_mark_star')
    def test_hp_alldoc_wechat_mark_star(self):
        logging.info('==========test_hp_alldoc_wechat_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_alldoc_wechat_move_file')
    def test_hp_alldoc_wechat_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_alldoc_wechat_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_hp_alldoc_wechat_rename_file')
    def test_hp_alldoc_wechat_rename_file(self):
        logging.info('==========test_hp_alldoc_wechat_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_hp_alldoc_wechat_search_file')
    def test_hp_alldoc_wechat_search_file(self):  # 搜索功能
        logging.info('==========test_hp_alldoc_wechat_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_alldoc_wechat_select_all')
    def test_hp_alldoc_wechat_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_alldoc_wechat_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_alldoc_wechat_select_all1')
    def test_hp_alldoc_wechat_select_all1(self):
        logging.info('==========test_hp_alldoc_wechat_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_hp_alldoc_wechat_share')
    @data(*index_share_list)
    def test_hp_alldoc_wechat_share(self, way):
        logging.info('==========test_hp_alldoc_wechat_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_alldoc_wechat_share_back')
    def test_hp_alldoc_wechat_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_hp_alldoc_wechat_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_alldoc_wechat_sort_file')
    def test_hp_alldoc_wechat_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_alldoc_wechat_sort_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_hp_alldoc_wechat_upload_file')
    def test_hp_alldoc_wechat_upload_file(self):  # 上传文件
        logging.info('==========test_hp_alldoc_wechat_upload_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        check = gv.upload_file('微信上传')
        if check == None:
            gv.jump_to_index('alldoc')
            gv.open_local_folder('微信')
            self.assertTrue(gv.check_open_folder('微信'), 'open fail')
            gv.file_more_info(7)
            check = gv.upload_file('微信上传')
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_cloud_create_folder')
    def test_hp_cloud_11_create_folder(self):  # "云文档"新建文件夹
        logging.info('==========test_hp_cloud_create_folder==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        folder_name = 'NewFolder'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        self.assertTrue(gv.get_element_result('//*[@text="自动上传"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % folder_name), '文件夹新建失败')

    @unittest.skip('skip test_hp_cloud_rename_folder')
    def test_hp_cloud_12_rename_folder(self):  # "云文档"新建文件夹
        logging.info('==========test_hp_cloud_rename_folder==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(2)
        folder_rename = 'RenameFolder'
        gv.rename_file(folder_rename)
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % folder_rename), '文件夹重命名失败')

    @unittest.skip('skip test_hp_cloud_13_deletd_folder')
    def test_hp_cloud_13_deletd_folder(self):  # "云文档"删除文件夹
        logging.info('==========test_hp_cloud_13_deletd_folder==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(2)
        gv.delete_file()
        time.sleep(1)
        folder_rename = 'RenameFolder'
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % folder_rename), '文件夹删除失败')

    @unittest.skip('skip test_hp_cloud_show_folder')
    def test_hp_cloud_1_show_folder(self):  # "云文档"中显示“自动上传”文件夹
        logging.info('==========test_hp_cloud_show_folder==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        name = ele.find_element(By.XPATH, '//*[@text="自动上传"]').text
        self.assertTrue(name != None)

    @unittest.skip('skip test_hp_cloud_delete_file')
    def test_hp_cloud_delete_file(self):
        logging.info('==========test_hp_cloud_delete_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        name = filename + '.' + suffix
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name), 'delete fail')

    @unittest.skip('skip test_hp_cloud_download')
    def test_hp_cloud_download(self):  # "云文档"中下载
        logging.info('==========test_hp_cloud_download==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        time.sleep(3)
        index = gv.identify_file_index()
        gv.file_more_info(index)
        check = gv.download_file()
        self.assertTrue(check, 'download fail')

    @unittest.skip('skip test_hp_cloud_copy')
    def test_hp_cloud_copy(self):  # 云文档中移动
        logging.info('==========test_hp_cloud_copy==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========copy action==========')
        self.driver.find_element(By.XPATH, '//*[@text="复制"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()

        self.assertTrue(gv.get_toast_message('操作成功'))

    @unittest.skip('skip test_hp_cloud_select_all')
    def test_hp_cloud_select_all(self):  # 云文档中全选
        logging.info('==========test_hp_cloud_select_all==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========select_all operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        num = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num) != 0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        num1 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num1) == 0)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[5].click()
        num2 = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text
        self.assertTrue(int(num2) == 1)

    @unittest.skip('skip test_hp_cloud_select_all_delete')
    def test_hp_cloud_select_all_delete(self):  # 云文档中全选
        logging.info('==========test_hp_cloud_select_all_delete==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========delete operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        eles = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')
        name1 = eles[6].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        name2 = eles[7].find_element(By.ID, 'com.yozo.office:id/tv_title').text
        names_del = [name1, name2]
        eles[6].click()
        eles[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        eles1 = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')
        names = list(map(lambda x: x.text, eles1))
        a = set(names_del) <= set(names)  # 前一个集合是否是后一个集合的子集
        self.assertFalse(a)

    @unittest.skip('skip test_hp_cloud_select_all_copy')
    def test_hp_cloud_select_all_copy(self):  # 云文档中全选
        logging.info('==========test_hp_cloud_select_all_copy==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========copy operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[6].click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="复制"]').click()
        time.sleep(2)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()

        self.assertTrue(gv.get_toast_message('操作成功'))

    @unittest.skip('skip test_hp_cloud_select_all_move')
    def test_hp_cloud_select_all_move(self):  # 云文档中全选
        logging.info('==========test_hp_cloud_select_all_move==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========copy operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[6].click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="移动"]').click()
        time.sleep(2)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()

        self.assertTrue(gv.get_toast_message('操作成功'))

    @unittest.skip('skip test_hp_cloud_select_all_download')
    def test_hp_cloud_select_all_download(self):  # 云文档中全选
        logging.info('==========test_hp_cloud_select_all_download==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========copy operation==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[6].click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[7].click()
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        is_displayed = WebDriverWait(self.driver, 120).until(
            lambda driver: self.driver.find_element(By.XPATH, '//*[@text="下载成功"]')).is_displayed()
        # gv.get_element_result('//*[@text="下载成功"]')
        self.assertTrue(is_displayed)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()

    @unittest.skip('skip test_hp_cloud_move')
    def test_hp_cloud_move(self):  # 云文档中复制
        logging.info('==========test_hp_cloud_move==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)

        logging.info('==========move action==========')
        self.driver.find_element(By.XPATH, '//*[@text="移动"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()

        self.assertTrue(gv.get_toast_message('操作成功'))

    @unittest.skip('skip test_hp_cloud_file_info')
    def test_hp_cloud_file_info(self):  # 云文件相关信息
        logging.info('==========test_hp_cloud_file_info==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
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

    @unittest.skip('skip test_hp_cloud_rename_file')
    def test_hp_cloud_rename_file(self):
        logging.info('==========test_hp_cloud_rename_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        gv.rename_file(newName)
        name = newName + '.' + suffix
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % name), 'rename fail')

    @unittest.skip('skip test_hp_cloud_share')
    @data(*index_share_list)
    def test_hp_cloud_share(self, way='more'):
        logging.info('==========test_hp_cloud_share==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_cloud_sort_file')
    def test_hp_cloud_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_hp_cloud_sort_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('cloud')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_head_logo_show')
    def test_hp_head_logo_show(self):  # 头像显示
        logging.info('==========test_head_logo_show==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index('last')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        gv.jump_to_index('alldoc')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        gv.jump_to_index('cloud')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        gv.jump_to_index('star')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user')
        self.assertTrue(ele != None)
        gv.jump_to_index('my')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon')
        self.assertTrue(ele != None)
        gv.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('my')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_userinfo')
        self.assertTrue(ele != None)
        gv.logout_action()

    @unittest.skip('skip test_hp_last_delete_file')
    def test_hp_last_delete_file(self):  # “最近”删除文件
        logging.info('==========test_hp_last_delete_file==========')
        gv = HomePageView(self.driver)
        gv.file_more_info(1)
        self.assertTrue(gv.delete_last_file())

    @unittest.skip('skip test_hp_last_file_info')
    def test_hp_last_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_last_file_info==========')
        gv = HomePageView(self.driver)
        gv.file_more_info(1)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_last_mark_star')
    def test_hp_last_mark_star(self):  # 最近中的标星操作
        logging.info('==========test_hp_last_mark_star==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_last_scroll')
    def test_hp_last_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_hp_last_scroll==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        first_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        ele = '//*[@resource-id="com.yozo.office:id/list_lastfile"]'
        gv.swipe_options(ele)
        second_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        self.assertTrue(first_name != second_name)

    @unittest.skip('skip test_hp_last_select_all')
    def test_hp_last_select_all(self):  # “最近”全选操作
        logging.info('==========test_hp_last_select_all==========')
        gv = HomePageView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_hp_last_select_all1')
    def test_hp_last_select_all1(self):  # “最近”全选操作
        logging.info('==========test_hp_last_select_all1==========')
        gv = HomePageView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消全选"]').click()
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num == 0)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0].click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[1].click()
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[2].click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.assertTrue(gv.get_toast_message('此操作只是将文件从最近列表中删除'))

    @unittest.skip('skip test_share_from_index')
    @data(*index_share_list)
    def test_hp_last_share(self, way):  # “最近”中的分享
        logging.info('==========test_hp_last_share==========')
        gv = HomePageView(self.driver)
        gv.file_more_info(1)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_last_share_back')
    def test_hp_last_share_back(self):  # “最近”中的分享的返回键
        logging.info('==========test_hp_last_share_back==========')
        gv = HomePageView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_hp_last_show_cloud_file')
    def test_hp_last_show_cloud_file(self):  # 登录时显示云文件
        logging.info('==========test_hp_last_show_cloud_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        gv.login_on_needed()
        gv.jump_to_index('last')
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/tv_from"]'))
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_last_show_open_file')
    def test_hp_last_show_open_file(self):  # “最近”中显示已打开的文件
        logging.info('==========test_hp_last_show_open_file==========')
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

    @unittest.skip('skip test_hp_last_unlogin_show')
    def test_hp_last_unlogin_show(self):  # 未登录时显示3个内置文件（初次安装）
        logging.info('==========test_hp_last_unlogin_show==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index()
        exist_files = ['欢迎使用永中Office.docx', '欢迎使用永中Office.pptx', '欢迎使用永中Office.pdf']
        for i in exist_files:
            file_ele = '//*[@text="%s"]' % i
            self.assertTrue(gv.get_element_result(file_ele), '文档不存在')

    @unittest.skip('skip test_hp_last_upload_file')
    def test_hp_last_upload_file(self):  # “最近”上传文件
        logging.info('==========test_hp_last_upload_file==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        file_name = '欢迎使用永中Office.xlsx'
        search_result = gv.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = gv.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        gv.close_file()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_back').click()
        time.sleep(1)
        gv.file_more_info(1)
        check = gv.upload_file('最近上传')
        self.assertTrue(check, 'upload fail')
        gv.jump_to_index('my')
        gv.logout_action()

    @unittest.skip('skip test_hp_my1_about_yozo')
    def test_hp_my1_about_yozo(self):
        logging.info('==========test_hp_my1_about_yozo==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
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
        self.assertTrue(gv.get_element_result('//*[@text="关于YOZO"]'))

    @unittest.skip('skip test_hp_my1_head_unlog')
    def test_hp_my1_head_unlog(self):
        logging.info('==========test_hp_my1_head_unlog==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.assertTrue(gv.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_hp_my2_account_edit')
    def test_hp_my2_account_edit(self):  # 登录账号信息展示及修改
        logging.info('==========test_hp_my2_about_head_login==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_useredit').click()
        username = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').text
        loc = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').location
        self.assertTrue(username != "")
        account = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfochange_username').text
        self.assertTrue(account == '139****5564')
        email = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_email').text
        self.assertTrue(email == 'branezhang@163.com')
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').click()
        self.assertTrue(gv.get_element_result('//*[@text="修改昵称"]'))
        gv.tap(loc['x'], loc['y'])
        self.assertFalse(gv.get_element_result('//*[@text="修改昵称"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').click()
        name_time = gv.getTime("%Y%m%d%H%M%S")
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newname').set_text(name_time)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        username = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_name').text
        self.assertTrue(username == name_time)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_myinfo_email').click()
        self.assertTrue(gv.get_element_result('//*[@text="绑定邮箱"]'))
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/et_newemai').is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/et_code').is_displayed())
        gv.tap(loc['x'], loc['y'])
        self.assertFalse(gv.get_element_result('//*[@text="绑定邮箱"]'))

    @unittest.skip('skip test_hp_my2_about_head_login')
    def test_hp_my2_head_login(self):  # 已登陆头像功能
        logging.info('==========test_hp_my2_about_head_login==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('my')
        username = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_username').text
        self.assertTrue(username != "")
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_userinfo').click()
        self.assertTrue(gv.get_element_result('//*[@text="拍照"]'))
        self.assertTrue(gv.get_element_result('//*[@text="从相册中选取"]'))
        self.assertTrue(gv.get_element_result('//*[@text="取消"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancle').click()

    @unittest.skip('skip test_hp_my2_login_way')
    def test_hp_my2_login_way(self):  # 登录操作
        logging.info('==========test_hp_my2_login_way==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index('my')
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_findpwd').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/et_account"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/et_pwd"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/btn_verifycode"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/btn_true"]'))
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_wechat').click()
        self.driver.keyevent(4)
        time.sleep(0.5)
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_register').click()
        self.assertTrue(gv.get_element_result('//*[@text="短信登录"]'))

    @unittest.skip('skip test_hp_my2_logout')
    def test_hp_my2_logout(self):  # 退出登录
        logging.info('==========test_hp_my2_logout==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('my')
        gv.swipe_options('//android.widget.ScrollView')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        self.assertTrue(gv.get_element_result('//*[@text="是否退出登录？"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()
        self.assertTrue(gv.get_element_result('//*[@text="退出登录"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        self.assertTrue(gv.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_hp_my2_opinion_feedback')
    def test_hp_my2_opinion_feedback(self):
        logging.info('==========test_hp_my2_opinion_feedback==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('my')
        content = gv.getTime("%Y-%m-%d %H:%M:%S")
        result = gv.opinion_feedback('content', content)
        self.assertTrue(result)
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/end').click()
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % content))

    @unittest.skip('skip test_hp_my2_sign_up')
    def test_hp_my2_sign_up(self):  # 注册
        logging.info('==========test_hp_my2_login_way==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_register').click()
        self.assertTrue(gv.get_element_result('//*[@text="注册"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_account').set_text('13915575564')
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_password').set_text('zhang199412')
        self.driver.find_element(By.ID, 'com.yozo.office:id/checkbox_privacy').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/tv_pwd_login2"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_register').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/et_figure_code"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/et_pwd"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/btn_verifycode"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/btn_register"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/tv_pwd_login2"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="《隐私协议》"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="关于YOZO"]'))

    @unittest.skip('skip test_hp_my2_sys_setting')
    def test_hp_my2_sys_setting(self):  # 系统设置
        logging.info('==========test_hp_my2_sys_setting==========')
        gv = HomePageView(self.driver)
        gv.login_on_needed()
        gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_mysys_setting').click()
        gv.wifi_trans('关闭')
        gv.wifi_trans('开启')
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        self.assertTrue(gv.get_toast_message('仅在WI-FI下传输'))
        self.driver.set_network_connection(ConnectionType.WIFI_ONLY)

    @unittest.skip('skip test_hp_my_login_fail')
    def test_hp_my_login_fail(self):
        logging.info('==========test_hp_my_login_fail==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index('my')
        data = gv.get_csv_data(csv_file, 5)

        gv.login_from_my(data[0], data[1])
        self.assertTrue(gv.get_element_result('//*[@text="忘记密码?"]'), msg='login success')

    @unittest.skip('skip test_login_success')
    def test_hp_my_login_success(self):
        logging.info('==========test_login_success==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('my')
        if gv.check_login_status():
            gv.logout_action()
        gv.jump_to_index('my')
        data = gv.get_csv_data(csv_file, 4)

        gv.login_from_my(data[0], data[1])
        time.sleep(1)
        gv.jump_to_index('my')
        self.assertTrue(gv.check_login_status(), msg='login fail')

        gv.logout_action()

    @unittest.skip('skip test_hp_rotate_index')
    def test_hp_rotate_index(self):
        logging.info('==========test_hp_rotate_index==========')
        gv = HomePageView(self.driver)
        gv.screen_rotate('landscape')
        gv.screen_rotate('portrait')
        gv.jump_to_index('alldoc')
        gv.screen_rotate('landscape')
        gv.screen_rotate('portrait')
        gv.jump_to_index('cloud')
        gv.screen_rotate('landscape')
        gv.screen_rotate('portrait')
        gv.jump_to_index('star')
        gv.screen_rotate('landscape')
        gv.screen_rotate('portrait')
        gv.jump_to_index('my')
        gv.screen_rotate('landscape')
        gv.screen_rotate('portrait')

    @unittest.skip('skip test_hp_search_icon_show')
    def test_hp_search_icon_show(self):  # 搜索键显示
        logging.info('==========test_hp_search_icon_show==========')
        gv = HomePageView(self.driver)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
        gv.jump_to_index('alldoc')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
        gv.jump_to_index('star')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)

    @unittest.skip('skip test_hp_star_copy_file')
    def test_hp_star_copy_file(self):  # “打开”复制文件
        logging.info('==========test_hp_star_copy_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('ss')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        fileName = location[location.rindex('/') + 1:]
        check = gv.copy_file()
        os.system('adb shell rm -rf /storage/emulated/0/0000/%s' % fileName)
        self.assertTrue(check, 'copy fail')
        gv.file_more_info(1)
        file = gv.mark_star()

    @unittest.skip('skip test_hp_star_delete_file')
    def test_hp_star_delete_file(self):
        logging.info('==========test_hp_star_delete_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('wp')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        name = filename + '.' + suffix
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name), 'delete fail')

    @unittest.skip('skip test_hp_star_file_info')
    def test_hp_star_file_info(self):  # 文档信息显示
        logging.info('==========test_hp_star_file_info==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
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
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_hp_star_move_file')
    def test_hp_star_move_file(self):  # “打开”移动文件
        logging.info('==========test_hp_star_move_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')
        gv.file_more_info(1)
        gv.mark_star()

    @unittest.skip('skip test_hp_star_rename_file')
    def test_hp_star_rename_file(self):
        logging.info('==========test_hp_star_rename_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')
        gv.file_more_info(1)
        gv.mark_star()

    @unittest.skip('skip test_hp_star_search_file')
    def test_hp_star_search_file(self):  # 搜索功能
        logging.info('==========test_hp_star_search_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('star')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_file(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_hp_star_select_all')
    def test_hp_star_select_all(self):  # “标星”全选操作
        logging.info('==========test_hp_star_select_all==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))
        gv.file_more_info(1)
        gv.mark_star()

    @unittest.skip('skip test_hp_star_select_all1')
    def test_hp_star_select_all1(self):
        logging.info('==========test_hp_star_select_all1==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        name_list = gv.select_all('multi', [1])
        for i in name_list:
            self.assertFalse(gv.get_element_result(i))

    @unittest.skip('skip test_hp_star_share')
    @data(*index_share_list)
    def test_hp_star_share(self, way='more'):
        logging.info('==========test_hp_star_share==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('star')
        if len(self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')) == 0:
            gv.jump_to_index('alldoc')
            gv.select_file_type('ss')
            gv.file_more_info(1)
            file = gv.mark_star()
            self.assertTrue(gv.check_mark_satr(file))
            self.driver.keyevent(4)
            gv.jump_to_index('star')
        gv.file_more_info(1)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_hp_star_share_back')
    def test_hp_star_share_back(self):  # “标星”中的分享的返回键
        logging.info('==========test_hp_star_share_back==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('star')
        if len(self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')) == 0:
            gv.jump_to_index('alldoc')
            gv.select_file_type('ss')
            gv.file_more_info(1)
            file = gv.mark_star()
            self.assertTrue(gv.check_mark_satr(file))
            self.driver.keyevent(4)
            gv.jump_to_index('star')
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))
        gv.mark_star()

    @unittest.skip('skip test_hp_star_show_no_file')
    def test_hp_star_1_show_no_file(self):
        logging.info('==========test_hp_star_show_no_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('star')
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/iv_view"]'))

    @unittest.skip('skip test_hp_star_upload_file')
    def test_hp_star_upload_file(self):  # 上传文件
        logging.info('==========test_hp_star_upload_file==========')
        gv = HomePageView(self.driver)
        gv.jump_to_index('star')
        if len(self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')) == 0:
            gv.jump_to_index('alldoc')
            gv.select_file_type('ss')
            gv.file_more_info(1)
            file = gv.mark_star()
            self.assertTrue(gv.check_mark_satr(file))
            self.driver.keyevent(4)
            gv.jump_to_index('star')
        gv.file_more_info(1)
        check = gv.upload_file('标星上传')
        self.assertTrue(check, 'upload fail')
        gv.file_more_info(1)
        gv.mark_star()
        gv.jump_to_index('my')
        gv.logout_action()
