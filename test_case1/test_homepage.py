#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest

from ddt import ddt, data

from businessView.createView import CreateView
from businessView.iconView import IconView
from businessView.insertView import InsertView
from businessView.loginView import LoginView
from businessView.searchView import SearchView
from businessView.selectView import SelectView
from businessView.sortView import SortView
from common.myunit import StartEnd
from common.tool import rm_file

# filetypes = ['all','wp','ss','pg','pdf']
filetypes = ['all']


@ddt
class TestHomePage(StartEnd):
    csv_file = '../data/account.csv'

    def test_insert_wp_table(self):
        iv = InsertView(self.driver)
        cv = CreateView(self.driver)
        cv.create_file('hiking','wp')
        iv.insert_table()

    # @unittest.skip('skip test_phone'
    def test_phone(self):
        slv = SelectView(self.driver)
        slv.select_index('alldoc')
        slv.phone_local()
        self.assertTrue(slv.cjeck_phone_local())

    # @unittest.skip('skip test_sort')
    def test_sort(self):
        logging.info('======test_sort=====')
        slv = SelectView(self.driver)
        slv.select_index('alldoc')
        slv.select_file_type('all')
        stv = SortView(self.driver)
        type = ['type', 'name', 'size', 'time']  # 可选择的排序类型
        sort = ['up', 'down']  # 升序还是降序
        for i in type:
            for j in sort:
                # type, sort = 'time', 'up'
                #         stv.sort_file(type, sort)
                stv.sort_file(i, j)
        # self.assertTrue(stv.check_sort_file(type, sort))

    # @unittest.skip('skip test_file_type')
    @data(*filetypes)
    def test_file_type(self, f):
        logging.info('======test_file_type=====')
        slv = SelectView(self.driver)
        slv.select_index('alldoc')

        slv.select_file_type(f)
        self.assertTrue(slv.check_select_file_type(f))

    # @unittest.skip('skip test_multi_select')
    def test_multi_select(self):
        logging.info('======test_multi_select=====')
        slv = SelectView(self.driver)
        slv.select_index('alldoc')
        iv = IconView(self.driver)
        iv.multi_select()
        self.assertTrue(iv.check_multi_select())
        name = iv.multi_select_del('alldoc')
        self.assertTrue(iv.check_delete_file('alldoc', name))

    # @unittest.skip('skip test_info_file')
    def test_info_file(self):
        logging.info('======test_info_file=====')
        iv = IconView(self.driver)
        iv.info_file()

        self.assertTrue(iv.check_info_file())

    # @unittest.skip('skip test_share_file')
    def test_share_file(self):
        logging.info('======test_share_file=====')
        iv = IconView(self.driver)
        iv.share_file()

        self.assertTrue(iv.check_share_file())

    # @unittest.skip('skip test_delete_file')
    def test_delete_file(self):
        logging.info('======test_delete_file=====')
        slv = SelectView(self.driver)
        iv = IconView(self.driver)
        types = ['last', 'alldoc']
        for i in types:
            slv.select_index(i)
            file_name = iv.delete_file(i)

            self.assertTrue(iv.check_delete_file(i, file_name))

    # @unittest.skip('skip test_mark_star')
    def test_mark_star(self):
        logging.info('======test_mark_star=====')
        iv = IconView(self.driver)
        sv = SelectView(self.driver)
        # 最近文档：第一个文档标星
        logging.info('======last_mark_star=====')
        sv.select_index('last')
        file_name = iv.mark_remove_star()
        self.assertTrue(iv.check_mark_star(file_name))
        # 打开文档：第一个文档标星
        logging.info('======alldoc_mark_star=====')
        sv.select_index('alldoc')
        sv.select_file_type('ss')
        file_name = iv.mark_remove_star()
        self.assertTrue(iv.check_mark_star(file_name))

    # @unittest.skip('skip test_upload')
    def test_upload(self):
        logging.info('======test_upload=====')
        iv = IconView(self.driver)
        iv.upload()

        # self.assertTrue(iv.check_upload())

    # @unittest.skip('skip test_login_13915575564')
    def test_login(self):
        logging.info('======test_login=====')
        sv = SearchView(self.driver)
        sv.user_logo()
        l = LoginView(self.driver)
        if l.check_login_status():
            l.logout_action()
        data = l.get_csv_data(self.csv_file, 4)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_login_status())
        l.logout_action()

    # @unittest.skip('skip test_user_log')
    def test_user_log(self):
        logging.info('==========test_user_log==========')
        sv = SearchView(self.driver)
        sv.user_logo()

        self.assertTrue(sv.check_user_logo())

    # @unittest.skip('skip test_create')
    def test_create(self):
        logging.info('==========test_create==========')
        cv = CreateView(self.driver)
        types = ['wp', 'ss', 'pg']
        for i in types:
            for ii in range(6):
                rm_file(i + str(ii))
                cv.create_file(i + str(ii), i, ii)

                self.assertTrue(cv.check_create_file())

    # @unittest.skip('skip test_search')
    def test_search(self):
        logging.info('==========test_search==========')
        sv = SearchView(self.driver)
        file_name = 'wp0.doc'
        sv.search_action(file_name)

        self.assertTrue(sv.check_search_action(file_name))


if __name__ == '__main__':
    unittest.main()
