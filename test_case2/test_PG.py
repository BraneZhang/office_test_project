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
from businessView.createView import CreateView
from businessView.generalView import GeneralView
from businessView.openView import OpenView
from businessView.pgView import PGView
from common.myunit import StartEnd
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import selenium.webdriver.support.expected_conditions as ec

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
ss_file = '../screenshots/'
folder_list = ['手机', '我的文档', 'Download', 'QQ', '微信']
index_share_list = ['qq', 'wechat', 'email', 'more']
auto_sum = ['求和', '平均值', '计数', '最大值', '最小值']

@ddt
class TestFunc(StartEnd):

    @unittest.skip('skip test_ppt_add_scroll_comment')
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

    @unittest.skip('skip test_ppt_format')
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

    @unittest.skip('skip test_ppt_play')
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

    @unittest.skip('skip test_ppt_template')
    def test_ppt_template(self):
        logging.info('==========test_ppt_template==========')
        cv = CreateView(self.driver)
        cv.create_file('pg')
        pg = PGView(self.driver)
        pg.group_button_click('编辑')
        for i in range(11):
            pg.edit_template(i)
        time.sleep(3)

    @unittest.skip('skip test_shape_text_attr_pg')
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

    logging.info('==========2019-11-05 add==========')

    @unittest.skip('skip test_ppt_insert_new')
    def test_ppt_insert_new(self):
        logging.info('==========test_ppt_insert_new==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')

        gv = GeneralView(self.driver)
        gv.wait_loading()
        gv.switch_write_read()
        time.sleep(1)

        logging.info('==========save picture to validate==========')
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, "android.view.View")
        pv = PGView(self.driver)
        pv.screenshot_edit_ppt(ss_file+'first.png')
        thumbnails_list[1].click()
        pv.screenshot_edit_ppt(ss_file + 'second.png')

        logging.info('==========insert new ppt==========')
        thumbnails_list[0].click()
        pv.insert_new_ppt()
        gv.fold_expand()

        logging.info('==========validate insert success==========')
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        thumbnails_list[0].click()
        pv.screenshot_edit_ppt(ss_file + 'new_first.png')
        thumbnails_list[1].click()
        pv.screenshot_edit_ppt(ss_file + 'new_second.png')
        thumbnails_list[2].click()
        pv.screenshot_edit_ppt(ss_file + 'new_third.png')

        result1 = gv.compare_pic('first.png', 'new_first.png')
        result2 = gv.compare_pic('new_second.png', 'new_ppt.png')
        result3 = gv.compare_pic('second.png', 'new_third.png')

        self.assertEqual(result1, 0.0)
        self.assertEqual(result2, 0.0)
        self.assertEqual(result3, 0.0)

        logging.info('==========delete pngs==========')
        os.remove(ss_file + 'first.png')
        os.remove(ss_file + 'second.png')
        os.remove(ss_file + 'new_first.png')
        os.remove(ss_file + 'new_second.png')
        os.remove(ss_file + 'new_third.png')

    @unittest.skip('skip test_ppt_play_to_first')
    @data(*['current', 'first'])
    def test_ppt_play_to_first(self, play_type):
        logging.info('==========test_ppt_play_to_first==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')

        logging.info('==========modify played pages==========')
        gv = GeneralView(self.driver)
        gv.wait_loading()
        gv.switch_write_read()
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        index = random.randint(1, len(thumbnails_list)-4)
        thumbnails_list[index].click()

        logging.info('==========play to the first page==========')
        pg = PGView(self.driver)
        pg.group_button_click('播放')
        pg.play_mode(play_type)
        if play_type == 'first':
            index = 0
        pg.play_to_first(index+1)
        time.sleep(1)

        logging.info('==========validate toast==========')
        try:
            toast = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_dialog_pgplay_tiptext_id')
        except NoSuchElementException:
            self.assertTrue(False, '未出现弹窗')
        else:
            self.assertEqual(toast.text, '已是简报首页', '验证弹窗信息为已是简报首页')

    @unittest.skip('skip test_ppt_play_to_last')
    @data(*['current', 'first'])
    def test_ppt_play_to_last(self, play_type='current'):
        logging.info('==========test_ppt_play_to_last==========')
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')

        logging.info('==========modify played pages==========')
        gv = GeneralView(self.driver)
        gv.wait_loading()
        gv.switch_write_read()
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        index = random.randint(1, len(thumbnails_list) - 4)
        thumbnails_list[index].click()

        logging.info('==========play to the last page==========')
        pg = PGView(self.driver)
        pg.group_button_click('播放')
        pg.play_mode(play_type)
        if play_type == 'first':
            index = 0
        pg.play_to_last(index-1, len(thumbnails_list))
        time.sleep(1)

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
        ov = OpenView(self.driver)
        ov.open_file('欢迎使用永中Office.pptx')

        logging.info('==========modify played pages==========')
        gv = GeneralView(self.driver)
        gv.wait_loading()
        gv.switch_write_read()
        thumbnails_list = self.driver.find_elements(By.CLASS_NAME, 'android.view.View')
        index = random.randint(1, len(thumbnails_list) - 4)
        thumbnails_list[index].click()

        logging.info('==========autoplay to the last page==========')
        pg = PGView(self.driver)
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
