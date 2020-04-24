#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def calc_FPS(device, apppackage):
    """
    结算app的fps
    :param device:设备id
    :param apppackage: app包名
    :return: 平均fps
    """

    # 通过包名与activity名，获取帧数（查看之前记得滑动APP界面，以便获取数据）
    content = os.popen("adb -s %s shell dumpsys gfxinfo %s" % (device, apppackage))
    # 读取行数
    data = content.readlines()
    print(data)
    start = 0
    end = 0
    i = 0
    p_col = 0
    # 为获得帧数据，先找具有代表性的开始行与结束行的字段“Draw"、"View hierarchy:"
    for line in data:
        if "Draw" in line:
            start = i
            print("start:", start)

        if "View hierarchy:" in line:
            end = i
            print("end", end)
        i = i + 1

    # 确定Draw， Process， Execute三列的下标
    title = data[start]
    print(title)
    title = title.strip()
    title = title.replace("\r\n", "")
    print('title=', title)
    title_list = title.split('\t')
    print("title_list=", title_list)
    Draw_index = title_list.index('Draw')
    Process_index = title_list.index('Process')
    Execute_index = title_list.index('Execute')

    # 精确定位帧数据的开始行与结束行
    result = data[start + 1:end - 1]
    print(result)

    total_fps = 0
    # 未操作所测试的APP时，没有数据
    if len(result) == 0:
        print("没有数据，请操作app哈哈哈")
    else:
        for l in result:
            # 用""代替"\r\n"，去掉"\r\n"
            l = l.replace("\r\n", "")
            l = l.strip()
            print("l=", l)
            datalist = l.split("\t")  # 以"\t"对数据进行切片
            print("datalist=", datalist)
            # 对每行帧数据进行加和操作
            sum = float(datalist[Draw_index]) + float(datalist[Process_index]) + float(datalist[Execute_index])
            print(sum)
            fps = int(1000 / sum)  # 每秒多少帧
            print("fps is %d" % fps)
            total_fps += fps
    avg_fps = total_fps / len(result)
    print("avg_fps is %d" % avg_fps)
    return avg_fps


if __name__ == '__main__':
    calc_FPS('5ENDU19830003766', 'com.yozo.office')
