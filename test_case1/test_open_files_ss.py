import os
import shutil
import logging
import unittest

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd
from common.tool import get_files_list

path = r'E:\MSfiles\MS2003files\xls'
path1 = r'E:\MSfiles\MS2007files\xlsx'

ss_sub_dirs = ['20000-20999', '21000-21999', '22000-22999', '23000-23999', '24000-24999', '25000-25999', '26000-26999',
               '27000-27999', '28000-28999', '29000-29999', '30000-30999', '31000-31999', '32000-32999', '33000-33999',
               '34000-34999', '35000-35999', '36000-36999', '37000-37999', '38000-38999', '39000-39999', '其他']

ss_sub_dirs1 = ['10000-10999', '11000-11999', '12000-12999', '13000-13999', '14000-14999', '15000-25999', '16000-26999',
                '17000-17999', '18000-18999', '19000-19999', '20000-20999', '21000-21999', '22000-22999', '23000-23999',
                '24000-24999', '25000-25999', '26000-26999', '27000-27999', '28000-28999', '29000-29999', '30000-30999',
                '31000-31999', '32000-32999', '33000-33999', '34000-34999', '35000-35999', '36000-36999', '37000-37999',
                '38000-38999', '39000-39999', '40000-40999', '41000-41999', '42000-42999', '43000-43999', '44000-44999',
                '45000-45999', '46000-46999', '47000-47999', '48000-48999', '49000-49999', '50000-50999', '51000-51999',
                '52000-52999', '53000-53999', '54000-54999']
path_list = []
path_list1 = []
for i in ss_sub_dirs:
    path_list.append(os.path.join(path, i))

for i in ss_sub_dirs:
    path_list1.append(os.path.join(path, i))

file_list = []
file_list1 = []
for i in path_list:
    file_list.append(get_files_list(i))
for i in ss_sub_dirs:
    path_list1.append(os.path.join(path, i))


@ddt
class OpenFiles_SS(StartEnd):

    # ***************** MS-2007 **********************
    @unittest.skip('skip test_bat_open_fiels07_54000_54999')
    @data(*file_list[44])
    def test_bat_open_fiels07_54000_54999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[44], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[44], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[44], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_53000_53999')
    @data(*file_list[43])
    def test_bat_open_fiels07_53000_53999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[43], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[43], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[43], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_52000_52999')
    @data(*file_list[42])
    def test_bat_open_fiels07_52000_52999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[42], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[42], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[42], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_51000_51999')
    @data(*file_list[41])
    def test_bat_open_fiels07_51000_51999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[41], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[41], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[41], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_50000_50999')
    @data(*file_list[40])
    def test_bat_open_fiels07_50000_50999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[40], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[40], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[40], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_49000_49999')
    @data(*file_list[39])
    def test_bat_open_fiels07_49000_49999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[39], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[39], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[39], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_48000_48999')
    @data(*file_list[38])
    def test_bat_open_fiels07_48000_48999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[38], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[38], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[38], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_47000_47999')
    @data(*file_list[37])
    def test_bat_open_fiels07_47000_47999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[37], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[37], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[37], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_46000_46999')
    @data(*file_list[36])
    def test_bat_open_fiels07_46000_46999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[36], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[36], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[36], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_45000_45999')
    @data(*file_list[35])
    def test_bat_open_fiels07_45000_45999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[35], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[35], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[35], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_44000_44999')
    @data(*file_list[34])
    def test_bat_open_fiels07_44000_44999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[34], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[34], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[34], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_43000_43999')
    @data(*file_list[33])
    def test_bat_open_fiels07_43000_43999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[33], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[33], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[33], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_42000_42999')
    @data(*file_list[32])
    def test_bat_open_fiels07_42000_42999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[32], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[32], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[32], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_41000_41999')
    @data(*file_list[31])
    def test_bat_open_fiels07_41000_41999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[31], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[31], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[31], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_40000_40999')
    @data(*file_list[30])
    def test_bat_open_fiels07_40000_40999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[30], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[30], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[30], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_39000_39999')
    @data(*file_list[29])
    def test_bat_open_fiels07_39000_39999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[29], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[29], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[29], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_38000_38999')
    @data(*file_list[28])
    def test_bat_open_fiels07_38000_38999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[28], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[28], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[28], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_37000_37999')
    @data(*file_list[27])
    def test_bat_open_fiels07_37000_37999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[27], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[27], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[27], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_36000_36999')
    @data(*file_list[26])
    def test_bat_open_fiels07_36000_36999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[26], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[26], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[26], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_35000_35999')
    @data(*file_list[25])
    def test_bat_open_fiels07_35000_35999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[25], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[25], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[25], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_34000_34999')
    @data(*file_list[24])
    def test_bat_open_fiels07_34000_34999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[24], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[24], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[24], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_33000_33999')
    @data(*file_list[23])
    def test_bat_open_fiels07_33000_33999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[23], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[23], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[23], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_32000_32999')
    @data(*file_list[22])
    def test_bat_open_fiels07_32000_32999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[22], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[22], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[22], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_31000_31999')
    @data(*file_list[21])
    def test_bat_open_fiels07_31000_31999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[21], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[21], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[21], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_30000_30999')
    @data(*file_list[20])
    def test_bat_open_fiels07_30000_30999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[20], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[20], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[20], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_29000_29999')
    @data(*file_list[19])
    def test_bat_open_fiels07_29000_29999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[19], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[19], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[19], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_28000_28999')
    @data(*file_list[18])
    def test_bat_open_fiels07_28000_28999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[18], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[18], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[18], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_27000_27999')
    @data(*file_list[17])
    def test_bat_open_fiels07_27000_27999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[17], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[17], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[17], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_26000_26999')
    @data(*file_list[16])
    def test_bat_open_fiels07_26000_26999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[16], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[16], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[16], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_25000_25999')
    @data(*file_list[15])
    def test_bat_open_fiels07_25000_25999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[15], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[15], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[15], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_24000_24999')
    @data(*file_list[14])
    def test_bat_open_fiels07_24000_24999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[14], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[14], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[14], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_23000_23999')
    @data(*file_list[13])
    def test_bat_open_fiels07_23000_23999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[13], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[13], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[13], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_22000_22999')
    @data(*file_list[12])
    def test_bat_open_fiels07_22000_22999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[12], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[12], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[12], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_21000_21999')
    @data(*file_list[11])
    def test_bat_open_fiels07_21000_21999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[11], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[11], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[11], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_20000_20999')
    @data(*file_list[10])
    def test_bat_open_fiels07_20000_20999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[10], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[10], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[10], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_19000_19999')
    @data(*file_list[9])
    def test_bat_open_fiels07_19000_19999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[9], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[9], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[9], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_18000_18999')
    @data(*file_list[8])
    def test_bat_open_fiels07_18000_18999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[8], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[8], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[8], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_17000_17999')
    @data(*file_list[7])
    def test_bat_open_fiels07_17000_17999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[7], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[7], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[7], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_16000_16999')
    @data(*file_list[6])
    def test_bat_open_fiels07_16000_16999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[6], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[6], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[6], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_15000_15999')
    @data(*file_list[5])
    def test_bat_open_fiels07_15000_15999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[5], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[5], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[5], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_14000_14999')
    @data(*file_list[4])
    def test_bat_open_fiels07_14000_14999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[4], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[4], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[4], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_13000_13999')
    @data(*file_list[3])
    def test_bat_open_fiels07_13000_13999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[3], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[3], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[3], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_12000_12999')
    @data(*file_list[2])
    def test_bat_open_fiels07_12000_12999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[2], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[2], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[2], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_21000_21999')
    @data(*file_list[1])
    def test_bat_open_fiels07_11000_11999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[1], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[1], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[1], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_fiels07_10000_10999')
    @data(*file_list[0])
    def test_bat_open_files07_10000_10999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[0], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[0], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[0], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    # ***************** MS-2003 **********************
    @unittest.skip('skip test_bat_open_files_other')
    @data(*file_list[20])
    def test_bat_open_files_other(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[20], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[20], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[20], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_39000_39999')
    @data(*file_list[19])
    def test_bat_open_files_39000_39999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[19], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[19], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[19], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_38000_38999')
    @data(*file_list[18])
    def test_bat_open_files_38000_38999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[18], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[18], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[18], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_37000_37999')
    @data(*file_list[17])
    def test_bat_open_files_37000_37999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[17], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[17], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[17], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_36000_36999')
    @data(*file_list[16])
    def test_bat_open_files_36000_36999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[16], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[16], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[16], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_35000_35999')
    @data(*file_list[15])
    def test_bat_open_files_35000_35999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[15], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[15], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[15], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_34000_34999')
    @data(*file_list[14])
    def test_bat_open_files_34000_34999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[14], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[14], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[14], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_33000_33999')
    @data(*file_list[13])
    def test_bat_open_files_33000_33999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[13], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[13], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[13], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_32000_32999')
    @data(*file_list[12])
    def test_bat_open_files_32000_32999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[12], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[12], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[12], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_31000_31999')
    @data(*file_list[11])
    def test_bat_open_files_31000_31999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[11], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[11], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[11], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_30000_30999')
    @data(*file_list[10])
    def test_bat_open_files_30000_30999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[10], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[10], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[10], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_29000_29999')
    @data(*file_list[9])
    def test_bat_open_files_29000_29999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[9], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[9], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[9], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_28000_28999')
    @data(*file_list[8])
    def test_bat_open_files_28000_28999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[8], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[8], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[8], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_27000_27999')
    @data(*file_list[7])
    def test_bat_open_files_27000_27999(self, file_name='33843.xls'):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[7], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[7], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[7], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_26000_26999')
    @data(*file_list[6])
    def test_bat_open_files_26000_26999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[6], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[6], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[6], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_25000_25999')
    @data(*file_list[5])
    def test_bat_open_files_25000_25999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[5], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[5], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[5], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_24000_24999')
    @data(*file_list[4])
    def test_bat_open_files_24000_24999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[4], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[4], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[4], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_23000_23999')
    @data(*file_list[3])
    def test_bat_open_files_23000_23999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[3], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[3], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[3], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_22000_22999')
    @data(*file_list[2])
    def test_bat_open_files_22000_22999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[2], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[2], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[2], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_21000_21999')
    @data(*file_list[1])
    def test_bat_open_files_21000_21999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[1], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[1], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[1], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

    @unittest.skip('skip test_bat_open_files_20000_20999')
    @data(*file_list[0])
    def test_bat_open_files_20000_20999(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path_list[0], file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            shutil.copy(os.path.join(path_list[0], file_name), pc_path)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path_list[0], file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')
