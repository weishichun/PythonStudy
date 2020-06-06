from datetime import datetime
data = [
    {'name': '小张', 'sex': '男', 'birthday': '19870615'},
    {'name': '小李', 'sex': '女', 'birthday': '19870615'},
    {'name': '小王', 'sex': '女', 'birthday': '19910615'},
    {'name': '小赵', 'sex': '男', 'birthday': '20000615'},
    {'name': '小强', 'sex': '男', 'birthday': '20051212'}
]

class Student:
    def __init__(self,name,sex,birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

    def getAge(self):
        return datetime.now().year - int(self.birthday[:4])

class Student_System:
    def __init__(self,name):
        self.name = name
        self.data = []

    def beautyPrint(self,data_list):
        for index,student in enumerate(data_list):
            print(f'序号:{index}',end=' ')
            print(f'姓名:{student.name}',end=' ')
            print(f'性别:{student.sex:2}',end=' ')
            print(f'年龄:{student.getAge()}',end=' ')
            print()

    def load_data(self):
        for item in data:
            student = Student(item['name'],item['sex'],item['birthday'])
            self.data.append(student)

    def show_menu(self):
        print(f"""
        ****************************
        欢迎使用[{self.name}]
            1. 显示所有学生信息
            2. 新建学生信息
            3. 查询学生信息
            4. 修改学生信息
            5. 删除学生信息
            0. 退出系统
        ****************************
            """)

    def show_all_studen(self):
        self.beautyPrint(self.data)

    def input_name(self):
        while True:
            name = input("输入名字:").strip()
            if name:
                return  name
            else:
                continue

    def chose_sex(self):
        sex = input("输入性别(1男|2女):").strip()
        if sex == '1':
            return  "男"
        elif sex == '0':
            return '女'
        else:
            return  '未知'

    def create_student(self):
        name = self.input_name()
        sex = self.chose_sex()
        birthday = input("输入生日:")
        student = Student(name,sex,birthday)
        self.data.append(student)

    def find_studen(self):
        find_list = self.find_stu_by_name()
        self.beautyPrint(find_list)

    def modify_student(self):
        find_list = self.find_stu_by_name()
        if find_list:
            self.beautyPrint(find_list)
            index = int(input("输入修改序号:"))
            student = find_list[index]
            print("当前修改的是:")
            self.beautyPrint([student])
            name = input('修改名字:').strip()
            sex = self.chose_sex()
            birthday = input("修改生日:")
            if name:
                student.name = name
            student.sex = sex
            student.birthday = birthday



    def find_stu_by_name(self):
        name = self.input_name()
        find_list = []
        for student in self.data:
            if name.lower() in student.name.lower():
                find_list.append(student)
        if find_list:
            return  find_list
        else:
            print(f'未找到学生{name}')

    def delete_student(self):
        find_list = self.find_stu_by_name()
        if find_list:
            self.beautyPrint(find_list)
            index = int(input("输入删除序号:"))
            student = find_list[index]
            print("当前删除的是:")
            self.beautyPrint([student])
            self.data.remove(student)

    def star(self):
        self.load_data()
        while True:
            self.show_menu()
            op = input("输入序列号,选择操作:")
            if op == '1':
                self.show_all_studen()
            elif op == '2':
                self.create_student()
            elif op == '3':
                self.find_studen()
            elif op == '4':
                self.modify_student()
            elif op == '5':
                self.delete_student()
            elif op == '0':
                print("退出系统")
                break
            else:
                print("请输入正确操作序号....")

if __name__ == '__main__':
    Student_System("ABC学生系统").star()

    def start(self):
        self.load_data()
