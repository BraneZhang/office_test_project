#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time
from selenium.webdriver.common.by import By
from businessView.createView import CreateView
from businessView.loginView import LoginView
from common.common_fun import Common
from common.tool import get_project_path


class GeneralView(Common):

    def pop_menu_click(self, option):  # 点击pop
        logging.info('==========pop_menu_click==========')
        time.sleep(1)
        x, y = self.find_pic_position(option)
        self.tap(x, y)

    def find_pic_position(self, option):  # 查找图片的中心坐标
        logging.info('==========find_pic_position==========')
        self.getScreenShot4Compare('source')
        src_path = get_project_path() + '\\screenshots\\source.png'  # （当前页面）
        obj_path = get_project_path() + '\\clickPicture\\%s.png' % option  # （需要点击的地方）
        x, y = self.find_image_cv(obj_path, src_path)
        return x, y
        # self.tap(x,y)

    def change_row_column(self):  # 切换行列
        logging.info('==========change_row_column==========')
        ele1 = '//*[@text="图表类型"]'
        ele2 = '//*[@text="图表元素"]'
        self.swipe_ele(ele2, ele1)
        self.driver.find_element(By.XPATH, '//*[@text="切换行列"]').click()

    def chart_element_XY(self, xy='X', label=1, grid=0, sub_grid=0, axis=1, line=0, sub_line=0):
        logging.info('==========chart_element_XY==========')
        if not self.get_element_result('//*[@text="%s轴"]' % str.upper(xy)):
            ele1 = '//*[@text="显示图表标题"]'
            ele2 = '//*[@text="显示数据标签"]'
            self.swipe_ele(ele2, ele1)
        self.driver.find_element(By.XPATH, '//*[@text="%s轴"]' % str.upper(xy)).click()
        if label != 1:
            label_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_label"]' \
                           '/android.widget.Switch' % (xy)
            if self.get_element(label_switch).text == '开启':
                self.driver.find_element(By.ID,
                                         'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_label'
                                         % (xy)).click()

        if grid != 0:
            grid_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_grid"]' \
                          '/android.widget.Switch' % (xy)
            if self.get_element(grid_switch).text == '关闭':
                self.driver.find_element(By.ID,
                                         'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_grid'
                                         % (xy)).click()

        if sub_grid != 0:
            sub_grid_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_subgrid"]' \
                              '/android.widget.Switch' % (xy)
            if self.get_element(sub_grid_switch).text == '关闭':
                self.driver.find_element(By.ID,
                                         'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_subgrid'
                                         % (xy)).click()

        if axis != 0:
            line_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_line"]' \
                          '/android.widget.Switch' % (xy)
            if self.get_element(line_switch).text == '关闭':
                self.driver.find_element(By.ID,
                                         'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_line' % (
                                             xy)).click()
            if line != 0:
                line_checked = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_majortick"]' \
                               '/android.widget.CheckBox' % (xy)
                if self.get_element(line_checked).get_attribute('checked') == 'false':
                    self.driver.find_element(By.ID,
                                             'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_majortick' % (
                                                 xy)).click()
            ele3 = '//*[@text="主网格线"]'
            ele4 = '//*[@text="轴线"]'
            self.swipe_ele(ele4, ele3)
            time.sleep(1)
            if sub_line != 0:
                sub_line_checked = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_minortick"]' \
                                   '/android.widget.CheckBox' % (xy)
                if self.get_element(sub_line_checked).get_attribute('checked') == 'false':
                    self.driver.find_element(By.ID,
                                             'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_%saxis_minortick'
                                             % (xy)).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def chart_element(self, types, title='', display=0, label=0):  # 图表元素
        logging.info('==========chart_element==========')
        self.driver.find_element(By.XPATH, '//*[@text="图表元素"]').click()
        if title != '':
            title_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_title_check"]' \
                           '/android.widget.Switch' % types
            if self.get_element(title_switch).text != '开启':
                self.find_element(By.ID,
                                  'com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_title_check' % types).click()
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_title' % types).click()
            time.sleep(1)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_chart_elem_title').set_text(title)
            self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()
            self.fold_expand()

        if display != 0:
            display_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_legend_check"]' \
                             '/android.widget.Switch' % types
            if self.get_element(display_switch).text != '开启':
                self.find_element(By.ID,
                                  'com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_legend_check' % types).click()
            # align_list = {'底部': '1', '顶部': '2', '靠左': '3', '靠右': '4', '右上角': '5'}
            self.find_element(By.XPATH,
                              '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_legend_list"]'
                              '/android.widget.FrameLayout[%s]' % (types, display)).click()

        if label != 0:
            label_switch = '//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_label_check"]' \
                           '/android.widget.Switch' % types
            if self.get_element(label_switch).text != '开启':
                self.find_element(By.ID,
                                  'com.yozo.office:id/yozo_ui_%s_option_id_chart_elem_label_check' % types).click()

    def chart_color(self, index):  # 图表颜色
        logging.info('==========chart_color==========')
        self.driver.find_element(By.XPATH, '//*[@text="更改颜色"]').click()
        eles_name = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
        eles = self.driver.find_elements(By.XPATH, eles_name)
        if index > len(eles):
            eles[-1].click()
        else:
            eles[index - 1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def chart_template(self):  # 图表样式
        logging.info('==========chart_template==========')
        self.driver.find_element(By.XPATH, '//*[@text="图表样式"]').click()
        eles_name = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
        time.sleep(1)
        if self.get_element_result(eles_name + '[1]'):
            eles = self.driver.find_elements(By.XPATH, eles_name)
            for e in eles:
                e.click()
            if len(eles) >= 9:
                self.swipe_ele1(eles[-1], eles[0])
                eles = self.driver.find_elements(By.XPATH, eles_name)
                for e in eles:
                    e.click()
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

    def insert_chart(self, chart, index):  # 插入图表,从插入选项进入
        logging.info('==========insert_chart==========')
        chart_list = ['柱形图', '条形图', '折线图', '饼图', '散点图', '面积图', '圆环图', '雷达图', '气泡图', '圆柱图',
                      '圆锥图', '棱锥图']
        ranges = '//android.support.v4.view.ViewPager/android.widget.ScrollView/android.widget.LinearLayout' \
                 '/android.widget.RelativeLayout'
        target = '//*[@text="%s"]' % chart
        self.swipe_search2(target, ranges)
        self.driver.find_element(By.XPATH, target).click()
        ele_name = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
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
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def shape_layer(self, lay='置于顶层'):  # 图形叠放次序
        logging.info('======shape_layer======')
        lay_dict = {'上移一层': '1', '置于顶层': '2', '下移一层': '3', '置于底层': '4'}
        self.driver.find_element(By.XPATH, '//*[@text="叠放次序"]').click()
        self.driver.find_element(By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]'
                                 % lay_dict[lay]).click()
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
        for i in range(x, x + width, 6):
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
            self.group_button_click('形状')
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
            self.group_button_click('形状')

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
        self.driver.find_element(By.XPATH, '//android.support.v7.widget.RecyclerView'
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
            self.driver.find_element(By.XPATH, '//android.support.v7.widget.RecyclerView'
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
            self.driver.find_element(By.XPATH, '//android.support.v7.widget.RecyclerView'
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
            login = LoginView(self.driver)
            login.login_action('13915575564', 'zhang199412')
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('file named %s' % file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(file_name)

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_type').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # save

    def check_export_pdf(self):
        logging.info('==========check_export_pdf==========')
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

    def screen_rotate(self, rotate):  # 旋转屏幕
        logging.info('==========screen_rotate==========')
        # allowed_values = ['LANDSCAPE', 'PORTRAIT']
        self.driver.orientation = rotate

    def check_rotate(self):
        logging.info('==========check_rotate==========')
        f_width = self.driver.get_window_size()['width']
        print(f_width)
        self.screen_rotate('LANDSCAPE')
        s_width = self.driver.get_window_size()['height']
        print(s_width)
        if f_width == s_width:
            return True
        else:
            return False

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
