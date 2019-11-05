#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import unittest
from ddt import ddt, data
from businessView.saveView import SaveView
from common.myunit import StartEnd
from common.tool import get_csv_data, get_data, image_contrast, img_unite, rm_file

script_file = '../data/need_run.csv'
data1 = get_csv_data(script_file, 1)
data_list = get_data(data1[0], data1[1], int(data1[2]), int(data1[3]))


@ddt
class TestSaveAs(StartEnd):

    @data(*data_list)
    def test_save_as(self, file_name):
        rm_file('untitledfile')
        logging.info('======test_save_as=====')
        s = SaveView(self.driver)
        s.save_as(file_name)
        result = image_contrast()  # 获取图片误差
        try:
            self.assertLess(result, 2000, '实际误差为%s' % result)  # 确认误差是否符合需求
        except Exception:
            img_unite(file_name)
            raise


if __name__ == '__main__':
    unittest.main()
    # driver = appium_desired()
    # list = TestSaveAs.get_info(driver)
    # print(list)
