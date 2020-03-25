import os
import logging
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from common.device import Device
from common.myunit import StartEnd
from common.tool import copy_file_to_wrong
from test_run.run_batch_open import test_dirs, dir_path

path_list = []
suffix_path = []
udid = Device.dev
# print(f'udid:{udid}')

for i in test_dirs:
    sub_dir_path = os.path.join(dir_path, i)
    path_list.append(sub_dir_path)
    os.system('adb -s %s shell rm -rf /mnt/shell/emulated/0/%s' % (udid, i))
    os.system('adb -s %s push %s /mnt/shell/emulated/0' % (udid, sub_dir_path))

    print(sub_dir_path)
    for root, dirs, files in os.walk(sub_dir_path):
        for file in files:
            suffix_path.append(i + '/' + file)


@ddt
class openFiles(StartEnd):

    @unittest.skip('skip test_bat_open_files07')
    # @data(*suffix_path)
    def test_bat_open_files1(self, file='44000.xlsx'):
        file_name = file.split('/')[-1]
        logging.info('==========正在打开%s==========' % file_name)
        hp = HomePageView(self.driver)
        try:
            if not file_name.endswith(('.xls', 'xlsx', '.doc', 'docx', '.ppt', 'pptx')):
                self.assertTrue(False, 'file format wrong')
            search_result = hp.search_file(file_name)
            self.assertTrue(search_result, 'cannot find file')
            open_result = hp.open_file(file_name)
            self.assertTrue(open_result, 'open file failed')
            hp.close_file()
            close_result = hp.check_close_file()
            self.assertTrue(close_result, msg='close file failed')
        except Exception:
            logging.error('%s execute Failed' % file)
            copy_file_to_wrong(dir_path, file_name)
