#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.webdriver.common.by import By

from businessView.generalView import GeneralView


class SSView(GeneralView):

    def object_position(self, A, B):  # 获取单元格的坐标
        logging.info('======cell_position=====')
        x1, y1 = self.find_pic_position(A)
        x2, y2 = self.find_pic_position(B)
        width = x2 - x1
        height = y2 - y1
        x = x2 - width / 2
        y = y2 - height / 2
        return x, y, width, height

    def formula_all(self, methods, submethods):  # 求和、平均值、计数、最大值、最小值
        logging.info('======formula_all=====')
        self.group_button_click('公式')
        ranges1 = '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout'
        methods_ele = '//*[@text="%s"]' % methods
        self.swipe_search2(methods_ele,ranges1)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % methods).click()

        ranges = '//android.widget.ListView/android.widget.LinearLayout'
        name = '//*[@text="%s"]' % submethods
        self.swipe_search2(name,ranges)
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % submethods).click()

        # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def auto_sum(self, method='求和'):  # 求和、平均值、计数、最大值、最小值
        logging.info('======auto_sum=====')
        self.group_button_click('公式')
        self.driver.find_element(By.XPATH, '//*[@text="自动求和"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % method).click()
        # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def sheet_style(self, option):  # (显示)100%、隐藏编辑栏、隐藏表头、隐藏网格线、冻结窗口
        logging.info('======sheet_style=====')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % option).click()

    def data_sort(self, sort):  # 升序降序
        logging.info('======insert_chart=====')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % sort).click()

    def swipe_chart(self, id=''):  # 图表滑动
        xpath_ele = '//android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout'
        eles = self.driver.find_elements(By.XPATH, xpath_ele)
        index = 0
        first_id = eles[0].get_attribute('resource-id')
        last_id = eles[-1].get_attribute('resource-id')
        if not '0' in first_id:
            for i, e in enumerate(eles):
                if e.get_attribute('resource-id') == id:
                    if i == len(eles) - 1:
                        return
                    else:
                        index = i + 1
                        break
        for e in eles[index:]:
            e.click()
            sub_eles = self.find_elements(By.XPATH,
                                          '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
            for sub_ele in sub_eles:
                sub_ele.click()
                try:
                    if self.driver.find_element(By.ID, 'android:id/customPanel').is_displayed():
                        self.driver.keyevent(4)
                except Exception:
                    print(Exception)
            self.driver.keyevent(4)
        self.swipe_ele1(eles[-1], eles[0])
        self.swipe_chart(last_id)

    def insert_chart(self):
        logging.info('======insert_chart=====')
        self.group_button_click('插入')
        self.find_element(By.XPATH, '//android.widget.TextView[@text="图表"]').click()  # 点击插入图表
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_chart_type_0').click()  # 点击插入柱状图
        self.find_element(By.XPATH,
                          '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]').click()  # 点击插入图表
        self.find_element(By.XPATH, '//android.widget.TextView[@text="图表类型"]').click()  # 点击图表类型
        # type_base_mark = '//android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout'
        # first_id = 'com.yozo.office:id/yozo_ui_ss_option_id_chart_type_0'
        # self.swipe_ss(self, type_base_mark, first_id)
        time.sleep(1)
        self.swipe_chart()
        self.driver.keyevent(4)

    def table_style(self):  # 表格样式
        logging.info('==========table_style==========')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_table_style"]/android.widget.FrameLayout[6]').click()
        eles = self.find_elements(By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        eleB = '//*[@text="表格样式"]'
        eleA = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[20]'
        for e in eles:
            e.click()
        self.swipe_ele(eleA, eleB)
        eles = self.find_elements(By.XPATH, '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for e in eles:
            e.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def cell_set_size(self, height, width):  # 设置行高列宽
        logging.info('==========cell_set_size==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_resize_cell_manual').click()
        height_ele = '//*[@resource-id="com.yozo.office:id/row_height"]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText'
        width_ele = '//*[@resource-id="com.yozo.office:id/column_width"]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText'
        self.driver.find_element(By.XPATH, height_ele).set_text(height)
        self.driver.find_element(By.XPATH, width_ele).set_text(width)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()

    def cell_fit_height(self):  # 适应行高
        logging.info('==========cell_fit_height==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_resize_cell_fit_height').click()

    def cell_fit_width(self):  # 适应列宽
        logging.info('==========cell_fit_width==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_resize_cell_fit_width').click()

    def cell_clear(self, clear):  # 清除
        logging.info('==========cell_clear==========')
        clear_dict = {'清除内容': 0, '清除格式': 1, '清除所有': 2}
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_clear_cell').click()
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index="%s"]' %
                                 clear_dict[clear]).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def cell_insert(self, insert):  # 插入单元格
        logging.info('==========cell_insert==========')
        insert_dict = {'右移': 0, '下移': 1, '插入整行': 2, '插入整列': 3}
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_insert_cell').click()
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index="%s"]' %
                                 insert_dict[insert]).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def cell_delete(self, delete):  # 删除单元格
        logging.info('==========cell_delete==========')
        delete_dict = {'左移': 0, '上移': 1, '删除整行': 2, '删除整列': 3}
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_delete_cell').click()
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index="%s"]' %
                                 delete_dict[delete]).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def cell_auto_wrap(self):  # 自动换行
        logging.info('==========cell_auto_wrap==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_auto_wrap').click()

    def cell_merge_split(self):  # 合并拆分单元格
        logging.info('==========cell_merge_split==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_merge_split').click()

    def cell_num_style(self):
        logging.info('==========cell_num_style==========')
        num_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_number_format"]' \
                    '/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, num_index).click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
        for i in eles:
            i.click()
        self.swipe_ele('//*[@text="时间"]', '//*[@text="常规"]')
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
        for i in eles:
            i.click()

    def cell_border(self):
        logging.info('==========cell_border==========')
        border_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_border"]/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, border_index).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_color').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_style').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def cell_align(self, horizontal='左对齐', vertical='垂直居中'):
        logging.info('==========cell_align: %s_%s==========' % (horizontal, vertical))
        align_dict = {'左对齐': '0', '水平居中': '1', '右对齐': '2', '上对齐': '3', '垂直居中': '4', '下对齐': '5'}
        style_index1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_align"]/android.widget.FrameLayout[@index="%s"]' % \
                       align_dict[horizontal]
        style_index2 = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_align"]/android.widget.FrameLayout[@index="%s"]' % \
                       align_dict[vertical]
        self.driver.find_element(By.XPATH, style_index1).click()
        self.driver.find_element(By.XPATH, style_index2).click()

    def cell_color(self):  # 单元格填充色
        logging.info('==========cell_color==========')
        color_index = '//*[@resource-id="com.yozo.office:id/yozo_ui_ss_option_id_cell_fill_color"]/android.widget.FrameLayout[6]'
        self.driver.find_element(By.XPATH, color_index).click()
        eles = self.driver.find_elements(By.XPATH,
                                         '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for i in eles:
            i.click()

    def unhide_sheet(self, index, index1):  # 取消隐藏
        logging.info('==========unhide_sheet==========')
        self.operate_sheet(index, 'unhide')
        self.driver.find_elements(By.ID, 'com.yozo.office:id/lv_ss_sheet_hide')[index1].click()

    def operate_sheet(self, index,
                      operation):  # sheet操作的公共部分 options=['rename','insert','copy','remove','hide','unhide']
        logging.info('==========operate_sheet_%s==========' % operation)
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index).click()
        if not self.get_element_result('//*[@resource-id="com.yozo.office:id/ll_ss_sheet"]'):
            self.driver.find_element(By.XPATH,
                                     '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_ss_sheet_%s' % operation).click()

    def hide_sheet(self):  # 隐藏工作表标签
        logging.info('==========hide_sheet==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_back').click()

    def show_sheet(self):  # 展开工作表标签
        logging.info('==========show_sheet==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_quick_option_ss_sheet_tabbar').click()

    def add_sheet(self):  # 新建工作表
        logging.info('==========add_sheet==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ss_sheet_iv_more').click()

    def rename_sheet(self, index, name):  # 重命名工作表
        logging.info('==========rename_sheet_%s==========' % name)
        self.operate_sheet(index, 'rename')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_office_ss_sheet_rename_text').set_text(name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_office_ss_sheet_rename_ok').click()

    def check_rename_sheet(self, index, name):
        base_ele = self.driver.find_element(By.XPATH,
                                            '//*[@resource-id="com.yozo.office:id/ll_ss_sheet_item"and @index="%s"]' % index)
        text_name = base_ele.find_element(By.ID, 'com.yozo.office:id/tv_ss_sheet_name').text
        if text_name == name:
            logging.info('rename success')
            return True
        else:
            logging.error('rename fail')
            self.getScreenShot('rename fail')
            return False
