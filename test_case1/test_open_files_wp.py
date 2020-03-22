import os
import shutil
import logging
import unittest

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.tool import get_files_list, copy_file_to_wrong
from test_run.run_batch_open import test03_dirs, test07_dirs

path = r'D:\MSfiles\MS2003files\DOC'
path1 = r'D:\MSfiles\MS2007files\docx'

path03_list = []
file03_list = []
for i in test03_dirs:
    path03_list.append(os.path.join(path, i))
for i in path03_list:
    file03_list = file03_list + get_files_list(i)

path07_list = []
file07_list = []
for i in test07_dirs:
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
