#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import random
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from businessView.homePageView import HomePageView
from common.common_fun import Common
import selenium.webdriver.support.expected_conditions as ec

from common.tool import get_project_path


class GeneralFunctionView(Common):

    def pop_menu_click(self, option):  # 点击pop
        logging.info('==========pop_menu_click==========')
        time.sleep(1)
        x, y = self.find_pic_position(option)
        self.tap(x, y)

    def find_pic_position(self, option):  # 查找图片的中心坐标
        logging.info('==========find_pic_position==========')
        self.getScreenShot4Compare('source')
        src_path = get_project_path() + '\\screenshots\\source.png'  # （当前页面）
        obj_path = get_project_path() + '\\clickPicture_CN\\%s.png' % option  # （需要点击的地方）
        # obj_path = get_project_path() + '\\clickPicture_EN\\%s.png' % option  # （需要点击的地方）
        x, y = self.find_image_cv(obj_path, src_path)
        return x, y
        # self.tap(x,y)

    def change_row_column(self):  # 切换行列
        logging.info('==========change_row_column==========')
        ele1 = '//*[@text="图表类型"]'
        ele2 = '//*[@text="图表元素"]'
        self.swipe_ele(ele2, ele1)
        self.driver.find_element(By.XPATH, '//*[@text="切换行列"]').click()

    def chart_element_axis_title(self, title=None):
        logging.info('==========chart_element_axis_title==========')
        title_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_axis_title_check"]' \
                       '/android.widget.Switch'
        if title != None:
            self.button_on_off(title_button, 1)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_axis_title').click()
            time.sleep(0.5)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_title').set_text(title)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.fold_expand()
        else:
            self.button_on_off(title_button, 0)

    def chart_element_axis_label(self, axis=None, label_state=0):
        logging.info('==========chart_element_axis_label==========')
        label_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_label"]' \
                       '/android.widget.Switch' % axis
        state = 1 if label_state != 0 else 0
        self.button_on_off(label_button, state)

    def chart_element_axis_grid(self, axis=None, grid_state=0):
        logging.info('==========chart_element_axis_grid==========')
        grid_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_grid"]' \
                      '/android.widget.Switch' % axis
        state = 1 if grid_state != 0 else 0
        self.button_on_off(grid_button, state)

    def chart_element_axis_subgrid(self, axis=None, subgrid_state=0):
        logging.info('==========chart_element_axis_subgrid==========')
        subgrid_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_subgrid"]' \
                         '/android.widget.Switch' % axis
        state = 1 if subgrid_state != 0 else 0
        self.button_on_off(subgrid_button, state)

    def chart_element_axis_baseline(self, axis=None, line=None):  # 主次刻度线
        logging.info('==========chart_element_axis_baseline==========')
        line_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_line"]' \
                      '/android.widget.Switch' % axis
        line1_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_majortick"]' % axis
        line2_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_minortick"]' % axis
        if line != None:
            self.button_on_off(line_button, 1)
            state1 = 1 if line[0] != 0 else 0
            self.button_on_off(line1_button, state1)
            state2 = 1 if line[1] != 0 else 0
            self.button_on_off(line2_button, state2)
        else:
            self.button_on_off(line_button, 0)

    def chart_element_XY(self, axis=None, title=None, label=0, grid=0, sub_grid=0, line=None):
        logging.info('==========chart_element_XY==========')
        self.driver.find_element(By.XPATH, '//*[@text="%s轴"]' % str.upper(axis)).click()
        self.chart_element_axis_title(title)
        self.chart_element_axis_label(axis, label)
        self.chart_element_axis_grid(axis, grid)
        self.chart_element_axis_subgrid(axis, sub_grid)
        self.swipe_options()
        self.swipe_options()
        self.chart_element_axis_baseline(axis, line)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def chart_element_title(self, file_type, title):  # 图表标题
        logging.info('==========chart_element_title==========')
        title_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_title_check"]' \
                       '/android.widget.Switch' % file_type
        if title != None:
            self.button_on_off(title_button, 1)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_title' % file_type).click()
            time.sleep(0.5)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_title').set_text(title[0])
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.fold_expand()
            locate_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_title_location_list"]' \
                         '/android.widget.FrameLayout[%s]' % (file_type, title[1])
            self.find_element(By.XPATH, locate_ele).click()
        else:
            self.button_on_off(title_button, 0)

    def chart_element_legend(self, file_type, position=None):  # 图表图例
        logging.info('==========chart_element_legend==========')
        # align_list = {'底部': '1', '顶部': '2', '靠左': '3', '靠右': '4', '右上角': '5'}
        legend_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_legend_check"]' \
                        '/android.widget.Switch' % file_type
        if position != None:
            self.button_on_off(legend_button, 1)
            self.find_element(By.XPATH,
                              '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_legend_list"]'
                              '/android.widget.FrameLayout[%s]' % (file_type, position)).click()
        else:
            self.button_on_off(legend_button, 0)

    def chart_element_label(self, file_type, label_state=0):  # 数据标签
        logging.info('==========chart_element_label==========')
        label_button = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_label_check"]' \
                       '/android.widget.Switch' % file_type
        state = 1 if label_state != 0 else 0
        self.button_on_off(label_button, state)

    def chart_element(self, file_type, title=None, position=None, label=0):  # 图表元素
        logging.info('==========chart_element==========')
        self.driver.find_element(By.XPATH, '//*[@text="图表元素"]').click()
        self.chart_element_title(file_type, title)
        self.chart_element_legend(file_type, position)
        self.swipe_options()
        self.chart_element_label(file_type, label)
        self.swipe_options()

    def chart_color(self, index):  # 图表颜色
        logging.info('==========chart_color==========')
        self.swipe_options()
        self.driver.find_element(By.XPATH, '//*[@text="更改颜色"]').click()
        eles_name = '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout'
        eles = self.driver.find_elements(By.XPATH, eles_name)
        if index > len(eles):
            eles[-1].click()
        else:
            eles[index - 1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def chart_template(self):  # 图表样式
        logging.info('==========chart_template==========')
        self.driver.find_element(By.XPATH, '//*[@text="图表样式"]').click()
        eles_name = '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout'
        time.sleep(1)
        eles = self.driver.find_elements(By.XPATH, eles_name)
        target_ele = eles_name + '[%s]' % random.randint(1, len(eles))
        self.driver.find_element(By.XPATH, target_ele).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def insert_chart_chart(self, chart, index):  # 插入图表，从图表选项进入
        logging.info('==========insert_chart_chart==========')
        self.driver.find_element(By.XPATH, '//*[@text="图表类型"]').click()
        self.insert_chart(chart, index)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def insert_chart_insert(self, chart, index=1):  # 插入图表,从插入选项进入
        logging.info('==========insert_chart_insert==========')
        self.driver.find_element(By.XPATH, '//*[@text="图表"]').click()
        self.insert_chart(chart, index)

    def insert_chart(self, chart, index):  # 插入图表,从图表选项进入
        logging.info('==========insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图',
                      '圆锥图', '棱锥图']
        ranges = '//android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout' \
                 '/android.widget.RelativeLayout'
        target = '//*[@text="%s"]' % chart
        while not self.get_element_result(target):
            self.swipe_options()
        self.driver.find_element(By.XPATH, target).click()
        ele_name = '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout'
        eles = self.driver.find_elements(By.XPATH, ele_name)
        if index > len(eles):
            eles[-1].click()
        else:
            eles[index - 1].click()

    def shape_content_align(self, type, horizontal='左对齐', vertical='上对齐'):
        logging.info('==========cell_align: %s_%s==========' % (horizontal, vertical))
        align_dict = {'左对齐': '1', '水平居中': '2', '右对齐': '3', '上对齐': '4', '垂直居中': '5', '下对齐': '6'}
        style_index1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_text_align"]' \
                       '/android.widget.FrameLayout[%s]' % (type, align_dict[horizontal])
        style_index2 = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_text_align"]' \
                       '/android.widget.FrameLayout[%s]' % (type, align_dict[vertical])
        self.driver.find_element(By.XPATH, style_index1).click()
        self.driver.find_element(By.XPATH, style_index2).click()

    def shape_insert(self, type, index=0, s_index=0):  # 插入自选图形
        logging.info('======shape_insert======')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_insert"]'
                                           '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            eleA = '//*[@text="最近使用"]'
            eleB = '//*[@text="基本形状"]'
            if self.get_element_result(eleA):
                self.swipe_ele(eleB, eleA)
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more_shape'
                                             '_main_container"]/android.widget.FrameLayout')
            if len(eles) < s_index:
                time.sleep(0.5)
                self.swipe_ele1(eles[-1], eles[0])
                time.sleep(0.5)
                eles = self.driver.find_elements(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more'
                                                           '_shape_main_container"]/android.widget.FrameLayout')
                eles[s_index - 19].click()
            else:
                eles[s_index - 1].click()
            time.sleep(1)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def text_wrap(self, wrap='浮于文字上方'):  # 文字环绕
        logging.info('======text_wrap======')
        wrap_list = ['浮于文字上方', '衬于文字下方', '嵌入型', '四周型', '紧密型']
        self.driver.find_element(By.XPATH, '//*[@text="文字环绕"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % wrap).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_layer(self, lay='置于顶层'):  # 图形叠放次序
        logging.info('======shape_layer======')
        lay_dict = {'上移一层': '1', '置于顶层': '2', '下移一层': '3', '置于底层': '4'}
        self.driver.find_element(By.XPATH, '//*[@text="叠放次序"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % lay).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def pic_effect_type(self, type, index=1, shadow=8):
        logging.info('======pic_effect_type======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_picture_effect"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            self.driver.find_element(By.XPATH,
                                     '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_shadow"]'
                                     '/android.widget.FrameLayout[%s]' % shadow).click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_effect_type(self, type, index=1, shadow=8, three_d=8):  # 边框效果
        logging.info('======shape_effect_type======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_effect_type"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            self.driver.find_element(By.XPATH,
                                     '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_shadow"]'
                                     '/android.widget.FrameLayout[%s]' % shadow).click()
            if self.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_3d"]'):
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_object_effect_3d"]'
                                         '/android.widget.FrameLayout[%s]' % three_d).click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def pic_border_width(self, type, index=1, size=1):  # 边框粗细size=1-30
        logging.info('======pic_border_width======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_picture_border_width"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            for i in range(60):
                font_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_recycler_view"]' \
                           '/android.widget.TextView[@index="1"]'
                font = int((self.get_element(font_ele).text)[:-2])
                if size != font:
                    if size < font:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
                    else:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
                else:
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
                    break

    def shape_border_width(self, type, index=1, size=1):  # 边框粗细size=1-30
        logging.info('======shape_border_width======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_border_width"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            for i in range(60):
                font_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_recycler_view"]' \
                           '/android.widget.TextView[@index="1"]'
                font = int((self.get_element(font_ele).text)[:-2])
                if size != font:
                    if size < font:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
                    else:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
                else:
                    self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
                    break

    def pic_border_type(self, type, index=1, s_index=1):  # 边框格式
        logging.info('======pic_border_type======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_picture_border_type"]'
                                 '/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_shape_border_type"]'
                                             '/android.widget.FrameLayout')
            eles[s_index - 1].click()

    def shape_border_type(self, type, index=1, s_index=1):  # 边框格式
        logging.info('======shape_boeder_type======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_border_type"]'
                                 '/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_shape_border_type"]'
                                             '/android.widget.FrameLayout')
            eles[s_index - 1].click()
            time.sleep(0.5)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def pic_border_color(self, type, index=1, s_index=0):  # 边框颜色
        logging.info('======shape_border_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_picture_broad"]'
                                 '/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]'
                                             '/android.widget.FrameLayout')
            eles[s_index - 1].click()
            time.sleep(0.5)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_border_color(self, type, index=1, s_index=0):  # 边框颜色
        logging.info('======shape_border_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_border_color"]'
                                 '/android.widget.FrameLayout[%s]' % (
                                     type, index)).click()
        if index >= 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]'
                                             '/android.widget.FrameLayout')
            eles[s_index - 1].click()
            time.sleep(0.5)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_fill_color_transparency(self, transparency=0):  # 0-100
        logging.info('======shape_fill_color_transparency======')
        eles = self.driver.find_elements(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]'
                                         '/android.widget.FrameLayout')
        self.swipe_ele1(eles[-1], eles[0])
        seekbar = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_seekbar').rect
        x, y, width, height = int(seekbar['x']), int(seekbar['y']), int(seekbar['width']), int(seekbar['height'])
        for i in range(x, x + width, 5):
            display = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_seekbar_display').text
            display_num = int(display[:-1])
            if transparency == display_num:
                break
            else:
                self.tap(i, y)
                time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_fill_color(self, type, index, s_index=36):
        logging.info('======shape_fill_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_fill_color"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index == 6:
            eles = self.driver.find_elements(By.XPATH,
                                             '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_color_all"]'
                                             '/android.widget.FrameLayout')
            if len(eles) < 42 and len(eles) > 0:
                self.swipe_ele1(eles[0], eles[-1])
            eles[s_index - 1].click()
            time.sleep(0.5)
            # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def pic_option(self, type, index, width=3.81, height=3.81, position='drag_pic3', x=0, y=0):  # 图片旋转等操作
        logging.info('======pic_option======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_picture_edit"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index == 5:
            width_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_width')
            width_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(width))
            height_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_height')
            height_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(height))
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.fold_expand()
        if index == 6:
            x1, y1 = self.find_pic_position(position)
            self.drag_coordinate(x1, y1, x1 + x, y1 + y)

    def shape_option(self, type, index, width=3.81, height=3.81, top=0.13, bottom=0.13, left=0.25,
                     right=0.25):  # 旋转、镜像、剪切
        logging.info('======shape_option======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index == 5:
            width_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_width')
            width_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(width))
            height_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_height')
            height_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(height))
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.fold_expand()
        if index == 6:
            top_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_top')
            top_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(top))
            bottom_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_bottom')
            bottom_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(bottom))
            left_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_left')
            left_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(left))
            eleA = '//*[@text="左边距(单位:厘米)"]'
            eleB = '//*[@text="上边距(单位:厘米)"]'
            self.swipe_ele(eleA, eleB)
            right_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/margin_right')
            right_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(right))
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.fold_expand()

    def shape_option_5(self, width=5, height=5):
        width_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_width')
        width_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(width))
        height_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/shape_height')
        height_ele.find_element(By.ID, 'com.yozo.office:id/margin_value').set_text(str(height))
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()

    def pen_size(self, type, index):  # 签批字粗细 1-6
        logging.info('======pen_size======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_sign_pen_size"]'
                                 '/android.widget.FrameLayout[%s]' % (type, index)).click()

    def pen_color(self, type, index=41):  # 签批颜色 1-42
        logging.info('======pen_color======')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_sign_pen_color"]'
                                 '/android.widget.FrameLayout[6]' % type).click()
        self.driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                           '/android.widget.FrameLayout[%s]' % index).click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def pen_type(self, type, pen='钢笔'):  # 钢笔、荧光笔、擦除
        logging.info('======pen_type======')
        pen_list = ['钢笔', '荧光笔', '擦除']
        index = pen_list.index(pen) + 1
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_sign_pen_type"]'
                                           '/android.widget.FrameLayout[%s]' % (type, index)).click()

    def use_finger(self, type):  # 是否使用手指
        logging.info('======use_finger======')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_sign_use_finger' % type).click()

    def insert_shape(self, type, index=1, s_index=0):  # 通用插入
        logging.info('======insert_shape======')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]'
                                           '/android.widget.FrameLayout[%s]' % (type, index)).click()
        if index >= 6:
            eleA = '//*[@text="最近使用"]'
            eleB = '//*[@text="基本形状"]'
            if self.get_element_result(eleA):
                self.swipe_ele(eleB, eleA)

            ele_id = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_id_more_shape_main_container"]' \
                     '/android.widget.FrameLayout'
            eles = self.driver.find_elements(By.XPATH, ele_id)
            if len(eles) < s_index:
                time.sleep(0.5)
                self.swipe_ele1(eles[-1], eles[0])
                time.sleep(0.5)
                eles = self.driver.find_elements(By.XPATH, ele_id)
                eles[s_index - 19].click()
            else:
                eles[s_index - 1].click()

    def text_indent(self, type, indent='左缩进'):  # 缩进
        logging.info('==========text_indent==========')
        if type == 'pg':
            if indent == '左缩进':
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_pg_option_id_edit_para_indent"]'
                                         '/android.widget.FrameLayout[1]').click()
            else:
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_pg_option_id_edit_para_indent"]'
                                         '/android.widget.FrameLayout[2]').click()
        else:
            if indent == '左缩进':
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_para_indent"]'
                                         '/android.widget.FrameLayout[1]' % type).click()
            else:
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_para_indent"]'
                                         '/android.widget.FrameLayout[2]' % type).click()

    def text_line_space(self, type, space):  # 行距
        logging.info('==========text_line_space==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_para_line_space' % type).click()
        space_dict = {1: 'single', 1.5: 'singles', 2: 'double'}
        if space in space_dict:
            self.driver.find_element(By.ID, 'com.yozo.office:id/linespace_%s' % space_dict[space]).click()
        else:
            for i in range(50):
                space_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_recycler_view"]' \
                            '/android.widget.TextView[@index="1"]'
                space_now = float(self.get_element(space_ele).text)
                if space != space_now:
                    if space < space_now:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
                    else:
                        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
                else:
                    break
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def text_align(self, type, align):  # 文本位置
        logging.info('==========text_align==========')
        align_dict = {'左对齐': '1', '居中': '2', '右对齐': '3', '两端对齐': '4', '分散对齐': '5'}
        if type == 'pg':
            align_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_pg_option_id_edit_para_hor_align"]' \
                          '/android.widget.FrameLayout[%s]' % (align_dict[align])
        else:
            align_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_para_hor_align"]' \
                          '/android.widget.FrameLayout[%s]' % (type, align_dict[align])
        self.driver.find_element(By.XPATH, align_index).click()

    def bullets_numbers(self, type, index, s_index=0):  # 项目符号、项目编码s_index=1-15
        logging.info('==========bullets_numbers==========')
        if type == 'pg':
            num_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_pg_option_id_edit_item_bullets_numbers"]' \
                        '/android.widget.FrameLayout[%s]' % index
        else:
            num_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_item_bullets_numbers"]' \
                        '/android.widget.FrameLayout[%s]' % (type, index)
        self.driver.find_element(By.XPATH, num_index).click()
        if index >= 6:
            if s_index <= 7 and s_index > 0:
                self.driver.find_elements(By.XPATH,
                                          '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_item_bullets"]'
                                          '/android.widget.FrameLayout[%s]' % (s_index)).click()
            elif s_index > 7 and s_index < 16:
                self.driver.find_element(By.XPATH,
                                         '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_item_numbers"]'
                                         '/android.widget.FrameLayout[%s]' % (s_index - 7)).click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def high_light_color(self, type, index=1, s_index=0):  # 高亮颜色
        logging.info('==========high_light_color==========')
        color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_highlight_color"]' \
                      '/android.widget.FrameLayout[%s]' % (type, index)
        self.driver.find_element(By.XPATH, color_index).click()
        if index >= 6:
            self.driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                               '/android.widget.FrameLayout[%s]' % s_index).click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def font_color(self, type, index=1, s_index=41):  # 字体颜色
        logging.info('==========font_color==========')
        if type == 'pg':
            color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_pg_option_id_edit_font_color"]' \
                          '/android.widget.FrameLayout[%s]' % index
        else:
            color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_font_color"]' \
                          '/android.widget.FrameLayout[%s]' % (type, index)
        self.driver.find_element(By.XPATH, color_index).click()
        if index >= 6:
            self.driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                               '/android.widget.FrameLayout[%s]' % s_index).click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def font_style(self, type, style):  # 加粗，倾斜，划掉，下划线
        logging.info('==========font_style==========')
        style_dict = {'加粗': '0', '倾斜': '1', '删除线': '2', '下划线': '3'}
        if type == 'pg':
            style_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_pg_option_id_edit_font_style"]' \
                          '/android.widget.FrameLayout[@index="%s"]' % style_dict[style]
        else:
            style_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_font_style"]' \
                          '/android.widget.FrameLayout[@index="%s"]' % (type, style_dict[style])
        self.driver.find_element(By.XPATH, style_index).click()

    def font_name(self, type, name='Noto Color Emoji'):  # 字体类型选择，目前只取系统自带选项的第一个
        logging.info('==========font_name==========')
        if type == 'pg':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_edit_font_name').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_font_name' % type).click()
        time.sleep(1)
        ele1 = '//*[@text="系统"]'
        ele2 = '//*[@text="最近"]'
        ele3 = '//*[@text="字体"]'
        self.swipe_ele(ele2, ele3)
        self.swipe_ele(ele1, ele3)
        range = '//*[@resource-id="com.yozo.office:id/system_font_names"]/android.widget.RelativeLayout'
        name_ele = '//*[@text="%s"]' % name
        self.swipe_search2(name_ele, range)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % name).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def font_size(self, size):  # 字体大小
        logging.info('==========font_size: %s==========' % size)
        font_ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_recycler_view"]' \
                   '/android.widget.TextView[@index="1"]'
        font = int(self.get_element(font_ele).text)
        if size != font:
            if size < font:
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left').click()
            else:
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_right').click()
            self.font_size(size)

    def fold_expand(self):
        logging.info('==========fold_expand==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()

    def search_content(self, type, content):  # 查找内容
        logging.info('==========search_content==========')
        setting_btn = '//*[@resource-id="com.yozo.office:id/yozo_ui_iv_find_replace_switch"]'
        if self.get_element_result(setting_btn):
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_find_replace_switch').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/rb_find').click()
        else:
            if type == 'wp':
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_find_replace').click()
            elif type == 'ss':
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_ll_find').click()
            else:
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_id_pg_find').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_et_find_content').set_text(content)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_icon_search').click()

    def replace_content(self, replace, num='one'):
        logging.info('==========replace==========')
        if not self.get_element_result('//*[@resource-id="com.yozo.office:id/yozo_ui_iv_replace_one"]'):
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_find_replace_switch').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/rb_replace').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_et_replace_content').set_text(replace)
        if num == 'one':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_iv_replace_one').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_tv_replace_all').click()

    def share_file(self, type, way):  # 分享way=['wx','qq','ding','mail']
        logging.info('==========share_file==========')
        self.group_button_click('文件')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_share_by_%s' % (type, way)).click()

    def export_pdf(self, file_name, save_path):  # 导出pdf
        logging.info('==========export_pdf==========')
        self.group_button_click('文件')
        self.driver.find_element(By.XPATH, '//*[@text="输出为PDF"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_folder').click()
        logging.info('choose save path %s' % save_path)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        if self.get_toast_message('您尚未登录，请登录'):
            # login = LoginView(self.driver)
            # login.login_action('13915575564', 'zhang199412')
            HomePageView.login_action(self.driver, '13915575564', 'zhang199412')
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('file named %s' % file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(file_name)

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_type').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # save
        self.cover_file(True)

    def check_export_pdf(self):
        logging.info('==========check_export_pdf==========')
        time.sleep(1)
        return self.get_toast_message('导出成功')

    def switch_write_read(self):  # 阅读模式与编辑模式切换
        logging.info('==========switch_write_read==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()

    def check_write_read(self):
        logging.info('==========check_write_read==========')
        undo = '//*[@resource-id="com.yozo.office:id/yozo_ui_toolbar_button_undo"]'
        if self.get_element_result(undo):
            logging.info('edit mode')
            return False
        else:
            logging.info('read mode')
            return True

    def undo_option(self):  # 撤销
        logging.info('==========undo_option==========')
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo').click()
        time.sleep(1)

    def redo_option(self):  # 重做
        logging.info('==========redo_option==========')
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_redo').click()
        time.sleep(1)

    def file_info(self):
        """
        打开文档信息
        :param file_type: 文档类型：'wp', 'ss', 'pg'
        :return:
        """
        logging.info('==========file_info==========')
        self.group_button_click('文件')
        try:
            self.driver.find_element(By.XPATH, '//*[@text="文档信息"]')
        except NoSuchElementException:
            ele_save = self.driver.find_element(By.XPATH, '//*[@text="保存"]')
            ele_share = self.driver.find_element(By.XPATH, '//*[@text="分享"]')
            Common(self).swipe_ele1(ele_share, ele_save)

        self.driver.find_element(By.XPATH, '//*[@text="文档信息"]').click()

    def check_file_info(self):
        """
        查看文档信息
        :return:
        """
        logging.info('==========check_file_info==========')
        try:
            file_name = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filename').text
            file_type = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetype').text
            location = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_fileloc').text
            file_size = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filesize').text
            edit_time = self.driver.find_element(By.ID, 'com.yozo.office:id/tv_filetime').text
            if file_name != '-' and file_type != '-' and location != '-' and file_size != '-' and edit_time != '-':
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def wait_loading(self, timeout=180):
        """
        等待加载控件消失,默认等待3分钟，超时则抛出异常
        :param timeout: 等待时间
        :return:
        """
        logging.info('==========wait_loading==========')
        try:
            WebDriverWait(self.driver, timeout).until_not(
                ec.visibility_of_element_located((By.CLASS_NAME, 'android.widget.ProgressBar')))
        except TimeoutException:
            logging.error('等待超时，抛出异常')

    def insert_pic(self):  # 插入图片，基于vivoX9手机,选取图片只能点选坐标
        logging.info('=========insert_pic==========')
        # 移动视图，调整插入对象的位置
        ele5 = self.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]')
        ele9 = self.get_element_xy('//*[@resource-id="com.yozo.office:id/yozo_ui_app_frame_office_view_container"]',
                                   x_y=9)
        self.swipe(ele5[0], ele5[1], ele9[0], ele9[1])
        self.driver.find_element(By.XPATH, '//*[@text="图片"]').click()
        self.driver.find_element(By.XPATH, '//android.widget.ListView/android.widget.RelativeLayout[1]').click()
        self.tap(145, 369)
        self.driver.find_element(By.XPATH, '//*[@text="确定"]').click()
