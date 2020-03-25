#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import unittest

from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from businessView.pgView import PGView
from businessView.ssView import SSView
from businessView.wpView import WPView
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


class openFiles(StartEnd):

    # @unittest.skip('skip test_bat_open_files')
    def test_bat_open_files(self):
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        for file in suffix_path:
            logging.info('>>>>>>start test')
            file_name = file.split('/')[-1]
            hp = HomePageView(self.driver)
            wp = WPView(self.driver)
            ss = SSView(self.driver)
            pg = PGView(self.driver)
            try:
                os.system(
                    'adb -s %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulated/0/%s' % (
                        udid, file))

                if not file_name.endswith(('.xls', 'xlsx', '.doc', 'docx', '.ppt', 'pptx')):
                    logging.error('file format wrong！')
                    copy_file_to_wrong(dir_path, file)
                    continue

                logging.info('>>>>>>>search %s' % file_name)
                self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(file_name)
                self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
                logging.info('searching...')
                result = hp.is_not_visible('//*[@text="文件搜索.."]', 60)
                if not result:
                    logging.error('searching timeout!')
                    hp.getScreenShot('searching timeout')
                    copy_file_to_wrong(dir_path, file)
                    continue
                if not hp.get_element_result('//android.widget.TextView[@text="%s"]' % file_name):
                    logging.error('no file!')
                    hp.getScreenShot('no file')
                    copy_file_to_wrong(dir_path, file)
                    continue
                else:
                    logging.info('got it!!!')

                # 打开指定文档
                logging.info('>>>>>>open file: %s' % file_name)
                self.driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@text="%s"]' % file_name).click()  # 打开对应文件

                # 加载
                loading_result = hp.is_not_visible('//*[contains(@text, "正在打开")]')
                if not loading_result:
                    logging.error('loading timeout')
                    raise

                # 弹出问题信息框
                if hp.get_element_result('//*[@text="提示"]') or hp.get_element_result(
                        '//*[contains(@text,"很抱歉")]'):
                    hp.getScreenShot(file_name + 'down info')
                    logging.error('shutdown app!')
                    raise

                # 弹出普通信息框
                try:
                    self.driver.find_element(By.XPATH, '//*[@text="确定"]').click()
                except Exception:
                    pass

                # 判定是否具备打开成功的条件
                if hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_main_option_title_container"]', 20):
                    logging.info('*****' + file_name + ' Open Success first!*****')
                else:
                    logging.info('+++++' + file_name + ' Open Failed first!+++++')
                    raise

                # 切换为编辑模式
                logging.info('>>>>>>edit file, then save')
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()
                ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_scale_motion_helper_layout_id')
                if file_name.endswith(('.doc', 'docx')):
                    hp.tap(200, 350)
                    self.driver.keyevent(30)
                elif file_name.endswith(('.xls', 'xlsx')):
                    hp.tap(110, 250)
                    hp.tap(388, 354)
                else:
                    ele = self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_main_view_container')
                    self.driver.find_element(By.XPATH,
                                             '//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.View[1]').click()
                    hp.tap(474, 1680)
                # 切换为阅读模式
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode').click()

                # 截图
                logging.info('first capture file')
                ele.screenshot('../screenshots/capture_first.png')

                # 保存
                logging.info('save file')
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
                hp.is_not_visible('//*[contains(@text, "文档保存中...")]')
                save_result = hp.get_toast_message('保存成功')
                self.assertTrue(save_result)

                # 关闭功能
                logging.info('>>>>>>close file: %s' % file_name)
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

                close_result = hp.check_close_file()
                self.assertTrue(close_result, msg='close file failed first')

                # 打开指定文档
                logging.info('>>>>>>second time open file: %s' % file_name)
                self.driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@text="%s"]' % file_name).click()  # 打开对应文件

                # 加载
                loading_result = hp.is_not_visible('//*[contains(@text, "正在打开")]')
                if not loading_result:
                    logging.error('loading timeout')
                    raise

                # 判定是否具备打开成功的条件
                if hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_main_option_title_container"]', 30):
                    logging.info('*****' + file_name + ' Open Success second!*****')
                else:
                    logging.info('+++++' + file_name + ' Open Failed second!+++++')
                    raise

                # 截图
                logging.info('second capture file')
                ele.screenshot('../screenshots/capture_second.png')

                result1 = hp.compare_pic('capture_first.png', 'capture_second.png')
                if file_name.endswith(('.doc', '.docx')):
                    self.assertEqual(result1, 0.0, 'two captures have difference')
                else:
                    self.assertLessEqual(result1, 200, 'two captures have difference')

                # 关闭功能
                logging.info('>>>>>>close file: %s' % file_name)
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
                close_result = hp.check_close_file()
                self.assertTrue(close_result, msg='close file failed second')

            except Exception:
                logging.info('+++++' + file_name + ' Execute Failed!+++++')
                try:
                    copy_file_to_wrong(dir_path, file)
                    os.system('adb -s %s shell rmdir /mnt/shell/emulated/0/.tmp/Yozo_Office' % udid)
                    self.driver.close_app()
                    self.driver.launch_app()
                    if hp.is_visible('//*[@resource-id = "com.yozo.office:id/im_title_bar_menu_search"]'):
                        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
                    else:
                        raise
                except Exception:
                    pass
