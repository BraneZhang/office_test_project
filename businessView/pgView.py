#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from businessView.generalView import GeneralView


class PGView(GeneralView):

    def switch_mode(self, switch, apply='one'):  # 切换
        logging.info('==========switch_mode==========')
        # switch = ['无切换', '平滑淡出', '从全黑淡出', '切出', '从全黑切出', '溶解', '向下擦除', '向左擦除', '向右擦除',
        #           '向上擦除', '扇形展开', '从下抽出', '从左抽出', '从右抽出', '从上抽出', '从左下抽出', '从左上抽出',
        #           '从右下抽出', '从右上抽出', '盒状收缩', '盒状展开', '1根轮辐', '2根轮辐', '3根轮辐', '4根轮辐', '8根轮辐',
        #           '上下收缩', '上下展开', '左右收缩', '左右展开', '左下展开', '左上展开', '右下展开', '右上展开', '圆形',
        #           '菱形', '加号', '新闻快报', '向下推出', '向左推出', '向右推出', '向上推出', '向下插入', '向左插入',
        #           '向右插入', '向上插入', '向左下插入', '向左上插入', '向右下插入', '向右上插入', '水平百叶窗',
        #           '垂直百叶窗', '横向棋盘式', '纵向棋盘式', '水平梳理', '垂直梳理', '水平线条', '垂直线条', '随机']
        ranges = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
        switch_ele = '//*[@text="%s"]' % switch
        self.swipe_search2(switch_ele, ranges)
        self.driver.find_element(By.XPATH, switch_ele).click()
        if not apply == 'one':
            for i in range(3):
                eles = self.driver.find_elements(By.XPATH, ranges)
                self.swipe_ele1(eles[0],eles[-1])
            self.driver.find_element(By.ID,'com.yozo.office:id/yozo_ui_pg_option_id_transition_apply_all').click()

    def pause_resume_play(self):  # 暂停、回复播放
        logging.info('==========pause_resume==========')
        # self.find_element(By.ID,'com.yozo.office:id/yozo_ui_id_pg_play_pause_button').click()
        # x, y = self.get_size()
        # self.tap(y * 0.5, x * 0.5)
        self.tap(880, 540)

    def quit_play(self):  # 退出播放
        logging.info('==========quit_paly==========')
        self.driver.keyevent(4)

    def play_mode(self, mode='autoplay'):  # 播放模式 current,first,autoplay
        logging.info('==========play_mode==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_play_%s' % mode).click()

    def edit_template(self, template):  # 模板
        logging.info('==========edit_template==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_edit_templet').click()
        range = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout'
        eles = self.driver.find_elements(By.XPATH, range)
        template_ele = '%s[@index="%s"]' % (range, template)
        if int(template) > 8:
            self.swipe_ele1(eles[-1], eles[0])
        self.driver.find_element(By.XPATH, template_ele).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def edit_format(self, format):  # 版式
        # format = ['标题与副标题', '标题', '标题与文本', '标题与两栏文本', '标题与竖排文本-上下', '标题与竖排文本-左右',
        #           '空白','标题与图片','标题、文本与图片','标题、图片与文本','标题、图片与竖排文本','标题、竖排文本与图片']
        logging.info('==========edit_format==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_option_id_edit_format').click()
        range = '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout'
        format_ele = '//*[@text="%s"]' % format
        self.swipe_search2(format_ele, range)
        self.driver.find_element(By.XPATH, format_ele).click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_back_button').click()

    def thumbnail_scroll(self):  # 缩略图滚屏
        logging.info('==========thumbnail_scroll==========')
        eles = self.driver.find_elements(By.XPATH, '//android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                                   '/android.view.View')
        if len(eles) >= 3:
            self.swipe_ele2(eles[2], eles[0])

    def add_new(self):  # 新建
        logging.info('==========add_new==========')
        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_pg_add_slide_button_id').click()

    def search_slide(self, index):  # 查找幻灯片
        logging.info('==========search_slide==========')
        for i in range(10000):
            if not self.get_element_result('//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.View[@index="%s"]' % (int(index) - 1)):
                self.thumbnail_scroll()
            else:
                break
        self.driver.find_element(By.XPATH, '//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.View[@index="%s"]' % (int(index) - 1)).click()

    def check_comment(self, index):
        logging.info('==========add_new==========')
        self.search_slide(index)

        if self.get_element_result('//android.widget.Button'):
            self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()

    def delete_comment(self):  # 删除备注
        logging.info('==========edit_comment==========')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_note_body_delete_note').click()

    def edit_comment(self, comment):  # 编辑备注
        logging.info('==========edit_comment==========')
        self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_note_body_edit_note').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_et').set_text(comment)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_ok').click()

    def add_comment(self, index, comment):  # 插入备注
        logging.info('==========add_comment==========')
        time.sleep(2)
        self.search_slide(index)

        if not self.get_element_result('//*[@text="备注"]'):
            self.group_button_click('插入')
        self.driver.find_element(By.XPATH, '//*[@text="备注"]').click()
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_et').set_text(comment)
        self.driver.find_element(By.ID, 'com.yozo.office:id/yozo_ui_pg_eidt_note_ok').click()

    def insert_new_ppt(self):
        """
        菜单插入幻灯片
        :return:
        """
        logging.info('==========insert_new_ppt==========')
        if not self.get_element_result('//*[@text="幻灯片"]'):
            self.group_button_click('插入')
        self.driver.find_element(By.XPATH, '//*[@text="幻灯片"]').click()

    def screenshot_edit_ppt(self, file_name):
        """
        截取当前编辑的ppt图片
        注：工具栏会被收缩
        :param file_name:
        :return:
        """
        logging.info('==========screenshot_current_editPpt==========')
        try:
            self.driver.find_element(By.CLASS_NAME, 'android.support.v4.view.ViewPager')
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(By.ID,
                                     'com.yozo.office:id/yozo_ui_option_expand_button').click()
        time.sleep(1)
        self.driver.find_element(By.ID, 'com.yozo.office:id/a0000_pg_slide_view_id').screenshot(file_name)

    def play_to_first(self, start_page):
        """
        非自动播放下，点击播放至首页
        :param start_page: 起始播放页，首页为0
        :return: None
        """
        x, y = self.get_size()
        while start_page > 0:
            time.sleep(1)
            self.tap(y * 0.25, x * 0.5)
            start_page -= 1

    def play_to_last(self, start_page, total_pages):
        """
        非自动播放下，点击播放至最后页
        :param start_page: 起始播放页，首页为0
        :param total_pages: ppt总页数
        :return: None
        """
        x, y = self.get_size()
        while total_pages-start_page > 1:
            time.sleep(1)
            self.tap(y * 0.75, x * 0.5)
            start_page += 1


if __name__ == '__main__':
    waylist = ['wx', 'qq', 'ding', 'mail']
    wps = ['wp', 'ss', 'pg']
    # ss = list(map(lambda x,y:x+'_'+y,wps,waylist))
    # ss = list(map(lambda x:x+'_wx',wps))
    ss = []
    for i in wps:
        for j in waylist:
            ss.append(i+'_'+j)
    print(ss)
    # for i in range(12):
    #     print(i)
