"""
# @FileName    : SourceModel.py
# @Date        : 2018/9/10
# @By          : 三的拱门
# @Email       : 1304787581@qq.com
# @Platform    : PyCharm ,Python3.7
# @Explain     : 介于界面层与底层之间
"""
from user_class import *
from Interface import *
#------------------------------------------------------------
# @FunctionName  : process_login()
# @Description   : 登录处理函数
# @Data          : 2018/9/10
# @Explain       : None
#------------------------------------------------------------
def process_login(position):
    while True:
        user_name = input("input name:\n")
        user_password = input("input password:\n")
        if position == "student":
            student_user = User("student", user_name, user_password)
            if student_user.login_correct("student") == True:
                print("登录成功！！！")
                process_student(student_user) # 登录成功：传递对象
                break
            else:
                print("输入错误")
                if input("-------输入yes重新登录，输入其它退出------- \n->输入:") != "yes":
                    break
        elif position == "manager":
            manager_user = User("manager", user_name, user_password)
            if manager_user.login_correct("manager") == True:
                print("登录成功！！！")
                process_magager(manager_user)  # 登录成功：传递对象
                break
            else:
                print("输入错误")
                if input("-------输入yes重新登录，输入其它退出------- \n->输入:") != "yes":
                    break
#------------------------------------------------------------
# @FunctionName  : process_resign()
# @Description   : 注册处理函数
# @Data          : 2018/9/10
# @Explain       : None
#------------------------------------------------------------
def process_resign():
    student_user = User("empty", "empty", "empty")  # 创建对象
    while True:
        user_name = input("input name:\n")
        user_password = input("input password:\n")
        student_user = User("student", user_name, user_password)
        if student_user.resign_correct() == True:
            print("注册成功！！！")
            process_student(student_user) # 注册成功：传递对象
            break
        else:
            print("输入错误---已存在该用户！！！")
            if input("-------输入yes重新注册，输入其它退出------- \n->输入:") != "yes":
                break
#------------------------------------------------------------
# @FunctionName  : process_student()
# @Description   : 学生处理
# @Data          : 2018/9/10
# @Explain       : None
#------------------------------------------------------------
def process_student(student_user):
    student_user.read_inforFromFile() #从文件中读取所有信息
    while True:
        option_cmd = display_style("page_student_deal") # 显示学生操作界面
        if option_cmd == 'Borrow':  # 借书
            while True:
                student_user.show_lib_books() # 显示当前图书馆图书
                bookname = input("请输入借书名称：")
                if student_user.borrow_books(bookname) == True: #若操作成功，更新用户文件
                    student_user.update_user_file()
                    print("借书成功！！！")
                    break
                else:
                    print("借书失败---输入错误！！！")
                    if input("-------输入yes重新借书，输入其它返回上一级----- \n->输入:") != "yes":
                        break
        elif option_cmd == 'Return':   # 还书
            student_user.show_books()  # 显示当前图书馆图书
            bookname = input("请输入还书名称：")
            if student_user.return_books(bookname) == True:  # 若操作成功，更新用户文件
                student_user.update_user_file()  # 更新用户文件
                student_user.update_libBooks_file()  # 更新图书馆书籍文件
                print("还书成功！！！")
                break
            else:
                print("还书失败---输入错误！！！")
                if input("-------输入yes重新还书，输入其它返回上一级----- \n->输入:") != "yes":
                    break
        elif option_cmd == 'All_Return':  # 一键还掉该用户所有的书籍
            if student_user.return_all_books() == True:  # 若操作成功
                student_user.update_user_file()  # 更新用户文件
                student_user.update_libBooks_file()  # 更新图书馆书籍文件
                print("还书成功！！！")
        elif option_cmd == 'show_borrow':   # 显示借书
            if student_user.show_books() == True:    #若操作成功
                student_user.update_user_file()      #更新用户文件
                student_user.update_libBooks_file()  #更新图书馆书籍文件
        elif option_cmd == 'show_infor':   # 显示个人信息
            student_user.show_privateInfor()
        elif option_cmd == 'change_password':  # 修改登录密码
            if student_user.change_password() == True:  # 若操作成功
                student_user.update_user_file()  # 更新用户文件
                print("修改密码成功！！！")
        elif option_cmd == 'exit':  # 显示个人信息
            student_user.update_user_file()
            print("退出系统！！！")
            break
# ------------------------------------------------------------
# @FunctionName  : process_student()
# @Description   : 学生处理
# @Data          : 2018/9/10
# @Explain       : None
# ------------------------------------------------------------
def process_magager(manager_user):
    manager_user.read_inforFromFile()  # 从文件中读取所有信息
    while True:
        option_cmd = display_style("page_manager_deal")  # 显示学生操作界面
        if option_cmd == 'show_lib':  # 显示图书馆藏书
            manager_user.show_lib_books()
        elif option_cmd == 'show_studentInfor':  #显示图书馆学生的资料
            manager_user.show_studentInfor()
        elif option_cmd == 'show_infor':  # 显示个人信息
            manager_user.show_privateInfor()
        elif option_cmd == 'change_password':  # 修改登录密码
            if manager_user.change_password() == True:  # 若操作成功
                manager_user.update_manager_file()  # 更新用户文件
                print("修改密码成功！！！")
        elif option_cmd == 'exit':  # 显示个人信息
            print("退出系统！！！")
            break
