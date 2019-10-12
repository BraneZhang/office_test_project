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
auto_sum = ['求和', '平均值', '计数', '最大值', '最小值']


@ddt
class TestFunc(StartEnd):

    @unittest.skip('skip test_insert_pic1')
    def test_insert_pic1(self, type='ss'):
        logging.info('==========test_insert_pic==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.group_button_click('插入')

        gv.insert_pic()
        gv.pic_option(type, 5, 4, 4)
        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        # ele3 = '//*[@text="文字环绕"]'
        # ele4 = '//*[@text="叠放次序"]'
        gv.swipe_ele(ele2, ele1)
        if type == 'wp':
            gv.text_wrap('四周型')
            gv.text_wrap('嵌入型')
            gv.text_wrap('紧密型')
            gv.text_wrap('衬于文字下方')
            gv.text_wrap()

        x, y = gv.find_pic_position('drag_pic')
        gv.tap(x, y)
        gv.pop_menu_click('cut')
        if type == 'wp':
            gv.long_press(x, y)
        else:
            gv.tap(x + 100, y)
            gv.tap(x + 100, y)
        gv.pop_menu_click('paste')

        x, y = gv.find_pic_position('drag_pic')
        gv.tap(x, y)
        x, y = gv.find_pic_position('rotate_90')
        gv.swipe(x, y, x - 50, y)

        gv.pop_menu_click('save_to_album')

        gv.pop_menu_click('delete')

    @unittest.skip('skip test_insert_pic')
    def test_insert_pic(self, type='ss'):
        logging.info('==========test_insert_pic==========')
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        cv.create_file(type)
        cv.group_button_click('插入')

        gv.insert_pic()
        gv.pic_option(type, 5, 4, 4)
        gv.pic_option(type, 1)
        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        # ele3 = '//*[@text="文字环绕"]'
        # ele4 = '//*[@text="叠放次序"]'
        gv.swipe_ele(ele2, ele1)
        if type == 'wp':
            gv.text_wrap()

        x, y = gv.find_pic_position('rotate_free')
        gv.swipe(x, y, x + 100, y + 100)

        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)
        gv.pop_menu_click('copy')
        gv.tap(x, y)
        gv.pop_menu_click('paste')
        gv.tap(x, y)
        gv.pop_menu_click('paste')
        gv.shape_layer('下移一层')
        gv.shape_layer('置于底层')
        gv.shape_layer('上移一层')
        gv.shape_layer()

    # @unittest.skip('skip test_a_show_file')
    def test_a_show_file(self):  # 未登录时显示3个内置文件（初次安装）
        logging.info('==========test_a_show_file==========')
        ov = OpenView(self.driver)
        exist_files = ['欢迎使用永中Office.docx', '欢迎使用永中Office.pptx', '欢迎使用永中Office.pdf']
        for i in exist_files:
            file_ele = '//*[@text="%s"]' % i
            self.assertTrue(ov.get_element_result(file_ele))

    # @unittest.skip('skip test_alldoc_copy_file')
    def test_alldoc_copy_file(self):  # “打开”复制文件
        logging.info('==========test_alldoc_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    # @unittest.skip('skip test_alldoc_delete_file')
    def test_alldoc_delete_file(self):
        logging.info('==========test_alldoc_delete_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.sort_files('name', 'up')
        gv.file_more_info(1)
        file_path = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
        index_e = file_path.rindex('/') + 1
        name = file_path[index_e:]
        gv.delete_file()
        self.driver.keyevent(4)
        self.assertFalse(gv.search_action(name))

    # @unittest.skip('skip test_alldoc_file_info')
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

    # @unittest.skip('skip test_alldoc_mark_star')
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

    # @unittest.skip('skip test_alldoc_scroll')
    def test_alldoc_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_alldoc_scroll==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        first_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        gv.swipeUp()
        second_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        self.assertTrue(first_name != second_name)

    # @unittest.skip('skip test_alldoc_move_file')
    def test_alldoc_move_file(self):  # “打开”移动文件
        logging.info('==========test_alldoc_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    # @unittest.skip('skip test_alldoc_rename_file')
    def test_alldoc_rename_file(self):
        logging.info('==========test_alldoc_rename_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        newName = 'rename' + gv.getTime('%Y%m%d%H%M%S')
        check = gv.rename_file(newName)
        self.assertTrue(check, 'rename fail')

    # @unittest.skip('skip test_alldoc_search_file')
    def test_alldoc_search_file(self):  # 搜索功能
        logging.info('==========test_alldoc_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    # @unittest.skip('skip test_alldoc_select_all')
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

    # @unittest.skip('skip test_alldoc_select_all1')
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

    # @unittest.skip('skip test_alldoc_share')
    @data(*index_share_list)
    def test_alldoc_share(self, way):
        logging.info('==========test_alldoc_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        gv.share_file_index(way)

    # @unittest.skip('skip test_alldoc_share_back')
    def test_alldoc_share_back(self):  # “打开”中的分享的返回键
        logging.info('==========test_alldoc_share_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('all')
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_alldoc_show_file')
    def test_alldoc_show_file(self):  # 点击文件类型
        logging.info('==========test_alldoc_show_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')

        type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
        for i in type_list:
            gv.select_file_type(i)
            self.assertTrue(gv.check_select_file_type(i), 'filter fail')
            self.driver.keyevent(4)

    # @unittest.skip('skip test_alldoc_sort_file')
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

    # @unittest.skip('skip test_alldoc_type_back')
    def test_alldoc_type_back(self):  # “打开”文档类型中的返回键
        logging.info('==========test_alldoc_type_back==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.select_file_type('pdf')

        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/fb_show_menu_main"]'))

    # @unittest.skip('skip test_alldoc_upload_file')
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

    # @unittest.skip('skip test_cell_attr')
    def test_cell_attr(self):
        logging.info('==========test_cell_attr==========')
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        x, y, width, height = ss.cell_location()
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.group_button_click('编辑')
        time.sleep(1)

        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ss.swipe_ele(ele2, ele1)
        ss.cell_align('水平居中', '下对齐')

    # @unittest.skip('skip test_cell_border')
    def test_cell_border(self):  # 遍历边框所有功能
        logging.info('==========test_cell_border==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        time.sleep(1)
        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ss.swipe_ele(ele2, ele1)
        ss.cell_border()

    # @unittest.skip('skip test_cell_inser_delete_fit')
    def test_cell_insert_delete_fit(self):  # 插入删除行宽列高清除
        logging.info('==========test_cell_inser_delete_fit==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        gv = GeneralView(self.driver)
        gv.font_style(type, '删除线')

        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ele3 = '//*[@text="单元格填充"]'
        ele4 = '//*[@text="数字格式"]'
        ele5 = '//*[@text="插入单元格"]'
        ele6 = '//*[@text="删除单元格"]'
        ele7 = '//*[@text="设置行高列宽"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele1)
        ss.swipe_ele(ele4, ele1)
        ss.cell_insert('右移')
        ss.cell_insert('下移')
        ss.cell_insert('插入整行')
        ss.cell_insert('插入整列')
        ss.cell_delete('删除整列')
        ss.cell_delete('删除整行')
        ss.cell_delete('上移')
        ss.cell_delete('左移')
        ss.swipe_ele(ele5, ele1)
        ss.cell_set_size(5, 5)
        ss.group_button_click('编辑')
        ss.cell_clear('清除格式')
        gv.undo_option()
        ss.cell_clear('清除内容')
        gv.undo_option()
        ss.cell_clear('清除所有')
        gv.undo_option()
        ss.swipe_ele(ele6, ele7)
        ss.cell_fit_height()
        ss.cell_fit_width()
        time.sleep(3)

    # @unittest.skip('skip test_cloud_create_folder')
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

    # @unittest.skip('skip test_cloud_rename_folder')
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

    # @unittest.skip('skip test_cloud_13_deletd_folder')
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

    # @unittest.skip('skip test_cloud_show_folder')
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

    # @unittest.skip('skip test_cloud_delete_file')
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
        self.assertTrue(gv.get_element_result('//*[@text="%s"]' % name), 'rename fail')

    # @unittest.skip('skip test_cloud_download')
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

    # @unittest.skip('skip test_cloud_file_info')
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

    # @unittest.skip('skip test_cloud_rename_file')
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

    # @unittest.skip('skip test_cloud_share')
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

    # @unittest.skip('skip test_cloud_sort_file')
    def test_cloud_sort_file(self):  # “打开”文档按条件排序
        logging.info('==========test_cloud_sort_file==========')
        gv = GeneralView(self.driver)
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

    # @unittest.skip('skip test_data_table')
    def test_data_table(self):  # 数据排序，工作表格式
        logging.info('==========test_data_table==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        for i in range(10):
            time.sleep(1)
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))  # 双击进入编辑
            cv.tap(110 + 263 * 1.5, 295 + 55 * (1.5 + i))
            self.driver.press_keycode(random.randint(7, 16))
        ss = SSView(self.driver)
        ss.group_button_click('查看')
        time.sleep(1)
        ss.data_sort('降序')
        ss.data_sort('升序')
        ss.sheet_style('隐藏编辑栏')
        ss.sheet_style('隐藏编辑栏')
        ss.sheet_style('隐藏表头')
        ss.sheet_style('隐藏表头')
        ss.sheet_style('隐藏网格线')
        # ss.sheet_style('冻结窗口') 功能未完成
        # ss.sheet_style('取消冻结')
        ss.sheet_style('100%')
        time.sleep(3)

    ##########“打开”中“Download”相关功能
    # @unittest.skip('skip test_Download_copy_file')
    def test_download_copy_file(self):
        logging.info('==========test_Download_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    # @unittest.skip('skip test_Download_delete_file')
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

    # @unittest.skip('skip test_Download_file_info')
    def test_download_file_info(self):  # 文档信息显示
        logging.info('==========test_Download_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_Download_mark_star')
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

    # @unittest.skip('skip test_Download_move_file')
    def test_download_move_file(self):  # “打开”移动文件
        logging.info('==========test_Download_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    # @unittest.skip('skip test_Download_rename_file')
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

    # @unittest.skip('skip test_Download_search_file')
    def test_download_search_file(self):  # 搜索功能
        logging.info('==========test_Download_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    # @unittest.skip('skip test_Download_select_all')
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

    # @unittest.skip('skip test_Download_select_all1')
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

    # @unittest.skip('skip test_Download_share')
    @data(*index_share_list)
    def test_download_share(self, way):
        logging.info('==========test_Download_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('Download')
        self.assertTrue(gv.check_open_folder('Download'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)

    # @unittest.skip('skip test_Download_share_back')
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

    # @unittest.skip('skip test_Download_sort_file')
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

    # @unittest.skip('skip test_Download_upload_file')
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

    # @unittest.skip('skip test_drag_sheet')
    def test_drag_sheet(self):  # sheet拖动
        logging.info('==========test_drag_sheet==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.add_sheet()
        ss.add_sheet()
        ele1 = ss.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="0"]')
        ele2 = ss.get_element('//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="2"]')
        # ele1 = ss.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="0"]')
        # ele2 = ss.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="2"]')
        ss.drag_element(ele1, ele2)

    # @unittest.skip('skip test_expand_fold')
    @data(*wps)
    def test_expand_fold(self, type):  # 编辑栏收起展开
        logging.info('==========test_expand_fold==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.fold_expand()
        gv.fold_expand()

    # @unittest.skip('skip test_export_pdf')
    @data(*wp)
    def test_export_pdf(self, type):  # 导出pdf
        logging.info('==========test_export_pdf==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)

        gv = GeneralView(self.driver)
        file_name = 'export_pdf ' + gv.getTime('%Y-%m-%d %H_%M_%S')
        gv.export_pdf(file_name, 'local')

        self.assertTrue(gv.check_export_pdf())

    # @unittest.skip('skip test_font_attr')
    def test_font_attr(self):
        logging.info('==========test_font_attr==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        for i in range(5):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        gv = GeneralView(self.driver)
        gv.group_button_click('编辑')
        type = 'ss'
        gv.font_name(type)
        gv.font_size(23)
        gv.font_style(type, '加粗')
        gv.font_style(type, '倾斜')
        gv.font_style(type, '删除线')
        gv.font_style(type, '下划线')
        gv.font_color(type)

    # @unittest.skip('skip test_formula1')
    def test_formula1(self):  # 其他类型公式
        logging.info('==========test_formula1==========')
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')
        time.sleep(1)

        x, y, width, height = ss.cell_location()  # cell B8
        for i in range(10):
            ss.tap(x + width * 0.5, y - height * (6.5 - i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))

        cv.tap(110 + 263 * 2.5, 295 + 55 * 0.5)
        ss.formula_all('最近使用', 'MAX')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 1.5)
        ss.formula_all('数学和三角', 'ABS')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 2.5)
        ss.formula_all('财务', 'DOLLARDE')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        time.sleep(0.5)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 5.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 3.5)
        ss.formula_all('逻辑', 'AND')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        time.sleep(0.5)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 5.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 4.5)
        ss.formula_all('文本', 'ASC')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 5.5)
        ss.formula_all('日期和时间', 'NOW')
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 6.5)
        ss.formula_all('查找与引用', 'COLUMN')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 7.5)
        ss.formula_all('统计', 'AVERAGE')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        # cv.tap(110 + 263 * 2.5, 295 + 55 * 8.5)
        # ss.formula_all('工程', 'DEC2BIN')
        # cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        # self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 9.5)
        ss.formula_all('信息', 'ISBLANK')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        cv.tap(110 + 263 * 2.5, 295 + 55 * 10.5)
        ss.formula_all('所有公式', 'ABS')
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    # @unittest.skip('skip test_formula')
    @data(*auto_sum)
    def test_formula(self, formula):
        logging.info('==========test_formula==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)

        ss = SSView(self.driver)
        x, y, width, height = ss.cell_location()  # cell B8
        for i in range(5):
            ss.tap(x + width * 0.5, y - height * (6.5 - i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))

        ss.tap(x + width * 1.5, y - height * 6.5)  # 求和
        ss.auto_sum(formula)
        ss.tap(x + width * 0.5, y - height * 6.5)
        ss.drag_coordinate(x + width, y - height * 6, x + width, y - height * 2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    # @unittest.skip('skip test_insert_chart1')
    @data(*ps)
    def test_insert_chart1(self, type):
        logging.info('==========test_insert_chart1==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)

        time.sleep(1)
        if type == 'ss':
            x, y, width, height = ss.cell_location()
            for i in range(3):
                cv.tap(x + width * 0.5, y + height * (i + 0.5))
                ss.cell_edit()  # 双击进入编辑
                self.driver.press_keycode(random.randint(7, 16))
            gv.drag_coordinate(x, y + height * 2, x, y)

        gv.group_button_click('插入')
        if type == 'pg':
            ele1 = '//*[@text="幻灯片"]'
            ele2 = '//*[@text="图片"]'
            gv.swipe_ele(ele2, ele1)
        gv.insert_chart_insert('柱形图', random.randint(1, 9))
        gv.chart_color(random.randint(1, 8))
        gv.chart_element(type, '大标题', 1, 1, 1)
        gv.chart_element_XY('x', 'x', 0, 1, 1, 1, 1, 1)
        gv.chart_element_XY('y', 'y', 0, 1, 1, 0, 1, 0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        gv.change_row_column()
        time.sleep(3)

    # @unittest.skip('skip test_insert_chart')
    @data(*ps)
    def test_insert_chart(self, type):  # 插入图表，仅ss，pg
        logging.info('==========test_insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '圆柱图', '圆锥图',
                      '棱锥图']
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)

        time.sleep(1)
        if type == 'ss':
            x, y, width, height = ss.cell_location()
            for i in range(3):
                cv.tap(x + width * 0.5, y + height * (i + 0.5))
                ss.cell_edit()  # 双击进入编辑
                self.driver.press_keycode(random.randint(7, 16))
            gv.drag_coordinate(x, y + height * 2, x, y)

        for i in range(3):
            gv.group_button_click('插入')
            if type == 'pg':
                ele1 = '//*[@text="幻灯片"]'
                ele2 = '//*[@text="图片"]'
                gv.swipe_ele(ele2, ele1)
            gv.insert_chart_insert(chart_list[i], random.randint(1, 9))
            gv.chart_template()
        ele1 = '//*[@text="图表"]'
        ele2 = '//*[@text="图表样式"]'
        gv.swipe_ele(ele2, ele1)
        gv.shape_layer('下移一层')
        gv.shape_layer('置于底层')
        gv.shape_layer('上移一层')
        gv.shape_layer()

        time.sleep(3)

    # @unittest.skip('skip test_insert_shape')
    @data(*wps)
    def test_insert_shape(self, type):
        logging.info('==========test_insert_shape==========')
        cv = CreateView(self.driver)
        cv.create_file(type)

        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        # ss.insert_chart()
        gv.group_button_click('插入')
        gv.insert_shape(type)
        for i in range(5):
            gv.shape_insert(type, 6, random.randint(1, 42))
        time.sleep(3)

    # @unittest.skip('skip test_last_delete_file')
    def test_last_delete_file(self):  # “最近”删除文件
        logging.info('==========test_last_delete_file==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.assertTrue(gv.delete_last_file())

    # @unittest.skip('skip test_last_file_info')
    def test_last_file_info(self):  # 文档信息显示
        logging.info('==========test_last_file_info==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_last_mark_star')
    def test_last_mark_star(self):  # 最近中的标星操作
        logging.info('==========test_last_mark_star==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertTrue(gv.check_mark_satr(file))
        gv.file_more_info(1)
        file = gv.mark_star()
        self.assertFalse(gv.check_mark_satr(file))

    # @unittest.skip('skip test_last_scroll')
    def test_z_last_scroll(self):  # 测试“最近”中的滑屏
        logging.info('==========test_last_scroll==========')
        gv = GeneralView(self.driver)
        first_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        gv.swipeUp()
        second_name = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')[0].text
        self.assertTrue(first_name != second_name)

    # @unittest.skip('skip test_last_select_all')
    def test_last_select_all(self):  # “最近”全选操作
        logging.info('==========test_last_select_all==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="全选"]').click()
        self.assertTrue(gv.get_element_result('//*[@text="取消全选"]'))
        num = int(self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_num').text)
        self.assertTrue(num != 0)
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()
        self.assertTrue(gv.get_element_result('//*[@resource-id="com.yozo.office:id/lay_more"]'))

    # @unittest.skip('skip test_last_select_all1')
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

    # @unittest.skip('skip test_share_from_index')
    @data(*index_share_list)
    def test_last_share(self, way):  # “最近”中的分享
        logging.info('==========test_last_share==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        gv.share_file_index(way)

    # @unittest.skip('skip test_last_share_back')
    def test_last_share_back(self):  # “最近”中的分享的返回键
        logging.info('==========test_last_share_back==========')
        gv = GeneralView(self.driver)
        gv.file_more_info(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_more_share').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_back').click()
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_last_upload_file')
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

    # @unittest.skip('skip test_local_folder')
    @data(*folder_list)
    def test_local_folder(self, folder):  # 测试本地文档打开
        logging.info('==========test_local_folder==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder(folder)
        self.assertTrue(gv.check_open_folder(folder), 'open fail')

    # @unittest.skip('skip test_login_fail')
    def test_login_fail(self):
        logging.info('==========test_login_fail==========')
        login = LoginView(self.driver)
        gv = GeneralView(self.driver)
        gv.jump_to_index('my')
        data = login.get_csv_data(csv_file, 5)

        login.login_from_my(data[0], data[1])
        self.assertTrue(login.get_element_result('//*[@text="忘记密码?"]'), msg='login success')

    # @unittest.skip('skip test_login_success')
    def test_login_success(self):
        logging.info('==========test_login_success==========')
        login = LoginView(self.driver)
        gv = GeneralView(self.driver)
        gv.jump_to_index('my')
        data = login.get_csv_data(csv_file, 4)

        login.login_from_my(data[0], data[1])
        gv.jump_to_index('my')
        self.assertTrue(login.check_login_status(), msg='login fail')

        login.logout_action()

    # @unittest.skip('skip test_merge_wrap')
    def test_merge_wrap(self):
        logging.info('==========test_merge_wrap==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        cv.drag_coordinate(110 + 263 * 2, 295 + 55 * 2, 110 + 263 * 3, 295 + 55 * 2)

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ele3 = '//*[@text="单元格填充"]'
        ele4 = '//*[@text="数字格式"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele1)
        ss.swipe_ele(ele4, ele1)
        ss.cell_merge_split()
        ss.cell_merge_split()
        ss.cell_auto_wrap()
        ss.cell_auto_wrap()
        time.sleep(3)

    ##########“打开”中“手机”相关功能
    # @unittest.skip('skip test_mobile_copy_file')
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

    # @unittest.skip('skip test_mobile_delete_file')
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

    # @unittest.skip('skip test_mobile_file_info')
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

    # @unittest.skip('skip test_mobile_mark_star')
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

    # @unittest.skip('skip test_mobile_move_file')
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

    # @unittest.skip('skip test_mobile_rename_file')
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

    # @unittest.skip('skip test_mobile_search_file')
    def test_mobile_search_file(self):  # 搜索功能
        logging.info('==========test_mobile_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('手机')
        self.assertTrue(gv.check_open_folder('手机'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    # @unittest.skip('skip test_mobile_select_all')
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

    # @unittest.skip('skip test_mobile_select_all1')
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

    # @unittest.skip('skip test_mobile_share')
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

    # @unittest.skip('skip test_mobile_share_back')
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

    # @unittest.skip('skip test_mobile_sort_file')
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

    # @unittest.skip('skip test_mobile_upload_file')
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

    ##########“打开”中“我的文档”相关功能
    # @unittest.skip('skip test_myfile_copy_file')
    def test_myfile_copy_file(self):
        logging.info('==========test_myfile_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    # @unittest.skip('skip test_myfile_delete_file')
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

    # @unittest.skip('skip test_myfile_file_info')
    def test_myfile_file_info(self):  # 文档信息显示
        logging.info('==========test_myfile_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_myfile_mark_star')
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

    # @unittest.skip('skip test_myfile_move_file')
    def test_myfile_move_file(self):  # “打开”移动文件
        logging.info('==========test_myfile_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    # @unittest.skip('skip test_myfile_rename_file')
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

    # @unittest.skip('skip test_myfile_search_file')
    def test_myfile_search_file(self):  # 搜索功能
        logging.info('==========test_myfile_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    # @unittest.skip('skip test_myfile_select_all')
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

    # @unittest.skip('skip test_myfile_select_all1')
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

    # @unittest.skip('skip test_myfile_share')
    @data(*index_share_list)
    def test_myfile_share(self, way):
        logging.info('==========test_myfile_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('我的文档')
        self.assertTrue(gv.check_open_folder('我的文档'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)

    # @unittest.skip('skip test_myfile_share_back')
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

    # @unittest.skip('skip test_myfile_sort_file')
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

    # @unittest.skip('skip test_myfile_upload_file')
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

    # @unittest.skip('skip test_num_style')
    def test_num_style(self):
        logging.info('==========test_num_style==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)  # 双击进入编辑
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        self.driver.press_keycode(15)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ele3 = '//*[@text="单元格填充"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele1)
        ss.cell_num_style()

    @unittest.skip('skip test_pop_cell_row_col1')
    def test_pop_cell_row_col1(self):  # 单元格、行、列相关操作
        logging.info('==========test_pop_cell_row_col1==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        time.sleep(1)

        x, y, width, height = ss.cell_location()  # 新建默认B8
        cv.tap(x + width * 0.5, y - height * 5.5)
        ss.cell_edit()  # 进入编辑
        for i in range(8):
            self.driver.press_keycode(random.randint(29, 54))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        time.sleep(0.5)
        cv.tap(x + width * 0.5, y - height * 5.5)  # 复制粘贴
        gv.pop_menu_click('copy')
        cv.tap(x + width * 0.5, y - height * 4.5)
        cv.tap(x + width * 0.5, y - height * 4.5)
        gv.pop_menu_click('paste')
        cv.tap(x + width * 1.5, y - height * 4.5)
        cv.tap(x + width * 1.5, y - height * 4.5)
        gv.pop_menu_click('paste')

        cv.tap(x + width * 1.5, y - height * 4.5)
        gv.pop_menu_click('cut')
        cv.tap(x + width * 0.5, y - height * 3.5)
        cv.tap(x + width * 0.5, y - height * 3.5)
        gv.pop_menu_click('paste')

        x, y = gv.find_pic_position('drag_point2')  # 多选单元格
        gv.drag_coordinate(x, y, x + width, y + height)

    # @unittest.skip('skip test_pop_cell_row_col2')
    def test_pop_cell_row_col2(self):  # 单元格、行、列相关操作
        logging.info('==========test_pop_cell_row_col2==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        time.sleep(1)

        x, y, width, height = ss.cell_location()  # 新建默认B8
        cv.tap(x + width * 0.5, y - height * 5.5)  # 点击B2
        ss.cell_edit()  # 进入编辑
        for i in range(8):
            self.driver.press_keycode(random.randint(29, 54))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        time.sleep(0.5)

        x1, y1, x2, y2 = ss.row_col_loc()
        ss.tap(x2 - 10, y2 + height * 1.5)
        gv.pop_menu_click('insert')
        ss.tap(x2 - 10, y2 + height * 1.5)
        gv.pop_menu_click('delete')
        ss.tap(x2 - 10, y2 + height * 1.5)
        gv.pop_menu_click('copy')
        ss.tap(x2 - 10, y2 + height * 4.5)
        x3, y3 = gv.find_pic_position('copy')
        x4, y4 = gv.find_pic_position('insert')
        gv.swipe(x3, y3, x4, y4)
        gv.pop_menu_click('paste')
        ss.tap(x2 - 10, y2 + height * 1.5)
        gv.pop_menu_click('cut')
        ss.tap(x2 - 10, y2 + height * 0.5)
        gv.pop_menu_click('paste')
        ss.tap(x2 - 10, y2 + height * 1.5)
        gv.pop_menu_click('hide')
        ss.tap(x2 - 10, y2 + height * 1.5)
        x3, y3 = gv.find_pic_position('hide')
        x4, y4 = gv.find_pic_position('copy')
        gv.swipe(x3, y3, x4, y4)
        gv.pop_menu_click('hide_cancel')
        ss.tap(x2 - 10, y2 + height * 4.5)
        x, y = gv.find_pic_position('row_down')
        gv.drag_coordinate(x, y, x, y + height * 2)
        gv.drag_coordinate(x2 - 10, y, x2 - 10, y + height * 2)

    @unittest.skip('skip test_pop_cell_row_col3')
    def test_pop_cell_row_col3(self):  # 单元格、行、列相关操作
        logging.info('==========test_pop_cell_row_col3==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        time.sleep(1)

        x, y, width, height = ss.cell_location()  # 新建默认B8
        cv.tap(x + width * 0.5, y - height * 5.5)
        ss.cell_edit()  # 进入编辑
        for i in range(8):
            self.driver.press_keycode(random.randint(29, 54))
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        time.sleep(0.5)

        x1, y1, x2, y2 = ss.row_col_loc()
        ss.tap(x2 + width * 1.5, y2 - 10)
        gv.pop_menu_click('insert')
        ss.tap(x2 + width * 1.5, y2 - 10)
        gv.pop_menu_click('delete')
        ss.tap(x2 + width * 1.5, y2 - 10)
        gv.pop_menu_click('copy')
        ss.tap(x2 + width * 2.5, y2 - 10)
        x3, y3 = gv.find_pic_position('copy')
        x4, y4 = gv.find_pic_position('insert')
        gv.swipe(x3, y3, x4, y4)
        time.sleep(1)
        gv.pop_menu_click('paste')
        ss.tap(x2 + width * 1.5, y2 - 10)
        gv.pop_menu_click('cut')
        ss.tap(x2 + width * 2.5, y2 - 10)
        gv.pop_menu_click('paste')
        ss.tap(x2 + width * 1.5, y2 - 10)
        gv.pop_menu_click('hide')
        ss.tap(x2 + width * 1.5, y2 - 10)
        x3, y3 = gv.find_pic_position('hide')
        x4, y4 = gv.find_pic_position('copy')
        gv.swipe(x3, y3, x4, y4)
        time.sleep(1)
        gv.pop_menu_click('hide_cancel')
        ss.tap(x2 + width * 1.5, y2 - 10)
        x, y = gv.find_pic_position('column_right')
        gv.drag_coordinate(x, y, x + width, y)
        gv.drag_coordinate(x, y2 - 10, x + width, y2 - 10)

    @unittest.skip('skip test_pop_menu_text_ss')
    def test_pop_menu_cell_text(self):
        logging.info('==========test_pop_menu_cell_text==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        time.sleep(1)

        x, y, width, height = ss.cell_location()  # 新建默认B8
        cv.tap(x + width * 0.5, y - height * 5.5)  # 点击B2
        ss.cell_edit()  # 进入编辑
        for i in range(15):
            self.driver.press_keycode(random.randint(29, 54))
        # time.sleep(1)
        gv.drag_coordinate(x + 200, y - height * 5.5, x + 50, y - height * 5.5)
        gv.pop_menu_click('copy')
        gv.tap(x + width * 0.5, y - height * 5.5)
        gv.pop_menu_click('paste')
        gv.drag_coordinate(x + 200, y - height * 5.5, x + 50, y - height * 5.5)
        gv.pop_menu_click('cut')
        gv.tap(x + width * 0.5, y - height * 5.5)
        gv.pop_menu_click('paste')

        gv.tap(x + width * 0.5, y - height * 5.5)
        gv.pop_menu_click('newline')

        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        gv.tap(x + width * 0.5, y - height * 5.5)
        gv.pop_menu_click('fill_data')
        x1, y1 = gv.find_pic_position('fill_down')
        gv.drag_coordinate(x1, y1, x1, y1 + height * 2)

        gv.tap(x + width * 0.5, y - height * 5.5)
        time.sleep(1)
        x2, y2 = gv.find_pic_position('fill_data')
        gv.swipe(x2, y2, x2 - width * 2, y2)
        gv.pop_menu_click('clear_content')

    @unittest.skip('skip test_pop_menu_shape1_ws')
    @data(*wps)
    def test_pop_menu_shape1(self, type):
        logging.info('==========test_pop_menu_shape1_ws==========')
        # type = 'pg'
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)

        if type == 'pg':
            pg = PGView(self.driver)
            gv.group_button_click('编辑')
            pg.edit_format('空白')

        time.sleep(1)
        gv.group_button_click('插入')
        gv.insert_shape(type)

        gv.fold_expand()
        x1, y1 = gv.find_pic_position('drag_all')
        gv.drag_coordinate(x1, y1, x1 - 100, y1)

        x1, y1 = gv.find_pic_position('drag_all')
        gv.drag_coordinate(x1, y1, x1 + 100, y1)

        x1, y1 = gv.find_pic_position('drag_all')
        gv.drag_coordinate(x1, y1, x1 - 50, y1 - 50)

        x2, y2 = gv.find_pic_position('drag_all1')
        gv.drag_coordinate(x2, y2, x2, y2 - 100)

        x2, y2 = gv.find_pic_position('drag_all1')
        gv.drag_coordinate(x2, y2, x2, y2 + 100)

        x2, y2 = gv.find_pic_position('drag_all1')
        gv.drag_coordinate(x2, y2, x2 - 50, y2 - 50)

        x, y = gv.find_pic_position('rotate_free')
        gv.drag_coordinate(x, y, x + 50, y + 50)

    # @unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_pop_menu_shape(self, type):
        logging.info('==========test_pop_menu_shape==========')
        cv = CreateView(self.driver)
        # type = 'pg'
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type)
        time.sleep(1)
        if type == 'pg':
            gv.tap(550, 450)
            gv.pop_menu_click('editText')
        else:
            gv.tap(700, 700, 2)
            gv.tap(700, 700, 3)

        for i in range(50):
            self.driver.press_keycode(random.randint(29, 54))

        if type == 'pg':
            gv.drag_coordinate(550, 830, 500, 800)
            gv.pop_menu_click('copy')
            gv.tap(550, 830)
            time.sleep(1)
            gv.long_press(550, 830)
            gv.pop_menu_click('paste')
            gv.drag_coordinate(550, 830, 500, 800)
            gv.pop_menu_click('cut')
            gv.tap(550, 830)
            time.sleep(1)
            gv.long_press(550, 830)
            gv.pop_menu_click('paste')
            gv.drag_coordinate(550, 830, 500, 800)
            gv.pop_menu_click('delete')
        else:
            gv.drag_coordinate(700, 700, 550, 550)
            gv.pop_menu_click('copy')
            gv.tap(700, 700)
            time.sleep(1)
            gv.long_press(700, 700)
            gv.pop_menu_click('paste')
            gv.drag_coordinate(700, 700, 550, 550)
            gv.pop_menu_click('cut')
            gv.tap(700, 700)
            time.sleep(1)
            gv.long_press(700, 700)
            gv.pop_menu_click('paste')
            gv.drag_coordinate(700, 700, 550, 550)
            gv.pop_menu_click('delete')

    # @unittest.skip('skip test_pop_menu_text_wp')
    def test_pop_menu_text_wp(self):
        logging.info('==========test_pop_menu_text_wp==========')
        cv = CreateView(self.driver)
        type = 'wp'
        cv.create_file(type)
        gv = GeneralView(self.driver)

        time.sleep(1)
        gv.tap(700, 700)
        for i in range(100):
            self.driver.press_keycode(random.randint(29, 54))
        gv.drag_coordinate(300, 540, 300, 200)
        gv.pop_menu_click('copy')
        gv.tap(700, 700)
        time.sleep(1)
        gv.long_press(700, 700)
        gv.pop_menu_click('paste')
        gv.drag_coordinate(300, 540, 300, 200)
        gv.pop_menu_click('cut')
        gv.tap(700, 700)
        time.sleep(1)
        gv.long_press(700, 700)
        gv.pop_menu_click('paste')

        time.sleep(3)

    # @unittest.skip('skip test_ppt_add_scroll_comment')
    def test_ppt_add_scroll_comment(self):  # ppt缩略图滚屏备注
        logging.info('==========test_ppt_add_scroll_comment==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')
        pg = PGView(self.driver)
        pg.switch_write_read()
        pg.add_new()
        pg.add_comment(5, 'test2')
        pg.add_new()
        pg.check_comment(5)
        pg.edit_comment('TEST')
        pg.add_new()
        pg.check_comment(5)
        pg.delete_comment()
        time.sleep(1)

    # @unittest.skip('skip test_ppt_format')
    def test_ppt_format(self):
        logging.info('==========test_ppt_format==========')
        format = ['标题与副标题', '标题', '标题与文本', '标题与两栏文本', '标题与竖排文本-上下', '标题与竖排文本-左右',
                  '空白', '标题与图片', '标题、文本与图片', '标题、图片与文本', '标题、图片与竖排文本', '标题、竖排文本与图片']
        cv = CreateView(self.driver)
        cv.create_file('pg')
        pg = PGView(self.driver)
        pg.group_button_click('编辑')
        for i in format:
            pg.edit_format(i)
        time.sleep(3)

    # @unittest.skip('skip test_ppt_play')
    def test_ppt_play(self):  # ppt播放
        logging.info('==========test_ppt_play==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')
        pg = PGView(self.driver)
        pg.group_button_click('播放')
        pg.play_mode('first')
        x, y = pg.get_size()

        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        pg.quit_play()
        # pg.screen_rotate('PORTRAIT')
        # pg.group_button_click('播放')
        pg.play_mode('current')
        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        time.sleep(1)
        pg.tap(y * 0.75, x * 0.5)
        pg.quit_play()
        # pg.screen_rotate('PORTRAIT')
        # pg.group_button_click('播放')
        pg.swipeRight()
        pg.swipeRight()
        pg.swipeRight()
        pg.play_mode('autoplay')
        time.sleep(2)
        pg.pause_resume_play()
        time.sleep(1)
        pg.pause_resume_play()
        time.sleep(20)
        # pg.screen_rotate('PORTRAIT')

    # @unittest.skip('skip test_ppt_play_switch')
    @data(*switch_list)
    def test_ppt_play_switch(self, switch):  # 幻灯片切换
        logging.info('==========test_ppt_play_switch==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')
        pg = PGView(self.driver)
        pg.switch_write_read()

        pg.group_button_click('切换')
        pg.switch_mode(switch, 'all')
        pg.group_button_click('播放')
        pg.play_mode()
        time.sleep(20)

    @unittest.skip('skip test_ppt_slide')
    def test_ppt_slide(self):  # 幻灯片复制、剪切、粘贴
        logging.info('==========test_ppt_slide==========')
        cv = CreateView(self.driver)
        type = 'pg'
        cv.create_file(type)
        gv = GeneralView(self.driver)

        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[1]').click()
        time.sleep(1)
        gv.pop_menu_click('copy')
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[1]').click()
        time.sleep(1)
        gv.pop_menu_click('paste')

        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[2]').click()
        time.sleep(1)
        gv.pop_menu_click('cut')
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[1]').click()
        time.sleep(1)
        gv.pop_menu_click('paste')

        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[2]').click()
        time.sleep(1)
        gv.pop_menu_click('create')
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[3]').click()
        time.sleep(1)
        gv.pop_menu_click('delete')

        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[2]').click()
        time.sleep(1)
        x1, y1 = gv.find_pic_position('copy')
        x2, y2 = gv.find_pic_position('delete')
        gv.swipe(x2, y2, x1, y1)
        gv.pop_menu_click('hide')
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[2]').click()
        time.sleep(1)
        gv.pop_menu_click('hide_cancel')
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView'
                                           '/android.widget.LinearLayout/android.view.View[2]').click()
        time.sleep(1)
        gv.pop_menu_click('comment')

        time.sleep(3)

    # @unittest.skip('skip test_ppt_template')
    def test_ppt_template(self):
        logging.info('==========test_ppt_template==========')
        cv = CreateView(self.driver)
        cv.create_file('pg')
        pg = PGView(self.driver)
        pg.group_button_click('编辑')
        for i in range(11):
            pg.edit_template(i)
        time.sleep(3)

    ##########“打开”中“QQ”相关功能
    # @unittest.skip('skip test_QQ_copy_file')
    def test_qq_copy_file(self):
        logging.info('==========test_QQ_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    # @unittest.skip('skip test_QQ_delete_file')
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

    # @unittest.skip('skip test_QQ_file_info')
    def test_qq_file_info(self):  # 文档信息显示
        logging.info('==========test_QQ_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_QQ_mark_star')
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

    # @unittest.skip('skip test_QQ_move_file')
    def test_qq_move_file(self):  # “打开”移动文件
        logging.info('==========test_QQ_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    # @unittest.skip('skip test_QQ_rename_file')
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

    # @unittest.skip('skip test_QQ_search_file')
    def test_qq_search_file(self):  # 搜索功能
        logging.info('==========test_QQ_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    # @unittest.skip('skip test_QQ_select_all')
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

    # @unittest.skip('skip test_QQ_select_all1')
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

    # @unittest.skip('skip test_QQ_share')
    @data(*index_share_list)
    def test_qq_share(self, way):
        logging.info('==========test_QQ_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('QQ')
        self.assertTrue(gv.check_open_folder('QQ'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)

    # @unittest.skip('skip test_QQ_share_back')
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

    # @unittest.skip('skip test_QQ_sort_file')
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

    # @unittest.skip('skip test_QQ_upload_file')
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

    ##################################
    # @unittest.skip('skip test_read_mode')
    @data(*wps)
    def test_read_mode(self, type):  # 阅读模式
        logging.info('==========test_read_mode==========')
        cv = CreateView(self.driver)
        cv.create_file(type)

        gv = GeneralView(self.driver)
        gv.switch_write_read()
        self.assertTrue(gv.check_write_read())

    # @unittest.skip('skip test_rotate')
    @data(*wps)
    def test_rotate(self, type):
        logging.info('==========test_rotate==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        # gv.screen_rotate('landscape')
        self.assertTrue(gv.check_rotate())
        gv.screen_rotate('portrait')

   
    # @unittest.skip('skip test_scroll_screen')
    @data(*wps)
    def test_scroll_screen(self, type):  # 滚屏
        logging.info('==========test_scroll_screen==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        if type == 'pg':
            time.sleep(3)
            ov.swipeLeft()
            ov.swipeLeft()
            ov.swipeRight()
        elif type == 'ss':
            time.sleep(3)
            ov.swipeLeft()
            ov.swipeLeft()
            ov.swipeRight()
            ov.swipeUp()
            ov.swipeUp()
            ov.swipeDown()
        else:
            time.sleep(3)
            ov.swipeUp()
            ov.swipeUp()
            ov.swipeDown()
        time.sleep(3)

    # @unittest.skip('skip test_search_replace')
    @data(*wps)
    def test_search_replace(self, type):  # 查找替换
        logging.info('==========test_search_replace==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        if type in ws:
            gv.group_button_click('查看')
        gv.search_content(type, '的')
        gv.replace_content('得')
        time.sleep(3)
        gv.replace_content('得', 'all')

    # @unittest.skip('skip test_shape_attr1')
    @data(*wps)
    def test_shape_attr1(self, type):  # 文本框字符属性
        logging.info('==========test_shape_attr1==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        x1, y1 = 0, 0
        if type == 'ss':
            ss = SSView(self.driver)
            x1, y1, w, h = ss.cell_location()
            self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        gv.group_button_click('插入')
        gv.insert_shape(type)
        time.sleep(1)
        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)  # 进入编辑
        gv.pop_menu_click('editText')

        if type == 'ss':
            gv.fold_expand()
            gv.fold_expand()
            x, y = gv.find_pic_position('drag_all')
            gv.tap(x, y)  # 进入编辑
            gv.pop_menu_click('editText')

        for i in range(50):
            self.driver.press_keycode(random.randint(7, 16))

        if type == 'pg':
            gv.tap(250, 250)
            gv.tap(550, 850)
        elif type == 'ss':
            gv.tap(x1, y1)
            gv.tap(x, y)
        else:
            gv.tap(250, 450)
            time.sleep(1)
            gv.fold_expand()
            gv.tap(x, y)
            time.sleep(1)
        gv.fold_expand()

        gv.shape_option(type, 5, width=5, height=5)
        gv.shape_option(type, 6, top=0.5, bottom=0.5, left=0.5, right=0.5)
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        ele3 = '//*[@text="效果"]'
        if type == 'pg':
            ele0 = '//*[@text="插入"]'
            gv.swipe_ele(ele0, ele1)
        gv.swipe_ele(ele2, ele1)
        gv.swipe_ele(ele3, ele1)
        gv.shape_content_align(type, '右对齐', '下对齐')
        gv.shape_content_align(type)
        gv.shape_content_align(type, '水平居中', '垂直居中')
        time.sleep(3)

    # @unittest.skip('skip test_shape_attr2')
    @data(*wps)
    def test_shape_attr2(self, type):
        logging.info('==========test_shape_att2r==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 6, 10)
        gv.shape_option(type, 2)
        gv.shape_fill_color(type, 6, 24)
        gv.shape_fill_color_transparency(5)
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        if type == 'pg':
            ele0 = '//*[@text="插入"]'
            gv.swipe_ele(ele0, ele1)
        gv.swipe_ele(ele2, ele1)
        gv.shape_border_color(type, 6, 5)
        gv.shape_border_type(type, 6, 3)
        gv.shape_border_width(type, 6, 5)
        gv.shape_effect_type(type, 6, 4, 5)
        time.sleep(1)

    # @unittest.skip('skip test_shape_attr')
    @data(*wps)
    def test_shape_attr(self, type):
        logging.info('==========test_shape_attr==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 6, 30)
        gv.shape_insert(type, 6, 31)
        gv.shape_insert(type, 6, 32)
        gv.shape_insert(type, 6, 33)
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        ele3 = '//*[@text="效果"]'
        if type == 'pg':
            ele0 = '//*[@text="插入"]'
            gv.swipe_ele(ele0, ele1)
        gv.swipe_ele(ele2, ele1)
        gv.swipe_ele(ele3, ele1)
        gv.shape_layer('下移一层')
        gv.shape_layer('置于底层')
        gv.shape_layer('上移一层')
        gv.shape_layer('置于顶层')

    # @unittest.skip('skip test_shape_text_attr_pg')
    def test_shape_text_attr_pg(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========test_shape_text_attr_pg==========')
        type = 'pg'
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        gv.group_button_click('编辑')
        gv.font_name(type, 'AndroidClock')
        gv.font_size(15)
        gv.font_style(type, '倾斜')
        gv.font_color(type, 6, 29)
        gv.swipe_ele('//*[@text="字体颜色"]', '//*[@text="编辑"]')
        gv.fold_expand()
        time.sleep(1)
        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)  # 进入编辑
        gv.pop_menu_click('editText')
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        time.sleep(1)
        gv.group_button_click('编辑')
        # gv.high_light_color(type,6,6)
        gv.bullets_numbers(type, 6, 10)
        gv.text_align(type, '分散对齐')
        gv.text_align(type, '右对齐')
        gv.text_line_space(type, 1.5)
        gv.text_line_space(type, 3)
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '左缩进')
        time.sleep(3)

    # @unittest.skip('skip test_shape_text_attr_wp')
    def test_shape_text_attr_wp(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========test_shape_text_attr_wp==========')
        type = 'wp'
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        gv.tap(680, 750)
        gv.pop_menu_click('editText')
        time.sleep(1)
        gv.group_button_click('编辑')
        gv.font_name(type, 'AndroidClock')
        gv.font_size(15)
        gv.font_style(type, '倾斜')
        gv.font_color(type, 6, 29)
        gv.swipe_ele('//*[@text="字体颜色"]', '//*[@text="编辑"]')
        time.sleep(1)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        time.sleep(1)
        gv.swipe_ele('//*[@text="高亮颜色"]', '//*[@text="编辑"]')
        gv.drag_coordinate(680, 750, 680, 600)
        gv.high_light_color(type, 6, random.randint(1, 15))
        gv.bullets_numbers(type, 6, 10)
        gv.text_align(type, '分散对齐')
        gv.text_align(type, '右对齐')
        gv.text_line_space(type, 1.5)
        gv.text_line_space(type, 3)
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '右缩进')
        gv.text_indent(type, '左缩进')
        time.sleep(3)

    # @unittest.skip('skip test_share_file')
    @data(*share_list)
    def test_share_file(self, way):  # 分享文件
        logging.info('==========test_share_file==========')
        index = way.index('_')
        suffix = search_dict[way[0:index]]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)

        gv = GeneralView(self.driver)
        gv.share_file(way[0:index], way[index + 1:])

    # @unittest.skip('skip test_sheet_operation')
    def test_sheet_operation(self):  # sheet相关功能
        logging.info('==========test_sheet_operation==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.hide_sheet()
        ss.show_sheet()
        ss.add_sheet()
        ss.rename_sheet(0, 'test')
        self.assertTrue(ss.check_rename_sheet(0, 'test'))

    # @unittest.skip('skip test_sheet_operation1')
    def test_sheet_operation1(self):  # sheet相关功能
        logging.info('==========test_sheet_operation1==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.show_sheet()
        ss.operate_sheet(0, 'insert')
        ss.operate_sheet(0, 'copy')
        ss.operate_sheet(0, 'remove')
        ss.operate_sheet(0, 'hide')
        ss.unhide_sheet(0, 0)

    # @unittest.skip('skip test_show_cloud_file')
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

    # @unittest.skip('skip test_show_open_file')
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

    # @unittest.skip('skip test_signature')
    @data(*wps)
    def test_signature(self, type):  # 签批
        logging.info('==========test_signature==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('签批')
        gv.use_finger(type)
        gv.use_finger(type)
        gv.pen_type(type, '钢笔')
        gv.pen_color(type, 15)
        gv.pen_size(type, 3)
        gv.swipe(300, 400, 800, 400, 500)
        gv.pen_type(type, '荧光笔')
        gv.pen_color(type, 30)
        gv.pen_size(type, 6)
        gv.swipe(300, 600, 800, 600, 500)
        gv.pen_type(type, '擦除')
        gv.swipe(200, 400, 900, 400, 500)
        gv.swipe(200, 600, 900, 600, 500)
        time.sleep(3)

    # @unittest.skip('skip test_ss_chart_pop')
    def test_ss_chart_pop(self):  # 图表相关操作
        logging.info('==========test_ss_chart_pop==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)
        ss = SSView(self.driver)
        gv = GeneralView(self.driver)
        time.sleep(2)
        x, y, width, height = ss.object_position('drag_point1', 'drag_point2')
        ss.tap(x, y)
        time.sleep(2)
        ss.pop_menu_click('edit')
        self.driver.press_keycode(12)
        ss.tap(x, y + height)
        time.sleep(1)

        ss.tap(x, y + height)
        time.sleep(2)
        ss.pop_menu_click('edit')
        self.driver.press_keycode(15)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        # ss.tap(x, y)
        x, y = ss.find_pic_position('drag_point1')
        ss.swipe(x, y, x, y - height)
        time.sleep(1)
        ss.group_button_click('插入')
        gv.insert_chart_insert('柱形图', 2)

        x, y, width, height = ss.object_position('chart_all1', 'chart_all4')
        ss.tap(x, y)
        time.sleep(2)
        ss.pop_menu_click('cut')
        ss.tap(x, y)
        time.sleep(2)
        ss.tap(x, y)
        ss.pop_menu_click('paste')
        ss.tap(x, y)
        time.sleep(2)
        ss.pop_menu_click('copy')
        ss.tap(x, y)
        time.sleep(2)
        ss.pop_menu_click('paste')
        ss.swipe(x, y, x - 100, y + 100)
        x, y = ss.find_pic_position('chart_all1')
        ss.swipe(x, y, x - 100, y - 100)

    # @unittest.skip('skip test_table_style')
    def test_table_style(self):  # 表格样式
        logging.info('==========test_table_style==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        time.sleep(1)
        cv.tap(110 + 263 * 1.5, 295 + 55 * 1.5)
        cv.drag_coordinate(110 + 263 * 2, 295 + 55 * 2, 110 + 263 * 3, 295 + 55 * 4)
        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ele3 = '//*[@text="单元格填充"]'
        ele4 = '//*[@text="数字格式"]'
        ele5 = '//*[@text="插入单元格"]'
        ss.swipe_ele(ele2, ele1)
        ss.swipe_ele(ele3, ele1)
        ss.swipe_ele(ele4, ele1)
        ss.swipe_ele(ele5, ele1)
        ss.table_style()

    # @unittest.skip('skip test_undo_redo')
    @data(*wps)
    def test_undo_redo(self, type):  # 撤销、重做
        logging.info('==========test_undo_redo==========')
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        cv.create_file(type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo')  # 判断页面是否已切过来

        gv.group_button_click('插入')
        gv.insert_shape(type, 1)
        gv.fold_expand()

        gv.undo_option()
        time.sleep(1)
        gv.redo_option()
        time.sleep(1)
        gv.undo_option()
        time.sleep(1)

        logging.info('capture before undo')
        gv.getScreenShot4Compare('before_undo')

        gv.redo_option()
        time.sleep(1)

        logging.info('capture before redo')
        gv.getScreenShot4Compare('before_redo')

        gv.undo_option()
        if type == 'ss':
            gv.fold_expand()
            gv.fold_expand()
        time.sleep(1)
        logging.info('capture after undo')
        gv.getScreenShot4Compare('after_undo')

        gv.redo_option()
        time.sleep(1)
        logging.info('capture after redo')
        gv.getScreenShot4Compare('after_redo')

        result1 = gv.compare_pic('before_undo.png', 'after_undo.png')
        result2 = gv.compare_pic('before_redo.png', 'after_redo.png')

        self.assertLess(result1, 100, 'undo fail!')
        self.assertLess(result2, 100, 'redo fail!')

    ##########“打开”中“微信”相关功能
    # @unittest.skip('skip test_wechat_copy_file')
    def test_wechat_copy_file(self):
        logging.info('==========test_wechat_copy_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        check = gv.copy_file()
        self.assertTrue(check, 'copy fail')

    # @unittest.skip('skip test_wechat_delete_file')
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

    # @unittest.skip('skip test_wechat_file_info')
    def test_wechat_file_info(self):  # 文档信息显示
        logging.info('==========test_wechat_file_info==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        self.assertTrue(gv.get_element_result('//*[@text="文档信息"]'))

    # @unittest.skip('skip test_wechat_mark_star')
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

    # @unittest.skip('skip test_wechat_move_file')
    def test_wechat_move_file(self):  # “打开”移动文件
        logging.info('==========test_wechat_move_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(2)
        check = gv.move_file()
        self.assertTrue(check, 'move fail')

    # @unittest.skip('skip test_wechat_rename_file')
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

    # @unittest.skip('skip test_wechat_search_file')
    def test_wechat_search_file(self):  # 搜索功能
        logging.info('==========test_wechat_search_file==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        search_file = '欢迎使用永中Office.pptx'
        result = gv.search_action(search_file)
        self.assertTrue(result)

    # @unittest.skip('skip test_wechat_select_all')
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

    # @unittest.skip('skip test_wechat_select_all1')
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

    # @unittest.skip('skip test_wechat_share')
    @data(*index_share_list)
    def test_wechat_share(self, way):
        logging.info('==========test_wechat_share==========')
        gv = GeneralView(self.driver)
        gv.jump_to_index('alldoc')
        gv.open_local_folder('微信')
        self.assertTrue(gv.check_open_folder('微信'), 'open fail')
        gv.file_more_info(7)
        gv.share_file_index(way)

    # @unittest.skip('skip test_wechat_share_back')
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

    # @unittest.skip('skip test_wechat_sort_file')
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

    # @unittest.skip('skip test_wechat_upload_file')
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

    ##################################
    # @unittest.skip('skip test_wp_bookmark')
    def test_wp_bookmark(self):
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.group_button_click('查看')
        wp.add_bookmark('test')
        self.assertTrue(wp.check_add_bookmark(), '书签插入失败！')
        wp.swipeUp()
        wp.swipeUp()
        wp.group_button_click('查看')
        wp.list_bookmark('test')

    # @unittest.skip('skip test_wp_check_approve')
    def test_wp_check_approve(self):  # 修订
        logging.info('==========test_wp_check_approve==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('审阅')
        wp.change_name('super_root')
        wp.group_button_click('审阅')
        wp.revision_on_off('开启')
        wp.tap(450, 550)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('审阅')
        wp.revision_accept_not('yes')
        wp.tap(450, 550)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('审阅')
        wp.revision_accept_not()
        wp.group_button_click('审阅')
        wp.revision_on_off('关闭')
        time.sleep(3)

    # @unittest.skip('skip test_wp_font_attr')
    def test_wp_font_attr(self):
        logging.info('==========test_wp_font_attr===========')
        cv = CreateView(self.driver)
        type = 'wp'
        cv.create_file(type)
        time.sleep(1)
        wp = WPView(self.driver)
        wp.group_button_click('编辑')
        wp.font_size(16)
        # wp.font_name(type)
        wp.font_style(type, '倾斜')
        wp.font_color(type, 3)
        ele1 = '//*[@text="编辑"]'
        ele2 = '//*[@text="字体颜色"]'
        ele3 = '//*[@text="高亮颜色"]'
        ele4 = '//*[@text="分栏"]'
        wp.swipe_ele(ele2, ele1)
        time.sleep(1)
        wp.tap(450, 450)
        for i in range(100):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('编辑')
        wp.drag_coordinate(450, 500, 200, 500)
        wp.high_light_color(type, 3)
        wp.bullets_numbers(type, 6, 14)
        wp.text_align(type, '右对齐')
        wp.swipe_ele(ele3, ele1)
        wp.text_line_space(type, 2.5)
        wp.text_indent(type, '右缩进')
        wp.swipe_ele(ele4, ele1)
        wp.text_columns(4)
        wp.text_columns(3)
        wp.text_columns(2)
        time.sleep(3)

    # @unittest.skip('skip test_wp_insert_watermark')
    def test_wp_insert_watermark(self):
        logging.info('==========test_wp_insert_watermark==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.insert_watermark('YOZO')
        time.sleep(1)
        wp.group_button_click('插入')
        wp.insert_watermark('yozo', delete='delete')
        time.sleep(3)

    # @unittest.skip('skip test_wp_jump')
    def test_wp_jump(self):  # 跳转页
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.group_button_click('查看')
        wp.page_jump(7)
        time.sleep(2)

    # @unittest.skip('skip test_wp_read_self_adaption')
    def test_wp_read_self_adaption(self):  # wp阅读自适应
        logging.info('==========test_wp_read_self_adaption==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.read_self_adaption()
        time.sleep(1)
        self.assertFalse(wp.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                         'read self adaption set fail!')

    # @unittest.skip('skip test_wp_text_select')
    def test_wp_text_select(self):  # 文本选取
        logging.info('==========test_wp_text_select==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.switch_write_read()
        x, y = wp.get_size()
        wp.drag_coordinate(x * 0.5, y * 0.4, x * 0.6, y * 0.5)
        time.sleep(3)

    # @unittest.skip('skip test_zoom_pinch')
    @data(*wps)
    def test_zoom_pinch(self, type):
        logging.info('==========test_zoom_pinch==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        ov.zoom()
        ov.pinch()

    # @unittest.skip('skip test_save_as_existFile')
    @data(*wps)
    def test_zz_save_as_existFile(self, type):  # 已有文件另存为
        logging.info('==========test_save_as_existFile==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        cv = CreateView(self.driver)
        file_name = 'save_as_exist ' + cv.getTime('%H_%M_%S')
        cv.save_as_file(file_name, 'local', 1)
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_save_as_newFile')
    @data(*wps)
    def test_zz_save_as_newFile(self, type):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = 'save_as_new ' + cv.getTime('%H_%M_%S')
        cv.save_as_file(file_name, 'local', 1)
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_save_existFile')
    @data(*wps)
    def test_zz_save_existFile(self, type):  # 已有文件改动保存
        logging.info('==========test_save_existFile==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        cv = CreateView(self.driver)
        gv = GeneralView(self.driver)
        gv.switch_write_read()
        gv.group_button_click('签批')
        gv.pen_type(type, '荧光笔')
        self.driver.swipe(300, 400, 800, 500)
        cv.save_file()
        self.assertTrue(cv.check_save_file())

    # @unittest.skip('skip test_save_newFile')
    @data(*wps)
    def test_zz_save_newFile(self, type):  # 新建脚本保存
        logging.info('==========test_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = 'save_new ' + cv.getTime('%Y-%m-%d %H-%M-%S')
        cv.save_new_file(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())
