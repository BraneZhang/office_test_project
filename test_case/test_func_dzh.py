import logging
import time
import unittest
from ddt import ddt, data
from businessView.createView import CreateView
from businessView.generalView import GeneralView
# from businessView.loginView import LoginView
# from businessView.openView import OpenView
from businessView.pgView import PGView
# from businessView.ssView import SSView
from businessView.wpView import WPView
from common.myunit import StartEnd

wps = ['wp', 'ss', 'pg']


@ddt
class TestFunc0(StartEnd):
    def wp_insert_table(self):
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.insert_example_table()

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_insert_table(self):
        self.wp_insert_table()

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_table_attr_1_type(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.table_list()

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_table_attr_2_fill_color(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.fill_color()

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_table_attr_3_border_line(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.border_line()

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_table_attr_4_insert_row_col(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        ele1 = '//*[@text="表格"]'
        ele2 = '//*[@text="单元格填充"]'
        wp.swipe_ele(ele2, ele1)
        wp.insert_row_col(direction='up')
        wp.insert_row_col(direction='down')
        wp.insert_row_col(direction='left')
        wp.insert_row_col(direction='light')

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_table_attr_5_delete_table(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        ele1 = '//*[@text="表格"]'
        ele2 = '//*[@text="单元格填充"]'
        wp.swipe_ele(ele2, ele1)
        wp.delete_table_row_col_all(del0='row')
        wp.delete_table_row_col_all(del0='col')
        wp.delete_table_row_col_all(del0='all')

    def insert_testbox(self, type):
        cv = CreateView(self.driver)
        cv.create_file(type)
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]'
                       '/android.widget.FrameLayout[1]' % type).click()
        time.sleep(1)

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_insert_testbox(self, type1):
        self.insert_testbox(type1)

    def insert_shape_rect(self, type):  # 将矩形插入wp中
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_insert_shape"]'
                       '/android.widget.FrameLayout[3]' % type).click()

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_shape_fixed_rotate(self, type1):  # 形状四种固定旋转角度

        self.insert_shape_rect(type1)
        gv = GeneralView(self.driver)
        for i in range(1, 5):
            gv.get_element('//*[@resource-id="com.yozo.office:id/yozo_ui_%s_option_id_shape_quick_function"]'
                           '/android.widget.FrameLayout[%s]' % (type1, i)).click()
            # print(i)

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_shape_text_round(self):
        # 仅wp存在文字环绕功能
        self.insert_shape_rect('wp')
        ele1 = '//*[@text="形状"]'
        ele2 = '//*[@text="轮廓"]'
        gv = GeneralView(self.driver)
        gv.swipe_ele(ele2, ele1)
        gv.text_wrap('四周型')
        gv.text_wrap('嵌入型')
        gv.text_wrap('紧密型')
        gv.text_wrap('衬于文字下方')
        gv.text_wrap()

    #@unittest.skip('skip test_pop_menu_shape')
    def test_wp_pic_text_round(self):
        # 仅wp存在文字环绕功能
        self.insert_pic_rect('wp')
        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        gv = GeneralView(self.driver)
        gv.swipe_ele(ele2, ele1)
        gv.text_wrap('四周型')
        gv.text_wrap('嵌入型')
        gv.text_wrap('紧密型')
        gv.text_wrap('衬于文字下方')
        gv.text_wrap()

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_pop_menu_shape_all_4(self, type='wp'):  # 该用例未完全需重写
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        if type == 'pg':
            pg = PGView(self.driver)
            gv.group_button_click('编辑')
            pg.edit_format('空白')
        time.sleep(1)
        gv.pinch()
        gv.group_button_click('插入')
        gv.insert_shape(type, index=3)
        gv.fold_expand()
        gv.pop_menu_click('rotate_free')
        gv.pop_menu_click('editText')  # 编辑文字
        gv.pop_menu_click('rotate_free')
        gv.pop_menu_click('copy')  # 复制
        gv.pop_menu_click('rotate_free')
        gv.pop_menu_click('paste')  # 粘贴
        gv.pop_menu_click('rotate_free')
        gv.pop_menu_click('cut')  # 剪切

        # gv.pop_menu_click('point')
        # gv.pop_menu_click('paste')
        # gv.pop_menu_click('rotate_free')
        # x1, y1 = gv.find_pic_position('copy')
        # x2, y2 = gv.find_pic_position('paste')
        # gv.swipe(x2, y2, x1, y1)
        # time.sleep(10)
        # gv.pop_menu_click('rotate_90')  # 旋转90°
        # gv.pop_menu_click('delete')  # 删除

    def insert_pic_rect(self, type):  # 将图片插入wp中
        cv = CreateView(self.driver)
        cv.create_file(type)
        gv = GeneralView(self.driver)
        gv.group_button_click('插入')
        gv.insert_pic()

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_pic_fixed_rotate(self, type1):  # 图片四种固定旋转角度
        # type1 = 'pg'
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        for i in range(1, 5):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_pic_width_to_height(self, type1='wp'):  # 无法调整插入对象位置，ss,pg手势调整大小，裁剪未实现
        # type1 = 'wp'
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'wp':
            ele1 = '//*[@text="图片"]'
            ele2 = '//*[@text="轮廓"]'
            gv.swipe_ele(ele2, ele1)
            gv.text_wrap('四周型')
            ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_broad"]'
            ele2 = '//*[@text="叠放次序"]'
            gv.swipe_ele(ele1, ele2)
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        gv.shape_option_5()
        # 调整图片位置
        if type1 == 'wp':
            x, y = gv.find_pic_position('drag_all')
            gv.swipe(x, y, x + 100, y + 100)
            # 手势调整大小
            x, y = gv.find_pic_position('rotate_free')
            gv.swipe(x, y + 90, x, y + 200)
            # 裁剪
            # gv.fold_expand()
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[6]' % cc).click()
            gv.swipe(x, y + 200, x, y + 90)
            time.sleep(10)

    #@unittest.skip('skip test_pop_menu_shape')
    # @data(*wps)
    def test_wp_pic_shadow(self, type1='wp'):
        # type1 = 'wp'
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1

        gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        gv.shape_option_5()
        if not gv.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            gv.fold_expand()
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_effect_type"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_effect" % type1
        for i in range(1, 7):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

        cc = 'com.yozo.office:id/yozo_ui_option_id_object_effect_shadow'
        for i in range(1, 6):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        time.sleep(10)

    #@unittest.skip('skip test_pop_menu_shape')
    # @data(*wps)
    def test_wp_pic_outline_color(self, type1='wp'):
        # type1 = 'wp'
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        gv.shape_option_5()
        if not gv.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            gv.fold_expand()
        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        gv.swipe_ele(ele2, ele1)

        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_border_color"
        elif type1 == 'wp':
            cc = "com.yozo.office:id/yozo_ui_wp_option_id_picture_broad"
        elif type1 == 'ss':
            cc = "com.yozo.office:id/yozo_ui_ss_option_id_picture_broad_color"

        for i in range(1, 7):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        print(gv.find_pic_position('tpl1570862716430'))
        cc = 'com.yozo.office:id/yozo_ui_option_id_color_all'
        list(map(lambda i: gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[%s]' % (cc, i)).click(), range(1, 43)))
        # for i in range(1, 43):
        #     gv.get_element(
        #         '//*[@resource-id="%s"]'
        #         '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    #@unittest.skip('skip test_pop_menu_shape')
    # @data(*wps)
    def test_wp_pic_outline_border_type(self, type1='wp'):
        # type1 = 'wp'
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        gv.shape_option_5()
        if not gv.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            gv.fold_expand()
        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        gv.swipe_ele(ele2, ele1)

        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_border_type"
        elif type1 == 'wp':
            cc = "com.yozo.office:id/yozo_ui_wp_option_id_picture_border_type"
        elif type1 == 'ss':
            cc = "com.yozo.office:id/yozo_ui_ss_option_id_picture_border_type"

        for i in range(1, 7):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        cc = 'com.yozo.office:id/yozo_ui_shape_border_type'
        for i in range(1, 8):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_pic_outline_border_px(self, type1='wp'):
        # type1 = 'wp'
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        gv.shape_option_5()
        if not gv.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            gv.fold_expand()

        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        gv.swipe_ele(ele2, ele1)

        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_border_width"
        elif type1 == 'wp':
            cc = "com.yozo.office:id/yozo_ui_wp_option_id_picture_border_width"
        elif type1 == 'ss':
            cc = "com.yozo.office:id/yozo_ui_ss_option_id_picture_border_width"

        for i in range(1, 7):
            gv.get_element(
                '//*[@resource-id="%s"]'
                '/android.widget.FrameLayout[%s]' % (cc, i)).click()
        # cc = 'com.yozo.office:id/yozo_ui_option_id_objec_border_width_select'
        for i in range(30):
            gv.get_element(
                '//*[@resource-id="com.yozo.office:id/yozo_ui_number_picker_arrow_right"]').click()

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_pic_order(self, type1='wp'):
        # type1 = 'wp'
        global pic_
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'wp':
            ele1 = '//*[@text="图片"]'
            ele2 = '//*[@text="轮廓"]'
            gv.swipe_ele(ele2, ele1)
            gv.text_wrap('四周型')
            ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_broad"]'
            ele2 = '//*[@text="叠放次序"]'
            gv.swipe_ele(ele1, ele2)
        # if type1 == 'pg':
        #     cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        # else:
        #     cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        # gv.get_element(
        #     '//*[@resource-id="%s"]'
        #     '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        # gv.shape_option_5()
        if type1 == 'pg':
            gv.fold_expand()
            gv.tap(500, 900)
            gv.pop_menu_click('copy')
            gv.tap(500, 900)
            gv.pop_menu_click('paste')
            gv.fold_expand()
        else:
            gv.tap(500, 900)
            gv.pop_menu_click('copy')
            gv.tap(500, 900)
            gv.pop_menu_click('paste')
            gv.tap(500, 900)
            gv.pop_menu_click('paste')

        ele1 = '//*[@text="图片"]'
        ele2 = '//*[@text="轮廓"]'
        gv.swipe_ele(ele2, ele1)
        gv.shape_layer('置于底层')
        gv.shape_layer('上移一层')
        gv.shape_layer('置于顶层')
        gv.shape_layer('下移一层')
        if type1 == 'wp':
            gv.shape_layer('衬于文字下方')
            gv.shape_layer('浮于文字上方')

    #@unittest.skip('skip test_pop_menu_shape')
    @data(*wps)
    def test_wp_pop_menu_pic_all_4(self, type1='wp'):  # 该用例未完全需重写
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)
        if type1 == 'wp':
            ele1 = '//*[@text="图片"]'
            ele2 = '//*[@text="轮廓"]'
            gv.swipe_ele(ele2, ele1)
            gv.text_wrap('四周型')
            ele1 = '//*[@resource-id="com.yozo.office:id/yozo_ui_wp_option_id_picture_broad"]'
            ele2 = '//*[@text="叠放次序"]'
            gv.swipe_ele(ele1, ele2)
        # gv.fold_expand()
        gv.pop_menu_click('drag_pic')
        gv.pop_menu_click('rotate_90')  # 旋转90°
        gv.pop_menu_click('drag_pic')
        gv.pop_menu_click('copy')  # 复制
        gv.pop_menu_click('drag_pic')
        gv.pop_menu_click('paste')  # 粘贴
        gv.pop_menu_click('drag_pic')
        gv.pop_menu_click('cut')  # 剪切

    @unittest.skip('skip test_pop_menu_shape')
    # @data(*wps)
    def test_wp_pic_free_rotate(self, type1='wp'):
        self.insert_pic_rect(type1)
        gv = GeneralView(self.driver)

        if type1 == 'pg':
            cc = "com.yozo.office:id/yozo_ui_pg_option_id_picture_quick_function"
        else:
            cc = "com.yozo.office:id/yozo_ui_%s_option_id_picture_edit" % type1
        gv.get_element(
            '//*[@resource-id="%s"]'
            '/android.widget.FrameLayout[5]' % cc).click()
        # 属性调整大小
        gv.shape_option_5()
        if gv.exist('//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'):
            gv.fold_expand()
        x, y = gv.find_pic_position('rotate_free')
        print(x,y)
        # 有毒

        gv.swipe(x+10, y+10, x + 400, y)
