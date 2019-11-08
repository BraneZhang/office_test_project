#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import random
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.pgView import PGView
from businessView.ssView import SSView
from common.myunit import StartEnd
from data import data_info

share_list = data_info.share_list
wps = data_info.wps
ps = data_info.ps
wp = data_info.wp
ws = data_info.ws
search_dict = data_info.search_dict
switch_list = data_info.switch_list


@ddt
class TestFunc(StartEnd):
    @unittest.skip('skip test_create_file')
    @data(*wps)
    def test_create_file(self, type):  # 新建文档
        logging.info('==========test_create_file==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict[type])

    @unittest.skip('skip test_expand_fold')
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

    @unittest.skip('skip test_export_pdf')
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

    @unittest.skip('skip test_insert_chart1')
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

    @unittest.skip('skip test_insert_chart')
    @data(*wps)
    def test_insert_chart(self, type):  # 插入图表，仅ss，pg
        logging.info('==========test_insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图',
                      '圆锥图', '棱锥图']
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

        for i in range(12):
            time.sleep(1)
            gv.group_button_click('插入')
            if type != 'ss':
                gv.swipe_options()
            gv.insert_chart_insert(chart_list[i], random.randint(1, 9))
            gv.chart_template()
            if type == 'wp':
                gv.tap(60, 250, 2)
        time.sleep(1)

    @unittest.skip('skip test_insert_shape')
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

    @unittest.skip('skip test_pop_menu_shape')
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

    @unittest.skip('skip test_read_mode')
    @data(*wps)
    def test_read_mode(self, type):  # 阅读模式
        logging.info('==========test_read_mode==========')
        cv = CreateView(self.driver)
        cv.create_file(type)

        gv = GeneralView(self.driver)
        gv.switch_write_read()
        self.assertTrue(gv.check_write_read())

    @unittest.skip('skip test_rotate')
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

    @unittest.skip('skip test_scroll_screen')
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

    @unittest.skip('skip test_search_replace')
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

    @unittest.skip('skip test_shape_attr1')
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

    @unittest.skip('skip test_shape_attr2')
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

    @unittest.skip('skip test_shape_attr')
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

    @unittest.skip('skip test_share_file')
    @data(*share_list)
    def test_share_file(self, way):  # 分享文件
        logging.info('==========test_share_file==========')
        index = way.index('_')
        suffix = search_dict[way[0:index]]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)

        gv = GeneralView(self.driver)
        gv.share_file(way[0:index], way[index + 1:])
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_share_file_create')
    @data(*share_list)
    def test_share_file_create(self, way):
        logging.info('==========test_share_file_create==========')
        index = way.index('_')
        type = way[0:index]
        share_way = way[index + 1:]
        gv = GeneralView(self.driver)
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict[type])
        gv.share_file(type, share_way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        save_name = gv.getTime("%Y%m%d%H%M%S")
        cv.save_step('local', save_name, 1)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_share_file_edit')
    @data(*share_list)
    def test_share_file_edit(self, way):
        logging.info('==========test_share_file_edit==========')
        index = way.index('_')
        suffix = search_dict[way[0:index]]
        type = way[0:index]
        share_way = way[index + 1:]
        gv = GeneralView(self.driver)
        ov = OpenView(self.driver)
        cv = CreateView(self.driver)

        ov.open_file('欢迎使用永中Office.%s' % suffix)
        gv.switch_write_read()
        gv.group_button_click('插入')
        gv.insert_shape(type)
        gv.share_file(type, share_way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_signature')
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

    @unittest.skip('skip test_undo_redo')
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

    @unittest.skip('skip test_zoom_pinch')
    @data(*wps)
    def test_zoom_pinch(self, type):
        logging.info('==========test_zoom_pinch==========')
        suffix = search_dict[type]
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.%s' % suffix)
        ov.zoom()
        ov.pinch()

    @unittest.skip('skip test_save_as_existFile')
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

    @unittest.skip('skip test_save_as_newFile')
    @data(*wps)
    def test_zz_save_as_newFile(self, type):  # 新建脚本另存为
        logging.info('==========test_save_as_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = 'save_as_new ' + cv.getTime('%H_%M_%S')
        cv.save_as_file(file_name, 'local', 1)
        self.assertTrue(cv.check_save_file())

    @unittest.skip('skip test_save_existFile')
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

    @unittest.skip('skip test_save_newFile')
    @data(*wps)
    def test_zz_save_newFile(self, type):  # 新建脚本保存
        logging.info('==========test_save_newFile==========')
        cv = CreateView(self.driver)
        cv.create_file(type)
        file_name = 'save_new ' + cv.getTime('%Y-%m-%d %H-%M-%S')
        cv.save_new_file(file_name, 'local', 2)
        self.assertTrue(cv.check_save_file())

    logging.info('==========2019-11-05 add==========')

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
        ov.open_random_file(search_dict[file_type])

        logging.info('==========show file info==========')
        gv = GeneralView(self.driver)
        gv.wait_loading()
        gv.file_info()