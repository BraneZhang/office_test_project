import logging
import random
import time

from businessView.generalView import GeneralView
from selenium.webdriver.common.by import By


class WPView(GeneralView):
    self_adaption_icon = (By.ID, 'com.yozo.office:id/yozo_ui_quick_option_wp_read_full_screen')
    toolbar_button = (By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode')  # 编辑签批切换
    option_group_button = (By.ID, 'com.yozo.office:id/yozo_ui_option_group_button')  # 菜单项
    find_replace = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_find_replace')  # 查看-查找替换
    find_content = (By.ID, 'com.yozo.office:id/yozo_ui_et_find_content')  # 查看-查找输入框
    icon_search = (By.ID, 'com.yozo.office:id/yozo_ui_iv_icon_search')  # 查看-查找搜索图标
    find_previous = (By.ID, 'com.yozo.office:id/yozo_ui_iv_find_previous')  # 查看-查找上一个
    find_next = (By.ID, 'com.yozo.office:id/yozo_ui_iv_find_next')  # 查看-查找下一个
    find_replace_switch = (By.ID, 'com.yozo.office:id/yozo_ui_iv_find_replace_switch')  # 查看-查找切换
    rb_replace = (By.ID, 'com.yozo.office:id/rb_replace')  # 查看-查找与替换
    replace_content = (By.ID, 'com.yozo.office:id/yozo_ui_et_replace_content')  # 查看-替换输入框
    replace_one = (By.ID, 'com.yozo.office:id/yozo_ui_iv_replace_one')  # 查看-替换单个
    replace_all = (By.ID, 'com.yozo.office:id/yozo_ui_tv_replace_all')  # 查看-替换所有
    bookmark_insert = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_bookmark_insert')  # 插入书签
    bookmark_name_edit = (By.ID, 'com.yozo.office:id/bookmark_name_edit')  # 书签名输入框
    bookmark_sure_btn = (By.ID, 'com.yozo.office:id/sure_btn')  # 书签弹窗确定
    bookmark_catalog = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_bookmark_catalog')  # 书签列表
    option_expand_button = (By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button')  # 展开菜单栏
    wp_goto = (By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_goto')  # 跳转页
    goto_page = (By.ID, 'com.yozo.office:id/et_goto_page')  # 输入页码
    goto_id_ok = (By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok')  # 跳转页确定
    high_light = (By.XPATH, '//android.widget.TextView[@text="高亮颜色"]')
    system2 = (By.ID, 'com.yozo.office:id/yozo_ui_option_title_container')  # 字体标题
    reduce_size = (By.ID, 'com.yozo.office:id/yozo_ui_number_picker_arrow_left')  # 缩小字号

    def read_self_adaption(self):  # wp阅读自适应
        logging.info('==========read_self_adaption==========')
        self.driver.find_element(*self.self_adaption_icon).click()

    def add_bookmark(self, marker):  # 插入书签
        logging.info('==========add_bookmark==========')
        self.driver.find_element(*self.bookmark_insert).click()
        self.driver.find_element(*self.bookmark_name_edit).send_keys(marker)
        self.driver.find_element(*self.bookmark_sure_btn).click()

    def check_add_bookmark(self):
        logging.info('==========check_add_bookmark==========')
        return self.get_toast_message('添加书签成功')

    def list_bookmark(self, marker):  # 书签列表
        logging.info('==========list_bookmark==========')
        self.driver.find_element(*self.bookmark_catalog).click()
        if self.get_element_result('//[@text="%s"]' % marker):
            self.driver.find_element(By.XPATH, '//[@text="%s"]' % marker).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def page_jump(self, page):  # 跳转页
        logging.info('==========page_jump==========')
        self.driver.find_element(*self.wp_goto).click()
        pages_str = self.driver.find_element(By.ID, 'com.yozo.office:id/insert_page_hint').text
        split_index = pages_str.index('~')
        end_page = pages_str[split_index + 1]
        if page > int(end_page):
            page = end_page
        self.driver.find_element(*self.goto_page).set_text(page)
        self.driver.find_element(*self.goto_id_ok).click()

    def text_columns(self, index):  # 分栏
        logging.info('==========text_columns==========')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_columns"]'
                                           '/android.widget.FrameLayout[%s]' % index).click()

    def insert_watermark(self, marker, style='斜视', delete=''):  # WP插入水印
        logging.info('======insert_watermark=====')
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="水印"]').click()  # 点击插入水印
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_water_mark').set_text(marker)  # 输入YOZO
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % style).click()
        if delete == 'delete':
            self.find_element(By.XPATH, '//*[@text="删除文档中的水印"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()  # 点击确定

    def revision_on_off(self, state):  # 修订
        logging.info('==========revision_on_off==========')
        mode = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_checkbox_switch').text
        if mode != state:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_group_checkbox_switch').click()

    def revision_accept_not(self, dec='no'):
        logging.info('==========revision_accept_not==========')
        if dec == 'yes':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_accept').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_reject').click()

    def change_name(self, name='root'):
        logging.info('==========change_name==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_revision_change_name').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_name').set_text(name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_full_screen_base_dialog_id_ok').click()

    def insert_example_table(self):
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_insert_table')
        parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')[0].click()

    def table_list(self):
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_table_style')
        childs = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs))
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_options_table_style_all')
        childs0 = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs0))
        table_list0 = (40 - len(childs0)) / 5
        ele_b = '//*[@text="表格样式"]'
        ele_a = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[20]'
        if int(table_list0) != 0:
            self.swipe_ele(ele_a, ele_b)
            # for i in range(-(int(table_list0) * 5), 0):
            #     parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')[i].click()
            list(map(lambda i: parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')[i].click(),
                     range(-(int(table_list0) * 5), 0)))

    def fill_color(self):  # 填充色

        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_cells_fill_color')
        childs = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs))
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_id_color_all')
        childs0 = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs0))

    def border_line(self):  # 边框线
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_table_border')
        childs = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs))
        # 边框线样式
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_group_all')
        childs0 = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs0))
        # 边框线颜色
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_color').click()
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_id_color_all')
        childs0 = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs0))
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()
        # 边框线线条样式
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_style').click()
        parent = self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_ss_option_id_cell_border_style')
        childs0 = parent.find_elements(By.CLASS_NAME, 'android.widget.FrameLayout')
        list(map(lambda i: i.click(), childs0))
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def insert_row_col(self, direction=''):
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_table_option_id_insert_table').click()
        row_col = ['up', 'down', 'left', 'light']
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index="%s"]' %
                                 row_col.index(direction)).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def delete_table_row_col_all(self, del0=''):
        ele_a = '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_table_option_id_insert_table"]'
        ele_b = '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_table_border"]'
        self.swipe_ele(ele_a, ele_b)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_wp_table_option_id_delete_table').click()
        del_ = ['row', 'col', 'all']
        self.driver.find_element(By.XPATH,
                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index="%s"]' %
                                 del_.index(del0)).click()
        if del0 != 'all':
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()


