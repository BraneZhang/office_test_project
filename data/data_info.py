#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

share_list = ['wp_wx', 'wp_qq', 'wp_ding', 'wp_mail', 'ss_wx', 'ss_qq', 'ss_ding',
              'ss_mail', 'pg_wx', 'pg_qq', 'pg_ding', 'pg_mail']
share_list1= ['wx','qq','ding','mail']
wps = ['wp', 'ss', 'pg']
ps = ['ss', 'pg']
wp = ['wp', 'pg']
ws = ['wp', 'ss']
search_dict = {'wp': 'docx', 'ss': 'xlsx', 'pg': 'pptx'}
switch_list = ['无切换', '平滑淡出', '从全黑淡出', '切出', '从全黑切出', '溶解', '向下擦除', '向左擦除', '向右擦除',
               '向上擦除', '扇形展开', '从下抽出', '从左抽出', '从右抽出', '从上抽出', '从左下抽出', '从左上抽出',
               '从右下抽出', '从右上抽出', '盒状收缩', '盒状展开', '1根轮辐', '2根轮辐', '3根轮辐', '4根轮辐', '8根轮辐',
               '上下收缩', '上下展开', '左右收缩', '左右展开', '左下展开', '左上展开', '右下展开', '右上展开', '圆形',
               '菱形', '加号', '新闻快报', '向下推出', '向左推出', '向右推出', '向上推出', '向下插入', '向左插入',
               '向右插入', '向上插入', '向左下插入', '向左上插入', '向右下插入', '向右上插入', '水平百叶窗',
               '垂直百叶窗', '横向棋盘式', '纵向棋盘式', '水平梳理', '垂直梳理', '水平线条', '垂直线条', '随机']
csv_file = '../data/account.csv'
folder_list = ['手机', '我的文档', 'Download', 'QQ', '微信']
index_share_list = ['qq', 'wechat', 'email', 'more']
index_share_list1 = ['qq', 'wechat', 'email', 'ding']
index_share_list2 = ['qq', 'wechat', 'email', 'dingding']
auto_sum = ['求和', '平均值', '计数', '最大值', '最小值']
date_filter = ['等于', '不等于', '在以下日期之后', '在以下日期之后或与之相同', '在以下日期之前',
               '在以下日期之前或与之相同', '开始于', '非开始于', '结束于', '非结束于', '包含', '不包含']
num_filter = ['等于', '不等于', '大于', '大于等于', '小于', '小于等于', '开始于', '非开始于', '结束于', '非结束于', '包含', '不包含']
text_filter = ['等于', '不等于', '大于', '大于等于', '小于', '小于等于', '开始于', '非开始于', '结束于', '非结束于', '包含', '不包含']
way_list = ['收藏', '下载']
search_template_dict = {'wp': ['教育教学', '灰色扁平化简约个人简历模板'],
                        'ss': ['财务统计', '养老金投资计算器'],
                        'pg': ['工作汇报', '彩色职场汇报总结PPT模板']}

templates_dict = {'wp': ['教育教学', '信纸贺卡', '产品宣传', '简历求职', '报告总结', '财务管理', '合同范文', '人力资源', '党政范文'],
                  'ss': ['财务统计', '购销发货', '教育教学', '教育教学', '人力资源', '办公常用', '日历日程', '日历日程', '日历日程'],
                  'pg': ['工作汇报', '毕业答辩', '计划总结', '求职简历', '年会颁奖', '节日庆典', '教学课件', '企业介绍', '营销策划']}
print_ways = ['current_table', 'all_table', 'select_range']
if __name__ == '__main__':
    # a = [False,False]
    # print(False in a)
    # a = [1, 2, 3.4, 5]
    # b = [1, 2, 3.4, 6]
    # print(a == b)
    # print(list(range(10)))
    # print(random.randint(1, 12))
    strs = '[48,337][1080,1810]'
    print(int(strs))
    # strs = '[48,337]'
    ss = strs[1:-1].split('][')
    cc = list(map(lambda a: eval(a), ss))
    print(ss)
    print(cc)
