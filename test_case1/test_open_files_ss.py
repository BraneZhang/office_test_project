import os
import shutil
import logging
import unittest

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.tool import get_files_list, copy_file_to_wrong

path = r'E:\MSfiles\MS2003files\xls'
path1 = r'E:\MSfiles\MS2007files\xlsx'

ss03_dirs = ['20000-20999', '21000-21999', '22000-22999', '23000-23999', '24000-24999', '25000-25999', '26000-26999',
             '27000-27999', '28000-28999', '29000-29999', '30000-30999', '31000-31999', '32000-32999', '33000-33999',
             '34000-34999', '35000-35999', '36000-36999', '37000-37999', '38000-38999', '39000-39999', '其他']

ss07_dirs = ['10000-10999', '11000-11999', '12000-12999', '13000-13999', '14000-14999', '15000-25999', '16000-26999',
             '17000-17999', '18000-18999', '19000-19999', '20000-20999', '21000-21999', '22000-22999', '23000-23999',
             '24000-24999', '25000-25999', '26000-26999', '27000-27999', '28000-28999', '29000-29999', '30000-30999',
             '31000-31999', '32000-32999', '33000-33999', '34000-34999', '35000-35999', '36000-36999', '37000-37999',
             '38000-38999', '39000-39999', '40000-40999', '41000-41999', '42000-42999', '43000-43999', '44000-44999',
             '45000-45999', '46000-46999', '47000-47999', '48000-48999', '49000-49999', '50000-50999', '51000-51999',
             '52000-52999', '53000-53999', '54000-54999']

ss03_test_dirs = ss03_dirs  # 03文档需要跑的文件夹
ss07_test_dirs = ss07_dirs  # 07文档需要跑的文件夹

path03_list = []
file03_list = []
for i in ss03_test_dirs:
    path03_list.append(os.path.join(path, i))
for i in path03_list:
    file03_list = file03_list + get_files_list(i)


path07_list = []
file07_list = []
for i in ss07_test_dirs:
    path07_list.append(os.path.join(path, i))
for i in path07_list:
    file07_list = file07_list + get_files_list(i)


@ddt
class OpenFiles_SS(StartEnd):



    @unittest.skip('skip test_bat_open_files07')
    # @data(*file07_list)
    def test_bat_open_files07(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        if not file_name.endswith(('.xls','xlsx')):
            copy_file_to_wrong(*path07_list,file_name=file_name)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            copy_file_to_wrong(*path07_list,file_name=file_name)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            copy_file_to_wrong(*path07_list,file_name=file_name)
        self.assertTrue(open_result, 'open file failed')
        close_result = hp.check_close_file()
        if not close_result:
            copy_file_to_wrong(*path07_list, file_name=file_name)
        self.assertTrue(close_result, msg='close file failed')

    @unittest.skip('skip test_bat_open_files03')
    # @data(*file03_list)
    def test_bat_open_files03(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        if not file_name.endswith(('.xls', 'xlsx')):
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
