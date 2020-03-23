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

    # @unittest.skip('skip test_bat_open_files')
    def test_bat_open_files(self):
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        for file in suffix_path[:10]:
            file_name = file.split('/')[-1]
            try:
                os.system(
                    'adb -s %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulated/0/%s' % (
                        udid, file))

                logging.info('==========正在打开%s==========' % file_name)
                if not file_name.endswith(('.xls', 'xlsx', '.doc', 'docx', '.ppt', 'pptx')):
                    self.assertTrue(False, 'file format wrong')
                hp = HomePageView(self.driver)
                logging.info('==========查找==========')
                search_result = hp.search_file1(file_name)
                self.assertTrue(search_result, 'cannot find file')
                open_result = hp.open_file(file_name)
                self.assertTrue(open_result, '%s open failed!' % file_name)
                hp.close_file()
                close_result = hp.check_close_file()
                self.assertTrue(close_result, msg='close file failed')
            except Exception:
                copy_file_to_wrong(dir_path, file_name)

    @unittest.skip('skip test_bat_open_files07')
    # @data(*suffix_path[:10])
    def test_bat_open_files1(self, file='44000.xlsx'):
        file_name = file.split('/')[-1]
        logging.info('==========正在打开%s==========' % file_name)
        if not file_name.endswith(('.xls', 'xlsx', '.doc', 'docx', '.ppt', 'pptx')):
            copy_file_to_wrong(dir_path, file_name)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        if not search_result:
            copy_file_to_wrong(dir_path, file_name)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            copy_file_to_wrong(dir_path, file_name)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        close_result = hp.check_close_file()
        if not close_result:
            copy_file_to_wrong(dir_path, file_name)
        self.assertTrue(close_result, msg='close file failed')
