#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest

from businessView.cloudView import CloudView

from businessView.selectView import SelectView
from businessView.sortView import SortView
from common.myunit import StartEnd
from common.tool import *


class TestCloud(StartEnd):
    csv_file = '../data/account.csv'

    def test_cloud_alogin(self):
        logging.info('======test_cloud=====')
        # 云文档登录
        sv = SelectView(self.driver)
        cv = CloudView(self.driver)
        sv.select_index('cloud')
        login_state = cv.exist("//*[@resource-id='com.yozo.office:id/btn_logo']")
        print("====%s=====" % login_state)
        if login_state:
            data1 = cv.get_csv_data(self.csv_file, 4)
            cv.cloud_login_action(username=data1[0], password=data1[1])
        self.assertTrue(cv.exist("//*[@text='自动上传']"), msg='Cloud login fail!')

    def test_cloud_folder_pop(self):
        self.test_cloud_alogin()
        # 新建文件夹
        cv = CloudView(self.driver)
        cv.cloud_new_folder('YOZO')
        stv = SortView(self.driver)
        self.assertTrue(cv.exist("//*[@text='YOZO']"), msg='New folder fail!')
        type, sort = 'time', 'up'
        stv.sort_file(type, sort)
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        # 重命名文件夹
        rename_folder = cv.cloud_rename_folder(index=count - 2)
        self.assertTrue(cv.exist("//*[@text='%s']" % rename_folder), msg='Rename folder fail!')
        # 复制文件夹

        # 删除文件夹
        delete_name = cv.cloud_delete_new_folder(index=count - 2)
        self.assertFalse(cv.exist("//*[@text='%s']" % delete_name), msg='Delete folder fail!')

    def test_cloud_file_sort(self):
        self.test_cloud_alogin()
        # 按时间升序排序
        stv = SortView(self.driver)
        type, sort = 'time', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort), msg='cloud file sort time_up success!')
        # 按时间降序排序
        type, sort = 'time', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort), msg='cloud file sort time_down success!')
        # 按类型升序排序
        type, sort = 'type', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort), msg='cloud file sort type_up success!')
        # 按类型降序排序
        type, sort = 'type', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort), msg='cloud file sort type_down success!')
        # 按名称升序排序
        type, sort = 'name', 'up'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort), msg='cloud file sort name_up success!')
        # 按名称降序排序
        type, sort = 'name', 'down'
        stv.sort_file(type, sort)
        self.assertTrue(stv.check_sort_file(type, sort), msg='cloud file sort name_down success!')

    def test_cloud_file_pop(self):
        self.test_cloud_alogin()
        stv = SortView(self.driver)
        cv = CloudView(self.driver)
        # 云文档按时间降序排序
        type, sort = 'time', 'down'
        stv.sort_file(type, sort)
        # 新建云文档
        logging.info('==========cloud_file_create==========')
        cv.cloud_create_file_wp()
        self.assertTrue(cv.exist("//*[@text='wp0.doc']"), msg='Cloud file create fail!')
        # 获取第一个云文档索引
        count = stv.get_first_file_index()
        logging.info('======first_file_index:%s=====' % count)
        # 云文档下载
        cv.cloud_download_file(count)
        self.assertTrue(cv.exist("//*[@text='文件下载成功']"), msg='Cloud file download fail!')
        # 云文档重命名
        rename_file = cv.cloud_rename_file(count)
        self.assertTrue(cv.exist("//*[@text='%s']" % rename_file), msg='Cloud file rename fail!')
        # 云文档分享
        cv.cloud_share_file(count)
        self.assertTrue(cv.exist("//*[@resource-id='com.yozo.office:id/ll_share']"), msg='Cloud file share fail!')
        self.driver.keyevent(4)
        # 云文档信息获取
        cv.cloud_file_info(count)
        self.assertTrue(cv.exist("//*[@resource-id='com.yozo.office:id/tv_fileloc']"), msg='Cloud file info get fail!')
        self.driver.keyevent(4)
        # 云文档删除
        delete_file = cv.cloud_delete_file(count)
        self.assertFalse(cv.exist("//*[@text='%s']" % delete_file), msg='Cloud file delete fail!')
        # 云文档复制
        cv.cloud_copy_file(count)
        self.assertTrue(cv.exist("//*[@text='操作成功']"), msg='Cloud file copy fail!')


if __name__ == '__main__':
    unittest.main()
