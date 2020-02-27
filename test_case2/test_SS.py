#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import random
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from businessView.ssView import SSView
from common.myunit import StartEnd
from data import data_info
from data.data_info import share_list1, search_dict

date_filter = data_info.date_filter
num_filter = data_info.num_filter
text_filter = data_info.text_filter
index_share_list2 = data_info.index_share_list2
print_ways = data_info.print_ways


@ddt
class TestSS(StartEnd):

    # =======add 2020_02_25===== 拆分共用功能

    @unittest.skip('skip test_ss_file_info')
    def test_ss_file_info(self, file_type='ss'):
        """
        文档信息
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_ss_file_info==========')
        gv = SSView(self.driver)
        gv.open_random_file(search_dict[file_type])

        logging.info('==========show file info==========')
        gv.wait_loading()
        gv.file_info()
    
    @unittest.skip('skip test_ss_share_editFile')
    @data(*share_list1)
    def test_ss_share_editFile(self, share_info):
        """
        编辑文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_ss_share_editFile==========')
        ss = SSView(self.driver)
        file_type = 'ss'

        logging.info('==========edit and save File==========')
        ss.open_random_file(search_dict[file_type])
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        ss.group_button_click('插入')
        ss.insert_shape(file_type, 1)
        ss.save_file()
        self.assertTrue(ss.get_toast_message('保存成功'))

        logging.info('==========share new File==========')
        ss.share_file(file_type, share_info)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')
    
    @unittest.skip('skip test_share_newFile')
    @data(*share_list1)
    def test_share_newFile(self, share_info):
        """
        新建文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_share_newFile==========')
        hp = SSView(self.driver)
        file_type = 'ss'

        logging.info('==========create and save new File==========')
        hp.create_file(file_type)
        hp.save_new_file('%s%s分享' % (file_type, share_info), 'local')
        time.sleep(1)
        hp.cover_file(True)
        self.assertTrue(hp.get_toast_message('保存成功'))

        logging.info('==========share new File==========')
        hp.share_file(file_type, share_info)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_ss_close_file')
    def test_ss_close_file(self, file_type='ss'):
        """
        关闭功能（X）
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_ss_close_file==========')
        hp = HomePageView(self.driver)
        isOpen = hp.open_random_file(search_dict[file_type])
        self.assertTrue(isOpen, 'open fail')
        hp.close_file()
        self.assertTrue(hp.check_close_file())

    @unittest.skip('skip test_ss_save_newFile')
    def test_ss_save_newFile(self, type='ss'):  # 新建脚本保存
        logging.info('==========test_ss_save_newFile==========')
        hp = SSView(self.driver)
        hp.create_file(type)
        file_name = 'save_new ' + hp.getTime('%Y-%m-%d %H-%M-%S')
        hp.save_new_file(file_name, 'local', 2)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_ss_save_existFile')
    def test_ss_save_existFile(self, type='ss'):  # 已有文件改动保存
        logging.info('==========test_ss_save_existFile==========')
        gv = SSView(self.driver)

        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = gv.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = gv.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        gv.switch_write_read()
        gv.group_button_click('签批')
        gv.pen_type(type, '荧光笔')
        self.driver.swipe(300, 400, 800, 500)
        gv.save_file()
        self.assertTrue(gv.check_save_file())

    @unittest.skip('skip test_ss_save_as_newFile')
    def test_ss_save_as_newFile(self, type='ss'):  # 新建脚本另存为
        logging.info('==========test_ss_save_as_newFile==========')
        hp = SSView(self.driver)
        hp.create_file(type)
        file_name = 'save_as_new ' + hp.getTime('%H_%M_%S')
        hp.save_as_file(file_name, 'local', 1)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_ss_save_as_existFile')
    def test_ss_save_as_existFile(self, type='ss'):  # 已有文件另存为
        logging.info('==========test_ss_save_as_existFile==========')
        hp = SSView(self.driver)

        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        file_name = '已有文档另存'
        hp.save_as_file(file_name, 'local', 1)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_ss_zoom_pinch')
    def test_ss_zoom_pinch(self, type='ss'):
        logging.info('==========test_ss_zoom_pinch==========')
        hp = SSView(self.driver)
        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        hp.zoom_in()
        hp.zoom_out()

    @unittest.skip('skip test_ss_undo_redo')
    def test_ss_undo_redo(self, type='ss'):  # 撤销、重做
        logging.info('==========test_ss_undo_redo==========')
        gv = SSView(self.driver)
        gv.create_file(type)
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

    @unittest.skip('skip test_ss_signature')
    def test_ss_signature(self, type='ss'):  # 签批
        logging.info('==========test_ss_signature==========')
        gv = SSView(self.driver)
        gv.create_file(type)
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

    @unittest.skip('skip test_ss_share_file_edit')
    @data(*share_list1)
    def test_ss_share_file_edit(self, way):
        logging.info('==========test_ss_share_file_edit==========')
        ss = SSView(self.driver)

        type = 'ss'
        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.group_button_click('插入')
        ss.insert_shape(type)
        ss.share_file(type, way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_ss_share_file_create')
    @data(*share_list1)
    def test_ss_share_file_create(self, way):
        logging.info('==========test_ss_share_file_create==========')
        ss = SSView(self.driver)

        type = 'ss'
        ss.create_file(type)
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict[type])
        ss.share_file(type, way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        save_name = ss.getTime("%Y%m%d%H%M%S")
        ss.save_step('local', save_name, 1)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_ss_share_file')
    @data(*share_list1)
    def test_ss_share_file(self, way):  # 分享文件
        logging.info('==========test_ss_share_file==========')
        ss = SSView(self.driver)
        file_type = 'ss'

        suffix = search_dict[file_type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.share_file(file_type, way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_ss_shape_attr')
    def test_ss_shape_attr(self, type='ss'):
        logging.info('==========test_ss_shape_attr==========')
        gv = SSView(self.driver)
        gv.create_file(type)
        gv.group_button_click('插入')
        gv.insert_shape(type, 6, 30)
        gv.shape_insert(type, 6, 31)
        gv.shape_insert(type, 6, 32)
        gv.shape_insert(type, 6, 33)
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        ele3 = '//*[@text="效果"]'
        gv.swipe_ele(ele2, ele1)
        gv.swipe_ele(ele3, ele1)
        gv.shape_layer('下移一层')
        gv.shape_layer('置于底层')
        gv.shape_layer('上移一层')
        gv.shape_layer('置于顶层')

    @unittest.skip('skip test_ss_shape_attr2')
    def test_ss_shape_attr2(self, file_type='ss'):
        logging.info('==========test_ss_shape_attr2==========')
        gv = SSView(self.driver)
        gv.create_file(file_type)
        gv.group_button_click('插入')
        gv.insert_shape(file_type, 6, 10)
        gv.shape_option(file_type, 2)
        gv.shape_fill_color(file_type, 6, 24)
        gv.shape_fill_color_transparency(5)
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        gv.swipe_ele(ele2, ele1)
        gv.shape_border_color(file_type, 6, 5)
        gv.shape_border_type(file_type, 6, 3)
        gv.shape_border_width(file_type, 6, 5)
        gv.shape_effect_type(file_type, 6, 4, 5)
        time.sleep(1)

    @unittest.skip('skip test_ss_shape_attr1')
    def test_ss_shape_attr1(self, file_type='ss'):  # 文本框字符属性
        logging.info('==========test_shape_attr1==========')
        gv = SSView(self.driver)
        gv.create_file(file_type)
        x1, y1 = 0, 0
        x1, y1, w, h = gv.cell_location()
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        gv.group_button_click('插入')
        gv.insert_shape(file_type)
        time.sleep(1)
        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)  # 进入编辑
        gv.pop_menu_click('editText')

        gv.fold_expand()
        gv.fold_expand()
        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)  # 进入编辑
        gv.pop_menu_click('editText')

        for i in range(50):
            self.driver.press_keycode(random.randint(7, 16))

        gv.tap(x1, y1)
        gv.tap(x, y)
        gv.fold_expand()

        gv.shape_option(file_type, 5, width=5, height=5)
        gv.shape_option(file_type, 6, top=0.5, bottom=0.5, left=0.5, right=0.5)
        gv.swipe_options()
        gv.swipe_options()
        gv.swipe_options()
        gv.swipe_options()
        gv.shape_content_align(file_type, '右对齐', '下对齐')
        gv.shape_content_align(file_type)
        gv.shape_content_align(file_type, '水平居中', '垂直居中')

    @unittest.skip('skip test_ss_search_replace')
    def test_ss_search_replace(self):  # 查找替换
        logging.info('==========test_ss_search_replace==========')
        gv = SSView(self.driver)
        file_name = '欢迎使用永中Office.xlsx'
        search_result = gv.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = gv.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        gv.switch_write_read()
        gv.group_button_click('查看')
        gv.search_content('ss', '的')
        gv.replace_content('得')
        time.sleep(3)
        gv.replace_content('得', 'all')

    @unittest.skip('skip test_ss_scroll_screen')
    def test_ss_scroll_screen(self):  # 滚屏
        logging.info('==========test_ss_scroll_screen==========')
        hp = SSView(self.driver)
        file_name = '欢迎使用永中Office.xlsx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        time.sleep(3)
        hp.swipeLeft()
        hp.swipeLeft()
        hp.swipeRight()
        hp.swipeUp()
        hp.swipeUp()
        hp.swipeDown()
        time.sleep(3)

    @unittest.skip('skip test_ss_rotate')
    def test_ss_rotate(self):
        logging.info('==========test_ss_rotate==========')
        hp = SSView(self.driver)
        file_name = '欢迎使用永中Office.xlsx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        # gv.screen_rotate('landscape')
        self.assertTrue(hp.check_rotate())
        hp.screen_rotate('portrait')

    @unittest.skip('skip test_ss_read_mode')
    def test_ss_read_mode(self):  # 阅读模式
        logging.info('==========test_ss_read_mode==========')
        ss = SSView(self.driver)

        ss.create_file('ss')
        ss.switch_write_read()
        self.assertTrue(ss.check_write_read())

    @unittest.skip('skip test_ss_pop_menu_shape')
    def test_ss_pop_menu_shape(self):  # pg未好
        logging.info('==========test_ss_pop_menu_shape==========')
        gv = SSView(self.driver)

        gv.create_file('ss')
        gv.group_button_click('插入')
        gv.insert_shape('ss')
        time.sleep(1)
        gv.tap(700, 700)
        gv.pop_menu_click('editText')

        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))

        gv.long_press(700, 700)
        gv.pop_menu_click('selectAll')
        # gv.drag_coordinate(700, 700, 550, 550)
        gv.pop_menu_click('copy')
        gv.tap(700, 700)
        gv.long_press(700, 700)
        gv.pop_menu_click('paste')
        gv.long_press(700, 700)
        gv.pop_menu_click('selectAll')
        # gv.drag_coordinate(700, 700, 550, 550)
        gv.pop_menu_click('cut')
        # gv.tap(700, 700)
        # time.sleep(1)
        gv.long_press(700, 700)
        gv.pop_menu_click('paste')
        # gv.drag_coordinate(700, 700, 550, 550)
        gv.long_press(700, 700)
        gv.pop_menu_click('selectAll')
        gv.pop_menu_click('delete')

    @unittest.skip('skip test_ss_pop_menu_shape1')
    def test_ss_pop_menu_shape1(self):
        logging.info('==========test_ss_pop_menu_shape1==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        time.sleep(1)
        ss.group_button_click('插入')
        ss.insert_shape('ss')

        ss.fold_expand()
        x1, y1 = ss.find_pic_position('drag_all')
        ss.drag_coordinate(x1, y1, x1 - 100, y1)

        x1, y1 = ss.find_pic_position('drag_all')
        ss.drag_coordinate(x1, y1, x1 + 100, y1)

        x1, y1 = ss.find_pic_position('drag_all')
        ss.drag_coordinate(x1, y1, x1 - 50, y1 - 50)

        x2, y2 = ss.find_pic_position('drag_all1')
        ss.drag_coordinate(x2, y2, x2, y2 - 100)

        x2, y2 = ss.find_pic_position('drag_all1')
        ss.drag_coordinate(x2, y2, x2, y2 + 100)

        x2, y2 = ss.find_pic_position('drag_all1')
        ss.drag_coordinate(x2, y2, x2 - 50, y2 - 50)

        x, y = ss.find_pic_position('rotate_free')
        ss.drag_coordinate(x, y, x + 50, y + 50)

    @unittest.skip('skip test_ss_insert_shape')
    def test_ss_insert_shape(self):
        logging.info('==========test_ss_insert_shape==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.group_button_click('插入')
        ss.insert_shape('ss')
        for i in range(5):
            ss.shape_insert('ss', 6, random.randint(1, 42))
        time.sleep(3)

    @unittest.skip('skip test_ss_insert_chart')
    def test_ss_insert_chart(self):  # 插入图表
        logging.info('==========test_ss_insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图',
                      '圆锥图', '棱锥图']
        ss = SSView(self.driver)
        ss.create_file('ss')

        time.sleep(1)
        x, y, width, height = ss.cell_location()
        for i in range(3):
            ss.tap(x + width * 0.5, y + height * (i + 0.5))
            ss.cell_edit()  # 双击进入编辑
            self.driver.press_keycode(random.randint(7, 16))
        ss.drag_coordinate(x, y + height * 2, x, y)

        for i in range(12):
            time.sleep(1)
            ss.group_button_click('插入')
            ss.insert_chart_insert(chart_list[i], random.randint(1, 9))
            ss.chart_template()
        time.sleep(1)

    @unittest.skip('skip test_ss_insert_chart1')
    def test_ss_insert_chart1(self):
        logging.info('==========test_ss_insert_chart1==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        time.sleep(1)
        x, y, width, height = ss.cell_location()
        for i in range(3):
            ss.tap(x + width * 0.5, y + height * (i + 0.5))
            ss.cell_edit()  # 双击进入编辑
            self.driver.press_keycode(random.randint(7, 16))
        ss.drag_coordinate(x, y + height * 2, x, y)

        ss.group_button_click('插入')
        ss.insert_chart_insert('柱形图', random.randint(1, 9))
        ss.chart_color(random.randint(1, 8))
        ss.chart_element('ss', ('大标题', 1), 2, 1)
        ss.chart_element_XY('x', 'xAxis', 0, 0, 0)
        ss.chart_element_XY('y', 'yAxis', 1, 1, 1, (1, 1))
        # gv.chart_element_XY('y', 'y', 0, 1, 1, 0, 1, 0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        ss.change_row_column()
        time.sleep(3)

    @unittest.skip('skip test_ss_expand_fold')
    def test_ss_expand_fold(self):  # 编辑栏收起展开
        logging.info('==========test_ss_expand_fold==========')
        ss = SSView(self.driver)

        file_name = '欢迎使用永中Office.xlsx'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.fold_expand()
        ss.fold_expand()

    @unittest.skip('skip test_ss_create_file')
    def test_ss_create_file(self):  # 新建文档
        logging.info('==========test_ss_create_file==========')
        hp = SSView(self.driver)
        hp.create_file('ss')
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict['ss'])

    # =======add 2020_01_03=====
    @unittest.skip('skip test_ss_print')
    @data(*print_ways)
    def test_ss_print(self, print_way='current_table'):
        logging.info('==========test_ss_print==========')
        ss = SSView(self.driver)
        search_result = ss.search_file('screen.xls')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = ss.open_file('screen.xls')
        self.assertEqual(open_result, True, '打开失败')
        ss.fold_expand()
        ss.swipe_options()

        logging.info('==========打印==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_print').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s' % print_way).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_middle_ok').click()
        self.assertTrue(ss.get_element_result('//*[@text="正在获取准备打印的文件"]'))

    @unittest.skip('skip test_ss_export_each_page_share')
    @data(*index_share_list2)
    def test_ss_export_each_page_share(self, share_way='email'):
        logging.info('==========test_ss_export_each_page_share==========')
        ss = SSView(self.driver)
        search_result = ss.search_file('screen.xls')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = ss.open_file('screen.xls')
        self.assertEqual(open_result, True, '打开失败')
        ss.fold_expand()
        ss.swipe_options()

        logging.info('==========逐页输出图片==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_export_image_by_page').click()
        self.assertTrue(ss.get_toast_message('图片预览加载中') == True, 'toast1 未捕捉到')
        time.sleep(1)
        self.assertTrue(ss.is_not_visible('//*[@text="已全部加载完"]') == True, 'toast2 未捕捉到')

        logging.info('==========选择==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range').click()
        edit_zone = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_frame_table_container')
        table = edit_zone.find_element(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup').get_attribute(
            'bounds')
        print(f'table:{table}')
        loc = table[1:-1].split('][')
        loca_list = list(map(lambda a: eval(a), loc))
        ss.tap(loca_list[0][0], loca_list[0][1])
        ss.drag_coordinate(loca_list[0][0], loca_list[0][1], loca_list[1][0] - 20, loca_list[1][1] - 10)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range_make_page_ok').click()

        logging.info('==========分享==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/rll_export_ss_long_picture_share_layout').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ss_rl_longPic_share_%s' % share_way).click()

        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_ss_export_each_page_save')
    def test_ss_export_each_page_save(self):
        logging.info('==========test_ss_export_each_page_save==========')
        ss = SSView(self.driver)
        search_result = ss.search_file('screen.xls')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = ss.open_file('screen.xls')
        self.assertEqual(open_result, True, '打开失败')
        ss.fold_expand()
        ss.swipe_options()

        logging.info('==========逐页输出图片==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_export_image_by_page').click()
        self.assertTrue(ss.get_toast_message('图片预览加载中') == True, 'toast1 未捕捉到')
        time.sleep(1)
        self.assertTrue(ss.is_not_visible('//*[@text="已全部加载完"]') == True, 'toast2 未捕捉到')

        logging.info('==========选中、取消选中==========')
        select_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_pic_checkbox')
        select_ele.click()
        self.assertTrue(select_ele.get_attribute('checked') == 'false', '取消选中失败')
        select_ele.click()
        self.assertTrue(select_ele.get_attribute('checked') == 'true', '选中失败')

        logging.info('==========选择==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range').click()
        edit_zone = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_frame_table_container')
        table = edit_zone.find_element(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup').get_attribute(
            'bounds')
        print(f'table:{table}')
        loc = table[1:-1].split('][')
        loca_list = list(map(lambda a: eval(a), loc))
        ss.tap(loca_list[0][0], loca_list[0][1])
        ss.drag_coordinate(loca_list[0][0], loca_list[0][1], loca_list[1][0] - 20, loca_list[1][1] - 10)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range_make_page_ok').click()

        logging.info('==========保存到相册==========')
        ss.is_not_visible('//*[@resource-id="图片预览加载中"]')
        ss.is_not_visible('//*[@resource-id="已全部加载完"]')
        self.driver.find_element(By.ID, 'com.yozo.office:id/rll_export_ss_long_picture_save_layout').click()
        self.assertTrue(ss.get_toast_message('已保存到/storage/emulated/0/Pictures') == True, 'toast 未捕捉到')

    @unittest.skip('skip test_ss_export_long_picture_share')
    @data(*index_share_list2)
    def test_ss_export_long_picture_share(self, share_way):
        logging.info('==========test_ss_export_long_picture_share==========')
        ss = SSView(self.driver)
        search_result = ss.search_file('screen.xls')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = ss.open_file('screen.xls')
        self.assertEqual(open_result, True, '打开失败')
        ss.fold_expand()
        ss.swipe_options()

        logging.info('==========输出长图==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_export_long_picture').click()
        self.assertTrue(ss.get_toast_message('图片预览加载中') == True, 'toast1 未捕捉到')
        time.sleep(1)
        # self.assertTrue(ss.get_toast_message('已全部加载完') == True, 'toast2 未捕捉到')

        logging.info('==========选择==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range').click()
        edit_zone = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_frame_table_container')
        table = edit_zone.find_element(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup').get_attribute(
            'bounds')
        print(f'table:{table}')
        loc = table[1:-1].split('][')
        loca_list = list(map(lambda a: eval(a), loc))
        ss.tap(loca_list[0][0], loca_list[0][1])
        ss.drag_coordinate(loca_list[0][0], loca_list[0][1], loca_list[1][0] - 20, loca_list[1][1] - 10)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range_make_page_ok').click()

        logging.info('==========分享==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/rll_export_ss_long_picture_share_layout').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ss_rl_longPic_share_%s' % share_way).click()

        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_ss_export_long_picture')
    def test_ss_export_long_picture_save(self):
        logging.info('==========test_ss_export_long_picture==========')
        ss = SSView(self.driver)
        search_result = ss.search_file('screen.xls')
        self.assertTrue(search_result == True, '搜索失败')
        open_result = ss.open_file('screen.xls')
        self.assertEqual(open_result, True, '打开失败')
        ss.fold_expand()
        ss.swipe_options()

        logging.info('==========输出长图==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_export_long_picture').click()
        self.assertTrue(ss.get_toast_message('图片预览加载中') == True, 'toast1 未捕捉到')
        time.sleep(1)
        # self.assertTrue(ss.get_toast_message('已全部加载完') == True, 'toast2 未捕捉到')

        logging.info('==========选择==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range').click()
        edit_zone = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_frame_table_container')
        table = edit_zone.find_element(By.XPATH, '//android.view.ViewGroup/android.view.ViewGroup').get_attribute(
            'bounds')
        print(f'table:{table}')
        loc = table[1:-1].split('][')
        loca_list = list(map(lambda a: eval(a), loc))
        ss.tap(loca_list[0][0], loca_list[0][1])
        ss.drag_coordinate(loca_list[0][0], loca_list[0][1], loca_list[1][0] - 20, loca_list[1][1] - 10)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_select_range_make_page_ok').click()

        logging.info('==========保存到相册==========')
        ss.is_not_visible('//*[@resource-id="图片预览加载中"]')
        ss.is_not_visible('//*[@resource-id="已全部加载完"]')
        self.driver.find_element(By.ID, 'com.yozo.office:id/rll_export_ss_long_picture_save_layout').click()
        self.assertTrue(ss.get_toast_message('已保存到/storage/emulated/0/Pictures') == True, 'toast 未捕捉到')

    # =======before 2019_12_31=====
    @unittest.skip('skip test_ss_cell_border')
    def test_ss_cell_border(self):  # 遍历边框所有功能
        logging.info('==========test_ss_cell_border==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.group_button_click('编辑')
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.cell_border()

    @unittest.skip('skip test_ss_cell_edit')
    def test_ss_cell_edit(self):
        logging.info('==========test_ss_cell_edit==========')
        ss = SSView(self.driver)
        ss.create_file('ss')
        ss.cell_edit()

        ss.group_button_click('编辑')
        type = 'ss'
        ss.font_name(type)
        ss.font_size(23)
        ss.font_style(type, '加粗')
        ss.font_style(type, '倾斜')
        ss.font_style(type, '删除线')
        ss.font_style(type, '下划线')
        ss.font_color(type)

        for i in range(5):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    @unittest.skip('skip test_ss_cell_options')
    def test_ss_cell_options(self):  # 插入删除行宽列高清除
        logging.info('==========test_ss_cell_options==========')
        ss = SSView(self.driver)
        type = 'ss'
        ss.create_file('ss')
        ss.cell_edit()
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss.group_button_click('编辑')
        ss.font_style(type, '删除线')

        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')

        ss.cell_insert('右移')
        ss.cell_insert('下移')
        ss.cell_insert('插入整行')
        ss.cell_insert('插入整列')
        ss.cell_delete('删除整列')
        ss.cell_delete('删除整行')
        ss.cell_delete('上移')
        ss.cell_delete('左移')

        ss.cell_clear('清除格式')
        ss.undo_option()
        ss.cell_clear('清除内容')
        ss.undo_option()
        ss.cell_clear('清除所有')
        ss.undo_option()

        ss.swipe_options(ele, 'up')
        ss.cell_set_size(5, 5)
        ss.group_button_click('编辑')

        ss.swipe_options(ele, 'down')
        ss.cell_fit_height()
        ss.cell_fit_width()
        time.sleep(1)

    @unittest.skip('skip test_ss_cell_pop_menu')
    def test_ss_cell_pop_menu(self):
        logging.info('==========test_ss_cell_pop_menu==========')
        ss = SSView(self.driver)
        type = 'ss'
        ss.create_file(type)

        ss.cell_edit()  # 进入编辑
        x, y, width, height = ss.cell_location()  # 新建默认A1
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('edit')
        self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('copy')
        ss.tap(x + width * 0.5, y + height * 1.5)
        ss.tap(x + width * 0.5, y + height * 1.5)
        ss.pop_menu_click('paste')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('cut')
        ss.tap(x + width * 0.5, y + height * 2.5)
        ss.tap(x + width * 0.5, y + height * 2.5)
        ss.pop_menu_click('paste')
        ss.tap(x + width * 0.5, y + height * 2.5)
        ss.pop_menu_click('fill_data')
        x1, y1 = ss.find_pic_position('fill_down')
        ss.drag_coordinate(x1, y1, x1, y1 + height * 2)
        ss.tap(x + width * 0.5, y + height * 2.5)
        ss.tap(x + width * 0.5, y + height * 2.5)
        time.sleep(1)
        x2, y2 = ss.find_pic_position('cut')
        print(f'x2,y2:{x2, y2}')
        ss.swipe(x2, y2, x2 - width, y2)
        ss.pop_menu_click('clear_content')

    @unittest.skip('skip test_ss_cell_pop_menu_text')
    def test_ss_cell_pop_menu_text(self):
        logging.info('==========test_ss_cell_pop_menu_text==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.cell_edit()  # 进入编辑
        x, y, width, height = ss.cell_location()
        for i in range(10):
            self.driver.press_keycode(random.randint(29, 54))
        ss.long_press(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('copy')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('paste')
        ss.drag_coordinate(x + width * 0.5, y + height * 0.5, x + width * 0.1, y + height * 0.5)
        ss.pop_menu_click('cut')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('paste')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('selectAll')
        ss.pop_menu_click('cut')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('paste')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('newline')
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    @unittest.skip('skip test_ss_cell_select')
    def test_ss_cell_select(self):
        logging.info('==========test_ss_cell_select==========')

        ss = SSView(self.driver)
        ss.create_file('ss')
        ss.cell_edit()
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.group_button_click('编辑')
        type = 'ss'

        ss.font_name(type)
        ss.font_size(23)
        ss.font_style(type, '加粗')
        ss.font_style(type, '倾斜')
        ss.font_style(type, '删除线')
        ss.font_style(type, '下划线')
        ss.font_color(type)

        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.cell_color()
        ss.cell_align('水平居中', '下对齐')

    @unittest.skip('skip test_ss_cells_select')
    def test_ss_cells_select(self):
        logging.info('==========test_ss_cells_select==========')
        ss = SSView(self.driver)
        ss.create_file('ss')
        ss.cell_edit()  # 进入编
        x, y, width, height = ss.cell_location()  # A1
        ss.tap(x + width * 1.5, y + height * 1.5)
        time.sleep(1)
        ss.drag_coordinate(x + width * 2, y + height * 2, x + width * 3, y + height * 3)
        ss.tap(x - 10, y - 10)

    @unittest.skip('skip test_ss_chart_pop')
    def test_ss_chart_pop(self):  # 图表相关操作
        logging.info('==========test_ss_chart_pop==========')
        ss = SSView(self.driver)
        ss.create_file('ss')
        x, y, width, height = ss.cell_location()
        for i in range(3):
            ss.tap(x + width * 0.5, y + height * (0.5 + i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.swipe(x + width, y + height, x + width, y + height * 3)
        ss.group_button_click('插入')
        ss.insert_chart_insert('柱形图', 2)
        ss.fold_expand()
        time.sleep(1)

        x1, y1 = ss.find_pic_position('chart_title')
        ss.tap(x1, y1)
        ss.pop_menu_click('cut')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('paste')
        # x1, y1 = ss.find_pic_position('chart_title')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('copy')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.pop_menu_click('paste')
        # x1, y1 = ss.find_pic_position('chart_title')
        ss.swipe(x + width * 0.5, y + height * 0.5, x1 + 100, y1 + 100)
        x1, y1 = ss.find_pic_position('chart_all1')
        ss.swipe(x1, y1, x1 + 10, y1 + 10)

    @unittest.skip('skip test_ss_column_options')
    def test_ss_column_options(self):
        logging.info('==========test_ss_column_options==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.cell_edit()  # 进入编辑
        x, y, width, height = ss.cell_location()
        for i in range(10):
            self.driver.press_keycode(36)
        ss.tap(x + width * 0.5, y - 10)
        x1, y1 = ss.find_pic_position('drag_column_right')  # 选择多列
        ss.swipe(x1, y1, x1 + width * 2, y1)
        ss.tap(x + width * 0.5, y - 10)
        ss.swipe(x + width, y - 10, x + width * 2, y - 10)
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        ss.pop_menu_click('fit_column_width')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        ss.pop_menu_click('insert')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        ss.pop_menu_click('delete')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        ss.pop_menu_click('cut')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        x2, y2 = ss.find_pic_position('cut')
        ss.swipe(x2, y2, x2 - width * 2, y2)
        ss.pop_menu_click('paste')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        ss.pop_menu_click('copy')
        ss.tap(x + width * 1.5, y - 10)  # 选择单列
        ss.pop_menu_click('paste')
        ss.tap(x + width * 1.5, y - 10)  # 选择单列
        ss.pop_menu_click('clear_content')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        x3, y3 = ss.find_pic_position('hide')
        ss.pop_menu_click('hide')
        ss.tap(x + width * 0.5, y - 10)  # 选择单列
        ss.swipe(x3, y3, x3 - width, y3)
        ss.pop_menu_click('hide_cancel')

    @unittest.skip('skip test_ss_data_table')
    def test_ss_data_table(self):  # 数据排序，工作表格式
        logging.info('==========test_ss_data_table==========')
        ss = SSView(self.driver)
        ss.create_file('ss')
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        for i in range(7):
            ss.tap(x + width * 0.5, y + height * (0.5 + i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))
        ss.group_button_click('查看')
        ss.data_sort('降序')
        ss.data_sort('升序')
        ss.sheet_style('隐藏编辑栏')
        ss.sheet_style('隐藏编辑栏')
        ele = '//android.widget.ScrollView'
        ss.swipe_options(ele, 'up')
        ss.sheet_style('隐藏表头')
        ss.sheet_style('隐藏表头')
        ss.sheet_style('隐藏网格线')
        ss.sheet_style('隐藏网格线')
        ss.sheet_style('冻结窗格')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_freeze_current').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_freeze_row').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_freeze_column').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        ss.sheet_style('取消冻结')
        ss.sheet_style('100%')

    @unittest.skip('skip test_ss_edit_area_fling')
    def test_ss_edit_area_fling(self):
        logging.info('==========test_ss_edit_area_fling==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ele = '//*[@resource-id="com.yozo.office:id/yozo_ss_frame_table_container"]'
        ss.swipe_options(ele=ele, option='up')
        ss.swipe_options(ele=ele, option='down')
        ss.swipe_options(ele=ele, option='left')
        ss.swipe_options(ele=ele, option='right')

    @unittest.skip('skip test_ss_worksheet_hide_show')
    def test_ss_edit_bar_expand_fold(self):
        logging.info('==========test_ss_edit_bar_expand_fold==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_ss_formula_drop_down').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_ss_formula_drop_down').click()

    @unittest.skip('skip test_ss_filter1')
    def test_ss_filter1(self):
        logging.info('==========test_ss_filter1==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        tip = self.driver.find_element(By.ID, 'com.yozo.office:id/text_content')
        self.assertTrue(tip != None)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_right').click()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        state = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_checkbox_switch').text
        self.assertTrue(state == '开启')
        ss.tap(x - width - 10, y - height * 3 - 10)
        self.assertTrue(self.driver.find_element_by_id('com.yozo.office:id/tv_ss_filter_complete'))
        self.assertTrue(self.driver.find_element_by_id('com.yozo.office:id/tv_ss_filter_cancel'))
        self.assertTrue(self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_asc'))
        self.assertTrue(self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_desc'))
        self.assertTrue(self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_customize'))
        self.assertTrue(self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_clean'))

    @unittest.skip('skip test_ss_filter2')
    def test_ss_filter2(self):
        logging.info('==========test_ss_filter2==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - width - 18
        y1 = y - height * 3 - 27
        ss.tap(x1, y1)
        self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_asc').click()
        ss.tap(x1, y1)
        self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_desc').click()
        ss.tap(x1, y1)
        self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_clean').click()
        self.driver.find_element_by_id('com.yozo.office:id/tv_ss_filter_complete').click()
        ss.tap(x1, y1)
        self.driver.find_element_by_id('com.yozo.office:id/tv_ss_filter_cancel').click()
        ss.tap(x1, y1)
        self.driver.find_element_by_id('com.yozo.office:id/tv_ss_filter_select_all').click()
        self.driver.find_element_by_id('com.yozo.office:id/iv_ss_filter_select').click()
        self.driver.find_element_by_id('com.yozo.office:id/tv_ss_filter_select_all').click()
        self.driver.find_element_by_id('com.yozo.office:id/ll_ss_filter_customize').click()
        self.driver.find_element_by_id('com.yozo.office:id/iv_ss_customize_back').click()

    @unittest.skip('skip test_ss_filter_by_color')
    def test_ss_filter_by_color(self):
        logging.info('==========test_ss_filter_cd1_none==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - width - 18
        y1 = y - height * 3 - 27
        ss.tap(x1, y1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_ss_filter_customize').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filter_color_type').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="字体颜色"]').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout')
        eles[random.randint(0, len(eles) - 1)].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_filter_ok').click()
        ss.tap(x1, y1, 2)
        self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filter_color_type').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="单元格颜色"]').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout')
        eles[random.randint(0, len(eles) - 1)].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_filter_ok').click()

    @unittest.skip('skip test_ss_filter_by_date')
    def test_ss_filter_by_date(self):
        logging.info('==========test_ss_filter_by_date==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - width - 18
        y1 = y - height * 3 - 27
        ss.filter_data(x1, y1, '自定义', date_filter[random.randint(0, 11)], date_filter[random.randint(0, 11)])

        # ss.filter_data(x1, y1, '自定义', '等于', '等于')
        # ss.tap(x1, y1)
        # ss.filter_data(x1, y1, '自定义', '等于', '不等于')

        # for cd1 in date_filter:
        #     for cd2 in date_filter:
        #         time.sleep(1)
        #         if cd2 != '等于' and cd1 != '等于':
        #             ss.tap(x1, y1,3)
        #         ss.filter_data(x1, y1, '自定义', cd1, cd2)

    @unittest.skip('skip test_ss_filter_by_num')
    def test_ss_filter_by_num(self):
        logging.info('==========test_ss_filter_by_num==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - 18
        y1 = y - height * 3 - 27
        ss.filter_data(x1, y1, '自定义', num_filter[random.randint(1, 12)], num_filter[random.randint(1, 12)])

    @unittest.skip('skip test_ss_filter_by_num_shortcut')
    def test_ss_filter_by_num_shortcut(self):
        logging.info('==========test_ss_filter_by_num_shortcut==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        time.sleep(1)
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - 18
        y1 = y - height * 3 - 27
        ss.tap(x1, y1)
        self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="前十项"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ok').click()
        ss.tap(x1, y1, 2)  # 非初次需要点两次
        self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="高于平均值"]').click()
        ss.tap(x1, y1, 2)
        self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="低于平均值"]').click()

    @unittest.skip('skip test_ss_filter_by_text')
    def test_ss_filter_by_text(self):
        logging.info('==========test_ss_filter_by_text==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x + width - 18
        y1 = y - height * 3 - 27
        ss.filter_data(x1, y1, '自定义', text_filter[random.randint(1, 12)], text_filter[random.randint(1, 12)])

    @unittest.skip('skip test_ss_filter_cd1_none')
    def test_ss_filter_cd1_none(self):
        logging.info('==========test_ss_filter_cd1_none==========')
        ss = SSView(self.driver)
        file_name = 'screen.xls'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        for i in range(3):
            x1 = x - width * (1 - i) - 18
            y1 = y - height * 3 - 27
            ss.tap(x1, y1)
            self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filter_condition1').click()
            self.driver.find_element(By.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_filter_ok').click()
            self.assertTrue(ss.get_toast_message('第一个条件不能为空'))
            self.driver.find_element(By.ID, 'com.yozo.office:id/iv_ss_customize_back').click()

    @unittest.skip('skip test_ss_formula_auto_sum')
    def test_ss_formula_auto_sum(self):
        logging.info('==========test_ss_formula_auto_sum==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.cell_edit()
        x, y, width, height = ss.cell_location()  # cell A1
        for i in range(5):
            ss.tap(x + width * 0.5, y + height * (0.5 + i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))

        auto_sum = ['求和', '平均值', '计数', '最大值', '最小值']
        for i, value in enumerate(auto_sum):
            ss.tap(x + width * 2.5, y + height * (0.5 + i))  # 求和
            ss.auto_sum(auto_sum[i])
            ss.tap(x + width * 0.5, y + height * 0.5)
            ss.drag_coordinate(x + width, y + height, x + width, y + height * 5)
            self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    @unittest.skip('skip test_ss_formula_all')
    def test_ss_formula_for_all(self):  # 其他类型公式
        logging.info('==========test_ss_formula_all==========')

        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.zoom_out()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()  # cell A1
        for i in range(11):
            ss.tap(x + width * 0.5, y + height * (0.5 + i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))

        ss.tap(x + width * 2.5, y + height * 0.5)
        ss.formula_all('最近使用', 'MAX')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.tap(x + width * 0.5, y + height * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 1.5)
        ss.formula_all('数学和三角', 'ABS')
        ss.tap(x + width * 0.5, y + height * 1.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 2.5)
        ss.formula_all('财务', 'DOLLARDE')
        ss.tap(x + width * 0.5, y + height * 2.5)
        ss.tap(x + width * 0.5, y + height * 3.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 3.5)
        ss.formula_all('逻辑', 'AND')
        ss.tap(x + width * 0.5, y + height * 3.5)
        ss.tap(x + width * 0.5, y + height * 4.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 4.5)
        ss.formula_all('文本', 'ASC')
        ss.tap(x + width * 0.5, y + height * 4.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 5.5)
        ss.formula_all('日期和时间', 'NOW')
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 6.5)
        ss.formula_all('查找与引用', 'COLUMN')
        ss.tap(x + width * 0.5, y + height * 6.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 7.5)
        ss.formula_all('统计', 'AVERAGE')
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.tap(x + width * 0.5, y + height * 1.5)
        ss.tap(x + width * 0.5, y + height * 2.5)
        ss.tap(x + width * 0.5, y + height * 3.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 8.5)
        ss.formula_all('工程', 'HEX2BIN')
        ss.tap(x + width * 0.5, y + height * 8.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 9.5)
        ss.formula_all('信息', 'ISBLANK')
        ss.tap(x + width * 0.5, y + height * 9.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.tap(x + width * 2.5, y + height * 10.5)
        ss.formula_all('所有公式', 'ABS')
        ss.tap(x + width * 0.5, y + height * 10.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    @unittest.skip('skip test_ss_merge_wrap')
    def test_ss_merge_wrap(self):
        logging.info('==========test_ss_merge_wrap==========')

        ss = SSView(self.driver)
        ss.create_file('ss')
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.cell_edit()
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss.drag_coordinate(x + width, y + height, x + width, y + height * 3)

        ss.group_button_click('编辑')
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.cell_merge_split()
        ss.cell_merge_split()
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.cell_auto_wrap()
        ss.cell_auto_wrap()

    @unittest.skip('skip test_num_style')
    def test_ss_num_format(self):
        logging.info('==========test_num_style==========')
        ss = SSView(self.driver)
        ss.create_file('ss')
        ss.cell_edit()
        self.driver.press_keycode(15)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

        ss.group_button_click('编辑')
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.cell_num_format()

    @unittest.skip('skip test_ss_row_options')
    def test_ss_row_options(self):
        logging.info('==========test_ss_row_options==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.cell_edit()  # 进入编辑
        x, y, width, height = ss.cell_location()
        self.driver.press_keycode(36)
        ss.tap(x - 10, y + height * 0.5)
        x1, y1 = ss.find_pic_position('drag_row_down')  # 选择多行
        ss.swipe(x1, y1, x1, y1 + height * 3)
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.swipe(x - 10, y + height, x - 10, y + height * 2)
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.pop_menu_click('fit_row_height')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.pop_menu_click('insert')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.pop_menu_click('delete')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.pop_menu_click('cut')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        x2, y2 = ss.find_pic_position('cut')
        ss.swipe(x2, y2, x2 - width * 2, y2)
        ss.pop_menu_click('paste')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.pop_menu_click('copy')
        ss.tap(x - 10, y + height * 1.5)  # 选择单行
        ss.pop_menu_click('paste')
        ss.tap(x - 10, y + height * 1.5)  # 选择单行
        ss.pop_menu_click('clear_content')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        x3, y3 = ss.find_pic_position('hide')
        ss.pop_menu_click('hide')
        ss.tap(x - 10, y + height * 0.5)  # 选择单行
        ss.swipe(x3, y3, x3 - width, y3)
        ss.pop_menu_click('hide_cancel')

    @unittest.skip('skip test_ss_show_file_info')
    def test_ss_show_file_info(self):
        logging.info('==========test_ss_show_file_info==========')
        ss = SSView(self.driver)
        file_name = '欢迎使用永中Office.xlsx'
        search_result = ss.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = ss.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        ss.file_info()
        self.assertTrue(ss.check_file_info())

    @unittest.skip('skip test_ss_worksheet_hide_show')
    def test_ss_worksheet_hide_show(self):
        logging.info('==========test_ss_worksheet_hide_show==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_ss_sheet_tabbar').click()
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_more'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_back').click()
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_ss_sheet_tabbar'))

    @unittest.skip('skip test_ss_worksheet_options')
    def test_ss_worksheet_options(self):
        logging.info('==========test_ss_worksheet_options==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.show_sheet()
        ss.add_sheet()
        result = ss.rename_sheet(3, 'rename_test')
        self.assertTrue(result == True)
        ss.operate_sheet(3, 'remove')
        ss.operate_sheet(2, 'insert')
        self.assertTrue(ss.get_element_result('//*[@text="工作表5"]'))
        ss.operate_sheet(2, 'remove')
        ss.operate_sheet(2, 'copy')
        self.assertTrue(ss.get_element_result('//*[@text="工作表3(2)"]'))
        ss.operate_sheet(2, 'hide')
        self.assertFalse(ss.get_element_result('//*[@text="工作表3(2)"]'))
        ss.operate_sheet(2, 'unhide')
        self.assertTrue(ss.get_element_result('//*[@text="工作表3(2)"]'))
        ele1 = self.driver.find_element(By.XPATH, '//*[@text="工作表1"]')
        ele2 = self.driver.find_element(By.XPATH, '//*[@text="工作表3"]')
        ss.drag_element(ele1, ele2)

    @unittest.skip('skip test_ss_table_style')
    def test_ss_table_style(self):  # 表格样式
        logging.info('==========test_ss_table_style==========')
        ss = SSView(self.driver)
        ss.create_file('ss')

        ss.cell_edit()  # 进入编辑
        x, y, width, height = ss.cell_location()
        ss.tap(x + width * 1.5, y + height * 1.5)
        ss.drag_coordinate(x + width * 2, y + height * 2, x + width * 3, y + height * 4)
        ss.group_button_click('编辑')
        ss.swipe_options()
        ss.swipe_options()
        ss.swipe_options()
        ss.swipe_options()
        ss.swipe_options()
        ss.table_style()
