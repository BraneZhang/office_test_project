#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import time

from selenium.webdriver.common.by import By

from appium_sync.appium_devices_sync import dir_path
from businessView.homePageView import HomePageView
from common.tool import copy_file_to_wrong


class openFilesPDF():

    def __init__(self, driver):
        """初始化"""
        self.driver = driver

    def test_bat_open_files(self, suffix_path, udid):
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()
        start_time = time.time()
        for file in suffix_path:
            logging.info('>>>>>>start test')
            file_name = file.split('/')[-1]
            hp = HomePageView(self.driver)
            try:
                os.system(
                    'adb -s %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulated/0/%s' % (
                        udid, file))

                if not file_name.endswith(('.pdf')):
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

                # 确认是否打开成功
                hp.tap(550, 950, 3)
                if hp.get_element_result('//*[@text="无效或损坏的 PDF 文件。"]'):
                    logging.info('+++++' + file_name + ' Open Failed !+++++')
                    raise
                else:
                    logging.info('*****' + file_name + ' Open Success !*****')

                # 关闭功能
                logging.info('>>>>>>close file: %s' % file_name)
                self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()
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
