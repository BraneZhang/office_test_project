import os
import shutil
import logging
import unittest

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.tool import get_files_list, copy_file_to_wrong

path = r'D:\MSfiles\MS2003files\DOC'
path1 = r'D:\MSfiles\MS2007files\docx'

wp03_dirs = ['10000-10999', '11000-11999', '12000-12999', '13000-13999', '14000-14999', '15000-15999', '16000-16999',
             '17000-17999', '18000-18999', '19000-19999', '20000-20999', '21000-21999', '22000-22999', '23000-23999',
             '24000-24999', '25000-25999', '26000-26999', '27000-27999', '28000-28999', '29000-29999', '30000-30999',
             '31000-31999', '32000-32999', '33000-33999', '34000-34999', '35000-35999', '36000-36999', '37000-37999',
             '38000-38999', '39000-39999', '40000-40999', '41000-41999', '42000-42999', '43000-43999', '44000-44999',
             '45000-45999', '46000-46999', '47000-47999', '48000-48999', '49000-49999', '50000-50999', '51000-51999',
             '52000-52999', '53000-53999', '54000-54999', '55000-55999', '56000-56999', '57000-57999', '58000-58999',
             '59000-59999', '60000-60999', '61000-61999', '62000-62999', '63000-63999', '64000-64999', '65000-65999',
             '66000-66999', '67000-67999', '68000-68999', '69000-69999', '70000-70999', '71000-71999', '72000-72999',
             '73000-73999', '74000-74999', '75000-75999', '76000-76999', '77000-77562']

wp07_dirs = ['10000-10999', '11000-11999', '12000-12999', '13000-13999', '14000-14999', '15000-15999', '16000-16999',
             '17000-17999', '18000-18999', '19000-19999', '20000-20999', '21000-21999', '22000-22999', '23000-23999',
             '24000-24999', '25000-25999', '26000-26999', '27000-27999', '28000-28999', '29000-29999', '30000-30999',
             '31000-31999', '32000-32999', '33000-33999', '34000-34999', '35000-35999', '36000-36999', '37000-37999',
             '38000-38999', '39000-39999', '40000-40999', '41000-41999', '42000-42999', '43000-43999', '44000-44999',
             '45000-45999', '46000-46999', '47000-47999', '48000-48999', '49000-49999', '50000-50999', '51000-51999',
             '52000-52999', '53000-53999', '54000-54999', '55000-55999', '56000-56999', '57000-57999', '58000-58999',
             '59000-59999', '60000-60999', '61000-61999', '62000-62999', '63000-63999', '64000-64999', '65000-65999',
             '66000-66999', '67000-67999', '68000-68999', '69000-69999', '70000-70999', '71000-71999', '72000-72999',
             '73000-73999', '74000-74999', '75000-75999', '76000-76999', '77000-77562']
wp03_test_dirs = ['31000-31999']  # 03文档需要跑的文件夹
wp07_test_dirs = ['18000-18999', '28000-28999', '69000-69999', '70000-70999', '71000-71999', '72000-72999',
                  '73000-73999', '74000-74999', '75000-75999', '76000-76999', '77000-77562']  # 07文档需要跑的文件夹

path03_list = []
file03_list = []
for i in wp03_test_dirs:
    path03_list.append(os.path.join(path, i))
for i in path03_list:
    file03_list = file03_list + get_files_list(i)

path07_list = []
file07_list = []
for i in wp07_test_dirs:
    path07_list.append(os.path.join(path1, i))
for i in path07_list:
    file07_list = file07_list + get_files_list(i)


@ddt
class OpenFiles_WP(StartEnd):

    # @unittest.skip('skip test_bat_open_files07')
    @data(*file07_list)
    def test_bat_open_files07(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        if not file_name.endswith(('.doc', 'docx')):
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
        hp.close_file()
        close_result = hp.check_close_file()
        if not close_result:
            copy_file_to_wrong(*path07_list, file_name=file_name)
        self.assertTrue(close_result, msg='close file failed')

    # @unittest.skip('skip test_bat_open_files03')
    @data(*file03_list)
    def test_bat_open_files03(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        if not file_name.endswith(('.doc', 'docx')):
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
