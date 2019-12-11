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

switch_list = data_info.switch_list

ss_file = '../screenshots/'


@ddt
class TestPG(StartEnd):

    @unittest.skip('skip test_ppt_add_scroll_comment')
    def test_ppt_add_scroll_comment(self):  # ppt缩略图滚屏备注
        logging.info('==========test_ppt_add_scroll_comment==========')
        pg = PGView(self.driver)
        pg.open_file('欢迎使用永中Office.pptx')
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
        pg.open_file('欢迎使用永中Office.pptx')
        pg.wait_loading()
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
        pg.open_file('欢迎使用永中Office.pptx')

        logging.info('==========modify played pages==========')
        pg.wait_loading()
        pg.switch_write_read()
        time.sleep(1)
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        # print(f'thumbnails_list_len:{len(thumbnails_list)}')
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
        pg.open_file('欢迎使用永中Office.pptx')

        logging.info('==========modify played pages==========')
        pg.wait_loading()
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
        pg.open_file('欢迎使用永中Office.pptx')

        logging.info('==========modify played pages==========')
        pg.wait_loading()
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
        pg.open_file('欢迎使用永中Office.pptx')
        pg.switch_write_read()

        pg.group_button_click('切换')
        pg.switch_mode(switch, 'all')
        pg.group_button_click('播放')
        pg.play_mode()
        time.sleep(20)
