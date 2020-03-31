#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import time

from selenium.webdriver.common.by import By

from appium_sync.appium_devices_sync import dir_path
from businessView.homePageView import HomePageView
from common.tool import copy_file_to_wrong


class openFiles(object):

    def __init__(self, driver):
        self.driver = driver

    def test_bat_open_files(self, suffix_path, udid):
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        start_time = time.time()
        for file in suffix_path[:10]:
            logging.info('>>>>>>start test')
            file_name = file.split('/')[-1]
            hp = HomePageView(self.driver)
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

                # 打开指定文档
                logging.info('>>>>>>open file: %s' % file_name)
                self.driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@text="%s"]' % file_name).click()  # 打开对应文件

                # 加载
                loading_result = hp.is_not_visible('//*[contains(@text, "正在打开")]')
                if not loading_result:
                    logging.error('loading timeout')
                    raise

                # 弹出普通信息框
                try:
                    self.driver.find_element(By.XPATH, '//*[@text="确定"]').click()
                except Exception:
                    logging.info('=====no messages at the begin of open file')
                else:
                    logging.info('=====some messages at the begi n of open file')

                if hp.is_visible('//*[@resource-id="com.yozo.office:id/yozo_ui_main_option_title_container"]', 20):
                    logging.info('*****' + file_name + ' Open Success first!*****')
                else:
                    logging.info('+++++' + file_name + ' Open Failed first!+++++')
                    raise

                # 关闭功能
                logging.info('>>>>>>close file: %s' % file_name)
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()

                close_result = hp.check_close_file()
                self.assertTrue(close_result, msg='close file failed first')

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
            else:
                logging.info('+++++' + file_name + ' Execute Success!+++++')
            end_time = time.time()
            last_time = end_time - start_time
            logging.info('>>>>>>>>>>>>>last_time:%s' % last_time)
