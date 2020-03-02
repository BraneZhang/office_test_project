import os
import shutil
import logging

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.tool import get_files_list

path = r'E:\MSfiles\MS2003files\xls'

ss_sub_dirs = ['20000-20999', '21000-21999', '22000-22999', '23000-23999', '24000-24999', '25000-25999', '26000-26999',
               '27000-27999', '28000-28999', '29000-29999', '30000-30999', '31000-31999', '32000-32999', '33000-33999',
               '34000-34999', '35000-35999', '36000-36999', '37000-37999', '38000-38999', '39000-39999', '其他']
path1 = os.path.join(path, ss_sub_dirs[0])
path2 = os.path.join(path, ss_sub_dirs[2])
path3 = os.path.join(path, ss_sub_dirs[3])
path4 = os.path.join(path, ss_sub_dirs[3])
path5 = os.path.join(path, ss_sub_dirs[3])
file_names1 = get_files_list(path1)
file_names2 = get_files_list(path2)
file_names3 = get_files_list(path3)
file_names4 = get_files_list(path4)
file_names5 = get_files_list(path5)


@ddt
class OpenFiles_SS(StartEnd):



    #***************** MS-2003 **********************

    # @unittest.skip('skip test_bat_open_files_24000_24999')
    @data(*file_names5)
    def test_bat_open_files_24000_24999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path5, file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path5, file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path5, file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    # @unittest.skip('skip test_bat_open_files_23000_23999')
    @data(*file_names4)
    def test_bat_open_files_23000_23999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path4, file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path4, file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path4, file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    # @unittest.skip('skip test_bat_open_files_22000_22999')
    @data(*file_names3)
    def test_bat_open_files_22000_22999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path3, file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path3, file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path3, file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    # @unittest.skip('skip test_bat_open_files_21000_21999')
    @data(*file_names2)
    def test_bat_open_files_21000_21999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path2, file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path2, file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path2, file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    # @unittest.skip('skip test_bat_open_files_20000_20999')
    @data(*file_names1)
    def test_bat_open_files_20000_20999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path1, file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path1, file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path1, file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')
