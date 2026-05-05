'''开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5. 列出所有学生：遍历所有学生信息并输出。
6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7．退出系统。
                   结构：student_cart = {"name":{"chinese_score":123,"math_score":150,"english_score":150}"}
'''

student_cart = {}
menu=()
menu="""
##################################################【菜单】#############################################
#       1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统    #
######################################################################################################
"""

print(menu)
while True:
    choice=input("请选择要执行的操作（1-7）：")
    match choice:
     case '1':
         student_name=input("请输入学生姓名：")
         if student_name  in student_cart:
             print("此学生已存在")
         else:
             chinese_score = float(input("请输入学生的语文成绩："))
             math_score = float(input("请输入学生的数学成绩："))
             english_score = float(input("请输入学生的英语成绩："))
             student_cart[student_name]= {"chinese": chinese_score,
                                          "math": math_score,
                                          "english": english_score}
             print("添加完成")
     case '2':
         student_name = input("请输入学生姓名：")
         if student_name  not in student_cart:
             print("此学生不已存在，错误输入")
         else:
             chinese_score = float(input("请输入学生的语文成绩："))
             math_score = float(input("请输入学生的数学成绩："))
             english_score = float(input("请输入学生的英语成绩："))
     case '3':
         wu=input('请输入您要删除的学生姓名：')
         if wu  not in student_cart:
             print("此学生不已存在，错误输入")
         else:
             del student_cart[wu]
     case '4':
         for student_name in student_cart:
             sum=student_cart[student_name]
             print(f"学生的名字：{student_name},学生的语文成绩：{sum['chinese']},学生的数学成绩：{sum['math']},学生的英语成绩：{sum['english']}")
     case '5':
         for student_name in student_cart:
             print(f'所有学生的名字为：{student_cart.keys()}')
     case '6':
            if not student_cart:
                print("暂无学生，无法统计！")
                continue

            # 1. 初始化统计变量
            total_stu = len(student_cart)  # 总人数
            # 语文
            sum_cn, max_cn, min_cn = 0, 0, 150
            max_cn_name, min_cn_name = "", ""
            # 数学
            sum_math, max_math, min_math = 0, 0, 150
            max_math_name, min_math_name = "", ""
            # 英语
            sum_en, max_en, min_en = 0, 0, 150
            max_en_name, min_en_name = "", ""

            # 2. 遍历所有学生，计算总分、最高分、最低分
            for name, score in student_cart.items():
                # 取出当前学生三科成绩
                cn = score["chinese"]
                math = score["math"]
                en = score["english"]

                # 累加总分（计算平均分用）
                sum_cn += cn
                sum_math += math
                sum_en += en

                # 统计语文最高分/最低分
                if cn > max_cn:
                    max_cn, max_cn_name = cn, name
                if cn < min_cn:
                    min_cn, min_cn_name = cn, name

                # 统计数学最高分/最低分
                if math > max_math:
                    max_math, max_math_name = math, name
                if math < min_math:
                    min_math, min_math_name = math, name

                # 统计英语最高分/最低分
                if en > max_en:
                    max_en, max_en_name = en, name
                if en < min_en:
                    min_en, min_en_name = en, name

            # 3. 计算平均分
            avg_cn = sum_cn / total_stu
            avg_math = sum_math / total_stu
            avg_en = sum_en / total_stu

            # 4. 打印统计结果
            print("=" * 50)
            print(f"班级总人数：{total_stu}")
            print(f"语文成绩：最高分={max_cn}({max_cn_name})，最低分={min_cn}({min_cn_name})，平均分={avg_cn:.1f}")
            print(
                f"数学成绩：最高分={max_math}({max_math_name})，最低分={min_math}({min_math_name})，平均分={avg_math:.1f}")
            print(f"英语成绩：最高分={max_en}({max_en_name})，最低分={min_en}({min_en_name})，平均分={avg_en:.1f}")
            print("=" * 50)

     case '7':  # 退出系统
            print("退出教务管理系统，再见！")
            break

     case _:  # 非法输入
            print("输入错误，请输入1-7的数字！")






