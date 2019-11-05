#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import random
import time
import unittest
from ddt import ddt, data
from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.wpView import WPView
from common.myunit import StartEnd
from airtest.core.api import *

chart_type = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图', '圆锥图', '棱锥图']
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

    @unittest.skip('skip test_pop_menu_text_wp')
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

    @unittest.skip('skip test_shape_text_attr_wp')
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

    @unittest.skip('skip test_wp_bookmark')
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

    @unittest.skip('skip test_wp_check_approve')
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

    @unittest.skip('skip test_wp_font_attr')
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

    @unittest.skip('skip test_wp_insert_watermark')
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

    @unittest.skip('skip test_wp_jump')
    def test_wp_jump(self):  # 跳转页
        logging.info('==========test_wp_bookmark==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.group_button_click('查看')
        wp.page_jump(7)
        time.sleep(2)

    @unittest.skip('skip test_wp_read_self_adaption')
    def test_wp_read_self_adaption(self):  # wp阅读自适应
        logging.info('==========test_wp_read_self_adaption==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.read_self_adaption()
        time.sleep(1)
        self.assertFalse(wp.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_close"]'),
                         'read self adaption set fail!')

    @unittest.skip('skip test_wp_text_select')
    def test_wp_text_select(self):  # 文本选取
        logging.info('==========test_wp_text_select==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.switch_write_read()
        x, y = wp.get_size()
        wp.drag_coordinate(x * 0.5, y * 0.4, x * 0.6, y * 0.5)
        time.sleep(3)

    def wp_insert_one_table(self):
        logging.info('==========wp_insert_one_table==========')
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.insert_example_table()

    def test_wp_table_move(self):
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        t = loop_find(wp.template_object('table_select.png'))
        wp.swipe(t[0], t[1], t[0], t[1] + 200, duration=2000)
        time.sleep(5)

    # def test_wp_table_pop_menu(self):
    #     self.wp_insert_one_table()
    #     wp = WPView(self.driver)
    #     x = loop_find(wp.template_object('table_select.png'))
    #     touch(wp.template_object('table_select.png'))
    #     time.sleep(2)
    #     touch(wp.template_object('copy.png'))
    #     time.sleep(10)
    # touch(wp.template_object('table_select.png'))
    # touch(wp.template_object('delete_table.png'))
    # if not exists(wp.template_object('point.png')):
    #     wp.tap(x[0],x[1])
    # touch(wp.template_object('point.png'))
    # touch(wp.template_object('paste.png'))
    # wp.tap(x[0]+200, x[1]+200)
    # touch(wp.template_object('table_select.png'))
    # touch(wp.template_object('cut.png'))

    def test_wp_table_merge_split(self):
        self.wp_insert_one_table()
        select_all_xy = self.wp_table_select()
        wp = WPView(self.driver)
        wp.tap(select_all_xy[0], select_all_xy[1])
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        wp.table_merge_split()
        time.sleep(10)

    def test_wp_table_insert(self):
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.table_insert_list()

    def test_wp_table_attr_1_type(self):
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        wp.table_type_list()

    def test_wp_table_attr_2_fill_color(self):
        logging.info('==========test_wp_table_attr_2_fill_color==========')
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        free_col = wp.table_fill_color()
        self.assertNotEquals(free_col, '000000', msg='自定义颜色选择失败')

    def test_wp_table_attr_3_border_line(self):
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        wp.table_border_line()

    def test_wp_table_attr_4_insert_row_col(self):
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="插入行或者列"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.table_insert_row_col(direction='up')
        wp.table_insert_row_col(direction='down')
        wp.table_insert_row_col(direction='left')
        wp.table_insert_row_col(direction='light')

    def test_wp_table_attr_5_delete_table(self):
        self.wp_insert_one_table()
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="删除行或者列"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.table_delete_row_col_all(del0='row')
        wp.table_delete_row_col_all(del0='col')
        wp.table_delete_row_col_all(del0='all')

    def insert_one_testbox(self, type):  # 将文本框插入wp中
        cv = CreateView(self.driver)
        cv.create_file(type)
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]'
                       '/android.widget.FrameLayout[1]' % type).click()
        time.sleep(1)

    def test_wp_insert_one_testbox(self, type1='wp'):
        self.insert_one_testbox(type1)

    def insert_one_shape(self, type):  # 将矩形插入wp中
        cv = CreateView(self.driver)
        cv.create_file(type)
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]'
                       '/android.widget.FrameLayout[3]' % type).click()

    def test_wp_shape_fixed_rotate(self, type1='wp'):  # 形状四种固定旋转角度

        self.insert_one_shape(type1)
        wp = WPView(self.driver)
        for i in range(1, 5):
            wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]'
                           '/android.widget.FrameLayout[%s]' % (type1, i)).click()
            # print(i)

    def test_wp_shape_text_round(self):
        # 仅wp存在文字环绕功能
        self.insert_one_shape('wp')
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="文字环绕"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.text_wrap('四周型')
        wp.text_wrap('嵌入型')
        wp.text_wrap('紧密型')
        wp.text_wrap('衬于文字下方')
        wp.text_wrap()

    def test_wp_shape_pop_menu_all(self, type1='wp'):
        cv = CreateView(self.driver)
        cv.create_file(type1)
        wp = WPView(self.driver)
        # if type1 == 'pg':
        #     pg = PGView(self.driver)
        #     wp.group_button_click('编辑')
        #     pg.edit_format('空白')
        time.sleep(1)
        wp.pinch()
        wp.group_button_click('插入')
        wp.insert_shape(type1, index=3)
        wp.fold_expand()
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('editText.png'))  # 编辑文字
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('copy.png'))  # 复制
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('cut.png'))  # 剪切
        touch(wp.template_object('point.png'))
        touch(wp.template_object('paste.png'))  # 粘贴
        touch(wp.template_object('rotate_free.png'))
        swipe(wp.template_object('editText.png'), wp.template_object('copy.png'))
        touch(wp.template_object('rotate_90.png'))
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('delete.png'))  # 删除

        time.sleep(10)

    def insert_one_pic(self, type1):  # 将图片插入wp中
        cv = CreateView(self.driver)
        cv.create_file(type1)
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.insert_pic()

    def test_wp_pic_fixed_rotate(self, type1='wp'):  # 图片四种固定旋转角度
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

    def test_wp_pic_width_to_height(self, type1='wp'):
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        if type1 == 'wp':
            s = wp.swipe_option('up')
            while not wp.exist('//*[@text="文字环绕"]'):
                wp.swipe(s[0], s[1], s[2], s[3])
            wp.text_wrap('四周型')
            ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_broad"]'
            ele2 = '//*[@text="叠放次序"]'
            wp.swipe_ele(ele1, ele2)
        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        # else:
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        wp.shape_option_5()
        # 手势拖拉大小控制点
        x, y = loop_find(wp.template_object('drag_pic.png'))
        wp.swipe(x, y, 500, 1000)
        time.sleep(10)

    def test_wp_pic_shadow(self, type1='wp'):
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
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_effect_type"
        # else:
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_effect" % type1
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

        cc = 'com.yozo.office:id/yozo_ui_option_id_object_effect_shadow'
        for i in range(1, 6):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        time.sleep(10)

    def test_wp_pic_outline_color(self, type1='wp'):
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
        while not wp.exist('//*[@resource-id="%s"]' % cc):
            wp.swipe(s[0], s[1], s[2], s[3])
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

    def test_wp_pic_outline_border_type(self, type1='wp'):
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
        while not wp.exist('//*[@resource-id="%s"]' % cc):
            wp.swipe(s[0], s[1], s[2], s[3])
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        cc = 'com.yozo.office:id/yozo_ui_shape_border_type'
        for i in range(1, 8):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    def test_wp_pic_outline_border_px(self, type1='wp'):
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
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_border_width"
        # elif type1 == 'wp':
        cc = "com.yozo.office:id/yozo_ui_wp_option_id_picture_border_width"
        # elif type1 == 'ss':
        #     cc = "com.yozo.office:id/yozo_ui_ss_option_id_picture_border_width"
        s = wp.swipe_option('up')
        while not wp.exist('//*[@resource-id="%s"]' % cc):
            wp.swipe(s[0], s[1], s[2], s[3])
        for i in range(1, 7):
            wp.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        # cc = 'com.yozo.office:id/yozo_ui_option_id_objec_border_width_select'
        for i in range(30):
            wp.get_element(
                '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_arrow_right"]').click()

    def test_wp_pic_order(self, type1='wp'):
        # type1 = 'wp'
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        if type1 == 'wp':

            while not wp.exist('//*[@text="文字环绕"]'):
                wp.swipe(s[0], s[1], s[2], s[3])
            wp.text_wrap('四周型')

        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        # else:
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        if type1 == 'wp':
            while not wp.exist('//*[@resource-id="%s"]' % cc):
                wp.swipe(s[2], s[3], s[0], s[1])
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        wp.shape_option_5()
        if wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        # if type1 == 'pg':
        #     pic_png = 'rotate_free.png'
        # else:
        pic_png = 'drag_pic.png'
        touch(wp.template_object(pic_png))
        touch(wp.template_object('copy.png'))
        touch(wp.template_object(pic_png))
        touch(wp.template_object('paste.png'))
        touch(wp.template_object(pic_png))
        touch(wp.template_object('paste.png'))
        if not wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        wp.swipe_ele(ele2, ele1)
        wp.shape_layer('置于底层')
        wp.shape_layer('上移一层')
        wp.shape_layer('置于顶层')
        wp.shape_layer('下移一层')
        if type1 == 'wp':
            wp.shape_layer('衬于文字下方')
            wp.shape_layer('浮于文字上方')

    def test_wp_pic_text_round(self):
        # 仅wp存在文字环绕功能
        self.insert_one_pic('wp')
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="文字环绕"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.text_wrap('四周型')
        wp.text_wrap('嵌入型')
        wp.text_wrap('紧密型')
        wp.text_wrap('衬于文字下方')
        wp.text_wrap()

    def test_wp_pic_pop_menu_all(self, type1='wp'):
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="文字环绕"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.text_wrap('四周型')
        # 属性调整大小
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        while not wp.exist('//*[@resource-id="%s"]' % cc):
            wp.swipe(s[2], s[3], s[0], s[1])
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        wp.shape_option_5()
        if wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()

        touch(wp.template_object('chart_all1.png'))
        touch(wp.template_object('copy.png'))  # 复制
        touch(wp.template_object('chart_all1.png'))
        touch(wp.template_object('cut.png'))  # 剪切
        touch(wp.template_object('point.png'))
        touch(wp.template_object('paste.png'))  # 粘贴
        touch(wp.template_object('rotate_free.png'))
        swipe(wp.template_object('editText.png'), wp.template_object('copy.png'))
        touch(wp.template_object('rotate_90.png'))
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('save_to_album.png'))  # 存至相册
        touch(wp.template_object('rotate_free.png'))
        touch(wp.template_object('edit_pic.png'))  # 裁剪
        touch(wp.template_object('delete.png'))  # 删除

    def test_wp_pic_free_rotate(self, type1='wp'):
        self.insert_one_pic(type1)
        wp = WPView(self.driver)
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="文字环绕"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.text_wrap('四周型')
        # 属性调整大小
        cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        while not wp.exist('//*[@resource-id="%s"]' % cc):
            wp.swipe(s[2], s[3], s[0], s[1])
        wp.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        wp.shape_option_5()
        if wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            wp.fold_expand()
        ele5 = wp.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]')
        ele9 = wp.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]',
                                 x_y=9)
        while not exists(wp.template_object('rotate_free.png')):
            wp.swipe(ele5[0], ele5[1], ele9[0], ele9[1])
        # 向右移动图片
        rotate_free = loop_find(wp.template_object('rotate_free.png'))
        wp.swipe(rotate_free[0], rotate_free[1] + 200, rotate_free[0] + 200, rotate_free[1] + 200)
        # 取消选中图片
        wp.tap(ele9[0], ele9[1])
        time.sleep(1)
        self.assertTrue(wp.exist('//*[@text="编辑"]'), msg='取消选中图片异常')

        # 选中图片
        wp.tap(rotate_free[0] + 200, rotate_free[1] + 200)
        time.sleep(1)
        self.assertTrue(wp.exist('//*[@text="图片"]'), msg='选中图片异常')
        # 自由旋转
        rotate_free = loop_find(wp.template_object('rotate_free.png'))
        wp.swipe(rotate_free[0], rotate_free[1], ele9[0], ele9[1])
        rotate_free2 = loop_find(wp.template_object('rotate_free.png'))
        self.assertEqual(rotate_free, rotate_free2, msg='图片自由旋转失败')

    @data(*chart_type)
    def test_wp_insert_chart_list(self, chart_type):

        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        s = wp.swipe_option('up')
        while not wp.exist('//*[@text="图表"]'):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.get_element('//*[@text="图表"]').click()

        while not wp.exist('//*[@text="%s"]' % chart_type):
            wp.swipe(s[0], s[1], s[2], s[3])
        wp.get_element('//*[@text="%s"]' % chart_type).click()
        wp.chart_insert_list('%s' % chart_type)

    def test_wp_print_long_pic(self):
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.docx')
        wp = WPView(self.driver)
        wp.wait_loading()
        # time.sleep(2)
        ov.group_button_click('文件')
        wp.print_long_pic()
        self.assertTrue(wp.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_export_longpic_share_buttons"]'),
                        msg='未弹出分享栏')
