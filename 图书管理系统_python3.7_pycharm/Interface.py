"""
# @FileName    : SourceModel.py
# @Date        : 2018/9/10
# @By          : 三的拱门
# @Email       : 1304787581@qq.com
# @Platform    : PyCharm ,Python3.7
# @Explain     : Python3 Code
"""
import  os
cmd_dictionary = {'page_main':['studentLogin','managerLogin','mainpage_exit'],
                  'page_student_login':['Login','Resign','exit'],
                  'page_student_deal':['Borrow','Return','All_Return','show_borrow','show_infor','change_password','exit'],
                  'page_manager_login': ['Login', 'exit'],
                  'page_manager_deal': ['show_lib','show_studentInfor','show_infor','change_password','exit'],
                  }
#------------------------------------------------------------
# @FunctionName  : display_style()
# @Description   : None
# @Data          : 2018/9/10
# @Explain       : 登录界面显示
#------------------------------------------------------------
def display_style(styles):
    if styles == 'page_main':
        print("——————图书管理系统——————————-")
        print("——1.学生              --—————————-")
        print("——2.管理者            --—————————-")
        print("——3.退出              --—————————-")
    elif styles == 'page_student_login':
        print("——————图书管理系统(student)——————")
        print("——1.登录              --—————————-")
        print("——2.注册              --—————————-")
        print("——3.退出              --—————————-")
    elif styles == 'page_manager_login':
        print("——————图书管理系统(manager)——————")
        print("——1.登录              --—————————-")
        print("——2.退出              --—————————-")
    elif styles == 'page_student_deal':
        print("——————图书管理系统(student)——————")
        print("——1.借书              --—————————-")
        print("——2.还书              --—————————-")
        print("——3.一键还掉所有书    --—————————-")
        print("——4.显示借书情况      --—————————-")
        print("——5.显示个人信息      --—————————-")
        print("——6.修改登录密码      --—————————-")
        print("——7.退出              --—————————-")
    elif styles == 'page_manager_deal':
        print("——————图书管理系统(manager)——————")
        print("——1.显示图书馆藏书    --—————————-")
        print("——2.查看学生借书情况  --—————————-")
        print("——3.显示个人信息      --—————————-")
        print("——4.修改登录密码      --—————————-")
        print("——5.退出              --—————————-")
    try:
        option = int(input("input number:\n")) - 1
       # print("---------"+cmd_dictionary[styles][option]+"---------")
    except IndexError and ValueError:
        os.system('cls')
        print("输入错误！！！")
    else:
        return cmd_dictionary[styles][option]   #在命令字典中查找对应的命令

