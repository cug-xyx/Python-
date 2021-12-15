'''
    设计“学生成绩管理系统”，实现学生信息的录入、显示、查找、添加、保存以及成绩排序等功能模块
    要求功能选择用菜单实现（菜单可用字符串输出，或用Tkinter实现），数据输入和结果输出要求用文件存放
    数据文件格式：
    学号  姓名  英语  高数  C语言
    8541  张三  75    72    86
    8537  李四  83    62    71
'''


class Student(object):
    def __init__(self, s_id, s_name, s_eng, s_math, s_clang):
        self.s_id = s_id
        self.s_name = s_name
        self.s_eng = s_eng
        self.s_math = s_math
        self.s_clang = s_clang


# 用于读取txt文档
def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('文件未找到')


# 用于修改数据
def write_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        import json
        json.dump(data, file)


# 用于读取数据
def read_json(file_name, default):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        return default


def add_students():
    d = read_json('student_data.json', dict())
    if not d:
        students = list()
        max_num = 0
    else:
        students = d['all_students']
        max_num = d['max_num']

    while True:
        # s_id = input('输入学生学号：')
        s_name = input('输入学生姓名：')
        s_eng = input('输入学生英语成绩：')
        s_math = input('输入学生高数成绩：')
        s_clang = input('输入学生C语言成绩：')

        max_num += 1

        s_id = str(max_num).zfill(4)

        s = Student(s_id, s_name, s_eng, s_math, s_clang)
        # 将一个对象的所有属性以dict保存
        students.append(s.__dict__)
        data = {
            'all_students': students,
            'num': len(students),
            'max_num': max_num
        }

        write_json('student_data.json', data)

        choice = input('添加成功！\n1. 继续\n2.返回\n请选择（1 - 2）：')
        if choice == '1':
            pass
        elif choice == '2':
            break
        else:
            print('请重新输入')


def show_students():
    d = read_json('student_data.json', dict())
    opt = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n4.返回\n请选择：')

    students = d.get('all_students', list())
    if not students:
        print('您还未添加学生，请添加学生')
        return
    if opt == '1':
        for student in students:
            print('学号：{s_id}，姓名：{s_name}，英语：{s_eng}，高数：{s_math}，C语言：{s_clang}'.format(**student))
    elif opt == '2':
        s_name = input('请输入学生姓名：')

        same_name_student = filter(lambda s: s['s_name'] == s_name, students)
        if not same_name_student:
            print('未找到该学员')

        for student in same_name_student:
            print('学号：{s_id}，姓名：{s_name}，英语：{s_eng}，高数：{s_math}，C语言：{s_clang}'.format(**student))
    elif opt == '3':
        s_id = input('请输入学生id：')
        same_id_student = filter(lambda s: s['s_id'] == s_id, students)
        if not same_id_student:
            print('未找到该学员')
        for student in same_id_student:
            print('学号：{s_id}，姓名：{s_name}，英语：{s_eng}，高数：{s_math}，C语言：{s_clang}'.format(**student))
    elif opt == '4':
        return
    else:
        print('输入有误')


def sort_students():
    d = read_json('student_data.json', dict())
    students = d.get('all_students', list())

    if not students:
        print('您还未添加学生，请添加学生')
        return

    opt = input('1.按英语成绩排序\n2.按高数成绩排序\n3.按C语言成绩排序\n请选择（1 - 3）：')
    if opt == '1':
        result = sorted(students, key=lambda x: int(x['s_eng']), reverse=True)
        for student in result:
            print('学号：{s_id}，姓名：{s_name}，英语：{s_eng}，高数：{s_math}，C语言：{s_clang}'.format(**student))
    elif opt == '2':
        result = sorted(students, key=lambda x: int(x['s_math']), reverse=True)
        for student in result:
            print('学号：{s_id}，姓名：{s_name}，英语：{s_eng}，高数：{s_math}，C语言：{s_clang}'.format(**student))
    elif opt == '3':
        result = sorted(students, key=lambda x: int(x['s_clang']), reverse=True)
        for student in result:
            print('学号：{s_id}，姓名：{s_name}，英语：{s_eng}，高数：{s_math}，C语言：{s_clang}'.format(**student))
    else:
        print('输入有误')


# 主程序
def start():
    content = read_file('welcome.txt')
    while True:
        operator = input(content + '\n请选择（1 - 4）：')
        if operator == '1':
            # 录入学生信息
            add_students()
        if operator == '2':
            # 查找学生信息
            show_students()
        elif operator == '3':
            # 学生成绩排序
            sort_students()
        if operator == '4':
            exit(0)
        else:
            print('输入有误')


if __name__ == '__main__':
    start()
