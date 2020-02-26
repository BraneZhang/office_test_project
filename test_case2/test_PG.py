#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import random
import time
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from businessView.generalFunctionView import GeneralFunctionView
from businessView.homePageView import HomePageView
from businessView.pgView import PGView
from common.myunit import StartEnd
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import selenium.webdriver.support.expected_conditions as ec

from data import data_info
from data.data_info import share_list1, search_dict

switch_list = data_info.switch_list

ss_file = '../screenshots/'


@ddt
class TestPG(StartEnd):
    # =======add 2020_02_25===== 拆分共用功能
    @unittest.skip('skip test_pg_file_info')
    def test_pg_file_info(self, file_type='pg'):
        """
        文档信息
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_pg_file_info==========')
        gv = PGView(self.driver)
        gv.open_random_file(search_dict[file_type])

        logging.info('==========show file info==========')
        gv.wait_loading()
        gv.file_info()

    @unittest.skip('skip test_pg_share_editFile')
    @data(*share_list1)
    def test_pg_share_editFile(self, share_info):
        """
        编辑文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_pg_share_editFile==========')
        wp = PGView(self.driver)
        file_type = 'wp'

        logging.info('==========edit and save File==========')
        wp.open_random_file(search_dict[file_type])
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
        wp.group_button_click('插入')
        wp.insert_shape(file_type, 1)
        wp.save_file()
        self.assertTrue(wp.get_toast_message('保存成功'))

        logging.info('==========share new File==========')
        wp.share_file(file_type, share_info)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_pg_close_file')
    def test_pg_close_file(self, file_type='pg'):
        """
        关闭功能（X）
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_pg_close_file==========')
        hp = HomePageView(self.driver)
        isOpen = hp.open_random_file(search_dict[file_type])
        self.assertTrue(isOpen, 'open fail')
        hp.close_file()
        self.assertTrue(hp.check_close_file())

    @unittest.skip('skip test_pg_save_newFile')
    def test_pg_save_newFile(self, type='pg'):  # 新建脚本保存
        logging.info('==========test_pg_save_newFile==========')
        hp = PGView(self.driver)
        hp.create_file(type)
        file_name = 'save_new ' + hp.getTime('%Y-%m-%d %H-%M-%S')
        hp.save_new_file(file_name, 'local', 2)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_pg_save_existFile')
    def test_pg_save_existFile(self, type='pg'):  # 已有文件改动保存
        logging.info('==========test_pg_save_existFile==========')
        gv = PGView(self.driver)

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

    @unittest.skip('skip test_pg_save_as_newFile')
    def test_pg_save_as_newFile(self, type='pg'):  # 新建脚本另存为
        logging.info('==========test_pg_save_as_newFile==========')
        hp = PGView(self.driver)
        hp.create_file(type)
        file_name = 'save_as_new ' + hp.getTime('%H_%M_%S')
        hp.save_as_file(file_name, 'local', 1)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_pg_save_as_existFile')
    def test_pg_save_as_existFile(self, type='pg'):  # 已有文件另存为
        logging.info('==========test_pg_save_as_existFile==========')
        hp = PGView(self.driver)

        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        file_name = '已有文档另存'
        hp.save_as_file(file_name, 'local', 1)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_pg_zoom_pinch')
    def test_pg_zoom_pinch(self, type='ss'):
        logging.info('==========test_pg_zoom_pinch==========')
        hp = PGView(self.driver)
        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        hp.zoom_in()
        hp.zoom_out()

    @unittest.skip('skip test_pg_undo_redo')
    def test_pg_undo_redo(self, type='pg'):  # 撤销、重做
        logging.info('==========test_pg_undo_redo==========')
        gv = PGView(self.driver)
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

    @unittest.skip('skip test_pg_signature')
    def test_pg_signature(self, type='pg'):  # 签批
        logging.info('==========test_pg_signature==========')
        gv = PGView(self.driver)
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

    @unittest.skip('skip test_pg_share_file_edit')
    @data(*share_list1)
    def test_pg_share_file_edit(self, way):
        logging.info('==========test_pg_share_file_edit==========')
        ss = PGView(self.driver)

        type = 'pg'
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

    @unittest.skip('skip test_pg_share_file_create')
    @data(*share_list1)
    def test_pg_share_file_create(self, way):
        logging.info('==========test_pg_share_file_create==========')
        pg = PGView(self.driver)

        type = 'pg'
        pg.create_file(type)
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict[type])
        pg.share_file(type, way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        save_name = pg.getTime("%Y%m%d%H%M%S")
        pg.save_step('local', save_name, 1)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_pg_share_file')
    @data(*share_list1)
    def test_pg_share_file(self, way):  # 分享文件
        logging.info('==========test_pg_share_file==========')
        pg = PGView(self.driver)
        file_type = 'pg'

        suffix = search_dict[file_type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        pg.share_file(file_type, way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_shape_attr')
    def test_shape_attr(self, type='pg'):
        logging.info('==========test_shape_attr==========')
        gv = PGView(self.driver)
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

    @unittest.skip('skip test_shape_attr2')
    def test_shape_attr2(self, file_type='pg'):
        logging.info('==========test_shape_attr2==========')
        gv = PGView(self.driver)
        gv.create_file(file_type)
        gv.group_button_click('插入')
        gv.insert_shape(file_type, 6, 10)
        gv.shape_option(file_type, 2)
        gv.shape_fill_color(file_type, 6, 24)
        gv.shape_fill_color_transparency(5)
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        ele0 = '//*[@text="插入"]'
        gv.swipe_ele(ele0, ele1)
        gv.swipe_ele(ele2, ele1)
        gv.shape_border_color(file_type, 6, 5)
        gv.shape_border_type(file_type, 6, 3)
        gv.shape_border_width(file_type, 6, 5)
        gv.shape_effect_type(file_type, 6, 4, 5)
        time.sleep(1)

    @unittest.skip('skip test_pg_shape_attr1')
    def test_pg_shape_attr1(self, file_type='pg'):  # 文本框字符属性
        logging.info('==========test_pg_shape_attr1==========')
        gv = PGView(self.driver)
        gv.create_file(file_type)
        x1, y1 = 0, 0

        gv.group_button_click('插入')
        gv.insert_shape(file_type)
        time.sleep(1)
        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)  # 进入编辑
        gv.pop_menu_click('editText')


        for i in range(50):
            self.driver.press_keycode(random.randint(7, 16))

        gv.tap(250, 250)
        gv.tap(525, 500)

        gv.shape_option(file_type, 5, width=5, height=5)
        gv.shape_option(file_type, 6, top=0.5, bottom=0.5, left=0.5, right=0.5)
        gv.swipe_options()
        gv.swipe_options()
        gv.swipe_options()
        gv.swipe_options()
        gv.shape_content_align(file_type, '右对齐', '下对齐')
        gv.shape_content_align(file_type)
        gv.shape_content_align(file_type, '水平居中', '垂直居中')

    @unittest.skip('skip test_pg_search_replace')
    def test_pg_search_replace(self):  # 查找替换
        logging.info('==========test_pg_search_replace==========')
        gv = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = gv.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = gv.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        gv.switch_write_read()
        gv.search_content('pg', '的')
        gv.replace_content('得')
        time.sleep(3)
        gv.replace_content('得', 'all')

    @unittest.skip('skip test_pg_scroll_screen')
    def test_pg_scroll_screen(self):  # 滚屏
        logging.info('==========test_pg_scroll_screen==========')
        hp = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        time.sleep(3)
        hp.swipeLeft()
        hp.swipeLeft()
        hp.swipeRight()
        time.sleep(3)

    @unittest.skip('skip test_pg_rotate')
    def test_pg_rotate(self):
        logging.info('==========test_pg_rotate==========')
        hp = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        # gv.screen_rotate('landscape')
        self.assertTrue(hp.check_rotate())
        hp.screen_rotate('portrait')

    @unittest.skip('skip test_pg_read_mode')
    def test_pg_read_mode(self):  # 阅读模式
        logging.info('==========test_pg_read_mode==========')
        pg = PGView(self.driver)

        pg.create_file('pg')
        pg.switch_write_read()
        self.assertTrue(pg.check_write_read())

    @unittest.skip('skip test_pg_pop_menu_shape')
    def test_pg_pop_menu_shape(self):  # pg未好
        logging.info('==========test_pg_pop_menu_shape==========')
        gv = PGView(self.driver)

        gv.create_file('pg')
        gv.group_button_click('插入')
        gv.insert_shape('pg')
        time.sleep(1)
        gv.tap(550, 450)
        gv.pop_menu_click('editText')

        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))

        gv.tap(525, 500)
        gv.long_press(525, 500)
        gv.pop_menu_click('selectAll')
        # gv.drag_coordinate(550, 830, 500, 800)
        gv.pop_menu_click('copy')
        # gv.tap(550, 830)
        # time.sleep(1)
        gv.long_press(525, 500)
        gv.pop_menu_click('paste')
        gv.long_press(525, 500)
        # gv.pop_menu_click('selectAll')
        # gv.drag_coordinate(550, 830, 500, 800)
        gv.pop_menu_click('cut')
        # gv.tap(550, 830)
        # time.sleep(1)
        gv.long_press(525, 500)
        gv.pop_menu_click('paste')
        # gv.drag_coordinate(550, 830, 500, 800)
        gv.long_press(525, 500)
        # gv.pop_menu_click('selectAll')
        gv.pop_menu_click('delete')

    @unittest.skip('skip test_pop_menu_shape1_ws')
    def test_pop_menu_shape1(self):
        logging.info('==========test_pop_menu_shape1_ws==========')
        pg = PGView(self.driver)
        pg.create_file('pg')

        pg.group_button_click('编辑')
        pg.edit_format('空白')

        time.sleep(1)
        pg.group_button_click('插入')
        pg.insert_shape('pg')

        pg.fold_expand()
        x1, y1 = pg.find_pic_position('drag_all')
        pg.drag_coordinate(x1, y1, x1 - 100, y1)

        x1, y1 = pg.find_pic_position('drag_all')
        pg.drag_coordinate(x1, y1, x1 + 100, y1)

        x1, y1 = pg.find_pic_position('drag_all')
        pg.drag_coordinate(x1, y1, x1 - 50, y1 - 50)

        x2, y2 = pg.find_pic_position('drag_all1')
        pg.drag_coordinate(x2, y2, x2, y2 - 100)

        x2, y2 = pg.find_pic_position('drag_all1')
        pg.drag_coordinate(x2, y2, x2, y2 + 100)

        x2, y2 = pg.find_pic_position('drag_all1')
        pg.drag_coordinate(x2, y2, x2 - 50, y2 - 50)

        x, y = pg.find_pic_position('rotate_free')
        pg.drag_coordinate(x, y, x + 50, y + 50)

    @unittest.skip('skip test_pg_insert_shape')
    def test_pg_insert_shape(self):
        logging.info('==========test_pg_insert_shape==========')
        pg = PGView(self.driver)
        pg.create_file('pg')

        pg.group_button_click('插入')
        pg.insert_shape('pg')
        for i in range(5):
            pg.shape_insert('pg', 6, random.randint(1, 42))
        time.sleep(3)

    @unittest.skip('skip test_pg_insert_chart')
    def test_pg_insert_chart(self):  # 插入图表
        logging.info('==========test_pg_insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图',
                      '圆锥图', '棱锥图']
        pg = PGView(self.driver)
        pg.create_file('pg')

        time.sleep(1)
        for i in range(12):
            time.sleep(1)
            pg.group_button_click('插入')
            pg.swipe_options()
            pg.insert_chart_insert(chart_list[i], random.randint(1, 9))
            pg.chart_template()
        time.sleep(1)

    @unittest.skip('skip test_pg_insert_chart1')
    def test_pg_insert_chart1(self):
        logging.info('==========test_pg_insert_chart1==========')
        pg = PGView(self.driver)
        pg.create_file('pg')

        time.sleep(1)
        pg.group_button_click('插入')
        ele1 = '//*[@text="幻灯片"]'
        ele2 = '//*[@text="图片"]'
        pg.swipe_ele(ele2, ele1)
        pg.insert_chart_insert('柱形图', random.randint(1, 9))
        pg.chart_color(random.randint(1, 8))
        pg.chart_element('pg', ('大标题', 1), 2, 1)
        pg.chart_element_XY('x', 'xAxis', 0, 0, 0)
        pg.chart_element_XY('y', 'yAxis', 1, 1, 1, (1, 1))
        # gv.chart_element_XY('y', 'y', 0, 1, 1, 0, 1, 0)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        pg.change_row_column()
        time.sleep(3)

    @unittest.skip('skip test_pg_export_pdf')
    def test_pg_export_pdf(self):  # 导出pdf
        logging.info('==========test_pg_export_pdf==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')

        file_name = '导出PDF '
        pg.export_pdf(file_name, 'local')

        self.assertTrue(pg.check_export_pdf())

    @unittest.skip('skip test_pg_expand_fold')
    def test_pg_expand_fold(self):  # 编辑栏收起展开
        logging.info('==========test_pg_expand_fold==========')
        pg = PGView(self.driver)

        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.apgertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.apgertTrue(open_result, '打开失败')
        pg.switch_write_read()
        pg.fold_expand()
        pg.fold_expand()

    @unittest.skip('skip test_pg_create_file')
    def test_pg_create_file(self):  # 新建文档
        logging.info('==========test_pg_create_file==========')
        hp = PGView(self.driver)
        hp.create_file('pg')
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict['pg'])

    # =======before 2019_12_31=====
    @unittest.skip('skip test_ppt_add_scroll_comment')
    def test_ppt_add_scroll_comment(self):  # ppt缩略图滚屏备注
        logging.info('==========test_ppt_add_scroll_comment==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
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

    @unittest.skip('skip test_ppt_format')
    def test_ppt_format(self):
        logging.info('==========test_ppt_format==========')
        format = ['标题与副标题', '标题', '标题与文本', '标题与两栏文本', '标题与竖排文本-上下', '标题与竖排文本-左右',
                  '空白', '标题与图片', '标题、文本与图片', '标题、图片与文本', '标题、图片与竖排文本', '标题、竖排文本与图片']
        pg = PGView(self.driver)
        pg.create_file('pg')
        pg.group_button_click('编辑')
        for i in format:
            pg.edit_format(i)
        time.sleep(3)

    @unittest.skip('skip test_ppt_slide')
    def test_ppt_slide(self):  # 幻灯片复制、剪切、粘贴
        logging.info('==========test_ppt_slide==========')
        hp = HomePageView(self.driver)
        gv = GeneralFunctionView(self.driver)
        type = 'pg'
        hp.create_file(type)

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

    @unittest.skip('skip test_ppt_template')
    def test_ppt_template(self):
        logging.info('==========test_ppt_template==========')
        pg = PGView(self.driver)
        pg.create_file('pg')
        pg.group_button_click('编辑')
        for i in range(11):
            pg.edit_template(i)
        time.sleep(3)

    @unittest.skip('skip test_shape_text_attr_pg')
    def test_ppt_shape_text_attr(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========test_ppt_shape_text_attr==========')
        type = 'pg'
        pg = PGView(self.driver)
        pg.create_file(type)
        pg.group_button_click('插入')
        pg.insert_shape(type, 1)
        pg.fold_expand()
        pg.pop_menu_click('rotate_free')
        pg.pop_menu_click('editText')
        pg.fold_expand()
        pg.font_name(type, 'AndroidClock')
        pg.font_size(15)
        pg.font_style(type, '倾斜')
        pg.font_color(type, 6, 29)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        time.sleep(1)
        pg.swipe_options()
        # pg.high_light_color(type,6,6)
        pg.bullets_numbers(type, 6, 10)
        pg.text_align(type, '分散对齐')
        pg.text_align(type, '右对齐')
        pg.text_line_space(type, 1.5)
        pg.text_line_space(type, 3)
        pg.text_indent(type, '右缩进')
        pg.text_indent(type, '右缩进')
        pg.text_indent(type, '左缩进')
        time.sleep(3)

    logging.info('==========2019-11-05 add==========')

    @unittest.skip('skip test_ppt_insert_new')
    def test_ppt_insert_new(self):
        logging.info('==========test_ppt_insert_new==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result,'查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        pg.switch_write_read()
        time.sleep(1)

        logging.info('==========save picture to validate==========')
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, "android.view.View")
        pg.screenshot_edit_ppt(ss_file + 'first.png')
        thumbnails_list[1].click()
        pg.screenshot_edit_ppt(ss_file + 'second.png')

        logging.info('==========insert new ppt==========')
        thumbnails_list[0].click()
        pg.add_new()
        pg.screenshot_edit_ppt(ss_file + 'new_ppt.png')

        logging.info('==========validate insert success==========')
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        thumbnails_list[0].click()
        pg.screenshot_edit_ppt(ss_file + 'new_first.png')
        thumbnails_list[1].click()
        pg.screenshot_edit_ppt(ss_file + 'new_second.png')
        thumbnails_list[2].click()
        pg.screenshot_edit_ppt(ss_file + 'new_third.png')

        result1 = pg.compare_pic('first.png', 'new_first.png')
        result2 = pg.compare_pic('new_second.png', 'new_ppt.png')
        result3 = pg.compare_pic('second.png', 'new_third.png')

        self.assertEqual(result1, 0.0)
        self.assertEqual(result2, 0.0)
        self.assertEqual(result3, 0.0)

        logging.info('==========delete pngs==========')
        os.remove(ss_file + 'first.png')
        os.remove(ss_file + 'second.png')
        os.remove(ss_file + 'new_ppt.png')
        os.remove(ss_file + 'new_first.png')
        os.remove(ss_file + 'new_second.png')
        os.remove(ss_file + 'new_third.png')

    @unittest.skip('skip test_ppt_play_to_first')
    @data(*['current', 'first'])
    def test_ppt_play_to_first(self, play_type):
        logging.info('==========test_ppt_play_to_first==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')

        logging.info('==========modify played pages==========')
        pg.switch_write_read()
        time.sleep(1)
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        index = random.randint(1, len(thumbnails_list) - 4)
        thumbnails_list[index].click()

        logging.info('==========play to the first page==========')
        pg.group_button_click('播放')
        pg.play_mode(play_type)
        if play_type == 'first':
            index = 0
        pg.play_to_first(index + 1)

        logging.info('==========validate toast==========')
        self.assertTrue(pg.get_toast_message('已是简报首页'))
        # try:
        #     toast = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_dialog_pgplay_tiptext_id')
        # except NoSuchElementException:
        #     self.assertTrue(False, '未出现弹窗')
        # else:
        #     self.assertEqual(toast.text, '已是简报首页', '验证弹窗信息为已是简报首页')

    @unittest.skip('skip test_ppt_play_to_last')
    @data(*['current', 'first'])
    def test_ppt_play_to_last(self, play_type):
        logging.info('==========test_ppt_play_to_last==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')

        logging.info('==========modify played pages==========')
        pg.switch_write_read()
        time.sleep(1)
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        index = random.randint(1, len(thumbnails_list) - 4)
        thumbnails_list[index].click()

        logging.info('==========play to the last page==========')

        pg.group_button_click('播放')
        pg.play_mode(play_type)
        if play_type == 'first':
            index = 0
        pg.play_to_last(index - 1, len(thumbnails_list))

        logging.info('==========validate toast==========')
        try:
            toast = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_dialog_pgplay_tiptext_id')
        except NoSuchElementException:
            self.assertTrue(False, '未出现弹窗')
        else:
            self.assertEqual(toast.text, '已是简报尾页', '验证弹窗信息为已是简报尾页')

    @unittest.skip('skip test_ppt_autoplay_to_last')
    def test_ppt_autoplay_to_last(self):
        logging.info('==========test_ppt_autoplay_to_last==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')

        logging.info('==========modify played pages==========')
        pg.switch_write_read()
        time.sleep(1)
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        index = random.randint(1, len(thumbnails_list) - 4)
        thumbnails_list[index].click()

        logging.info('==========autoplay to the last page==========')

        pg.group_button_click('播放')
        pg.play_mode('autoplay')

        logging.info('==========validate toast==========')
        try:
            WebDriverWait(self.driver, 120).until(
                ec.visibility_of_element_located((By.ID, 'com.yozo.office:id/yozo_ui_dialog_pgplay_tiptext_id')))
        except TimeoutException:
            self.assertTrue(False, '等待自动播放两分钟，未找到弹窗')
        else:
            toast = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_dialog_pgplay_tiptext_id')
            self.assertEqual(toast.text, '已是简报尾页', '验证弹窗信息为已是简报尾页')

    @unittest.skip('skip test_ppt_play_switch')
    @data(*switch_list)
    def test_ppt_play_switch(self, switch):  # 幻灯片切换
        logging.info('==========test_ppt_play_switch==========')
        pg = PGView(self.driver)
        file_name = '欢迎使用永中Office.pptx'
        search_result = pg.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = pg.open_file(file_name)
        self.assertTrue(open_result, '打开失败')

        pg.switch_write_read()
        pg.group_button_click('切换')
        pg.switch_mode(switch, 'all')
        pg.group_button_click('播放')
        pg.play_mode()
        time.sleep(20)
