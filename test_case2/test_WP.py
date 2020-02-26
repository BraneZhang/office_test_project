#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import random

import unittest
from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from businessView.wpView import WPView
from common.myunit import StartEnd
from airtest.core.api import *

from data import data_info
from data.data_info import share_list1

chart_type = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图', '圆锥图', '棱锥图']
search_dict = data_info.search_dict

@ddt
class TestWP(StartEnd):
    # =======add 2020_02_25===== 拆分共用功能
    @unittest.skip('skip test_wp_file_info')
    def test_wp_file_info(self, file_type='wp'):
        """
        文档信息
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_wp_file_info==========')
        gv = WPView(self.driver)
        gv.open_random_file(search_dict[file_type])

        logging.info('==========show file info==========')
        gv.wait_loading()
        gv.file_info()

    @unittest.skip('skip test_wp_share_editFile')
    @data(*share_list1)
    def test_wp_share_editFile(self, share_info):
        """
        编辑文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_wp_share_editFile==========')
        wp = WPView(self.driver)
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

    @unittest.skip('skip test_share_newFile')
    @data(*share_list1)
    def test_share_newFile(self, share_info):
        """
        新建文档分享
        :param share_info: 分享相关信息，'wp_wx', 'wp_qq', 'wp_ding', 'wp_mail'..
        :return: None
        """
        logging.info('==========test_share_newFile==========')
        hp = WPView(self.driver)
        file_type = 'wp'

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

    @unittest.skip('skip test_wp_close_file')
    def test_wp_close_file(self, file_type='wp'):
        """
        关闭功能（X）
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return: None
        """
        logging.info('==========test_wp_close_file==========')
        hp = HomePageView(self.driver)
        isOpen = hp.open_random_file(search_dict[file_type])
        self.assertTrue(isOpen, 'open fail')
        hp.close_file()
        self.assertTrue(hp.check_close_file())

    @unittest.skip('skip test_wp_save_newFile')
    def test_wp_save_newFile(self, type='wp'):  # 新建脚本保存
        logging.info('==========test_wp_save_newFile==========')
        hp = WPView(self.driver)
        hp.create_file(type)
        file_name = 'save_new ' + hp.getTime('%Y-%m-%d %H-%M-%S')
        hp.save_new_file(file_name, 'local', 2)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_wp_save_existFile')
    def test_wp_save_existFile(self, type='wp'):  # 已有文件改动保存
        logging.info('==========test_wp_save_existFile==========')
        gv = WPView(self.driver)

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

    @unittest.skip('skip test_wp_save_as_newFile')
    def test_wp_save_as_newFile(self, type='wp'):  # 新建脚本另存为
        logging.info('==========test_wp_save_as_newFile==========')
        hp = WPView(self.driver)
        hp.create_file(type)
        file_name = 'save_as_new ' + hp.getTime('%H_%M_%S')
        hp.save_as_file(file_name, 'local', 1)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_wp_save_as_existFile')
    def test_wp_save_as_existFile(self, type='wp'):  # 已有文件另存为
        logging.info('==========test_wp_save_as_existFile==========')
        hp = WPView(self.driver)

        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        file_name = '已有文档另存'
        hp.save_as_file(file_name, 'local', 1)
        self.assertTrue(hp.check_save_file())

    @unittest.skip('skip test_wp_zoom_pinch')
    def test_wp_zoom_pinch(self, type='wp'):
        logging.info('==========test_wp_zoom_pinch==========')
        hp = WPView(self.driver)
        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        hp.zoom_in()
        hp.zoom_out()

    @unittest.skip('skip test_wp_undo_redo')
    def test_wp_undo_redo(self, type='wp'):  # 撤销、重做
        logging.info('==========test_wp_undo_redo==========')
        gv = WPView(self.driver)
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

    @unittest.skip('skip test_wp_signature')
    def test_wp_signature(self, type='wp'):  # 签批
        logging.info('==========test_wp_signature==========')
        gv = WPView(self.driver)
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

    @unittest.skip('skip test_wp_share_file_edit')
    @data(*share_list1)
    def test_wp_share_file_edit(self, way):
        logging.info('==========test_wp_share_file_edit==========')
        wp = WPView(self.driver)

        type = 'wp'
        suffix = search_dict[type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.switch_write_read()
        wp.group_button_click('插入')
        wp.insert_shape(type)
        wp.share_file(type, way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_wp_share_file_create')
    @data(*share_list1)
    def test_wp_share_file_create(self, way):
        logging.info('==========test_wp_share_file_create==========')
        wp = WPView(self.driver)

        type = 'wp'
        wp.create_file(type)
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict[type])
        wp.share_file(type, way)
        self.driver.find_element(By.ID, 'android:id/button1').click()
        save_name = wp.getTime("%Y%m%d%H%M%S")
        wp.save_step('local', save_name, 1)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_wp_share_file')
    @data(*share_list1)
    def test_wp_share_file(self, way):  # 分享文件
        logging.info('==========test_wp_share_file==========')
        wp = WPView(self.driver)
        file_type = 'wp'

        suffix = search_dict[file_type]
        file_name = '欢迎使用永中Office.%s' % suffix
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.share_file(file_type, way)
        os.system('adb shell am force-stop com.tencent.mobileqq')
        os.system('adb shell am force-stop com.tencent.mm')
        os.system('adb shell am force-stop com.vivo.email')
        os.system('adb shell am force-stop com.alibaba.android.rimet')

    @unittest.skip('skip test_wp_shape_attr')
    def test_wp_shape_attr(self, type='wp'):
        logging.info('==========test_wp_shape_attr==========')
        gv = WPView(self.driver)
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

    @unittest.skip('skip test_wp_shape_attr2')
    def test_wp_shape_attr2(self, file_type='wp'):
        logging.info('==========test_wp_shape_attr2==========')
        gv = WPView(self.driver)
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

    @unittest.skip('skip test_wp_shape_attr1')
    def test_wp_shape_attr1(self):  # 文本框字符属性
        logging.info('==========test_wp_shape_attr1==========')
        gv = WPView(self.driver)
        gv.create_file('wp')

        gv.group_button_click('插入')
        gv.insert_shape('wp')
        time.sleep(1)
        x, y = gv.find_pic_position('drag_all')
        gv.tap(x, y)  # 进入编辑
        gv.pop_menu_click('editText')

        gv.tap(250, 450)
        gv.fold_expand()
        gv.tap(x, y)

        gv.shape_option('wp', 5, width=5, height=5)
        gv.shape_option('wp', 6, top=0.5, bottom=0.5, left=0.5, right=0.5)
        gv.swipe_options()
        gv.swipe_options()
        gv.swipe_options()
        gv.swipe_options()
        gv.shape_content_align('wp', '右对齐', '下对齐')
        gv.shape_content_align('wp')
        gv.shape_content_align('wp', '水平居中', '垂直居中')

    @unittest.skip('skip test_wp_search_replace')
    def test_wp_search_replace(self):  # 查找替换
        logging.info('==========test_wp_search_replace==========')
        gv = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = gv.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = gv.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        gv.switch_write_read()
        gv.group_button_click('查看')
        gv.search_content('wp', '的')
        gv.replace_content('得')
        time.sleep(3)
        gv.replace_content('得', 'all')

    @unittest.skip('skip test_wp_scroll_screen')
    def test_wp_scroll_screen(self):  # 滚屏
        logging.info('==========test_wp_scroll_screen==========')
        hp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        time.sleep(3)
        hp.swipeUp()
        hp.swipeUp()
        hp.swipeDown()
        time.sleep(3)

    @unittest.skip('skip test_wp_rotate')
    def test_wp_rotate(self):
        logging.info('==========test_wp_rotate==========')
        hp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = hp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        # gv.screen_rotate('landscape')
        self.assertTrue(hp.check_rotate())
        hp.screen_rotate('portrait')

    @unittest.skip('skip test_wp_read_mode')
    def test_wp_read_mode(self):  # 阅读模式
        logging.info('==========test_wp_read_mode==========')
        wp = WPView(self.driver)

        wp.create_file('wp')
        wp.switch_write_read()
        self.assertTrue(wp.check_write_read())

    @unittest.skip('skip test_wp_pop_menu_shape')
    def test_wp_pop_menu_shape(self):  # pg未好
        logging.info('==========test_wp_pop_menu_shape==========')
        gv = WPView(self.driver)

        gv.create_file('wp')
        gv.group_button_click('插入')
        gv.insert_shape('wp')
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

    @unittest.skip('skip test_wp_pop_menu_shape1')
    def test_wp_pop_menu_shape1(self):
        logging.info('==========test_wp_pop_menu_shape1==========')
        wp = WPView(self.driver)
        wp.create_file('wp')

        time.sleep(1)
        wp.group_button_click('插入')
        wp.insert_shape('wp')

        wp.fold_expand()
        x1, y1 = wp.find_pic_position('drag_all')
        wp.drag_coordinate(x1, y1, x1 - 100, y1)

        x1, y1 = wp.find_pic_position('drag_all')
        wp.drag_coordinate(x1, y1, x1 + 100, y1)

        x1, y1 = wp.find_pic_position('drag_all')
        wp.drag_coordinate(x1, y1, x1 - 50, y1 - 50)

        x2, y2 = wp.find_pic_position('drag_all1')
        wp.drag_coordinate(x2, y2, x2, y2 - 100)

        x2, y2 = wp.find_pic_position('drag_all1')
        wp.drag_coordinate(x2, y2, x2, y2 + 100)

        x2, y2 = wp.find_pic_position('drag_all1')
        wp.drag_coordinate(x2, y2, x2 - 50, y2 - 50)

        x, y = wp.find_pic_position('rotate_free')
        wp.drag_coordinate(x, y, x + 50, y + 50)

    @unittest.skip('skip test_wp_insert_shape')
    def test_wp_insert_shape(self):
        logging.info('==========test_wp_insert_shape==========')
        wp = WPView(self.driver)
        wp.create_file('wp')

        wp.group_button_click('插入')
        wp.insert_shape('wp')
        for i in range(5):
            wp.shape_insert('wp', 6, random.randint(1, 42))
        time.sleep(3)

    @unittest.skip('skip test_wp_insert_chart')
    def test_wp_insert_chart(self):  # 插入图表
        logging.info('==========test_wp_insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图',
                      '圆锥图', '棱锥图']
        wp = WPView(self.driver)
        wp.create_file('wp')

        time.sleep(1)
        for i in range(12):
            time.sleep(1)
            wp.group_button_click('插入')
            wp.swipe_options()
            wp.insert_chart_insert(chart_list[i], random.randint(1, 9))
            wp.chart_template()
            wp.tap(60, 250, 2)
        time.sleep(1)

    @unittest.skip('skip test_wp_export_pdf')
    def test_wp_export_pdf(self):  # 导出pdf
        logging.info('==========test_wp_export_pdf==========')
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')

        file_name = '导出PDF '
        wp.export_pdf(file_name, 'local')

        self.assertTrue(wp.check_export_pdf())

    @unittest.skip('skip test_wp_expand_fold')
    def test_wp_expand_fold(self):  # 编辑栏收起展开
        logging.info('==========test_wp_expand_fold==========')
        wp = WPView(self.driver)

        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.switch_write_read()
        wp.fold_expand()
        wp.fold_expand()

    @unittest.skip('skip test_wp_create_file')
    def test_wp_create_file(self):  # 新建文档
        logging.info('==========test_wp_create_file==========')
        hp = WPView(self.driver)
        hp.create_file('wp')
        file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_title_text_view').text
        create_dict = {'wp': '新建空白.doc', 'ss': '新建空白.xls', 'pg': '新建空白.ppt'}
        self.assertTrue(file_name == create_dict['wp'])

    # =======before 2019_12_31=====
    @unittest.skip('skip test_pop_menu_text_wp')
    def test_wp_pop_menu_text(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        type = 'wp'
        wp.create_file(type)

        time.sleep(1)
        wp.tap(700, 700)
        for i in range(100):
            self.driver.press_keycode(random.randint(29, 54))
        wp.drag_coordinate(300, 540, 300, 200)
        wp.pop_menu_click('copy')
        wp.tap(700, 700)
        time.sleep(1)
        wp.long_press(700, 700)
        wp.pop_menu_click('paste')
        wp.drag_coordinate(300, 540, 300, 200)
        wp.pop_menu_click('cut')
        wp.tap(700, 700)
        time.sleep(1)
        wp.long_press(700, 700)
        wp.pop_menu_click('paste')

        time.sleep(3)

    @unittest.skip('skip test_shape_text_attr_wp')
    def test_wp_shape_text_attr(self):  # 自选图形文本属性，仅WP和PG
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        type = 'wp'
        wp.create_file(type)
        wp.group_button_click('插入')
        wp.insert_shape(type, 1)
        wp.tap(680, 750)
        wp.pop_menu_click('editText')
        time.sleep(1)
        wp.group_button_click('编辑')
        wp.font_name(type, 'AndroidClock')
        wp.font_size(15)
        wp.font_style(type, '倾斜')
        wp.font_color(type, 6, 29)
        wp.swipe_ele('//*[@text="字体颜色"]', '//*[@text="编辑"]')
        time.sleep(1)
        for i in range(20):
            self.driver.press_keycode(random.randint(29, 54))
        time.sleep(1)
        wp.swipe_ele('//*[@text="高亮颜色"]', '//*[@text="编辑"]')
        wp.drag_coordinate(680, 750, 680, 600)
        wp.high_light_color(type, 6, random.randint(1, 15))
        wp.bullets_numbers(type, 6, 10)
        wp.text_align(type, '分散对齐')
        wp.text_align(type, '右对齐')
        wp.text_line_space(type, 1.5)
        wp.text_line_space(type, 3)
        wp.text_indent(type, '右缩进')
        wp.text_indent(type, '右缩进')
        wp.text_indent(type, '左缩进')
        time.sleep(3)

    @unittest.skip('skip test_wp_bookmark')
    def test_wp_bookmark(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.group_button_click('查看')
        wp.add_bookmark('test')
        self.assertTrue(wp.check_add_bookmark(), '书签插入失败！')

        wp.group_button_click('查看')
        wp.list_bookmark('test')

    @unittest.skip('skip test_wp_check_approve')
    def test_wp_check_approve(self):  # 修订
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file('wp')
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

    @unittest.skip('skip test_wp_font_attr')
    def test_wp_font_attr(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        type = 'wp'
        wp.create_file(type)
        time.sleep(1)
        wp.group_button_click('编辑')
        wp.font_size(16)
        # wp.font_name(type)
        wp.font_style(type, '倾斜')
        wp.font_color(type, 3)
        wp.swipe_options()
        wp.tap(450, 450)
        for i in range(100):
            self.driver.press_keycode(random.randint(29, 54))
        wp.group_button_click('编辑')
        wp.drag_coordinate(450, 500, 200, 500)
        wp.high_light_color(type, 3)
        wp.bullets_numbers(type, 6, 14)
        wp.swipe_options()
        wp.text_align(type, '右对齐')
        wp.text_line_space(type, 2.5)
        wp.text_indent(type, '右缩进')
        wp.swipe_options()
        wp.text_columns(4)
        wp.text_columns(3)
        wp.text_columns(2)

    @unittest.skip('skip test_wp_insert_watermark')
    def test_wp_insert_watermark(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file('wp')
        wp.group_button_click('插入')
        wp.insert_watermark('YOZO')
        time.sleep(1)
        wp.group_button_click('插入')
        wp.insert_watermark('yozo', delete='delete')
        time.sleep(3)

    @unittest.skip('skip test_wp_jump')
    def test_wp_jump(self):  # 跳转页
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.group_button_click('查看')
        wp.page_jump(7)
        time.sleep(2)

    @unittest.skip('skip test_wp_read_self_adaption')
    def test_wp_read_self_adaption(self):  # wp阅读自适应
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.read_self_adaption()
        time.sleep(1)
        self.assertFalse(wp.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                         'read self adaption set fail!')

    @unittest.skip('skip test_wp_text_select')
    def test_wp_text_select(self):  # 文本选取
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.switch_write_read()
        x, y = wp.get_size()
        wp.drag_coordinate(x * 0.5, y * 0.4, x * 0.6, y * 0.5)
        time.sleep(3)

    def wp_insert_one_table(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file('wp')
        wp.group_button_click('插入')
        wp.insert_example_table()

    @unittest.skip('skip test_wp_table_move')
    def test_wp_table_move(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        t = loop_find(wp.template_object('table_select.png'))
        wp.swipe(t[0], t[1], t[0], t[1] + 200, duration=2000)
        time.sleep(10)

    @unittest.skip('skip test_wp_table_pop_menu')
    def test_wp_table_pop_menu(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        touch(wp.template_object('table_select.png'))
        touch(wp.template_object('copy.png'))
        touch(wp.template_object('table_select.png'))
        touch(wp.template_object('delete_table.png'))
        # time.sleep(2)
        if wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        text("YOZOYOZOYOZO")
        text("YOZOYOZOYOZO")
        if not exists(wp.template_object('point.png')):
            wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]').click()
        touch(wp.template_object('point.png'))
        touch(wp.template_object('selectAll.png'))
        touch(wp.template_object('cut.png'))
        wp.group_button_click('插入')
        wp.insert_example_table()
        touch(wp.template_object('table_select.png'))
        touch(wp.template_object('paste.png'))
        touch(wp.template_object('table_select.png'))
        touch(wp.template_object('clear.png'))
        touch(wp.template_object('table_select.png'))
        touch(wp.template_object('cut.png'))

    @unittest.skip('skip test_wp_table_size')
    def test_wp_table_size(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]'
        e7 = wp.get_element_xy(ele, x_y=7)
        e9 = wp.get_element_xy(ele, x_y=9)
        # 改变表格大小
        start = time.time()
        while not exists(wp.template_object('table_size.png')):
            wp.swipe(e9[0], e9[1], e7[0], e7[1])
            if time.time() - start > 15:
                raise TimeoutError('%s' % self.__str__().split(' ')[0])
        swipe(wp.template_object('table_size.png'), wp.get_element_xy(ele, x_y=4))
        time.sleep(5)

    @unittest.skip('skip test_wp_table_right_cols')
    def test_wp_table_right_cols(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]'
        e7 = wp.get_element_xy(ele, x_y=7)
        e9 = wp.get_element_xy(ele, x_y=9)
        # 插入列
        start = time.time()
        while not exists(wp.template_object('table_size.png')):
            wp.swipe(e9[0], e9[1], e7[0], e7[1])
            if time.time() - start > 10:
                raise TimeoutError('%s' % self.__str__().split(' ')[0])
        touch(wp.template_object('table_cols_rows.png'))
        time.sleep(5)

    @unittest.skip('skip test_wp_table_left_rows')
    def test_wp_table_left_rows(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]'
        e7 = wp.get_element_xy(ele, x_y=7)
        e9 = wp.get_element_xy(ele, x_y=9)
        # 插入行
        start = time.time()
        while not exists(wp.template_object('table_select.png')):
            wp.swipe(e7[0], e7[1], e9[0], e9[1])
            if time.time() - start > 5:
                raise TimeoutError('%s' % self.__str__().split(' ')[0])
        touch(wp.template_object('table_cols_rows.png'))
        time.sleep(5)

    @unittest.skip('skip test_wp_table_pop_cell')
    def test_wp_table_pop_cell(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        text('YOZOYOZOYOZO', enter=False)
        touch(wp.template_object('table_select.png', target_pos=9))
        touch(wp.template_object('cut.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        touch(wp.template_object('paste.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        touch(wp.template_object('copy.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        touch(wp.template_object('clear.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        swipe(wp.template_object('clear.png'), wp.template_object('cut.png'))
        touch(wp.template_object('insert_rows.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        touch(wp.template_object('insert_cols.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        swipe(wp.template_object('insert_cols.png'), wp.template_object('clear.png'))
        touch(wp.template_object('delete_rows.png'))
        touch(wp.template_object('table_select.png', target_pos=9))
        touch(wp.template_object('delete_cols.png'))

    @unittest.skip('skip test_wp_table_pop_A_cols')
    def test_wp_table_pop_A_cols(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        text('YOZOYOZOYOZO', enter=False)
        table_all = loop_find(wp.template_object('table_select.png', target_pos=6))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('cut.png'))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('paste.png'))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('copy.png'))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('clear.png'))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('paste.png'))
        touch([table_all[0] + 200, table_all[1]])
        swipe(wp.template_object('clear.png'), wp.template_object('cut.png'))
        touch(wp.template_object('insert_cols.png'))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('delete_cols.png'))
        touch([table_all[0] + 200, table_all[1]])
        touch(wp.template_object('delete_table.png'))
        time.sleep(10)

    @unittest.skip('skip test_wp_table_pop_1_rows')
    def test_wp_table_pop_1_rows(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        text('YOZOYOZOYOZO', enter=False)
        table_all = loop_find(wp.template_object('table_select.png', target_pos=7))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('cut.png'))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('paste.png'))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('copy.png'))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('clear.png'))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('paste.png'))
        touch([table_all[0], table_all[1] + 50])
        swipe(wp.template_object('clear.png'), wp.template_object('cut.png'))
        touch(wp.template_object('insert_rows.png'))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('delete_rows.png'))
        touch([table_all[0], table_all[1] + 50])
        touch(wp.template_object('delete_table.png'))
        time.sleep(10)

    @unittest.skip('skip test_wp_table_cell_extend_cols')
    def test_wp_table_cell_extend_cols(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        extend = loop_find(wp.template_object('table_select.png', target_pos=9))
        swipe([extend[0], extend[1]], [extend[0], extend[1] + 200])
        time.sleep(1)

    @unittest.skip('skip test_wp_table_merge_split')
    def test_wp_table_merge_split(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        touch(wp.template_object('table_select.png'))
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        wp.table_merge_split()
        time.sleep(10)

    @unittest.skip('skip test_wp_table_insert')
    def test_wp_table_insert(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file('wp')
        wp.group_button_click('插入')
        wp.table_insert_list()

    @unittest.skip('skip test_wp_table_attr_1_type')
    def test_wp_table_attr_1_type(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        wp.table_type_list()

    @unittest.skip('skip test_wp_table_attr_2_fill_color')
    def test_wp_table_attr_2_fill_color(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        free_col = wp.table_fill_color()
        self.assertNotEquals(free_col, '000000', msg='表格自定义颜色选择失败')

    @unittest.skip('skip test_wp_table_attr_3_border_line')
    def test_wp_table_attr_3_border_line(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        wp.table_border_line()

    @unittest.skip('skip test_wp_table_attr_4_insert_row_col')
    def test_wp_table_attr_4_insert_row_col(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="插入行或者列"]',s)
        wp.table_insert_row_col(direction='up')
        wp.table_insert_row_col(direction='down')
        wp.table_insert_row_col(direction='left')
        wp.table_insert_row_col(direction='light')

    @unittest.skip('skip test_wp_table_attr_5_delete_table')
    def test_wp_table_attr_5_delete_table(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="删除行或者列"]', s)
        wp.table_delete_row_col_all(del0='row')
        wp.table_delete_row_col_all(del0='col')
        wp.table_delete_row_col_all(del0='all')

    def insert_one_testbox(self, type):  # 将文本框插入wp中
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file(type)
        wp.group_button_click('插入')
        wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]'
                       '/android.widget.FrameLayout[1]' % type).click()
        time.sleep(1)

    @unittest.skip('skip test_wp_insert_testbox')
    def test_wp_insert_testbox(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_testbox(type1)

    def insert_one_shape(self):  # 将矩形插入wp中
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file('wp')
        wp.group_button_click('插入')
        wp.insert_example_shape()

    @unittest.skip('skip test_wp_shape_fixed_rotate')
    def test_wp_shape_fixed_rotate(self, type1='wp'):  # 形状四种固定旋转角度
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        for i in range(1, 5):
            wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]'
                           '/android.widget.FrameLayout[%s]' % (type1, i)).click()
            # print(i)

    @unittest.skip('skip test_wp_shape_attr_preset')
    def test_wp_shape_attr_preset(self):  # 形状35种预设样式
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        wp.shape_preset()

    @unittest.skip('skip test_wp_shape_fill_color')
    def test_wp_shape_fill_color(self):  # 形状填充色
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        wp.shape_fill_color_common()
        wp.shape_fill_color_all()
        wp.shape_fill_color_tran_seekbar()
        wp.other_color()
        wp.shape_fill_color_gradation()

    @unittest.skip('skip test_wp_shape_outline')
    def test_wp_shape_outline(self):  # 形状轮廓
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        # # 形状轮廓 线条颜色
        wp.while_not_exist_ele_swipe('//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_shape_border_color"]',s)
        wp.shape_border_color_common()
        wp.shape_fill_color_all()
        wp.other_color()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_group_button"]'):
            wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_option_back_button"]').click()
        # 形状轮廓 线条类型
        wp.while_not_exist_ele_swipe('//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_shape_border_type"]',s)
        wp.shape_border_type_common()
        wp.shape_border_type_all()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_group_button"]'):
            wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_option_back_button"]').click()
        # 形状轮廓 线条像素
        wp.while_not_exist_ele_swipe('//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_shape_border_width"]',s)
        wp.shape_border_width_common()
        wp.shape_border_width_all()

    @unittest.skip('skip test_wp_shape_effect_type')
    def test_wp_shape_effect_type(self):  # 形状效果 ：三维 阴影
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_shape_effect_type"]',s)
        wp.shape_effect_type_common()
        wp.shape_effect_type_shadow()
        wp.shape_effect_type_3d()

    @unittest.skip('skip test_wp_shape_text_round')
    def test_wp_shape_text_round(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # 仅wp存在文字环绕功能
        self.insert_one_shape()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="文字环绕"]',s)
        wp.text_wrap('四周型')
        wp.text_wrap('嵌入型')
        wp.text_wrap('紧密型')
        wp.text_wrap('衬于文字下方')
        wp.text_wrap()

    @unittest.skip('skip test_wp_shape_order')
    def test_wp_shape_order(self):  # 形状叠放次序
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        wp.object_wp_order()

    @unittest.skip('skip test_wp_shape_pop_menu_all')
    def test_wp_shape_pop_menu_all(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        shape = loop_find(wp.template_object('rotate_free.png'))
        shape_xy = shape[0], shape[1] + 300
        touch(shape)
        touch(wp.template_object('cut.png'))  # 剪切
        wp.group_button_click('插入')
        wp.insert_example_shape()
        touch(shape)
        touch(wp.template_object('copy.png'))  # 复制
        touch(shape)
        touch(wp.template_object('editText.png'))  # 编辑文字
        touch(shape)
        swipe(wp.template_object('editText.png'), wp.template_object('copy.png'))
        touch(wp.template_object('rotate_90.png'))
        touch(shape_xy)
        touch(wp.template_object('delete.png'))  # 删除
        text("YOZOYOZOYOZO", enter=False)
        touch(wp.template_object('point.png'))
        touch(wp.template_object('selectAll.png'))
        touch(wp.template_object('cut.png'))
        wp.group_button_click('插入')
        wp.insert_example_shape()
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('paste.png'))

        time.sleep(10)

    @unittest.skip('skip test_wp_shape_gesture_exit')
    def test_wp_shape_gesture_exit(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_shape()
        wp = WPView(self.driver)
        x, y = loop_find(wp.template_object('rotate_free.png'))
        # 点击左侧，取消选中形状
        touch([20, y + 300])
        sleep(2)
        # 选中形状
        touch([x, y + 100])
        sleep(2)
        # 手动调整控制点
        wp.swipe(x, y + 100, x, y + 300)
        # 向左旋转
        x, y = loop_find(wp.template_object('rotate_free.png'))
        wp.swipe(x, y, 10, 10)
        # 移动形状
        wp.swipe(x, y + 200, 20, y + 200)
        sleep(5)

    def insert_one_pic(self, type1):  # 将图片插入wp中
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file(type1)
        wp.group_button_click('插入')
        wp.insert_pic()

    @unittest.skip('skip test_wp_pic_fixed_rotate')
    def test_wp_pic_fixed_rotate(self, type1='wp'):  # 图片四种固定旋转角度
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'pg'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        # else:
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        for i in range(1, 5):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    @unittest.skip('skip test_wp_pic_width_to_height')
    def test_wp_pic_width_to_height(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="文字环绕"]',s)
        wp.text_wrap('四周型')
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        s1 = [s[2], s[3], s[0], s[1]]
        wp.while_not_exist_ele_swipe('//*[@resource-id="%s"]' % cc,s1)
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        wp.shape_option_5()
        # 手势拖拉大小控制点
        x, y = loop_find(wp.template_object('rotate_free.png'))
        wp.swipe(x, y + 90, x, y + 390)
        time.sleep(10)

    @unittest.skip('skip test_wp_pic_shadow')
    def test_wp_pic_shadow(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        wp.get_element(
            '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_edit"]'
            '/android.widget.FrameLayout[5]').click()
        # 属性调整大小
        wp.shape_option_5()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_effect"]'
                '/android.widget.FrameLayout[%s]' % i).click()
        for i in range(1, 6):
            wp.get_element(
                '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_shadow"]'
                '/android.widget.FrameLayout[%s]' % i).click()
        time.sleep(10)

    @unittest.skip('skip test_wp_pic_outline_color')
    def test_wp_pic_outline_color(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        # else:
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        wp.shape_option_5()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()

        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_border_color"
        # elif type1 == 'wp':
        cc = "com.yozo.office:id/yozo_ui_wp_option_id_picture_broad"
        # elif type1 == 'ss':
        #     cc = "com.yozo.office:id/yozo_ui_ss_option_id_picture_broad_color"
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@resource-id="%s"]' % cc,s)
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        cc = 'com.yozo.office:id/yozo_ui_option_id_color_all'
        list(map(lambda i: wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[%s]' % (cc, i)).click(), range(1, 43)))
        # for i in range(1, 43):
        #     wp.get_element(
        #         '//*[@resource-id="%s"]'
        #         '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    @unittest.skip('skip test_wp_pic_outline_border_type')
    def test_wp_pic_outline_border_type(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        # else:
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        wp.shape_option_5()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()

        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_border_type"
        # elif type1 == 'wp':
        cc = "com.yozo.office:id/yozo_ui_wp_option_id_picture_border_type"
        # elif type1 == 'ss':
        #     cc = "com.yozo.office:id/yozo_ui_ss_option_id_picture_border_type"
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@resource-id="%s"]' % cc,s)
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        cc = 'com.yozo.office:id/yozo_ui_shape_border_type'
        for i in range(1, 8):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    @unittest.skip('skip test_wp_pic_outline_border_px')
    def test_wp_pic_outline_border_px(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        wp.get_element(
            '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_edit"]'
            '/android.widget.FrameLayout[5]').click()
        # 属性调整大小
        wp.shape_option_5()
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_border_width"]',s)
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_border_width"]'
                '/android.widget.FrameLayout[%s]' % i).click()
        for i in range(30):
            wp.get_element(
                '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_arrow_right"]').click()

    @unittest.skip('skip test_wp_pic_order')
    def test_wp_pic_order(self, type1='wp'):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="文字环绕"]',s)
        wp.text_wrap('四周型')
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        s1 = [s[2], s[3], s[0], s[1]]
        wp.while_not_exist_ele_swipe('//*[@resource-id="%s"]' % cc,s1)
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        wp.shape_option_5()
        wp.object_wp_order()

    @unittest.skip('skip test_wp_pic_text_round')
    def test_wp_pic_text_round(self):  # 图片 文字环绕
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        # 仅wp存在文字环绕功能
        self.insert_one_pic('wp')
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="文字环绕"]',s)
        wp.text_wrap('四周型')
        wp.text_wrap('嵌入型')
        wp.text_wrap('紧密型')
        wp.text_wrap('衬于文字下方')
        wp.text_wrap()

    @unittest.skip('skip test_wp_pic_pop_menu_all')
    def test_wp_pic_pop_menu_all(self, type1='wp'):  # 图片 pop菜单
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="文字环绕"]',s)
        wp.text_wrap('四周型')
        # 属性调整大小
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        s1 = [s[2], s[3], s[0], s[1]]
        wp.while_not_exist_ele_swipe('//*[@resource-id="%s"]' % cc,s1)
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        wp.shape_option_5()
        if wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        x, y = loop_find(wp.template_object('rotate_free.png'))
        touch([x, y + 300])

        touch(wp.template_object('copy.png'))  # 复制
        touch([x, y + 300])
        touch(wp.template_object('cut.png'))  # 剪切
        touch(wp.template_object('point.png'))
        touch(wp.template_object('paste.png'))  # 粘贴
        touch([x, y + 300])
        swipe(wp.template_object('rotate_90.png'), wp.template_object('copy.png'))
        touch(wp.template_object('rotate_90.png'))
        touch([x, y + 300])
        touch(wp.template_object('save_to_album.png'))  # 存至相册
        touch([x, y + 300])
        touch(wp.template_object('edit_pic.png'))  # 裁剪
        touch(wp.template_object('delete.png'))  # 删除

    @unittest.skip('skip test_wp_pic_free_rotate')
    def test_wp_pic_free_rotate(self, type1='wp'):  # 图片 移动图片 选中/取消选中 自由旋转
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="文字环绕"]',s)
        wp.text_wrap('四周型')
        # 属性调整大小
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        s1 = [s[2], s[3], s[0], s[1]]
        wp.while_not_exist_ele_swipe('//*[@resource-id="%s"]' % cc,s1)
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        wp.shape_option_5()
        if wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        ele5 = wp.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]')
        ele9 = wp.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]',
                                 x_y=9)

        start = time.time()
        while not exists(wp.template_object('rotate_free.png')):
            wp.swipe(ele5[0], ele5[1], ele9[0], ele9[1])
            if time.time() - start > 5:
                raise TimeoutError('%s' % self.__str__().split(' ')[0])
        # 向右移动图片
        x, y = loop_find(wp.template_object('rotate_free.png'))
        wp.swipe(x, y + 200, x + 200, y + 200)
        # 取消选中图片
        wp.tap(ele9[0], ele9[1])
        time.sleep(1)
        self.assertTrue(wp.exist('//*[@text="编辑"]'), msg='取消选中图片异常')

        # 选中图片
        wp.tap(x + 200, y + 200)
        time.sleep(1)
        self.assertTrue(wp.exist('//*[@text="图片"]'), msg='选中图片异常')
        # 自由旋转
        x, y = loop_find(wp.template_object('rotate_free.png'))
        wp.swipe(x, y, ele9[0], ele9[1])

    @unittest.skip('skip test_wp_insert_chart_list')
    @data(*chart_type)
    def test_wp_insert_chart_list(self, chart_type):  # 插入图表 依次插入所有图表
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        logging.info('==========%s==========' % chart_type)
        wp = WPView(self.driver)
        wp.create_file('wp')
        wp.group_button_click('插入')
        s = wp.swipe_option('up')
        wp.while_not_exist_ele_swipe('//*[@text="图表"]',s)
        wp.get_element('//*[@text="图表"]').click()
        wp.while_not_exist_ele_swipe('//*[@text="%s"]' % chart_type,s)
        wp.get_element('//*[@text="%s"]' % chart_type).click()
        wp.chart_insert_list('%s' % chart_type)

    def insert_chart_first_type(self, chart_type):  # 插入图表 chart_type 图表类型 默认为首个样式
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        wp.create_file('wp')
        wp.group_button_click('插入')
        wp.option_insert_first_chart(chart_type)

    @unittest.skip('skip test_wp_chart_get_data')
    def test_wp_chart_get_data(self, chart_type='柱形图'):  # 图表 查看数据源
        self.insert_chart_first_type(chart_type)
        wp = WPView(self.driver)
        wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_chart_datasource"]').click()
        self.assertTrue(wp.exist('//*[@resource-id="com.yozo.office:id/a0000_pg_chart_embedtable_table"]'),
                        msg='%s data source not exist' % chart_type)

    @unittest.skip('skip test_wp_chart_fill_color')
    def test_wp_chart_fill_color(self, chart_type='柱形图'):  # 图表 图表背景色填充
        self.insert_chart_first_type(chart_type)
        wp = WPView(self.driver)
        free_col = wp.chart_fill_color()
        self.assertNotEquals(free_col, '000000', msg='表格自定义颜色选择失败')

    @unittest.skip('skip test_wp_chart_type')
    def test_wp_chart_type(self, chart_type='柱形图'):  # 图表 图表类型
        self.insert_chart_first_type(chart_type)
        wp = WPView(self.driver)
        wp.chart_change_type_same(chart_type)

    @unittest.skip('skip test_wp_chart_random_style')
    def test_wp_chart_random_style(self, chart_type='柱形图'):  # 图表 图表样式 随机
        self.insert_chart_first_type(chart_type)
        wp = WPView(self.driver)
        wp.chart_random_style()

    @unittest.skip('skip test_wp_chart_change_color')
    def test_wp_chart_change_color(self, chart_type='柱形图'):  # 图表 更改颜色
        self.insert_chart_first_type(chart_type)
        wp = WPView(self.driver)
        wp.chart_change_color()

    @unittest.skip('skip test_wp_print_long_pic')
    def test_wp_print_long_pic(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        wp.group_button_click('文件')
        wp.print_long_pic()
        self.assertTrue(wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_export_longpic_share_buttons"]'),
                        msg='未弹出分享栏')

    @unittest.skip('skip test_wp_swipe_up_down')
    def test_wp_swipe_up_down(self):
        logging.info('==========%s==========' % self.__str__().split(' ')[0])
        wp = WPView(self.driver)
        file_name = '欢迎使用永中Office.docx'
        search_result = wp.search_file(file_name)
        self.assertTrue(search_result, '查找失败')
        open_result = wp.open_file(file_name)
        self.assertTrue(open_result, '打开失败')
        frame5 = wp.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]')
        frame2 = wp.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]',
                                   x_y=2)
        wp.swipe(frame5[0], frame5[1], frame2[0], frame2[1])
        wp.swipe(frame5[0], frame5[1], frame2[0], frame2[1])
        wp.swipe(frame2[0], frame2[1], frame5[0], frame5[1])
        wp.swipe(frame2[0], frame2[1], frame5[0], frame5[1])


if __name__ == '__main__':
    unittest.main()
