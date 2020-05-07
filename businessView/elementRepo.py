#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

# 打开
alldoc = By.ID, 'com.yozo.office:id/ll_bottommenu_alldoc'

# 我的模板
mytemplate = By.ID, 'com.yozo.office:id/end'

# 批量管理
batch_manage = By.ID, 'com.yozo.office:id/end'

# 模板标题
temp_title = By.ID, 'com.yozo.office:id/title'

# 收藏/已收藏
subscribe = By.ID, 'com.yozo.office:id/star'

# 下载
download = By.ID, 'com.yozo.office:id/download'

# 返回
return1 = By.ID, 'com.yozo.office:id/back'
return2 = By.ID, 'com.yozo.office:id/im_title_bar_menu_user'

# 取消收藏
unsubscribe = By.ID, 'com.yozo.office:id/btnTv'

# 取消收藏
delete_temp = By.ID, 'com.yozo.office:id/btnTv'

# 我的模板-下载页
my_download = By.ID, 'com.yozo.office:id/tvRight'

# 我的模板-收藏页
my_subscribe = By.ID, 'com.yozo.office:id/tvLeft'

# 弹出框-确认
pop_confirm = By.ID, 'com.yozo.office:id/btn_sure'
pop_confirm2 = By.ID, 'com.yozo.office:id/btn_true'

# 弹出框-取消
pop_cancel = By.ID, 'com.yozo.office:id/btn_cancel'

# 完成
finish = By.ID, 'com.yozo.office:id/end'

# 立即应用
apply = By.ID, 'com.yozo.office:id/applyTv'

# 阅读/编辑模式切换
mode_switch = By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_mode'

# 保存
save = By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_save'

# 保存-云
save_cloud = By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_cloud'

# 保存-本地
save_local = By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_local'

# 保存-路径_取消
save_path_cancel = By.ID, 'com.yozo.office:id/yozo_ui_select_path_cancel'

# 保存-路径_取消
save_confirm = By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_save_btn'

# 保存-路径_取消
save_cancel = By.ID, 'com.yozo.office:id/yozo_ui_select_save_path_cancle_btn'

# 关闭
close = By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_close'

# 回退
undo = By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo'

# 前进
redo = By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_redo'

# 标星
star = By.ID, 'com.yozo.office:id/ll_filework_pop_star'

# 文档信息-文件名
file_name = By.ID, 'com.yozo.office:id/tv_filename'

# 文档信息-类型
file_type = By.ID, 'com.yozo.office:id/tv_filetype'

# 文档信息-大小
file_size = By.ID, 'com.yozo.office:id/tv_filesize'

# 文档信息-修改时间
modify_time = By.ID, 'com.yozo.office:id/tv_filetime'

# 文档信息-位置
file_location = By.ID, 'com.yozo.office:id/tv_fileloc'

# 分享-微信
wechat = By.ID, 'com.yozo.office:id/ll_wechat_share'

# 分享-QQ
qq = By.ID, 'com.yozo.office:id/ll_qq_share'

# 分享-邮箱
email = By.ID, 'com.yozo.office:id/ll_email_share'

# 分享-更多
more = By.ID, 'com.yozo.office:id/ll_more_share'

# 上传
upload = By.ID, 'com.yozo.office:id/ll_filework_pop_upcloud'

# 复制
copy = By.ID, 'com.yozo.office:id/ll_filework_pop_copy'

# 移动
move = By.ID, 'com.yozo.office:id/ll_filework_pop_move'

# 重命名
rename = By.ID, 'com.yozo.office:id/ll_filework_pop_rename'

# 删除
delete = By.ID, 'com.yozo.office:id/ll_filework_pop_del'

# 多选
multi_select = By.ID, 'com.yozo.office:id/ll_filework_pop_allcheck'

# 多选-复制
multi_copy = By.ID, 'com.yozo.office:id/ll_check_bottom_copy'

# 多选-移动
multi_move = By.ID, 'com.yozo.office:id/ll_check_bottom_move'

# 多选-上传
multi_upload = By.ID, 'com.yozo.office:id/ll_check_bottom_upload'

# 多选-删除
multi_delete = By.ID, 'com.yozo.office:id/ll_check_bottom_del'

# 多选-分享
multi_share = By.ID, 'com.yozo.office:id/ll_check_bottom_share'

# 全选/取消全选
select_all = By.ID, 'com.yozo.office:id/tv_file_checked_tab_all'

# 多选-取消
multi_cancel = By.ID, 'com.yozo.office:id/tv_file_checked_tab_chanel'

# 已选文件数
selected_num = By.ID, 'com.yozo.office:id/tv_file_checked_tab_num'

# 重命名-编辑区
rename_edit = By.ID, 'com.yozo.office:id/et_newfoldername'

# 新建文件夹
new_folder = By.ID, 'com.yozo.office:id/opt_cancel'

# 文件夹名称编辑区
folder_name = By.ID, 'com.yozo.office:id/et'

# 复制/移动至此路径
paste = By.ID, 'com.yozo.office:id/opt_ok'

# 跳过
skip = By.ID, 'com.yozo.office:id/btn_jump'

# 覆盖
cover = By.ID, 'com.yozo.office:id/btn_cover'

# 全部保留
keep = By.ID, 'com.yozo.office:id/btn_hold'

# 覆盖提示
cover_tips = By.ID, 'com.yozo.office:id/tvContent'

# 操作成功
option_success = By.XPATH, '//*[@text="操作成功"]'

# 操作失败
option_fail = By.XPATH, '//*[@text="操作失败"]'

# 请先登录账号
login_first = By.XPATH, '//*[@text="请先登录账号"]'

# 当前为非WIFI环境，无法进行文件传输，如需更改设置，请到我的->系统设置中进行更改
no_wifi = By.XPATH, '//*[@text="当前为非wifi环境，无法进行文件传输\n如需更改设置请到我的->系统设置中进行更改"]'

# 系统设置
sys_setting = By.XPATH, '//*[@text="系统设置"]'

# 仅wifi传输开启/关闭
wifi_trans = By.ID, 'com.yozo.office:id/wifiSwitch'

# 上传失败
upload_fail = By.XPATH, '//*[@text="上传失败"]'

# 未登录显示
unlogin_state = By.ID, 'com.yozo.office:id/loginLayout'

# 上传保存
upload_cancel = By.ID, 'com.yozo.office:id/opt_cancel'

# 上传取消
upload_save = By.ID, 'com.yozo.office:id/opt_ok'

# 上传超过20
great20 = By.XPATH, '//*[@text="选择文件数量最多为20个"]'

# 已取消
cancelled = By.XPATH, '//*[@text="已取消"]'

# 请先选择文件
select_file_first = By.XPATH, '//*[@text="请先选择文件"]'

# 服务器DNS解析失败,请检查您的网络
dns_fail = By.XPATH, '//*[@text="服务器DNS解析失败,请检查您的网络"]'

# 请选择要编辑的模板
select_temp = By.XPATH, '//*[@text="请选择要编辑的模板"]'

# 常用文件夹-添加
add_folder = By.ID, 'com.yozo.office:id/ll_add_common'

# 添加至常用
add2common = By.ID, 'com.yozo.office:id/btn_add'

# 请选择要添加的文件夹
select_folder2add = By.XPATH, '//*[@text="请选择要添加的文件夹"]'

# 选择项标题
item_title = By.ID, 'com.yozo.office:id/tv_title'

# 文件夹选中框
folder_check = By.ID, 'com.yozo.office:id/lay_check'

# 下移
move_down = By.ID, 'com.yozo.office:id/tv_move_down'

# 上移
move_up = By.ID, 'com.yozo.office:id/tv_move_up'

# 移除
remove = By.ID, 'com.yozo.office:id/tv_remove'

# 排序
sort = By.ID, 'com.yozo.office:id/im_title_bar_menu_shot'

# 登录送1G空间
unlogin_cloud = By.XPATH, '//*[@text="登录送1G空间"]'

# 位置-云文档
cloud = By.XPATH, '//*[@text="云文档"]'

# 位置-手机
phone = By.XPATH, '//*[@text="手机"]'

# 登录按键
login_button = By.ID, 'com.yozo.office:id/btn_login'

# 账号输入
account_input = By.ID, 'com.yozo.office:id/et_account'

# 密码输入
pwd_input = By.ID, 'com.yozo.office:id/et_pwd'

# 忘记密码
forget_pwd = By.XPATH, '//*[@text="忘记密码"]'

# 注册
register = By.ID, 'com.yozo.office:id/tv_register'

# 登录取消
login_cancel = By.XPATH, '//*[@text="取消"]'

# 微信登录
login_wechat = By.XPATH, '//*[@text="微信登录"]'

# 短信登录
login_SMS = By.XPATH, '//*[@text="短信登录"]'

# 单条选项
item = By.ID, 'com.yozo.office:id/file_item'

# 您尚未登录，请登录
login_first1 = By.XPATH, '//*[@text="您尚未登录，请登录"]'

# 联网后可查看更多在线模板
net4more_temp = By.ID, 'com.yozo.office:id/tpOnlineTip'

# 未联网新建空白
create_nonet_blank = By.ID, 'com.yozo.office:id/create_empty_offline_img'

# 联网新建空白
create_blank = By.ID, 'com.yozo.office:id/createEmpty'

# 模板搜索
temp_search = By.ID, 'com.yozo.office:id/searchTv'

# 模板搜索输入
temp_search_input = By.ID, 'com.yozo.office:id/et'

# 模板搜索启动
temp_search_start = By.ID, 'com.yozo.office:id/searchv'

# 没有找到相关模板
no_related_temp = By.XPATH, '//*[@text="没有找到相关模板"]'

# 搜索历史记录
search_history = By.ID, 'com.yozo.office:id/rv'

# 清空历史记录
clear_history = By.ID, 'com.yozo.office:id/trash'
