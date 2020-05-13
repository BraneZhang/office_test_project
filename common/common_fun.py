import math
import operator
import cv2 as cv
from argparse import Action
from functools import reduce

from PIL import Image
from airtest.core.cv import Template
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time, os
import csv

from businessView.elementRepo import *
from common.tool import get_project_path

width_cell = 263
height_cell = 55
x0 = 0
x1 = 110
y0 = 240
y1 = 295


class Common(BaseView):

    def find_image_cv(self, obj_path, src_path):
        source = cv.imread(src_path)
        template = cv.imread(obj_path)
        # print('source')
        # print(source.shape)
        # print('template')
        # print(template.shape)
        result = cv.matchTemplate(source, template, cv.TM_CCOEFF_NORMED)
        # print('result')
        # print(result)
        # print(len(result))
        pos_start = cv.minMaxLoc(result)[3]
        test = cv.minMaxLoc(result)
        # print('pos_start')
        # print(pos_start)
        # print('test')
        # print(test)
        x = int(pos_start[0]) + int(template.shape[1] / 2)
        y = int(pos_start[1]) + int(template.shape[0] / 2)
        similarity = cv.minMaxLoc(result)[1]
        if similarity < 0.85:
            return (-1, -1)
        else:
            # print("pass")
            print(str(x) + ',' + str(y))
            return x, y

    def swipe_search2(self, target, range):
        if not self.get_element_result(target):
            eles = self.driver.find_elements(By.XPATH, range)
            self.swipe_ele1(eles[-1], eles[0])
            self.swipe_search2(target, range)

    def swipe_ele2(self, eleA, eleB):
        y_ele1 = eleA.location['y']
        x_ele1 = eleA.location['x']
        x_ele2 = eleB.location['x']
        self.driver.swipe(x_ele1, y_ele1, x_ele2, y_ele1, 3000)

    def swipe_ele1(self, eleA, eleB):
        y_ele1 = eleA.location['y']
        x_ele1 = eleA.location['x']
        y_ele2 = eleB.location['y']
        self.driver.swipe(x_ele1, y_ele1, x_ele1, y_ele2, 4000)

    def swipe_ele(self, ele_begin, ele_end):
        ele1 = self.find_element(*ele_begin)
        ele2 = self.find_element(*ele_end)
        y_ele1 = ele1.location['y']
        x_ele1 = ele1.location['x']
        x_ele2 = ele2.location['x']
        y_ele2 = ele2.location['y']
        self.driver.swipe(x_ele1, y_ele1, x_ele2, y_ele2, 3000)

    def drag_element(self, ele1, ele2):  # 拖动
        logging.info('drag')
        action = TouchAction(self.driver)

        action.long_press(el=ele1).move_to(el=ele2).release()
        action.perform()

    def drag_coordinate(self, x1, y1, x2, y2):  # 拖动
        logging.info('drag')
        action = TouchAction(self.driver)

        action.long_press(x=x1, y=y1).move_to(x=x2, y=y2).release()
        action.perform()

    def long_press(self, x, y):  # 长按
        logging.info('long_press')
        action = TouchAction(self.driver)

        action.long_press(x=x, y=y).wait(1000).release()
        action.perform()

    def double_click(self, x, y):  # 长按
        logging.info('double_click')
        action = TouchAction(self.driver)

        action.press(x=x, y=y).release().perform().wait(100).press(x=x, y=y).release().perform()

    def tap(self, x, y, count=1):  # 点击
        time.sleep(1)
        logging.info('Tap')
        action = TouchAction(self.driver)

        action.tap(x=x, y=y, count=count)
        action.perform()
        time.sleep(1)

    def zoom_in(self):  # 放大
        logging.info('Zoom')
        action1 = TouchAction(self.driver)  # 第一个手势
        action2 = TouchAction(self.driver)  # 第二个手势
        zoom_action = MultiAction(self.driver)  # 放大手势

        x, y = self.get_size()
        action1.press(x=x * 0.5, y=y * 0.4).wait(1000).move_to(x=x * 0.5, y=y * 0.2).release()
        action2.press(x=x * 0.5, y=y * 0.6).wait(1000).move_to(x=x * 0.5, y=y * 0.8).release()

        zoom_action.add(action1, action2)  # 加载
        time.sleep(2)
        zoom_action.perform()  # 执行

    def zoom_out(self):  # 缩小
        logging.info('==========Pinch==========')
        action1 = TouchAction(self.driver)  # 第一个手势
        action2 = TouchAction(self.driver)  # 第二个手势
        pinch_action = MultiAction(self.driver)  # 放大手势

        x, y = self.get_size()
        action1.press(x=x * 0.8, y=y * 0.3).wait(1000).move_to(x=x * 0.5, y=y * 0.5).release()
        action2.press(x=x * 0.3, y=y * 0.8).wait(1000).move_to(x=x * 0.5, y=y * 0.5).release()

        pinch_action.add(action1, action2)  # 加载
        time.sleep(2)
        pinch_action.perform()  # 执行

    def group_button_click(self, option):
        logging.info('==========group_button_click_%s==========' % option)
        if self.find_element(*option_group).text == option:
            self.click_element(*expand)
        else:
            self.click_element(*option_group)
            self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="%s"]' % option).click()

    def get_elements_attribute(self, elements, attr):
        logging.info('==========get_elements_attribute==========')
        try:
            # attr1 = (By.XPATH, '//*[@resource-id="%s"]' % elements)
            eles = self.driver.find_elements(By.XPATH, elements)
        except NoSuchElementException:
            logging.error("%s locate fail" % str(elements))
            self.getScreenShot("%s locate fail" % str(elements))
            raise
        else:
            logging.info("%s locate success" % str(elements))
            eles_attr = map(lambda x: x.get_attribute(attr), eles)
            return eles_attr

    def get_element(self, ele):
        logging.info('get_element')
        return self.driver.find_element(By.XPATH, ele)

    def get_element_result(self, ele):
        logging.info('==========get_element_result==========')
        try:
            self.driver.find_element(By.XPATH, ele)
        except NoSuchElementException:
            logging.error('get element: %s fail!' % ele)
            return False
        else:
            logging.info('get element: %s success!' % ele)
            return True

    def get_message(self, ele):
        logging.info('==========get_toast_message==========')
        try:
            # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(By.XPATH, message))
            self.find_element(*ele)
        except NoSuchElementException:
            logging.error('get message fail!')
            return False
        else:
            logging.info('get toast message success!')
            return True

    def get_toast_message(self, toast_message):
        logging.info('==========get_toast_message==========')
        message = '//*[@text="' + toast_message + '"]'
        try:
            # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(By.XPATH, message))
            self.driver.find_element(By.XPATH, message)
        except NoSuchElementException:
            logging.error('get toast message: %s fail!' % toast_message)
            return False
        else:
            logging.info('get toast message: %s success!' % toast_message)
            return True

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeRight(self):
        logging.info('swipeRight')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x2, y1, x1, y1, 1000)

    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.swipe(x1, y1, x1, y2, 1000)

    def swipeDown(self):
        logging.info('swipeDown')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.swipe(x1, y2, x1, y1, 1000)

    def getTime(self, timestr):
        # self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        self.now = time.strftime(timestr)
        return self.now

    def getScreenShot4Compare(self, file_name):
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s.png' % file_name

        logging.info('get %s screenshot' % file_name)
        self.driver.get_screenshot_as_file(image_file)

    def compare_pic(self, pic1, pic2):  # 图片对比
        logging.info('compare %s with %s' % (pic1, pic2))
        pic_path = get_project_path() + '/screenshots/'
        image1 = Image.open(pic_path + pic1)
        image2 = Image.open(pic_path + pic2)
        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
        # print(f'result:{result}')
        logging.info('result: %s' % result)
        return result

    def getScreenShot(self, module):
        time = self.getTime("%Y-%m-%d %H_%M_%S")
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def exist(self, element):
        try:
            self.driver.find_element(By.XPATH, element)
        except NoSuchElementException:
            logging.info('=====%s element not exist!======' % element)
            return False
        else:
            logging.info('=====%s element exist!======' % element)
            return True

    @staticmethod
    def clear_special_str(a):
        c = ['.', '_', '-']
        for i in c:
            a = a.replace(i, '')
        return a

    def get_element_xy(self, ele1, x_y=5):
        element = self.driver.find_element(By.XPATH, ele1)
        x1 = int(element.location['x'])
        y1 = int(element.location['y'])

        x9 = int(element.size['width']) + x1
        y9 = int(element.size['height']) + y1

        x5 = (x1 + x9) / 2
        y5 = (y1 + y9) / 2
        px = 1
        if x_y == 1:
            return x1 + px, y1 + px
        elif x_y == 2:
            x2 = x5
            y2 = y1
            return x2, y2 + px
        elif x_y == 3:
            x3 = x9
            y3 = y1
            return x3 - px, y3 + px
        elif x_y == 4:
            x4 = x1 + px
            y4 = y5
            return x4, y4
        elif x_y == 5:
            return x5, y5
        elif x_y == 6:
            x6 = x9 - px
            y6 = y5
            return x6, y6
        elif x_y == 7:
            x7 = x1
            y7 = y9
            return x7 + px, y7 - px
        elif x_y == 8:
            x8 = x5
            y8 = y9
            return x8, y8 - px
        elif x_y == 9:
            return x9 - px, y9 - px

    def swipe_option(self, direction):
        ele = '//*[@resource-id="com.yozo.office:id/yozo_ui_option_content_container"]'
        s2 = self.get_element_xy(ele, x_y=2)
        s5 = self.get_element_xy(ele)
        if direction == 'up':
            return s5[0], s5[1], s2[0], s2[1]
        elif direction == 'down':
            return s2[0], s2[1], s5[0], s5[1]
        else:
            s4 = self.get_element_xy(ele, x_y=4)
            s6 = self.get_element_xy(ele, x_y=6)
            if direction == 'left':
                return s5[0], s5[1], s4[0], s4[1]
            elif direction == 'right':
                return s5[0], s5[1], s6[0], s6[1]

    def get_swipe_xy(self, ele):
        logging.info('=====get_swipe_xy======')
        loc_str = self.find_element(*ele).get_attribute('bounds')
        loc_list = loc_str.replace('[', '').replace(']', ',').split(',')
        x1 = int(loc_list[0])
        y1 = int(loc_list[1])
        x2 = int(loc_list[2])
        y2 = int(loc_list[3])
        x3 = int((x1 + x2) / 2)
        y3 = int((y1 + y2) / 2)
        list_xy = [x1 + 1, x3, x2 - 1, y1 + 1, y3, y2 - 1]
        return list_xy

    def swipe_options(self, ele=option_content, option='up'):
        logging.info('=====swipe_options======')
        list_xy = self.get_swipe_xy(ele)
        x1 = list_xy[0]
        x2 = list_xy[1]
        x3 = list_xy[2]
        y1 = list_xy[3]
        y2 = list_xy[4]
        y3 = list_xy[5]
        if option == 'up':
            self.swipe(x2, y2, x2, y1)
        elif option == 'down':
            self.swipe(x2, y2, x2, y3)
        elif option == 'left':
            self.swipe(x2, y2, x1, y2)
        else:
            self.swipe(x2, y2, x3, y2)

    def template_object(self, filename, target_pos=5, record_pos=None):
        pro_path = get_project_path()
        clickpic_path = os.path.join(pro_path, 'clickPicture_CN')
        # 图像识别阈值：threshold
        # 图像识别新增参数:target_pos 图像点击位置
        # 是否灰度：rgb
        # 图片位置：record_pos  优先在录制时的位置附近查找，如果找不到符合条件的图片，再扩大寻找范围到整个画面
        t = Template(os.path.join(clickpic_path, filename), resolution=(1080, 1920), rgb=True, target_pos=target_pos,
                     threshold=0.8, record_pos=record_pos)
        time.sleep(0.5)
        return t

    def button_on_off(self, button_ele, state=0):  # 开关按钮
        button_state = self.driver.find_element(By.XPATH, button_ele).get_attribute('checked')
        state_dict = {'true': 1, 'false': 0}
        if state != state_dict[button_state]:
            self.driver.find_element(By.XPATH, button_ele).click()

    def cover_file(self, is_cover):
        """
        是否覆盖文档
        :param is_cover: True or False
        :return: None
        """
        logging.info('==========cover_file==========')
        try:
            self.driver.find_element(By.ID, 'android:id/message')
        except NoSuchElementException:
            pass
        else:
            if is_cover:
                self.driver.find_element(By.ID, 'android:id/button1').click()
            else:
                self.driver.find_element(By.ID, 'android:id/button2').click()

    def check_option(self, is_do):
        """
        确认操作
        :param is_cover: True or False
        :return: None
        """
        logging.info('==========cover_file==========')
        try:
            self.driver.find_element(By.ID, 'com.yozo.office:id/msgTv')
        except NoSuchElementException:
            pass
        else:
            if is_do:
                self.driver.find_element(By.ID, 'com.yozo.office:id/btn_sure').click()
            else:
                self.driver.find_element(By.ID, 'com.yozo.office:id/btn_cancel').click()

    def get_element_index(self, ele):
        """
        获取元素的index
        :param ele: 元素条件
        :return:  元素index
        """
        logging.info('==========cover_file==========')
        eles = None
        try:
            # index = self.driver.find_element(By.XPATH, ele).get_attribute('index')
            eles = self.driver.find_element(By.XPATH, ele)
        except NoSuchElementException:
            logging.error('cannot find element')
            return -1
        else:
            index = eles.get_attribute('index')
            # index = self.driver.find_element(By.XPATH, ele).get_attribute('index')
            return int(index)


if __name__ == '__main__':
    # driver=appium_desired()
    # com=Common(driver)
    # com.check_cancelBtn()
    # # com.check_skipBtn()
    # com.swipeLeft()
    # com.getScreenShot('startApp')

    list = ["这", "是", "一个", "测试", "数据"]
    # for i in range(len(list)):
    # print(i, list[i])

    list1 = ["这", "是", "一个", "测试", "数据"]
    # for index, item in enumerate(list1):
    #     print(index, item)
