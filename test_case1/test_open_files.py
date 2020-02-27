import os
import shutil
import unittest
import logging
from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd

path1 = r'E:\MSfiles\MS2003files\xls\23000-23999'
file_names = []
for root, dirs, files in os.walk(path1):
    for f in files:
        file_names.append(f)


@ddt
class OpenFiles(StartEnd):

    @data(*file_names)
    def test_bat_open_files(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)
        try:
            type1 = os.path.splitext(file_name)[1]
            if type1 != '.xls' and type1 != '.xlsx':
                raise Exception("文件格式为%s" % type1)
            hp = HomePageView(self.driver)
            hp.search_file(file_name)
            hp.open_file(file_name)
            hp.close_file()
            self.assertTrue(hp.check_close_file(), msg='文档关闭失败')
        except Exception as e:
            logging.info(e)
            PC_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
            shutil.copy(os.path.join(path1, file_name), PC_path)
            raise


if __name__ == '__main__':
    unittest.main()
