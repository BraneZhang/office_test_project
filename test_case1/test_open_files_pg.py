import os
import shutil
import logging
import unittest

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.tool import get_files_list, copy_file_to_wrong

path = r'E:\MSfiles\MS2003files\ppt'
path1 = r'E:\MSfiles\MS2007files\pptx'

pg03_dirs = ['1001-2000', '3001-4000', '4001-4640']

pg07_dirs = ['10001-11000', '11001-12000', '12001-13000', '13001-14000', '14001-15000', '15001-16000', '16001-17000',
             '17001-18000', '18001-19000', '19001-19999', '20000-20000', '21001-22000', '22001-23000', '23001-24000',
             '24001-25000', '25001-26000', '26001-27000', '27001-28000', '28001-29000', '29000-29999', '30000-30999',
             '31001-32000', '32001-33000', '33001-34000', '34001-35000', '35001-36000', '36001-37000', '37001-38000',
             '38001-39000', '39001-40000', '40001-41000', '41001-42000', '42001-42950']

pg03_test_dirs = pg03_dirs  # 03文档需要跑的文件夹
pg07_test_dirs = pg03_dirs  # 07文档需要跑的文件夹

path03_list = []
file03_list = []
for i in pg03_test_dirs:
    path03_list.append(os.path.join(path, i))
for i in path03_list:
    file03_list = file03_list + get_files_list(i)

path07_list = []
file07_list = []
for i in pg07_test_dirs:
    path07_list.append(os.path.join(path, i))
for i in path07_list:
    file07_list = file07_list + get_files_list(i)


@ddt
class OpenFiles_PG(StartEnd):

    @unittest.skip('skip test_bat_open_files07')
    # @data(*file07_list)
    def test_bat_open_files07(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        if not file_name.endswith(('.ppt', 'pptx')):
            copy_file_to_wrong(*path07_list, file_name=file_name)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            copy_file_to_wrong(*path07_list, file_name=file_name)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            copy_file_to_wrong(*path07_list, file_name=file_name)
        self.assertTrue(open_result, 'open file failed')
        close_result = hp.check_close_file()
        if not close_result:
            copy_file_to_wrong(*path07_list, file_name=file_name)
        self.assertTrue(close_result, msg='close file failed')

    @unittest.skip('skip test_bat_open_files03')
    # @data(*file03_list)
    def test_bat_open_files03(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        if not file_name.endswith(('.ppt', 'pptx')):
            copy_file_to_wrong(*path03_list, file_name=file_name)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            copy_file_to_wrong(*path03_list, file_name=file_name)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            copy_file_to_wrong(*path03_list, file_name=file_name)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        close_result = hp.check_close_file()
        if not close_result:
            copy_file_to_wrong(*path03_list, file_name=file_name)
        self.assertTrue(close_result, msg='close file failed')
