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
temp_download = By.ID, 'com.yozo.office:id/download'

# 返回
return1 = By.ID, 'com.yozo.office:id/back'
return2 = By.ID, 'com.yozo.office:id/im_title_bar_menu_user'
return3 = By.ID, 'com.yozo.office:id/iv_back'
return4 = By.ID, 'com.yozo.office:id/im_title_bar_menu_back'

# 取消收藏
unsubscribe = By.ID, 'com.yozo.office:id/btnTv'

# 删除模板
delete_temp = By.ID, 'com.yozo.office:id/btnTv'

# 我的模板-下载页
my_download = By.ID, 'com.yozo.office:id/tvRight'

# 我的模板-收藏页
my_subscribe = By.ID, 'com.yozo.office:id/tvLeft'

# 弹出框-确认
pop_confirm = By.ID, 'com.yozo.office:id/btn_sure'
pop_confirm2 = By.ID, 'com.yozo.office:id/btn_true'
pop_confirm3 = By.ID, 'com.yozo.office:id/btn_right'
pop_confirm4 = By.ID, 'com.yozo.office:id/sure_btn'

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

# 撤销
undo = By.ID, 'com.yozo.office:id/yozo_ui_toolbar_button_undo'

# 重做
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

# 下载
download = By.ID, 'com.yozo.office:id/ll_filework_pop_download'

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

# 多选-下载
multi_download = By.ID, 'com.yozo.office:id/ll_check_bottom_download'

# 全选/取消全选
select_all = By.ID, 'com.yozo.office:id/tv_file_checked_tab_all'
cancel_all = By.ID, 'com.yozo.office:id/tv_file_checked_tab_all'

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

# 上传成功
upload_success = By.XPATH, '//*[@text="上传成功"]'

# 未登录显示
unlogin_state = By.ID, 'com.yozo.office:id/loginLayout'

# 上传取消
upload_cancel = By.ID, 'com.yozo.office:id/opt_cancel'

# 上传保存
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
login_button_SMS = By.ID, 'com.yozo.office:id/btn_login_verfiy'

# 账号输入
account_input = By.ID, 'com.yozo.office:id/et_account'

# 密码输入
pwd_input = By.ID, 'com.yozo.office:id/et_pwd'
pwd_input1 = By.ID, 'com.yozo.office:id/et_password'

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

# 没有更多数据
no_more_data = By.ID, 'com.yozo.office:id/emptyTv'

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

# 换一换
change = By.ID, 'com.yozo.office:id/changeTv'

# 第一个模板名
first_temp_name = By.ID, 'com.yozo.office:id/tpTitle1'

# 第一个模板
first_temp = By.ID, 'com.yozo.office:id/card1'

# 文件已存在于云文档
cloud_exist = By.XPATH, '//*[@text="文件已存在于云文档"]'

# 此操作只是将文件从最近列表中删除
delete_from_last = By.XPATH, '//*[@text="此操作只是将文件从最近列表中删除"]'

# 文件下载成功,已保存至/storage/emulated/0/yozoCloud文件夹
download_success = By.XPATH, '//*[@text="文件下载成功,已保存至/storage/emulated/0/yozoCloud文件夹"]'

# 小云朵标志
cloud_logo = By.ID, 'com.yozo.office:id/tv_from'

# 搜索
search = By.ID, 'com.yozo.office:id/im_title_bar_menu_search'

# 搜索返回
search_back = By.ID, 'com.yozo.office:id/iv_search_back'

# 搜索输入
search_input = By.ID, 'com.yozo.office:id/et_search'

# 搜索启动
search_start = By.ID, 'com.yozo.office:id/iv_search_search'

# 搜索无结果
search_no_result = By.ID, 'com.yozo.office:id/emptyView'

# 搜索关键词清空
search_keyword_clear = By.ID, 'com.yozo.office:id/iv_search_content_clear'

# 搜索本地文档
search_tips = By.XPATH, '//*[@text="搜索本地文档"]'

# 账号头像
account_logo = By.ID, 'com.yozo.office:id/im_title_bar_menu_user'

# 关于YOZO
about_yozo = By.XPATH, '//*[@text="关于YOZO"]'

# 账号编辑
account_edit = By.XPATH, '//*[@resource-id="com.yozo.office:id/rl_myinfo_name"]/android.widget.ImageView'

# 账号名称
nickname = By.XPATH, '//*[@resource-id="com.yozo.office:id/rl_myinfo_name"]/android.widget.TextView'
nickname2 = By.ID, 'com.yozo.office:id/tv_myinfo_name'

# 账号
account = By.ID, 'com.yozo.office:id/tv_myinfo_account'

# 邮箱
account_email = By.ID, 'com.yozo.office:id/tv_myinfo_email'

# 昵称未修改
nickname_not_change = By.XPATH, '//*[@text="昵称未修改"]'

# 昵称修改
nickname_edit = By.ID, 'com.yozo.office:id/et_newname'

# 用户信息修改成功
info_modified_success = By.XPATH, '//*[@text="用户信息修改成功"]'

# 请输入邮箱
please_enter_email = By.XPATH, '//*[@text="请输入邮箱"]'

# 邮箱更改
enter_email = By.ID, 'com.yozo.office:id/et_newemai'

# 请输入验证码
please_enter_verfycode = By.XPATH, '//*[@text="请输入验证码"]'

# 输入的邮箱格式有误
incorrect_email_format = By.XPATH, '//*[@text="输入的邮箱格式有误"]'

# 邮箱验证码输入
enter_email_verfycode = By.ID, 'com.yozo.office:id/et_code'

# 邮箱验证码错误
email_verfycode_wrong = By.XPATH, '//*[@text="邮箱验证码错误"]'

# 转换工具
convert_tools = By.XPATH, '//*[@text="转换工具"]'

# 转换选项
convert_item = By.ID, 'com.yozo.office:id/ll_convert_tools_item'

# 无法连接网络,请检查网络连接
check_net = By.XPATH, '//*[@text="无法连接网络,请检查网络连接"]'

# 解锁更多功能，请先登录！
login4more_functions = By.XPATH, '//*[@text="解锁更多功能，请先登录！"]'

# 自动上传
auto_folder = By.XPATH, '//*[@text="自动上传"]'

# 退出登录
logout = By.XPATH, '//*[@text="退出登录"]'

# 意见反馈
feedback = By.XPATH, '//*[@text="意见反馈"]'

# 意见反馈-历史记录
feedback_history = By.ID, 'com.yozo.office:id/end'

# 反馈内容
feedback_content = By.ID, 'com.yozo.office:id/contentEt'

# 反馈联系方式
feedback_contact = By.ID, 'com.yozo.office:id/contactEt'

# 反馈提交
feedback_submit = By.ID, 'com.yozo.office:id/submitTv'

# 请填写反馈内容
enter_feedback_content = By.XPATH, '//*[@text="请填写反馈内容"]'

# 请填写联系方式
enter_feedback_contact = By.XPATH, '//*[@text="请填写联系方式"]'

# 联系方式不正确
contact_wrong = By.XPATH, '//*[@text="联系方式不正确"]'

# 提交成功
feedback_submit_success = By.XPATH, '//*[@text="提交成功"]'

# 回收站
recycle = By.XPATH, '//*[@text="回收站"]'

# 我的模板
my_template = By.XPATH, '//*[@text="我的模板"]'

# 版本号
version = By.ID, 'com.yozo.office:id/iv_version'

# yozo官网
yozo_web = By.ID, 'com.yozo.office:id/_phone_web'

# yozo邮箱
yozo_email = By.ID, 'com.yozo.office:id/_phone_email'

# yozo客服
yozo_phone = By.ID, 'com.yozo.office:id/_phone_phone'

# 推荐给朋友
share2others = By.ID, 'com.yozo.office:id/ll_share_app'

# 下载二维码
download_QR = By.ID, 'com.yozo.office:id/ll_save_phone'

# 网络异常
net_exception = By.XPATH, '//*[@text="网络异常"]'

# 云新建文件夹
cloud_add_folder = By.ID, 'com.yozo.office:id/im_title_bar_menu_newf'

# 云文件夹名输入
cloud_folder_name = By.ID, 'com.yozo.office:id/et'

# 还原
recycle_revert = By.ID, 'com.yozo.office:id/tv_recycle_revert'

# 回收站-删除
recycle_delete = By.ID, 'com.yozo.office:id/tv_recycle_delete'

# 已还原
already_revert = By.XPATH, '//*[@text="已还原"]'

# 已删除
already_delete = By.XPATH, '//*[@text="已删除"]'

# 回收站-清空
recycle_clear = By.ID, 'com.yozo.office:id/tv_clear_all'

# 已删除的文件夹无法打开
cannot_open = By.XPATH, '//*[@text="已删除的文件夹无法打开"]'

# 已清空
already_clear = By.XPATH, '//*[@text="已清空"]'

# 已取消收藏
already_unsubscribe = By.XPATH, '//*[@text="已取消收藏"]'

# 已收藏
already_subscribe = By.XPATH, '//*[@text="已收藏"]'

# 注册-下一步
register_next_step = By.ID, 'com.yozo.office:id/btn_register'

# 请输入手机号
enter_phone_number = By.XPATH, '//*[@text="请输入手机号"]'

# 请输入密码
enter_pwd = By.XPATH, '//*[@text="请输入密码"]'

# 请重新输入密码,必须包含字母和数字,且密码长度为6到12位
re_enter_pwd = By.XPATH, '//*[@text="请重新输入密码,必须包含字母和数字,且密码长度为6到12位"]'

# 请先仔细阅读并勾选同意永中Office的《隐私政策》和《服务条款》
accept_agreement = By.XPATH, '//*[@text="请先仔细阅读并勾选同意永中Office的《隐私政策》和《服务条款》"]'

# 协议勾选框
checkbox_agreement = By.ID, 'com.yozo.office:id/checkbox_privacy'

# 请输入正确的手机号
enter_right_phone_number = By.XPATH, '//*[@text="请输入正确的手机号"]'

# 注册取消
register_cancel = By.ID, 'com.yozo.office:id/iv_add_back'

# 获取验证码
get_verfycode = By.ID, 'com.yozo.office:id/btn_verifycode'

# 请输入图片验证码
enter_picture_verfycode = By.XPATH, '//*[@text="请输入图片验证码"]'
enter_picture_verfycode2 = By.XPATH, '//*[@text="请输入图形验证码"]'

# 图形验证码
picture_code_input = By.ID, 'com.yozo.office:id/et_figure_code'

# 手机号的格式有误
phone_format_wrong = By.XPATH, '//*[@text="手机号的格式有误"]'

# 网络连接异常
net_connect_exception = By.XPATH, '//*[@text="网络连接异常"]'

# 输入的账号格式有误
account_format_wrong = By.XPATH, '//*[@text="输入的账号格式有误"]'

# 请输入账号
please_enter_accout = By.XPATH, '//*[@text="请输入账号"]'

# 请输入密码
please_enter_pwd = By.XPATH, '//*[@text="请输入密码"]'

# 登录失败：网络连接异常
login_fail_nonet = By.XPATH, '//*[@text="登录失败：网络连接异常"]'

# 重要文件，珍藏在这里
star_no_file = By.XPATH, '//*[@text="重要文件，珍藏在这里"]'

# 文件下载失败
download_fail = By.XPATH, '//*[@text="文件下载失败"]'

# 当前操作不支持文件夹
option_not4folder = By.XPATH, '//*[@text="当前操作不支持文件夹"]'

# 删除文档名
delete_file = By.ID, 'com.yozo.office:id/tv_show_title'

# 原文件名和新文件名一样，无需重命名
filename_same = By.XPATH, '//*[@text="原文件名和新文件名一样，无需重命名"]'

# 请不要包含特殊字符
exist_special_char = By.XPATH, '//*[@text="请不要包含特殊字符"]'

# 不得大于40个字符
chars_40_more = By.XPATH, '//*[@text="不得大于40个字符"]'

# 新建文件夹失败
create_folder_fail = By.XPATH, '//*[@text="新建文件夹失败"]'

# 立即使用按键
cloud_use = By.ID, 'com.yozo.office:id/btn_logo'

# 登录失败：用户名或密码错误
login_fail_account_wrong = By.XPATH, '//*[@text="登录失败：用户名或密码错误"]'

# 登录失败：次数过多，请转手机号验证码登录
login_fail_too_much = By.XPATH, '//*[@text="登录失败：次数过多，请转手机号验证码登录"]'

# 请输入短信验证码
enter_SMS_code = By.XPATH, '//*[@text="请输入短信验证码"]'

# 短信验证码输入
SMS_code_input = By.ID, 'com.yozo.office:id/etSms'

# 文件名已存在
name_exist = By.XPATH, '//*[@text="文件名已存在"]'

# 目标文件夹与源文件相同
same_folder = By.XPATH, '//*[@text="目标文件夹与源文件相同。"]'

# 更多操作
more_options = By.ID, 'com.yozo.office:id/lay_more'

# 最近/打开/云文档/标星/我的
index_page = By.ID, 'com.yozo.office:id/ll_tap'

# 返回云文档初始页
cloud_first_page = By.XPATH, '//*[@text="云文档 > "]'

# wp编辑区域
wp_edit = By.ID, 'com.yozo.office:id/a0000_main_view_container'

# 打开收起编辑选项
expand = By.ID, 'com.yozo.office:id/yozo_ui_option_expand_button'

# 文件-保存
save2 = By.XPATH, '//*[@text="保存"]'

# 文件-另存为
save_as = By.XPATH, '//*[@text="另存为"]'

# 文件输出为PDF
export_pdf = By.XPATH, '//*[@text="输出为PDF"]'

# 输出为长图
export_long_pic = By.XPATH, '//*[@text="输出为长图"]'

# 逐页输出图片
export_images = By.XPATH, '//*[@text="逐页输出图片"]'

# 保存到相册
save2album = By.ID, 'com.yozo.office:id/rll_export_long_picture_save_layout'

# 已保存到相册
saved = By.XPATH, '//*[contains(@text,"已保存到")]'

# 分享
image_share = By.ID, 'com.yozo.office:id/rll_export_long_picture_share_layout'

# 当前操坐选项
option_group = By.ID, 'com.yozo.office:id/yozo_ui_option_group_button'

# 文件搜索中
searching = By.XPATH, '//*[@text="文件搜索.."]'

# 正在打开
opening = By.XPATH, '//*[contains(@text, "正在打开")]'

# 文档名
file_title = By.ID, 'com.yozo.office:id/yozo_ui_title_text_view'

# 查找
find_replace = By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_find_replace'

# 查找输入
find_input = By.ID, 'com.yozo.office:id/yozo_ui_et_find_content'

# 查找开始
find_start = By.ID, 'com.yozo.office:id/yozo_ui_iv_icon_search'

# 未找到匹配的数据
find_nothing = By.XPATH, '//*[@text="未找到匹配的数据。"]'

# 查找前一个
find_previous = By.ID, 'com.yozo.office:id/yozo_ui_iv_find_previous'

# 查找后一个
find_next = By.ID, 'com.yozo.office:id/yozo_ui_iv_find_next'

# 查找返回
find_return = By.ID, 'com.yozo.office:id/yozo_ui_iv_back'

# 适应屏幕显示
full_screen = By.ID, 'com.yozo.office:id/yozo_ui_quick_option_wp_read_full_screen'

# 退出适应屏幕显示
exit_full_screen = By.XPATH, '//android.widget.ImageView'

# 插入书签
bookmark_insert = By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_bookmark_insert'

# 书签名输入框
bookmark_edit = By.ID, 'com.yozo.office:id/bookmark_name_edit'

# 添加书签成功
bookmark_insert_succes = By.XPATH, '//*[@text="添加书签成功"]'

# 书签列表
bookmark_list = By.ID, 'com.yozo.office:id/yozo_ui_wp_option_id_bookmark_catalog'

# 书签列表返回
bookmark_return = By.ID, 'com.yozo.office:id/yozo_ui_option_back_button'

# 操作内容区域
option_content = By.ID, 'com.yozo.office:id/yozo_ui_option_content_container'

# 操作标题区域
option_title = By.ID, 'com.yozo.office:id/yozo_ui_main_option_title_container'

# 屏幕常亮按钮
screen_light = By.ID, 'com.yozo.office:id/yozo_ui_option_group_light_switch'

# 已开启阅读模式下屏幕常亮
screen_light_on = By.XPATH, '//*[@text="已开启阅读模式下屏幕常亮"]'

# 已关闭阅读模式下屏幕常亮
screen_light_off = By.XPATH, '//*[@text="已关闭阅读模式下屏幕常亮"]'

# 书签名称已存在，请重新输入
bookmark_exist = By.XPATH, '//*[@text="书签名称已存在，请重新输入"]'

# 保存成功
save_success = By.XPATH, '//*[@text="保存成功"]'

# 导出成功
export_success = By.XPATH, '//*[@text="导出成功"]'

# pdf文档标题
pdf_file_title = By.ID, 'com.yozo.office:id/tv_pdf_title_name'
