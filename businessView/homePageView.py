#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import random
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

from businessView.elementRepo import *
from common.common_fun import Common


class HomePageView(Common):

    def open_folder(self, folder):
        """
        打开中进入[手机、存储卡（若有）、我的文档、Download、QQ、TIM、微信、常用位置]文件夹，不包含子文件夹
        :return:
        """
        common = Common(self.driver)
        if folder not in ['手机', '存储卡', '云文档']:
            flag = False
            while not flag:
                try:
                    self.driver.find_element(By.XPATH, '//*[@text=%s]' % folder)
                except NoSuchElementException:
                    last_folder = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_folder_item_name')[-1]
                    last_name = last_folder.text
                    common_use = self.driver.find_element(By.XPATH, '//*[@text="常用"]')
                    common.swipe_ele1(last_folder, common_use)
                    last_folder = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_folder_item_name')[-1]
                    if last_folder.text == last_name:
                        pass
                        # self.assertTrue(False, '常用中不存在该文件夹，请检查')
                else:
                    flag = True
                    self.driver.find_element(By.XPATH, '//*[@text=%s]' % folder).click()
        else:
            self.driver.find_element(By.XPATH, '//*[@text=%s]' % folder).click()

    def recycle_files_clear(self):
        logging.info('==========recycle_files_revert==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        if not self.is_not_visible('//*[@text="数据加载中.."]'):
            logging.error('回收站加载过长')
            return False
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_clear_all').click()
        self.check_option(True)
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_back').click()
        return self.get_toast_message('已清空')

    def recycle_files_revert(self, *num):
        logging.info('==========recycle_files_revert==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        if not self.is_not_visible('//*[@text="数据加载中.."]'):
            logging.error('回收站加载过长')
            return False
        eles = self.find_elements(By.ID, 'com.yozo.office:id/file_item')
        if len(eles) == 0:
            logging.error('回收站无文件')
            return False
        for index in num:
            eles[index].find_element(By.ID, 'com.yozo.office:id/yozo_ui_file_list_item_check').click()
        # map(lambda index:eles[index].find_element(By.ID,'com.yozo.office:id/yozo_ui_file_list_item_check').click(),num)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_recycle_revert').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_back').click()
        return self.get_toast_message('已还原')

    def recycle_files_delete(self, *num):
        logging.info('==========recycle_files_delete==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_mydel').click()
        if not self.is_not_visible('//*[@text="数据加载中.."]'):
            logging.error('回收站加载过长')
            return False
        eles = self.find_elements(By.ID, 'com.yozo.office:id/file_item')
        if len(eles) == 0:
            logging.error('回收站无文件')
            return False
        for index in num:
            eles[index].find_element(By.ID, 'com.yozo.office:id/yozo_ui_file_list_item_check').click()
        # map(lambda index:eles[index].find_element(By.ID,'com.yozo.office:id/yozo_ui_file_list_item_check').click(),num)
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv_recycle_delete').click()
        self.check_option(True)
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_back').click()
        return self.get_toast_message('已删除')

    def templates_access(self, file_type='wp', *options):  # 模板获取：收藏或者下载
        logging.info('==========templates_access==========')
        time.sleep(2)
        self.tap(925, 1669)
        time.sleep(2)
        type_dict = {'wp': 3, 'ss': 2, 'pg': 1}
        self.driver.find_element(By.XPATH, '//android.widget.ImageButton[%s]' % type_dict[file_type]).click()
        null_file = '//*[@resource-id="com.yozo.office:id/createEmpty"]'
        if not self.exist(null_file):
            return False
        self.driver.find_element(By.ID, 'com.yozo.office:id/card1').click()  # 选取模板目前写死
        for i in options:
            if i == '收藏':
                self.driver.find_element(By.ID, 'com.yozo.office:id/star').click()
                if not self.get_toast_message('已收藏'):
                    logging.error('收藏失败')
                    return False
            elif i == '下载':
                self.driver.find_element(By.ID, 'com.yozo.office:id/download').click()
                if not self.is_not_visible('//*[@text="请稍等..."]'):
                    logging.error('请稍等加载失败')
                    return False
                if not self.get_toast_message('模板文件下载成功'):
                    logging.error('模板文件下载成功提示失败')
                    return False
            time.sleep(2)
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/back').click()
        return True

    def templates_delete(self, check=True):
        logging.info('==========templates_option==========')  # 目前写死
        self.driver.find_element(By.XPATH, '//*[@text="批量管理"]').click()
        self.swipe_options('//*[@resource-id="com.yozo.office:id/rv"]')
        sup_ele = self.driver.find_element(By.ID, 'com.yozo.office:id/rv')
        sub_eles = sup_ele.find_elements(By.ID, 'com.yozo.office:id/tpTitle')
        names = list(map(lambda e: e.text, sub_eles))
        list(map(lambda e: e.click(), sub_eles))
        self.driver.find_element(By.ID, 'com.yozo.office:id/btnTv').click()
        self.check_option(check)
        results = list(map(lambda e: self.get_element_result('//*[@text="%s"]' % e), names))
        return True if False in results else False

    def templates_preview(self, view_type):
        logging.info('==========templates_preview==========')
        view_dict = {'收藏': 'Left', '下载': 'Right'}
        self.login_needed()
        self.jump_to_index('my')
        self.driver.find_element(By.ID, 'com.yozo.office:id/mouldSec').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/tv%s' % view_dict[view_type]).click()
        eles = self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
        return True if len(eles) > 0 else False

    def screen_rotate(self, rotate):  # 旋转屏幕
        logging.info('==========screen_rotate==========')
        # allowed_values = ['LANDSCAPE', 'PORTRAIT']
        self.driver.orientation = rotate

    def check_rotate(self):
        logging.info('==========check_rotate==========')
        f_width = self.driver.get_window_size()['width']
        print(f_width)
        self.screen_rotate('LANDSCAPE')
        s_width = self.driver.get_window_size()['height']
        print(s_width)
        if f_width == s_width:
            return True
        else:
            return False

    def share_file_index(self, way):  # 主页分享
        logging.info('=========file_more_info==========')
        # share_list = ['qq', 'wechat', 'email', 'ding']
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_%s_share' % way).click()
        if way == 'more':
            ranges = '//androidx.recyclerview.widget.RecyclerView'
            target = '//*[@text="钉钉"]'
            while not self.get_element_result(target):
                self.swipe_options(ranges)
            self.driver.find_element(By.XPATH, target).click()

    def check_mark_satr(self, file):
        logging.info('=========check_mark_satr==========')
        # ele = '//*[@text="%s"]/following-sibling::android.widget.ImageView' % file
        ele = '//*[@text="%s"]/../android.widget.ImageView' % file
        # ele = '//*[@text="%s"]/parent::android.widget.LinearLayout/android.widget.ImageView' % file
        return self.get_element_result(ele)

    def mark_star(self):
        logging.info('=========file_more_info==========')

        self.click_element(*star)

    def file_more_info(self, index):  # 查看指定文件信息
        logging.info('=========file_more_info==========')
        ele = self.driver.find_element(By.CLASS_NAME, 'androidx.recyclerview.widget.RecyclerView')
        eles = ele.find_elements(*item)
        if index < 0:
            eles[0].find_element(*more_options).click()
        elif index > len(eles):
            eles[-1].find_element(*more_options).click()
        else:
            eles[index].find_element(*more_options).click()
        file_name1 = self.find_element(*file_name).text
        file_type1 = self.find_element(*file_type).text
        file = file_name1 + '.' + file_type1
        location = self.find_element(*file_location).text
        return {'file_name': file, 'location': location}

    def check_select_file_type(self, file_type):
        logging.info('==========check_select_file_type==========')
        suffix_dict = {'all': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf'], 'wp': ['doc', 'docx'],
                       'ss': ['xls', 'xlsx'], 'pg': ['ppt', 'pptx'], 'pdf': ['pdf']}
        eles = self.driver.find_elements(By.ID, 'com.yozo.office:id/tv_title')
        eles_str = list(map(lambda x: x.text, eles))
        eles_suffix = list(set(map(lambda x: x[x.rindex('.') + 1:].lower(), eles_str)))
        print(eles_suffix)
        if [False for i in eles_suffix if i not in suffix_dict[file_type]]:
            return False
        else:
            return True

    def select_file_type(self, file_type):  # 文档类型
        logging.info('==========select_file_type==========')
        # type_list = ['all', 'wp', 'ss', 'pg', 'pdf']
        logging.info('select %s files', file_type)
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_filetype_%s' % file_type).click()
        time.sleep(2)

    def open_local_folder(self, folder_type):  # 打开本地文档
        logging.info('==========open_local_folder==========')
        # folder_list = ['手机', '我的文档', 'Download', 'QQ', '微信']
        if folder_type == '微信':
            self.swipe_options('//*[@resource-id="com.yozo.office:id/lv_floder_list"]')
        self.driver.find_element(By.XPATH, '//*[@text="%s"]' % folder_type).click()

    def check_open_folder(self, folder):
        logging.info('==========check_open_folder==========')
        folder_dict = {'手机': '浏览目录 > 手机', '我的文档': ' > Documents', 'Download': ' > Download',
                       'QQ': ' > QQfile_recv', '微信': ' > Download', 'TIM': ' > TIMfile_recv'}
        path = self.driver.find_elements(By.XPATH, '//*[@resource-id="com.yozo.office:id/name_layout"]'
                                                   '/android.widget.TextView')[-1].text
        if path == folder_dict[folder]:
            return True
        else:
            return False

    def search_file(self, keyword):
        logging.info('==========search_file==========')
        self.find_element(*search).click()
        logging.info('input keyword %s' % keyword)
        self.find_element(*search_input).send_keys(keyword)
        self.find_element(*search_start).click()
        logging.info('searching...')
        result = self.is_not_visible(searching)
        if not result:
            logging.error('searching timeout!')
            self.getScreenShot('searching timeout')
            return False
        if not self.get_element_result('//android.widget.TextView[@text="%s"]' % keyword):
            logging.error('no file!')
            self.getScreenShot('no file')
            return False
        else:
            logging.info('got it!!!')
            return True

    def search_file1(self, keyword):
        logging.info('==========search_file==========')
        logging.info('input keyword %s' % keyword)
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(keyword)
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()
        logging.info('searching...')
        result = self.is_not_visible(searching)
        if not result:
            logging.error('searching timeout!')
            self.getScreenShot('searching timeout')
            return False
        if not self.get_element_result('//android.widget.TextView[@text="%s"]' % keyword):
            logging.error('no file!')
            self.getScreenShot('no file')
            return False
        else:
            logging.info('got it!!!')
            return True

    def jump_to_index(self, file_type='last'):  # 5个主页界面
        logging.info('===========jump_to_%s==========' % file_type)
        # index = ['last', 'alldoc', 'cloud', 'star', 'my']  # office的五个页面组件尾缀
        index = {'last': 0, 'alldoc': 1, 'cloud': 2, 'star': 3, 'my': 4, }
        # self.driver.find_elements(By.ID, 'com.yozo.office:id/ll_tap')[index[file_type]].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_bottommenu_%s' % file_type).click()
        time.sleep(1)

    def sort_files(self, way='type', order='down'):  # 排序
        logging.info('=========sort_files==========')
        # way_list = ['type', 'name', 'size', 'time']
        # order_list = ['up', 'down']
        self.click_element(*sort)
        self.driver.find_element(By.ID, 'com.yozo.office:id/rl_sort_%s' % way).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sort_%s' % order).click()
        time.sleep(1)

    def identify_file_index(self):  # 识别云文档中首个文件
        suffix = (
            '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.pdf', '.txt', '.xlt', '.xltx', '.dot', '.dotx', '.pot',
            '.potx', '.wps', '.wpt', '.et', '.ett', '.dps', '.dpt')
        eles = self.find_elements(*item)

        for i, ele in enumerate(eles):
            ele_name = ele.find_element(*item_title).text
            if ele_name.endswith(suffix):
                return i
        else:
            self.swipe_ele1(eles[-1], eles[0])
            return self.identify_file_index()

    def download_file(self):  # 下载文件
        logging.info('=========download_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="下载"]').click()
        return self.get_toast_message('文件下载成功,已保存至 /storage/emulated/0/yozoCloud 文件夹')

    def select_all(self, select='all', del_list=[]):  # 全选、多选
        logging.info('=========select_all==========')
        self.driver.find_element(By.XPATH, '//*[@text="多选"]').click()
        name_list = []
        if select == 'all':
            self.driver.find_element(By.ID, 'com.yozo.office:id/tv_file_checked_tab_all').click()
        else:
            eles = self.driver.find_elements(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                                       '/android.widget.RelativeLayout')
            # print(len(eles))
            time.sleep(1)
            for i in del_list:
                name = eles[i - 1].find_element(By.ID, 'com.yozo.office:id/tv_title').text
                name_list.append(name)
                eles[i - 1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_check_bottom_del').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        return name_list

    def delete_last_file(self):  # "最近"删除文件
        logging.info('=========delete_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        return self.get_toast_message('此操作只是将文件从最近列表中删除')

    def delete_file(self):  # 删除文件
        logging.info('=========delete_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="删除"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        time.sleep(1)  # 删除加载项尚未能捕捉，先写死

    def rename_file(self, new_name):  # 重命名文件
        logging.info('=========rename_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="重命名"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_newfoldername').set_text(new_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_true').click()
        return self.get_toast_message('操作成功')

    def move_file(self):  # 移动文件
        logging.info('=========move_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="移动"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/framelayout_cover').click()
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        return self.get_toast_message('移动操作成功')

    def copy_file(self):  # 复制文件
        logging.info('=========copy_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="复制"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/framelayout_cover').click()
        time.sleep(1)
        self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[1].click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/btn_move_true').click()
        return self.get_toast_message('操作成功')

    def upload_file(self, filename):  # 上传文件
        logging.info('=========upload_file==========')
        self.driver.find_element(By.XPATH, '//*[@text="上传"]').click()
        if self.get_toast_message('请先登录账号'):
            if not self.get_element_result('//*[@text="我的"]'):
                self.driver.keyevent(4)
            self.jump_to_index('my')
            self.login_from_my('13915575564', 'zhang199412')
            logging.error('未登录')
            return False
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(filename)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()
        self.cover_file(True)
        return self.get_toast_message('上传成功')

    def wifi_trans(self, state='开启'):  # 设置wifi传输的开或者关
        logging.info('=========wifi_trans==========')
        state_set = self.find_element(*wifi_trans).text
        if state != state_set:
            self.click_element(*wifi_trans)

    def opinion_feedback(self, fb='func', content=''):  # 意见反馈
        logging.info('=========suggestion_feedback==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myfb').click()
        # type = ['func', 'content', 'bug', 'other']
        ele = self.driver.find_element(By.ID, 'com.yozo.office:id/%sRg' % fb)
        ele.click()
        checked = ele.get_attribute('checked')
        if checked != 'true':
            return False
        self.driver.find_element(By.ID, 'com.yozo.office:id/contentEt').set_text(content)
        self.driver.find_element(By.ID, 'com.yozo.office:id/uploadTv').click()
        upway = random.randint(0, 2)
        if upway == 0:
            self.driver.find_element(By.ID, 'com.yozo.office:id/photo_sec').click()
            self.driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                               '/android.widget.FrameLayout[1]').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/button_apply').click()
        else:
            self.driver.find_element(By.ID, 'com.yozo.office:id/file_sec').click()
            self.driver.find_element(By.ID, 'com.yozo.office:id/file_item').click()
            self.driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                               '/android.widget.RelativeLayout[2]').click()
            self.driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView'
                                               '/android.widget.RelativeLayout[2]').click()
        uped = self.driver.find_element(By.ID, 'com.yozo.office:id/uploadTv').text
        if uped != '已上传':
            return False
        self.driver.find_element(By.ID, 'com.yozo.office:id/contactEt').set_text('13915575564')
        self.swipeUp()
        self.driver.find_element(By.ID, 'com.yozo.office:id/submitTv').click()
        if self.get_element_result('//*[@text="提交成功"]'):
            return True
        else:
            return False

    def create_file_preoption(self, file_type, x=925, y=1669):  # 新建文档前置操作
        logging.info('==========create_file_preoption_%s==========' % file_type)
        time.sleep(2)
        self.tap(x, y)  # “+”元素不可捕捉，只能通过坐标来点击，坐标不唯一，随手机改变
        time.sleep(2)
        type_dict = {'wp': 3, 'ss': 2, 'pg': 1}
        self.driver.find_element(By.XPATH, '//android.widget.ImageButton[%s]' % type_dict[file_type]).click()
        time.sleep(1)

    def create_file(self, file_type, x=925, y=1669):  # 新建空白文档
        logging.info('==========create_file_%s==========' % file_type)
        self.create_file_preoption(file_type, x, y)
        null_file = '//*[@resource-id="com.yozo.office:id/createEmpty"]'
        if not self.exist(null_file):
            null_file = '//*[@resource-id="com.yozo.office:id/create_empty_offline_img"]'
        self.driver.find_element(By.XPATH, null_file).click()

    def save_as_file(self, file_name, save_path, item=1):  # 另存为
        logging.info('==========save_as_file==========')
        if not self.get_element_result('//*[@text="另存为"]'):
            self.group_button_click('文件')
        self.driver.find_element(By.XPATH, '//*[@text="另存为"]').click()
        if self.get_element_result('//*[@text="保存路径"]'):
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_folder').click()
        self.save_step(save_path, file_name, item)

    def save_file(self):  # 点击保存图标或者保存选项，随机
        logging.info('==========save_file==========')
        if random.randint(0, 1) == 0:
            # self.click_element(*save_confirm)
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save').click()
        else:
            if not self.get_element_result('//*[@text="保存"]'):
                self.group_button_click('文件')
            self.driver.find_element(By.XPATH, '//*[@text="保存"]').click()
            time.sleep(0.5)
            # self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button').click()

    def save_new_file(self, file_name, save_path, item=1):  # 文件名，本地还是云端save_path=['local','cloud']，文件类型item=[1,2]
        logging.info('==========save_exist_file==========')
        self.save_file()
        self.save_step(save_path, file_name, item)

    def save_step(self, save_path, file_name, item):
        logging.info('==========save_step==========')
        logging.info('choose save path %s' % save_path)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('whether need login')
        if self.get_toast_message('您尚未登录，请登录'):
            self.login_action('13915575564', 'zhang199412')
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_%s' % save_path).click()

        logging.info('file named %s' % file_name)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_name').set_text(file_name)

        logging.info('choose file type %s' % item)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_file_type').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/file_type_item%s' % item).click()

        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn').click()  # save
        self.cover_file(True)

    def check_save_file(self):
        logging.info('==========check_create_file==========')
        return self.get_toast_message('保存成功')

    def login_from_my(self, username, password):
        logging.info('==========login_from_my==========')
        self.click_element(*unlogin_state)
        self.login_action(username, password)

    def login_action(self, username, password):  # 登录操作
        logging.info('==========login_action==========')
        # self.driver.find_element(By.ID,'com.yozo.office:id/ll_myinfo_unlogin').click()
        logging.info('username is:%s' % username)
        self.find_element(*account_input).send_keys(username)
        # self.find_element(By.ID, 'com.yozo.office:id/et_account').set_text(username)  # 输入手机号

        logging.info('password is:%s' % password)
        self.find_element(*pwd_input).send_keys(password)
        # self.find_element(By.ID, 'com.yozo.office:id/et_pwd').set_text(password)  # 输入密码

        logging.info('click loginBtn')
        self.find_element(By.ID, 'com.yozo.office:id/btn_login').click()  # 点击登录按钮
        logging.info('login finished!')

    def check_login_status(self):
        logging.info('==========check_login_status==========')
        time.sleep(1)
        try:
            self.find_element(*sys_setting)
        except NoSuchElementException:
            logging.error('login off!')
            return False
        else:
            logging.info('login on!')
            return True

    def logout_action(self):  # 退出登录
        logging.info('==========logout_action==========')
        self.swipe_options('//android.widget.ScrollView')
        self.click_element(*logout)
        self.click_element(*pop_confirm)
        # self.driver.find_element(By.ID, 'com.yozo.office:id/ll_myinfo_logout').click()
        # self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
        logging.info('logout finished!')
        self.click_element(*login_cancel)
        # self.driver.find_element(By.ID, 'com.yozo.office:id/iv_add_back').click()
        time.sleep(1)

    def login_needed(self):  # 需要登录
        logging.info('==========login_needed==========')
        self.jump_to_index('my')
        if not self.check_login_status():
            self.login_from_my('13915575564', 'zhang199412')
        else:
            self.jump_to_index('last')

    def close_file(self):
        logging.info('======close_file=====')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close').click()  # 关闭功能

    def check_close_file(self):
        """
        验证文档是否被关闭
        :return: flag
        """
        logging.info('==========check_close_file==========')
        time.sleep(1)
        flag = False
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close')
        except NoSuchElementException:
            logging.info('==========the file closed==========')
            flag = True
        return flag

    def open_file(self, file_name):
        logging.info('======open_file_%s=====' % file_name)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % file_name).click()  # 打开对应文件

        show_result = self.is_visible(option_title,20)
        if not show_result:
            logging.error('open failed')
            # self.getScreenShot(file_name + ' open fail')
            return False
        else:
            logging.info(file_name + ' open success!')
            return True

    def open_random_file(self, keywords):
        logging.info('======open_random_file=====')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_search').click()  # 点击搜索功能
        self.driver.find_element(By.ID, 'com.yozo.office:id/et_search').send_keys(keywords)  # 输入关键字
        self.driver.find_element(By.ID, 'com.yozo.office:id/iv_search_search').click()  # 点击搜索按钮
        time.sleep(1)
        results_list = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')
        num = random.randint(0, len(results_list) - 1)
        result = self.driver.find_elements(By.ID, 'com.yozo.office:id/file_item')[num]
        result.click()
        try:
            WebDriverWait(self.driver, 30).until(
                lambda driver: self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close'))
            time.sleep(1)
            return True
        except NoSuchElementException:
            return False

    def user_logo(self):
        logging.info('==========user_logo==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/im_title_bar_menu_user').click()

    def check_user_logo(self):
        logging.info('==========check_user_logo==========')
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/rl_myinfo_name')
        except NoSuchElementException:
            logging.error('user logo click Fail!')
            self.getScreenShot('user logo fail clicking')
            return False
        else:
            logging.info('user logo click Success!')
            return True

    # 一直等待某元素可见，默认超时10秒
    def is_visible(self, locator, timeout=60):
        try:
            # ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(self, locator,timeout=60 ):
        try:
            # ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_visible_elements(self, *eles):
        results = list(map(lambda e: self.is_visible(3,e), eles))
        if False in results:
            logging.error('element loading timeout')
            return False
        else:
            return True
