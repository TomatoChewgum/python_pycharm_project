"""
# @FileName    : SourceModel.py
# @Date        : 2018/9/10
# @By          : 三的拱门
# @Email       : 1304787581@qq.com
# @Platform    : PyCharm ,Python3.7
# @Explain     : Python3 Code
"""
#------------------------------------------------------------
# @FunctionName  : User()
# @Description   : None
# @Data          : 2018/9/10
# @Explain       : user 类
#------------------------------------------------------------
class User():
    # @Description: 初始化
    def __init__(self,position,name,password):
          #  books = {}
            self.position = position;self.name = name;self.password = password;
            self.books = {} #借书
            self.books_typeNum =0  # 借的书有多少种
            self.pre_books_typeNum = 0  # 存储上一次的借书种类
            self.lib_books= {} #图书馆剩余书籍
         #   self.all_user_Infor = {}  # 图书馆剩余书籍
            self.user_filename = 'Source_user.txt'
            self.manager_filename = 'Source_manager.txt'
            self.filename_lib_books = 'Source_lib_books.txt'  #当前图书馆藏书文本

    # @Description: 登录验证函数
    def change_password(self):
        password = input("请输入新的登录密码：")
        self.password = password
        return True
    # @Description: 登录验证函数
    def login_correct(self,position):
        if position == "student":
            with open(self.user_filename, 'r', encoding='UTF-8') as file_object:
                lines = file_object.readlines()
            for single_line in lines:
                if self.name in single_line and self.password in single_line:
                    return True
        elif position == "manager":
            with open(self.manager_filename, 'r', encoding='UTF-8') as file_object:
                file_list = list(file_object)
                if self.name in file_list[0] and self.password in file_list[0]:
                    return True
        return False
        # @Description: 登录验证函数
    def resign_correct(self):
        with open(self.user_filename, 'r', encoding='UTF-8') as file_object:
            lines = file_object.readlines()
            for sigle_line in lines:
                if self.name in sigle_line :
                    return False
            return True
    #@Description: 显示图书馆藏书
    def show_lib_books(self):
        print("------图书馆藏书情况------")
        for key,value in self.lib_books.items():
           print("\t《" + key + "》\t剩余" + str(value) + "本")
    #@Description: 显示所有学生借书情况
    def show_studentInfor(self):
        index = 0
        with open(self.user_filename, 'r', encoding='UTF-8') as file_object:
            file_list = list(file_object)
            while index < len(file_list):  # 用户文件中存在该用户信息，则查找数据块并更新
                if "student" in file_list[index]:
                    temp = file_list[index].rstrip().split()
                    print("姓名："+temp[1]+"\t密码："+temp[2])
                    if int(temp[3]) == 0:
                        print("\t 没有借书！！！")
                    for n in range(0,int(temp[3])):
                        temp = file_list[index+n+1].rstrip().split()
                        print("\t《" + temp[0] + "》\t" + temp[1] + "本")
                index += 1
    #@Description: 借书
    def borrow_books(self,bookname):
        for key in self.lib_books.keys():
            if key.find(bookname) != -1:  #在图书馆找到该书：bookname
                if key in self.books.keys():  #要借的书已经存在，直接更新value值
                    value = self.books.get(key)
                    self.books[key] = int(value) + 1
                else:                        #要借的书不存在，则创建相应的字典项
                    self.books[key] = 1
                self.lib_books[key] -= 1  #图书馆中的对应书籍数目 减1
                if self.lib_books[key] == 0:
                    self.lib_books.pop(key) #若书籍的数量为0 则移除
                return True
        else:return False
    # @Description: 显示借书的情况
    def show_books(self):
        print("----------借书情况--------")
        if len(self.books) != 0:
            for key,value in self.books.items():
                print("\t《"+key+"》\t"+str(value)+"本")
        else: print("\t无借书！！！")
    # @Description: 还书
    def return_books(self,bookname):
        if len(self.books) == 0:
            print("\t无借书！！！")
            return False
        if bookname in self.books.keys():   # 在所借的书中找到该书：bookname
            value = int(self.books.get(bookname))
            if value == 1:
                self.books.pop(bookname)
             #   self.books_typeNum -= 1
            elif value >= 2:
                self.books[bookname] = value - 1
            if bookname in self.lib_books.keys(): #图书馆中还有此书
                self.lib_books[bookname] += 1
            else :                                #图书馆中没有此书
                self.lib_books[bookname] = 1      #创建一项
            return True
        else:
            print("书名输入错误！！！")
            return False
    # @Description: 还掉所有的书
    def return_all_books(self):
        if len(self.books) == 0:
            print("\t无借书！！！")
            return False
        for key,value in self.books.items():
            if key in self.lib_books.keys():  # 图书馆中还有此书
                self.lib_books[key] += value
            else:  # 图书馆中没有此书
                self.lib_books[key] = value  # 创建一项
          #  self.books_typeNum = 0
            self.books ={}
        return True
    # @Description: 显示个人信息
    def show_privateInfor(self):
        print("------个人信息输出--------")
        print("职位：" + self.position +"\t姓名：" + self.name +"\t密码：" +self.password)
    # @Description: 将个人信息写入用户文件
    def update_user_file(self):
        file_data = ""
        index = 0
        with open(self.user_filename, 'r', encoding='UTF-8') as file_object:
                file_list = list(file_object)
                while index < len(file_list):          #用户文件中存在该用户信息，则查找数据块并更新
                    if self.name in file_list[index]:  # 找到存储该用户数据的起始行
                        temp = self.books_typeNum
                        self.books_typeNum =len(self.books)
                        file_data += self.position + ' '+self.name  + ' '+self.password + ' '+str(self.books_typeNum) + '\n'
                        for key, value in self.books.items():
                            file_data += key + ' ' + str(value) + '\n'
                        index += int(temp) +1
                        if index == len(file_list): #说明已经到了文件的末尾 直接跳出来
                            break
                    file_data += file_list[index]
                    index += 1
        if self.name not in file_data:   #表用此用户是新注册用户，用户文件还没有存储该用户信息
            self.books_typeNum = len(self.books)
            file_data += self.position + ' ' + self.name + ' ' + self.password + ' ' + str(self.books_typeNum) + '\n'
            for key, value in self.books.items():
                file_data += key + ' ' + str(value) + '\n'
        with open(self.user_filename, 'w', encoding='UTF-8') as file_object:
            file_object.write(file_data)   #重新写入
    # @Description: 将管理者信息写入管理者文件中
    def update_manager_file(self):
        with open(self.manager_filename, 'w', encoding='UTF-8') as file_object:
            file_data = self.name + ' ' + self.password  + '\n'
            file_object.write(file_data)
    # @Description: 更新图书馆书籍文件
    def update_libBooks_file(self):
        file_data = ""
        with open(self.filename_lib_books, 'w', encoding='UTF-8') as file_object:
            for key, value in self.lib_books.items():
                file_data += key + ' ' + str(value) + '\n'
            file_object.write(file_data)   #重新写入
    # @Description: 在用户文件中读取个人信息
    def read_inforFromFile(self):
        with open(self.user_filename, 'r', encoding='UTF-8') as file_object:
            all_lines = file_object.readlines()  #按行读取用户文件
        for location in range(0, len(all_lines)):
            if self.name in all_lines[location].rstrip(): #定位到该行
                temp = all_lines[location].rstrip().split()  # 默认以空格为分隔符对字符串进行切片
                self.position = temp[0]
                self.name = temp[1]
                self.password = temp[2]
                self.books_typeNum = int(temp[3])
                for i in range(0,self.books_typeNum):
                    temp = all_lines[location+i+1].rstrip().split()  # 默认以空格为分隔符对字符串进行切片
                    self.books[temp[0]] = int(temp[1])  # 按行读取借书情况
        with open(self.filename_lib_books, 'r', encoding='UTF-8') as file_object:
            all_lines = file_object.readlines()
        for line in all_lines:
            temp = line.rstrip().split()  # 默认以空格为分隔符对字符串进行切片
            self.lib_books[temp[0]] = int(temp[1])# 按行读取图书馆藏书


