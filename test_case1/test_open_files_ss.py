import os
import logging
import unittest

from ddt import ddt, data
from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from common.desired_caps import  udid
from common.myunit import StartEnd
from common.tool import copy_file_to_wrong, Device
from test_run.run_batch_open import test_dirs, dir_path

path_list = []
suffix_path = []

for i in test_dirs:
    sub_dir_path = os.path.join(dir_path, i)
    path_list.append(sub_dir_path)
    print(sub_dir_path)
    print(f'udid:{udid}')
    # os.system('adb -s 127.0.0.1:62001 shell rm -rf /mnt/shell/emulated/0/44000-44999')
    os.system('adb -s %s shell rm -rf /mnt/shell/emulated/0/%s' % (udid, i))
    # os.system('adb -s 127.0.0.1:62001 push %s /mnt/shell/emulated/0' %  sub_dir_path)
    os.system('adb -s %s push %s /mnt/shell/emulated/0' % (udid, sub_dir_path))
    for root, dirs, files in os.walk(sub_dir_path):
        for file in files:
            suffix_path.append(i + '/' + file)


# for i in path_list:
#     file_list = file_list + get_files_list(i)
#     os.system('adb -s %s push %s /mnt/shell/emulated/0' % (udid, i))


@ddt
class openFiles(StartEnd):

    def test_bat_open_files(self):
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        for file in suffix_path[:10]:
            try:
                file_name = file.split('/')[-1]
                os.system(
                    'adb -s %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulatec/0/%s' % file)
                logging.info('==========正在打开%s==========' % file_name)
                if not file_name.endswith(('.xls', 'xlsx', '.doc', 'docx', '.ppt', 'pptx')):
                    self.assertTrue(False, 'file format wrong')
                hp = HomePageView(self.driver)
                logging.info('==========查找==========')
                search_result = hp.search_file1(file_name)
                self.assertTrue(search_result, 'cannot find file')
                open_result = hp.open_file(i)
                self.assertTrue(open_result, '%s open failed!' % file_name)
                hp.close_file()
                close_result = hp.check_close_file()
                self.assertTrue(close_result, msg='close file failed')
            except Exception:
                copy_file_to_wrong(*path_list, file_name=file_name)

    # # @unittest.skip('skip test_bat_open_files07')
    # @data(*suffix_path[:10])
    # def test_bat_open_files(self, file_name='44000.xlsx'):
    #
    #     logging.info('==========正在打开%s==========' % file_name)
    #     if not file_name.endswith(('.xls', 'xlsx', '.doc', 'docx', '.ppt', 'pptx')):
    #         copy_file_to_wrong(*path_list, file_name=file_name)
    #         self.assertTrue(False, 'file format wrong')
    #     hp = HomePageView(self.driver)
    #     search_result = hp.search_file(file_name)
    #     if not search_result:
    #         copy_file_to_wrong(*path_list, file_name=file_name)
    #     self.assertTrue(search_result, 'cannot find file')
    #     open_result = hp.open_file(file_name)
    #     if not open_result:
    #         copy_file_to_wrong(*path_list, file_name=file_name)
    #     self.assertTrue(open_result, 'open file failed')
    #     close_result = hp.check_close_file()
    #     if not close_result:
    #         copy_file_to_wrong(*path_list, file_name=file_name)
    #     self.assertTrue(close_result, msg='close file failed')
