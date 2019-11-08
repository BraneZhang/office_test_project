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

    @unittest.skip('skip test_ss_cell_options')
    def test_ss_cell_options(self):  # 插入删除行宽列高清除
        logging.info('==========test_ss_cell_options==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file('ss')
        ss = SSView(self.driver)

        # 新建表格默认选中A1，目前不是，手动调整
        ss.cell_edit()  # 进入编
        x0, y0, width, height = ss.cell_location()
        cv.tap(x0 - width * 3, y0 - height * 5)

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

    @unittest.skip('skip test_ss_cells_select')
    def test_ss_cells_select(self):
        logging.info('==========test_ss_cells_select==========')
        cv = CreateView(self.driver)
        ss = SSView(self.driver)
        cv.create_file('ss')

        # 新建表格默认选中A1，目前不是，手动调整
        ss.cell_edit()  # 进入编
        x0, y0, width, height = ss.cell_location()
        cv.tap(x0 - width * 3, y0 - height * 5)

        ss.cell_edit()  # 进入编
        x, y, width, height = ss.cell_location()  # A1
        ss.tap(x + width * 1.5, y + height * 1.5)
        time.sleep(1)
        ss.drag_coordinate(x + width * 2, y + height * 2, x + width * 3, y + height * 3)
        ss.tap(x - 10, y - 10)

    @unittest.skip('skip test_ss_data_table')
    def test_ss_data_table(self):  # 数据排序，工作表格式
        logging.info('==========test_ss_data_table==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)
        ss.cell_edit()
        x, y, width, height = ss.cell_location()
        for i in range(10):
            ss.tap(x - width * 1.5, y - height * (4.5 - i))
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

    @unittest.skip('skip test_drag_sheet')
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

    @unittest.skip('skip test_ss_formula_auto_sum')
    def test_ss_formula_auto_sum(self):
        logging.info('==========test_ss_formula_auto_sum==========')
        cv = CreateView(self.driver)
        cv.create_file('ss')
        ss = SSView(self.driver)

        # 新建表格默认选中A1，目前不是，手动调整
        ss.cell_edit()  # 进入编
        x0, y0, width, height = ss.cell_location()
        cv.tap(x0 - width * 3, y0 - height * 5)

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

        # 新建表格默认选中A1，目前不是，手动调整
        ss.cell_edit()  # 进入编
        x0, y0, width, height = ss.cell_location()
        cv.tap(x0 - width * 3, y0 - height * 5)

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
        ss.tap(x - width * 2, y - height * 4)
        ss.cell_edit()
        for i in range(20):
            self.driver.press_keycode(45)
        self.driver.find_element(By.ID, 'com.yozo.office:id/formulabar_ok').click()
        cv.drag_coordinate(x - width, y - height * 3, x, y)

        ss.group_button_click('编辑')
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.swipe_options(ele, 'up')
        ss.cell_merge_split()
        ss.cell_merge_split()
        ss.cell_auto_wrap()
        ss.cell_auto_wrap()
        time.sleep(1)

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

    @unittest.skip('skip test_ss_cell_pop_menu')
    def test_ss_cell_pop_menu(self):
        logging.info('==========test_ss_cell_pop_menu==========')
        cv = CreateView(self.driver)
        type = 'ss'
        cv.create_file(type)

        ss = SSView(self.driver)
        # 新建表格默认选中A1，目前不是，手动调整
        ss.cell_edit()  # 进入编
        x0, y0, width, height = ss.cell_location()
        cv.tap(x0 - width * 3, y0 - height * 5)

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
        # 新建表格默认选中A1，目前不是，手动调整
        ss.cell_edit()  # 进入编
        x0, y0, width, height = ss.cell_location()
        cv.tap(x0 - width * 3, y0 - height * 5)
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

    @unittest.skip('skip test_pop_cell_row_col2')
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
                                         '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout')
        eles[random.randint(0, len(eles) - 1)].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_filter_ok').click()
        ss.tap(x1, y1, 2)
        self.driver.find_element(By.XPATH, '//*[@text="自定义"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filter_color_type').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@text="单元格颜色"]').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout')
        eles[random.randint(0, len(eles) - 1)].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_filter_ok').click()

    @unittest.skip('skip test_sheet_operation')
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

    @unittest.skip('skip test_sheet_operation1')
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

    @unittest.skip('skip test_show_file_info')
    def test_show_file_info(self):
        logging.info('==========test_show_file_info==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.xlsx')
        gv = GeneralView(self.driver)
        gv.file_info()
        self.assertTrue(gv.check_file_info())

    @unittest.skip('skip test_ss_chart_pop')
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

    @unittest.skip('skip test_table_style')
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
