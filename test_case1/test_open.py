#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from ddt import ddt, data

from businessView.openView import OpenView
from common.myunit import StartEnd
from common.tool import *

script_file = '../data/need_run.csv'
datas = get_csv_data(script_file, 1)
# sheet_name = datas[1]
data_list = get_data(datas[0], datas[1], int(datas[2]), int(datas[3]))


@ddt
class TestOpen(StartEnd):

    @data(*data_list)
    def test_open(self, file_name):
        logging.info('======test_open_file_%s=====' % file_name)
        ov = OpenView(self.driver)
        ov.open_file(file_name)
        self.assertTrue(ov.check_open_status(file_name))


if __name__ == '__main__':
    unittest.main()
