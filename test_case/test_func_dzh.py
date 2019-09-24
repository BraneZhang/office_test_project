import logging
import time
import unittest

from businessView.createView import CreateView
# from businessView.generalView import GeneralView
# from businessView.loginView import LoginView
# from businessView.openView import OpenView
# from businessView.pgView import PGView
# from businessView.ssView import SSView
from businessView.wpView import WPView
from common.myunit import StartEnd


class TestFunc0(StartEnd):
    def wp_insert_table(self):
        cv = CreateView(self.driver)
        cv.create_file('wp')
        wp = WPView(self.driver)
        wp.group_button_click('插入')
        wp.insert_example_table()

    def test_wp_insert_table(self):
        self.wp_insert_table()

    def test_wp_table_attr_1_type(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.table_list()

    def test_wp_table_attr_2_fill_color(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.fill_color()

    def test_wp_table_attr_3_border_line(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.border_line()

    def test_wp_table_attr_4_insert_row_col(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.insert_row_col(direction='up')
        wp.insert_row_col(direction='down')
        wp.insert_row_col(direction='left')
        wp.insert_row_col(direction='light')

    def test_wp_table_attr_5_delete_table(self):
        self.wp_insert_table()
        wp = WPView(self.driver)
        wp.delete_table_row_col_all(del0='row')
        wp.delete_table_row_col_all(del0='col')
        wp.delete_table_row_col_all(del0='all')
