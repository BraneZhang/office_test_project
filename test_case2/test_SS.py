#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import random
import time
import unittest

from selenium.webdriver.common.by import By

from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.ssView import SSView
from common.myunit import StartEnd
from data import data_info

date_filter = data_info.date_filter
num_filter = data_info.num_filter
text_filter = data_info.text_filter


class TestSS(StartEnd):

    @unittest.skip('skip test_ss_cell_border')
    def test_ss_cell_border(self):  # 遍历边框所有功能
        logging.info('==========test_ss_cell_border==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
        ss.group_button_click('编辑')
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.cell_border()

    @unittest.skip('skip test_ss_cell_edit')
    def test_ss_cell_edit(self):
        logging.info('==========test_ss_cell_edit==========')
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')
        ss.cell_edit()

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

        for i in range(5):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()

    @unittest.skip('skip test_ss_cell_options')
    def test_ss_cell_options(self):  # 插入删除行宽列高清除
        logging.info('==========test_ss_cell_options==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.cell_edit()
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        ss.group_button_click('编辑')
        gv = GeneralView(self.driver)
        gv.font_style(type, '删除线')

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
        gv.undo_option()
        ss.cell_clear('清除内容')
        gv.undo_option()
        ss.cell_clear('清除所有')
        gv.undo_option()

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
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)

        ss = SSView(self.driver)
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
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
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
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')
        ss.cell_edit()
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
        self.driver.press_keycode(45)
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

        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.cell_color()
        ss.cell_align('水平居中', '下对齐')

    @unittest.skip('skip test_ss_cells_select')
    def test_ss_cells_select(self):
        logging.info('==========test_ss_cells_select==========')
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')

        ss.cell_edit()  # 进入编
        x, y, width, height = ss.cell_location()  # A1
        ss.tap(x + width * 1.5, y + height * 1.5)
        time.sleep(1)
        ss.drag_coordinate(x + width * 2, y + height * 2, x + width * 3, y + height * 3)
        ss.tap(x - 10, y - 10)

    @unittest.skip('skip test_ss_chart_pop')
    def test_ss_chart_pop(self):  # 图表相关操作
        logging.info('==========test_ss_chart_pop==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        gv = GeneralView(self.driver)
        x, y, width, height = ss.cell_location()
        for i in range(3):
            ss.tap(x + width * 0.5, y + height * (0.5 + i))
            ss.cell_edit()
            self.driver.press_keycode(random.randint(7, 16))
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.swipe(x + width, y + height, x + width, y + height * 3)
        ss.group_button_click('插入')
        gv.insert_chart_insert('柱形图', 2)
        gv.fold_expand()
        time.sleep(1)

        x1, y1 = ss.find_pic_position('chart_title')
        ss.tap(x1, y1)
        ss.pop_menu_click('cut')
        ss.tap(x1, y1)
        ss.tap(x1, y1)
        ss.pop_menu_click('paste')
        x1, y1 = ss.find_pic_position('chart_title')
        ss.tap(x1, y1)
        ss.pop_menu_click('copy')
        ss.tap(x1, y1)
        ss.pop_menu_click('paste')
        x1, y1 = ss.find_pic_position('chart_title')
        ss.swipe(x1, y1, x1 + 100, y1 + 100)
        x1, y1 = ss.find_pic_position('chart_all1')
        ss.swipe(x1, y1, x1 + 10, y1 + 10)

    @unittest.skip('skip test_ss_column_options')
    def test_ss_column_options(self):
        logging.info('==========test_ss_column_options==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
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
        ss.swipe(x2, y2, x2 - width * 3, y2)
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
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        for i in range(10):
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
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ele = '//*[@resource-id="com.yozo.office:id/yozo_ss_frame_table_container"]'
        cv.swipe_options(ele=ele, option='up')
        cv.swipe_options(ele=ele, option='down')
        cv.swipe_options(ele=ele, option='left')
        cv.swipe_options(ele=ele, option='right')

    @unittest.skip('skip test_ss_worksheet_hide_show')
    def test_ss_edit_bar_expand_fold(self):
        logging.info('==========test_ss_edit_bar_expand_fold==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_ss_formula_drop_down').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_ss_formula_drop_down').click()

    @unittest.skip('skip test_ss_filter1')
    def test_ss_filter1(self):
        logging.info('==========test_ss_filter1==========')
        gv = GeneralView(self.driver)
        ss = SSView(self.driver)
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
        gv.switch_write_read()
        gv.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        tip = self.driver.find_element(By.ID, 'com.yozo.office:id/text_content')
        self.assertTrue(tip != None)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_right').click()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        gv.tap(x + width / 2, y - height / 2)
        gv.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        state = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_checkbox_switch').text
        self.assertTrue(state == '开启')
        gv.tap(x - width - 10, y - height * 3 - 10)
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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - width - 18
        y1 = y - height * 3 - 27
        ss.tap(x1, y1)
        self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
        ss.switch_write_read()
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width / 2, y - height / 2)
        ss.group_button_click('查看')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_filter').click()
        x1 = x - width - 18
        y1 = y - height * 3 - 27
        ss.filter_data(x1, y1, '自定义', date_filter[random.randint(1, 12)], date_filter[random.randint(1, 12)])

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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
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
        ov = OpenView(self.driver)
        ov.open_file('screen.xls')
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
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)

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
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')

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
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        ss.tap(x + width * 0.5, y + height * 0.5)
        ss.cell_edit()
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        cv.drag_coordinate(x + width, y + height, x + width, y + height * 3)

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
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
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
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
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
        ss.swipe(x2, y2, x2 - width * 3, y2)
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
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.xlsx')
        gv = GeneralView(self.driver)
        gv.file_info()
        self.assertTrue(gv.check_file_info())

    @unittest.skip('skip test_ss_worksheet_hide_show')
    def test_ss_worksheet_hide_show(self):
        logging.info('==========test_ss_worksheet_hide_show==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_ss_sheet_tabbar').click()
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_more'))
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_back').click()
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_ss_sheet_tabbar'))

    @unittest.skip('skip test_ss_worksheet_options')
    def test_ss_worksheet_options(self):
        logging.info('==========test_ss_worksheet_options==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
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
        cv = CreateView(self.driver)
        cv.create_file('ss')

        ss = SSView(self.driver)
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
