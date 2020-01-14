#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import time
from random import randint

from selenium.webdriver.common.by import By

from businessView.homePageView import HomePageView
from common.myunit import StartEnd


class TestEBen(StartEnd):

    def test_new_file_edit_30min_save(self):
        os.system('adb shell rm -rf /storage/emulated/0/Office_Docs/new_edit30save.doc')
        logging.info('==========test_new_file_edit_30min_save==========')
        hp = HomePageView(self.driver)
        self.driver.find_element(By.ID, 'com.yozo.office:id/_toolbar_btn_insert').click()  # 新建“+”
        self.driver.find_element(By.XPATH, '//*[@text="文字"]').click()  # 选择文字
        self.driver.find_element(By.XPATH, '//*[@text="空白"]/../android.widget.LinearLayout').click()  # 新建button
        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_scale_motion_helper_layout_id').click()  # 进入编辑状态

        start_time = time.time()
        for i in range(10):
            self.driver.keyevent(randint(29, 54))
        end_time = time.time()

        last_time = end_time - start_time
        print(f'las_ttime:{last_time}')
        while last_time < 32 * 60:
            self.driver.keyevent(randint(29, 54))
            end_time = time.time()
            last_time = end_time - start_time

        self.driver.find_element(By.ID, 'com.yozo.office:id/title_bar_save_phone_text').click()  # 保存
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/select_save_path_btn_next').is_displayed(),
                        '下一步未显示')
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/select_save_path_btn_next').click()  # 下一步
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/btn_save').is_displayed(), '保存按钮未显示')
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/edit_save_name').set_text('new_edit30save')  # 保存
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_save').click()  # 保存
        saving = hp.get_element_result('//*[@text="正在保存文档，请稍候..."]')
        self.assertTrue(saving == True, '保存过程未显示')
        self.assertTrue(hp.get_toast_message('保存完成'))

    def test_exist_file_edit_30min_save(self):
        os.system('adb shell rm -rf /storage/emulated/0/Office_Docs/exist_edit30save.doc')
        logging.info('==========test_new_file_edit_30min_save==========')
        hp = HomePageView(self.driver)
        self.driver.find_element(By.ID, 'com.yozo.office:id/_toolbar_btn_insert').click()  # 新建“+”
        self.driver.find_element(By.XPATH, '//*[@text="文字"]').click()  # 选择文字
        self.driver.find_element(By.XPATH, '//*[@text="空白"]/../android.widget.LinearLayout').click()  # 新建button
        # self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_scale_motion_helper_layout_id').click()  # 进入编辑状态

        self.driver.find_element(By.ID, 'com.yozo.office:id/title_bar_save_phone_text').click()  # 保存
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/select_save_path_btn_next').is_displayed(),
                        '下一步未显示')
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/select_save_path_btn_next').click()  # 下一步
        self.assertTrue(self.driver.find_element(By.ID, 'com.yozo.office:id/btn_save').is_displayed(), '保存按钮未显示')
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'com.yozo.office:id/edit_save_name').set_text('exist_edit30save')  # 保存
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_save').click()  # 保存
        saving = hp.get_element_result('//*[@text="正在保存文档，请稍候..."]')
        self.assertTrue(saving == True, '保存过程未显示')
        self.assertTrue(hp.get_toast_message('保存完成'))

        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_scale_motion_helper_layout_id').click()  # 进入编辑状态
        start_time = time.time()
        for i in range(10):
            self.driver.keyevent(randint(29, 54))
        end_time = time.time()

        last_time = end_time - start_time
        print(f'las_ttime:{last_time}')
        while last_time < 32 * 60:
            self.driver.keyevent(randint(29, 54))
            end_time = time.time()
            last_time = end_time - start_time

        self.driver.find_element(By.ID, 'com.yozo.office:id/title_bar_save_phone_text').click()  # 保存
        saving = hp.get_element_result('//*[@text="正在保存文档，请稍候..."]')
        self.assertTrue(saving == True, '保存过程未显示')
        self.assertTrue(hp.get_toast_message('保存完成'))
