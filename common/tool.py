import csv
import json
import logging
from http import server

import flask
import requests
import xlrd
from PIL import Image, ImageChops
import os
import math
import operator
import xlwt
from functools import reduce

from selenium.webdriver.common.by import By

def read_csv(file_path):#读取csv文件
    name_list =[]
    with open(file_path, 'r', encoding='utf-8') as f:
        # name_list.append(f.readlines())
        name_list1=f.readlines()
        for i in name_list1:
            name_list.append(i.strip())
    # print(name_list)
    return name_list

def get_online_templates_name(file_type='pg'):  # 获取所有在线模板的名字
    name_list = []
    file_dict = {'wp': 0, 'pg': 1, 'ss': 2}
    name_dict = {'wp': 'WP_Online_Templates.csv', 'pg': 'PG_Online_Templates.csv', 'ss': 'SS_Online_Templates.csv'}
    page = 0
    url = 'http://www.yomoer.cn/office/mobile/templateList'
    while True:
        print(f'page:{page}')
        response = requests.post(url, data={'key': '', 'offset': page, 'type': file_dict[file_type]}).content.decode(
            'utf-8')

        page += 1
        result = json.loads(response)
        data_list = result['data']
        if not data_list:
            break
        for e in data_list:
            print(f'No.{data_list.index(e)}')
            name_list.append(e['name'])
    with open('../data/' + name_dict[file_type], 'w', encoding='utf-8') as f:
        for i in name_list:
            f.writelines(i + '\n')

    # print(type(result))
    # print(type(data_list))
    # name_list.append(data_list[0]['name'])
    # print(name_list)
    # print(result['data'][0])
    # html = requests.get(url).content.decode('gbk')
    # print(html)
    # toc_url_list = get_toc(html, start_url)


class Device_Select(object):  # 选择使用的设备
    pass


def ele_screenshots(ele, pic_name):
    left = ele.location['x']
    top = ele.location['y']
    right = ele.location['x'] + ele.size['width']
    bottom = ele.location['y'] + ele.size['height']
    im = Image.open(pic_name)
    im = im.crop((left, top, right, bottom))
    im.save(pic_name)


def rm_file(file_name):
    logging.info('=====rm_file======')
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.xls" % file_name)
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.xlsx" % file_name)
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.doc" % file_name)
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.docx" % file_name)
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.ppt" % file_name)
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.pptx" % file_name)
    os.system("adb shell rm -r /mnt/shell/emulated/0/%s.pdf" % file_name)


def image_contrast():
    image1 = Image.open('before_save.png')
    image2 = Image.open('after_save.png')
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    print(result)
    return result


def get_csv_data(csv_file, line):
    # logging.info('=====get_csv_data======')
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            if index == line:
                return row


def get_data(file_path, sheet_name, begin=0, end=5000):  # 获取A2开始第一列的数据
    file = xlrd.open_workbook(file_path, encoding_override="uft-8")
    sheet = file.sheet_by_name(sheet_name)
    return sheet.col_values(0)[begin:end]


def get_project_path():  # 获取当前项目的路径
    path = os.path.dirname(os.path.dirname(__file__))
    return path


def img_unite(save_name):
    img1, img2 = Image.open('before_save.png'), Image.open('after_save.png')
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox() is None:
        print("两张图片一样")
    else:
        diff.save('contrast.png')
        print("两张图片不一样")
    size1, size2, size3 = img1.size, img2.size, diff.size
    joint = Image.new('RGB', (size1[0] + size2[0] + size3[0], size1[1]))
    loc1, loc2, loc3 = (0, 0), (size1[0], 0), (size1[0] + size2[0], 0)
    joint.paste(img1, loc1)
    joint.paste(img2, loc2)
    joint.paste(diff, loc3)
    joint.save(get_project_path() + '\\screenshots\\%s.png' % save_name)
    os.remove('before_save.png')
    os.remove('after_save.png')
    os.remove('contrast.png')


def write_data():
    book = xlwt.Workbook()
    for d in os.listdir(r'D:\1111'):
        sheet = book.add_sheet(d)
        row_num = 0
        for f in os.listdir(r'D:\1111\%s' % d):
            sheet.write(row_num, 0, f)
            row_num += 1
    # sheet1 = book.add_sheet('ppt10')
    # row_num = 0
    # for f in os.listdir(r"D:\1111\ppt10"):
    #     sheet1.write(row_num, 0, f)
    #     row_num += 1
    book.save('files_list.xls')

def chart(self, i):
    b1 = self.find_element(By.ID, 'com.yozo.office:id/yozo_ui_option_content_container')  # 获取父节点
    b2 = b1.find_elements_by_class_name("android.widget.RadioButton")  # 点位到所有子节点，保存到e2列表中
    print(b2)
    x = 0
    while x < i:
        b2[x].click()
        x += 1


if __name__ == '__main__':
    read_csv('../data/SS_Online_Templates.csv')
    # get_online_templates_name()
    # capture_path = get_project_path() + '\Screenshot\sheet_name\cile_name.png'
    # print(capture_path)
    # prth = get_project_path()
    # print(os.path.dirname(os.path.dirname(__file__)))
    # print(os.path.dirname(os.getcwd()))
    # report_path = str(get_project_path) + '\Report\Mobile_Office_Report_%s.html' % time.strftime("%Y_%m_%d_%H_%M_%S")
    # print(report_path)
    # fp = open(r'%s' % report_path, "wb")
    # write_data()
    # report_path = get_project_path()
    # report_path = get_project_path() + '\\Report\\Mobile_Office_Report_%s.html' % time.strftime("%Y_%m_%d_%H_%M_%S")
    # print(report_path)
