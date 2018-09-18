"""
# @FileName    : main.py
# @Date        : 2018/9/10
# @By          : 三的拱门
# @Email       : 1304787581@qq.com
# @Platform    : PyCharm ,Python3.7
# @Explain     : 图书管理平台
"""
import os
from process_deal import *
from Interface import *
#------------------------------main------------------------------
input_cmd = ''
while input_cmd !=  'mainpage_exit':  #输入的命令 不是 mainpage_exit命令  首页退出命令
    input_cmd =display_style("page_main")  # 进入首页
    if input_cmd == cmd_dictionary['page_main'][0]: #命令为:studentLogin
        input_cmd = display_style("page_student_login")
        if input_cmd == 'Login' :     #学生登录界面
            process_login("student")
        if input_cmd == 'Resign':     #学生注册界面
            process_resign()
    if input_cmd == cmd_dictionary['page_main'][1]: #命令为:managerLogin
        input_cmd = display_style("page_manager_login")
        if input_cmd == 'Login' :     #管理者登录界面
            process_login("manager")
os.system('cls')
print("exit successful!!!")
