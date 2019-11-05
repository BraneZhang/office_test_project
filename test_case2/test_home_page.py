#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import time
import unittest

from appium.webdriver.connectiontype import ConnectionType
from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.generalView import GeneralView
from businessView.loginView import LoginView
from businessView.openView import OpenView
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
auto_sum = ['求和', '平均值', '计数', '最大值', '最小值']


@ddt
class TestFunc(StartEnd):

    @unittest.skip('skip test_star_show_no_file')
    def test_star_show_no_file(self):
        logging.info('==========test_star_show_no_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('star')
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/iv_view"]'))

    @unittest.skip('skip test_a_show_file')
    def test_a_show_file(self):  # 未登录时显示3个内置文件（初次安装）
        logging.info('==========test_a_show_file==========')
        ov = OpenView(self.driver)
        exist_files = ['欢迎使用永中Office.docx', '欢迎使用永中Office.pptx', '欢迎使用永中Office.pdf']
        for i in exist_files:
            file_ele = '//*[@text="%s"]' % i
            self.assertTrue(ov.get_element_result(file_ele))

    @unittest.skip('skip test_alldoc_copy_file')
    def test_alldoc_copy_file(self):  # “打开”复制文件
        logging.info('==========test_alldoc_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_alldoc_delete_file')
    def test_alldoc_delete_file(self):
        logging.info('==========test_alldoc_delete_file==========')
        gv = GeneralView(self.driver)
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
        # self.assertFalse(gv.search_action(name))

    @unittest.skip('skip test_alldoc_file_info')
    def test_alldoc_file_info(self):  # 文档信息显示
        logging.info('==========test_alldoc_file_info==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_alldoc_mark_star')
    def test_alldoc_mark_star(self):
        logging.info('==========test_alldoc_mark_star==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_alldoc_scroll')
    def test_alldoc_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_alldoc_scroll==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        first_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        gv.swipeUp()
        second_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        self.assertTrue(first_name != second_name)

    @unittest.skip('skip test_alldoc_move_file')
    def test_alldoc_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_alldoc_rename_file')
    def test_alldoc_rename_file(self):
        logging.info('==========test_alldoc_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_alldoc_search_file')
    def test_alldoc_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_alldoc_select_all')
    def test_alldoc_select_all(self):  # “最近”全选操作
        logging.info('==========test_alldoc_select_all==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_alldoc_select_all1')
    def test_alldoc_select_all1(self):
        logging.info('==========test_alldoc_select_all1==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.sort_files('name', 'up')
        gv.file_more_info(1)
        name_list = gv.select_all('multi', [1, 3, 5, 6, 7])
        for i in name_list:
            self.assertFalse(gv.search_action(i))
            self.driver.keyevent(4)

    @unittest.skip('skip test_alldoc_share')
    @data(*index_share_list)
    def test_alldoc_share(self, way):
        logging.info('==========test_alldoc_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_alldoc_share_back')
    def test_alldoc_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_alldoc_show_file')
    def test_alldoc_show_file(self):  # 点击文件类型
        logging.info('==========test_alldoc_show_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')

        type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
        for i in type_list:
            gv.select_file_type(i)
            self.assertTrue(gv.check_select_file_type(i), 'filter fail')
            self.driver.keyevent(4)

    @unittest.skip('skip test_alldoc_sort_file')
    def test_alldoc_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_alldoc_sort_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_alldoc_type_back')
    def test_alldoc_type_back(self):  # “打开”文档类型中的返回键
        logging.info('==========test_alldoc_type_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('pdf')

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/fb_show_menu_main"]'))

    @unittest.skip('skip test_alldoc_upload_file')
    def test_alldoc_upload_file(self):  # 上传文件
        logging.info('==========test_alldoc_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.select_file_type('all')
            gv.file_more_info(1)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_cloud_create_folder')
    def test_cloud_11_create_folder(self):  # "云文档"新建文件夹
        logging.info('==========test_cloud_create_folder==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        folder_name = 'NewFolder'
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        text_name = self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').text
        self.assertTrue(folder_name == text_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_chanle').click()
        self.assertTrue(gv.get_element_result('//*[@text="自动上传"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_newf').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').send_keys(folder_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % folder_name))

    @unittest.skip('skip test_cloud_rename_folder')
    def test_cloud_12_rename_folder(self):  # "云文档"新建文件夹
        logging.info('==========test_cloud_rename_folder==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        gv.file_more_info(2)
        folder_rename = 'RenameFolder'
        gv.rename_file(folder_rename)
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % folder_rename))

    @unittest.skip('skip test_cloud_13_deletd_folder')
    def test_cloud_13_deletd_folder(self):  # "云文档"新建文件夹
        logging.info('==========test_cloud_13_deletd_folder==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        gv.file_more_info(2)
        gv.delete_file()
        folder_rename = 'RenameFolder'
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % folder_rename))

    @unittest.skip('skip test_cloud_show_folder')
    def test_cloud_1_show_folder(self):  # "云文档"中显示“自动上传”文件夹
        logging.info('==========test_cloud_show_folder==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        ele = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[0]
        name = ele.find_element(By.XPATH, '//*[@text="自动上传"]').text
        self.assertTrue(name != None)

    @unittest.skip('skip test_cloud_delete_file')
    def test_cloud_delete_file(self):
        logging.info('==========test_cloud_delete_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        filename = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text.strip()
        name = filename + '.' + suffix
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name), 'delete fail')

    @unittest.skip('skip test_cloud_download')
    def test_cloud_download(self):  # "云文档"中下载
        logging.info('==========test_cloud_download==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        time.sleep(3)
        index = gv.identify_file_index()
        gv.file_more_info(index + 1)
        check = gv.download_file()
        self.assertTrue(check, 'download fail')

    @unittest.skip('skip test_cloud_file_info')
    def test_cloud_file_info(self):  # 云文件相关信息
        logging.info('==========test_cloud_file_info==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
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

    @unittest.skip('skip test_cloud_rename_file')
    def test_cloud_rename_file(self):
        logging.info('==========test_cloud_rename_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
        suffix = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text.strip()
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        gv.rename_file(newName)
        name = newName + '.' + suffix
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % name), 'rename fail')

    @unittest.skip('skip test_cloud_share')
    @data(*index_share_list)
    def test_cloud_share(self, way):
        logging.info('==========test_cloud_share==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_cloud_sort_file')
    def test_cloud_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_cloud_sort_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('cloud')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_Download_copy_file')
    def test_download_copy_file(self):
        logging.info('==========test_Download_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_Download_delete_file')
    def test_download_delete_file(self):
        logging.info('==========test_Download_delete_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_Download_file_info')
    def test_download_file_info(self):  # 文档信息显示
        logging.info('==========test_Download_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_Download_mark_star')
    def test_download_mark_star(self):
        logging.info('==========test_Download_mark_star==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_Download_move_file')
    def test_download_move_file(self):  # “打开”移动文件
        logging.info('==========test_Download_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_Download_rename_file')
    def test_download_rename_file(self):
        logging.info('==========test_Download_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_Download_search_file')
    def test_download_search_file(self):  # 搜索功能
        logging.info('==========test_Download_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_Download_select_all')
    def test_download_select_all(self):  # “最近”全选操作
        logging.info('==========test_Download_select_all==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_Download_select_all1')
    def test_download_select_all1(self):
        logging.info('==========test_Download_select_all1==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5, 6, 7])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_Download_share')
    @data(*index_share_list)
    def test_download_share(self, way):
        logging.info('==========test_Download_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_Download_share_back')
    def test_download_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_Download_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_Download_sort_file')
    def test_download_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_Download_sort_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_Download_upload_file')
    def test_download_upload_file(self):  # 上传文件
        logging.info('==========test_Download_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.open_local_folder('Download')
            self.assertTrue(gv.check_open_folder('Download'), 'open fail')
            gv.file_more_info(7)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_head_logo_show')
    def test_head_logo_show(self):  # 头像显示
        logging.info('==========test_head_logo_show==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if gv.get_element_result('//*[@text="退出登录"]'):
            l.logout_action()
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
        l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('my')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/iv_userinfo')
        self.assertTrue(ele != None)
        l.logout_action()

    @unittest.skip('skip test_last_delete_file')
    def test_last_delete_file(self):  # “最近”删除文件
        logging.info('==========test_last_delete_file==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.assertTrue(gv.delete_last_file())

    @unittest.skip('skip test_last_file_info')
    def test_last_file_info(self):  # 文档信息显示
        logging.info('==========test_last_file_info==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_last_mark_star')
    def test_last_mark_star(self):  # 最近中的标星操作
        logging.info('==========test_last_mark_star==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_last_scroll')
    def test_z_last_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_last_scroll==========')
        gv = GeneralView(self.driver)
        first_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        gv.swipeUp()
        second_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        self.assertTrue(first_name != second_name)

    @unittest.skip('skip test_last_select_all')
    def test_last_select_all(self):  # “最近”全选操作
        logging.info('==========test_last_select_all==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_last_select_all1')
    def test_last_select_all1(self):  # “最近”全选操作
        logging.info('==========test_last_select_all1==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="取消全选"]').click()
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num == 0)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.assertTrue(gv.get_toast_message('此操作只是将文件从最近列表中删除'))

    @unittest.skip('skip test_share_from_index')
    @data(*index_share_list)
    def test_last_share(self, way):  # “最近”中的分享
        logging.info('==========test_last_share==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_last_share_back')
    def test_last_share_back(self):  # “最近”中的分享的返回键
        logging.info('==========test_last_share_back==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_last_upload_file')
    def test_last_upload_file(self):  # “最近”上传文件
        logging.info('==========test_last_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.file_more_info(1)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.select_file_type('all')
            gv.file_more_info(1)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_local_folder')
    @data(*folder_list)
    def test_local_folder(self, folder):  # 测试本地文档打开
        logging.info('==========test_local_folder==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder(folder)
        self.assertTrue(gv.check_open_folder(folder), 'open fail')

    @unittest.skip('skip test_login_fail')
    def test_login_fail(self):
        logging.info('==========test_login_fail==========')
        gv = GeneralView(self.driver)
        login = LoginView(self.driver)
        gv.jump_to_index('my')
        if gv.get_element_result('//*[@text="退出登录"]'):
            login.logout_action()
        gv.jump_to_index('my')
        data = login.get_csv_data(csv_file, 5)

        login.login_from_my(data[0], data[1])
        self.assertTrue(login.get_element_result('//*[@text="忘记密码?"]'), msg='login success')

    @unittest.skip('skip test_login_success')
    def test_login_success(self):
        logging.info('==========test_login_success==========')
        gv = GeneralView(self.driver)
        login = LoginView(self.driver)
        gv.jump_to_index('my')
        if gv.get_element_result('//*[@text="退出登录"]'):
            login.logout_action()
        gv.jump_to_index('my')
        data = login.get_csv_data(csv_file, 4)

        login.login_from_my(data[0], data[1])
        gv.jump_to_index('my')
        self.assertTrue(login.check_login_status(), msg='login fail')

        login.logout_action()

    @unittest.skip('skip test_mobile_copy_file')
    def test_mobile_copy_file(self):
        logging.info('==========test_mobile_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_mobile_delete_file')
    def test_mobile_delete_file(self):
        logging.info('==========test_mobile_delete_file==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_mobile_file_info')
    def test_mobile_file_info(self):  # 文档信息显示
        logging.info('==========test_mobile_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_mobile_mark_star')
    def test_mobile_mark_star(self):
        logging.info('==========test_mobile_mark_star==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_mobile_move_file')
    def test_mobile_move_file(self):  # “打开”移动文件
        logging.info('==========test_mobile_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_mobile_rename_file')
    def test_mobile_rename_file(self):
        logging.info('==========test_mobile_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_mobile_search_file')
    def test_mobile_search_file(self):  # 搜索功能
        logging.info('==========test_mobile_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_mobile_select_all')
    def test_mobile_select_all(self):  # “最近”全选操作
        logging.info('==========test_mobile_select_all==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_mobile_select_all1')
    def test_mobile_select_all1(self):
        logging.info('==========test_mobile_select_all1==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(1)
        name_list = gv.select_all('multi', [1, 3, 5, 6, 7])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_mobile_share')
    @data(*index_share_list)
    def test_mobile_share(self, way):
        logging.info('==========test_mobile_share==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_mobile_share_back')
    def test_mobile_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_mobile_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_mobile_sort_file')
    def test_mobile_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_mobile_sort_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_mobile_upload_file')
    def test_mobile_upload_file(self):  # 上传文件
        logging.info('==========test_mobile_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        for i in range(10):
            gv.swipeUp()
        gv.file_more_info(7)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.open_local_folder('手机')
            self.assertTrue(gv.check_open_folder('手机'), 'open fail')
            for i in range(10):
                gv.swipeUp()
            gv.file_more_info(7)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_my1_about_yozo')
    def test_my1_about_yozo(self):
        logging.info('==========test_my1_about_yozo==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_my1_head_unlog')
    def test_my1_head_unlog(self):
        logging.info('==========test_my1_head_unlog==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.assertTrue(gv.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_my2_account_edit')
    def test_my2_account_edit(self):  # 登录账号信息展示及修改
        logging.info('==========test_my2_about_head_login==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
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

    @unittest.skip('skip test_my2_about_head_login')
    def test_my2_head_login(self):  # 已登陆头像功能
        logging.info('==========test_my2_about_head_login==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
            gv.jump_to_index('my')
        username = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_username').text
        self.assertTrue(username != "")
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_userinfo').click()
        self.assertTrue(gv.get_element_result('//*[@text="拍照"]'))
        self.assertTrue(gv.get_element_result('//*[@text="从相册中选取"]'))
        self.assertTrue(gv.get_element_result('//*[@text="取消"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancle').click()

    @unittest.skip('skip test_my2_login_way')
    def test_my2_login_way(self):  # 登录操作
        logging.info('==========test_my2_login_way==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_user_unlogin_icon').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_findpwd').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/et_account"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/et_pwd"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/btn_verifycode"]'))
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/btn_true"]'))
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_wechat').click()
        self.driver.keyevent(4)
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_login_register').click()
        self.assertTrue(gv.get_element_result('//*[@text="短信登录"]'))

    @unittest.skip('skip test_my2_logout')
    def test_my2_logout(self):  # 退出登录
        logging.info('==========test_my2_logout==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
            gv.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_sure').click()
        self.assertTrue(gv.get_element_result('//*[@text="是否退出登录？"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_chanle').click()
        self.assertTrue(gv.get_element_result('//*[@text="退出登录"]'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_sure').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        self.assertTrue(gv.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_my2_opinion_feedback')
    def test_my2_opinion_feedback(self):
        logging.info('==========test_my2_opinion_feedback==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
            gv.jump_to_index('my')
        content = gv.getTime("%Y-%m-%d %H:%M:%S")
        result = gv.opinion_feedback('content', content)
        self.assertTrue(result)
        self.driver.keyevent(4)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/end').click()
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % content))

    @unittest.skip('skip test_my2_sign_up')
    def test_my2_sign_up(self):  # 注册
        logging.info('==========test_my2_login_way==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
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
        self.assertTrue(gv.get_element_result('//*[@text="账号登录"]'))

    @unittest.skip('skip test_my2_sys_setting')
    def test_my2_sys_setting(self):  # 系统设置
        logging.info('==========test_my2_sys_setting==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
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

    @unittest.skip('skip test_myfile_copy_file')
    def test_myfile_copy_file(self):
        logging.info('==========test_myfile_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_myfile_delete_file')
    def test_myfile_delete_file(self):
        logging.info('==========test_myfile_delete_file==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_myfile_file_info')
    def test_myfile_file_info(self):  # 文档信息显示
        logging.info('==========test_myfile_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_myfile_mark_star')
    def test_myfile_mark_star(self):
        logging.info('==========test_myfile_mark_star==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_myfile_move_file')
    def test_myfile_move_file(self):  # “打开”移动文件
        logging.info('==========test_myfile_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_myfile_rename_file')
    def test_myfile_rename_file(self):
        logging.info('==========test_myfile_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_myfile_search_file')
    def test_myfile_search_file(self):  # 搜索功能
        logging.info('==========test_myfile_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_myfile_select_all')
    def test_myfile_select_all(self):  # “最近”全选操作
        logging.info('==========test_myfile_select_all==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_myfile_select_all1')
    def test_myfile_select_all1(self):
        logging.info('==========test_myfile_select_all1==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5, 6, 7])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_myfile_share')
    @data(*index_share_list)
    def test_myfile_share(self, way):
        logging.info('==========test_myfile_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_myfile_share_back')
    def test_myfile_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_myfile_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_myfile_sort_file')
    def test_myfile_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_myfile_sort_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_myfile_upload_file')
    def test_myfile_upload_file(self):  # 上传文件
        logging.info('==========test_myfile_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.open_local_folder('我的文档')
            self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
            gv.file_more_info(7)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_QQ_copy_file')
    def test_qq_copy_file(self):
        logging.info('==========test_QQ_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_QQ_delete_file')
    def test_qq_delete_file(self):
        logging.info('==========test_QQ_delete_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_QQ_file_info')
    def test_qq_file_info(self):  # 文档信息显示
        logging.info('==========test_QQ_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_QQ_mark_star')
    def test_qq_mark_star(self):
        logging.info('==========test_QQ_mark_star==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_QQ_move_file')
    def test_qq_move_file(self):  # “打开”移动文件
        logging.info('==========test_QQ_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_QQ_rename_file')
    def test_qq_rename_file(self):
        logging.info('==========test_QQ_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_QQ_search_file')
    def test_qq_search_file(self):  # 搜索功能
        logging.info('==========test_QQ_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_QQ_select_all')
    def test_qq_select_all(self):  # “最近”全选操作
        logging.info('==========test_QQ_select_all==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_QQ_select_all1')
    def test_qq_select_all1(self):
        logging.info('==========test_QQ_select_all1==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5, 6, 7])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_QQ_share')
    @data(*index_share_list)
    def test_qq_share(self, way):
        logging.info('==========test_QQ_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_QQ_share_back')
    def test_qq_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_QQ_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_QQ_sort_file')
    def test_qq_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_QQ_sort_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_QQ_upload_file')
    def test_qq_upload_file(self):  # 上传文件
        logging.info('==========test_QQ_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.open_local_folder('QQ')
            self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
            gv.file_more_info(7)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_search_icon_show')
    def test_search_icon_show(self):  # 搜索键显示
        logging.info('==========test_search_icon_show==========')
        gv = GeneralView(self.driver)
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
        gv.jump_to_index('alldoc')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)
        gv.jump_to_index('star')
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search')
        self.assertTrue(ele != None)

    @unittest.skip('skip test_show_cloud_file')
    def test_show_cloud_file(self):  # 登录时显示云文件
        logging.info('==========test_show_cloud_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('my')
        if not gv.get_element_result('//*[@text="退出登录"]'):
            l.login_from_my('13915575564', 'zhang199412')
        gv.jump_to_index('last')
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/tv_from"]'))
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_show_open_file')
    def test_show_open_file(self):  # “最近”中显示已打开的文件
        logging.info('==========test_show_open_file==========')
        ov = OpenView(self.driver)
        file_name = '欢迎使用永中Office.xlsx'
        ov.open_file(file_name)
        ov.close_file()
        time.sleep(1)
        self.driver.press_keycode(4)
        file_ele = '//*[@text="%s"]' % file_name
        self.assertTrue(ov.get_element_result(file_ele))

    @unittest.skip('skip test_star_copy_file')
    def test_star_copy_file(self):  # “打开”复制文件
        logging.info('==========test_star_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_star_delete_file')
    def test_star_delete_file(self):
        logging.info('==========test_star_delete_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.sort_files('name', 'up')
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

    @unittest.skip('skip test_star_file_info')
    def test_star_file_info(self):  # 文档信息显示
        logging.info('==========test_star_file_info==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_star_move_file')
    def test_star_move_file(self):  # “打开”移动文件
        logging.info('==========test_star_move_file==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_star_rename_file')
    def test_star_rename_file(self):
        logging.info('==========test_star_rename_file==========')
        gv = GeneralView(self.driver)
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

    @unittest.skip('skip test_star_search_file')
    def test_star_search_file(self):  # 搜索功能
        logging.info('==========test_star_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('star')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_star_select_all')
    def test_star_select_all(self):  # “最近”全选操作
        logging.info('==========test_star_select_all==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        self.driver.keyevent(4)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_star_select_all1')
    def test_star_select_all1(self):
        logging.info('==========test_star_select_all1==========')
        gv = GeneralView(self.driver)
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
            self.assertFalse(gv.search_action(i))
            self.driver.keyevent(4)

    @unittest.skip('skip test_star_share')
    @data(*index_share_list)
    def test_star_share(self, way):
        logging.info('==========test_star_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_star_share_back')
    def test_star_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_star_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_star_upload_file')
    def test_star_upload_file(self):  # 上传文件
        logging.info('==========test_star_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('star')
        gv.file_more_info(1)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.select_file_type('all')
            gv.file_more_info(1)
            gv.mark_star()
            self.driver.keyevent(4)
            gv.jump_to_index('star')
            gv.file_more_info(1)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_wechat_copy_file')
    def test_wechat_copy_file(self):
        logging.info('==========test_wechat_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    @unittest.skip('skip test_wechat_delete_file')
    def test_wechat_delete_file(self):
        logging.info('==========test_wechat_delete_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.assertFalse(gv.get_element_result('//*[@text="%s"]' % name))

    @unittest.skip('skip test_wechat_file_info')
    def test_wechat_file_info(self):  # 文档信息显示
        logging.info('==========test_wechat_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_wechat_mark_star')
    def test_wechat_mark_star(self):
        logging.info('==========test_wechat_mark_star==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(2)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    @unittest.skip('skip test_wechat_move_file')
    def test_wechat_move_file(self):  # “打开”移动文件
        logging.info('==========test_wechat_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    @unittest.skip('skip test_wechat_rename_file')
    def test_wechat_rename_file(self):
        logging.info('==========test_wechat_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    @unittest.skip('skip test_wechat_search_file')
    def test_wechat_search_file(self):  # 搜索功能
        logging.info('==========test_wechat_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    @unittest.skip('skip test_wechat_select_all')
    def test_wechat_select_all(self):  # “最近”全选操作
        logging.info('==========test_wechat_select_all==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    @unittest.skip('skip test_wechat_select_all1')
    def test_wechat_select_all1(self):
        logging.info('==========test_wechat_select_all1==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        name_list = gv.select_all('multi', [1, 3, 5, 6, 7])
        for i in name_list:
            self.assertFalse(gv.get_element_result('//*[@text="%s"]' % i))

    @unittest.skip('skip test_wechat_share')
    @data(*index_share_list)
    def test_wechat_share(self, way):
        logging.info('==========test_wechat_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_wechat_share_back')
    def test_wechat_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_wechat_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    @unittest.skip('skip test_wechat_sort_file')
    def test_wechat_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_wechat_sort_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        way_list = ['type', 'name', 'size', 'time']
        order_list = ['up', 'down']
        for i in way_list:
            for j in order_list:
                gv.sort_files(i, j)

    @unittest.skip('skip test_wechat_upload_file')
    def test_wechat_upload_file(self):  # 上传文件
        logging.info('==========test_wechat_upload_file==========')
        gv = GeneralView(self.driver)
        l = LoginView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(7)
        check = gv.upload_file()
        if check == None:
            gv.jump_to_index('alldoc')
            gv.open_local_folder('微信')
            self.assertTrue(gv.check_open_folder('微信'), 'open fail')
            gv.file_more_info(7)
            check = gv.upload_file()
        self.assertTrue(check, 'upload fail')
        self.driver.keyevent(4)
        gv.jump_to_index('my')
        l.logout_action()

    @unittest.skip('skip test_rotate_index')
    def test_rotate_index(self):
        logging.info('==========test_rotate_index==========')
        gv = GeneralView(self.driver)
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
