# #元组基本操作-tuple----->元素可重复，有序，不可修改
# #定义
# from itertools import count
#
# t1=(12,32,412,523,23,123,523,5,2345,123,1123)
# print(t1)
# print(type(t1))
#
# #索引访问
# print(t1[0])
# print(t1[-1])
# #切片
# print(t1[0:6])
# #count()统计元素个数
# print(t1.count(123))
# #index()获取元素的位置
# print(t1.index(123))
#
# #注意点：如果定义单元素的原组，单个元素之后需要加上逗号（100，）
# t2=()
# print(t2)
# print(type(t2))
#
# t3=(100)
# print(t3)
# print(type(t3))
#----------------------------------------------元组tuple组包与解包-------------------------------------------
# #组包操作
# t1=12,2,35,3,53,26,32,7,324
# t2=(1,1323,4,234,532,7654,8,43,5,34,63,45)
# #基础解包
# a,b,c,d,e,f,g,h,i=t1
# print(a,b,c,d,e,f,g,h,i)
# # *扩展解包（* 收集剩余的所有元素，封装列表list中）
# first,second,*other,last=t1
# print(first)
# print(second)
# print(*other)
# print(last)
# #案例1：现在俩个变量，分别为：a=10，b=20，现在需要将这两个变量值交换，然后输出到控制台
# a=10
# b=20
# a,b=b,a
# print(a,b)
# #案例2:现在有三个变量，分别为a=100，b=200，c=300，现在需要将着三个变量值进行交换，将a，b，c的值分别赋值给c，a，b并将其输出到控制台
# a=100
# b=200
# c=300
# c,a,b=a,b,c
# print(a,b,c)

"""
根据如下提供的学生成绩单，完成如下需求
  1.计算每个学生的总分，各科平局分，然后一并输出出来
  2.统计各科成绩的最低分，最高分，平均分，并输出
  3.查找成绩优秀（平均分大于90）的学生，并输出
"""
from builtins import max
from os import name

students=(("s001","王林",85,92,78),
          ("s002","李慕",92,88,95),
          ("s003","十三",78,85,82),
          ("s004","犁牛",88,79,91),
          ("s005","增牛",95,96,89),
          ("s006","时期",76,82,77),
          ("s007","洋妞",89,91,94),
          ("s008","甩锅",75,69,82),
          ("s009","美女",86,89,98),
          ("s010","徐天",66,59,72))



#1.计算每个学生的总分，各科平均分，然后一并输出出来----->{avg:.1f}----->保留一位小数
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总数\t\t平均数")
#方式一：
# for s in students:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}")
#方式二：元组解包
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    print(f"{id}\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}")
#2，统计各科成绩的最低分，最高分，平均分，并输出
#2.1获取各科的成绩列表
chinese_scores=[s[2] for s in students]
math_scores=[s[3] for s in students]
english_scores=[s[4] for s in students]
#2.2统计各科成绩的最低分、最高分、平均分，并输出
print(f"语文最低分：{min(chinese_scores)}，最高分：{max(chinese_scores)}，平均分：{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分：{min(math_scores)}，最高分：{max(math_scores)}，平均分：{sum(math_scores)/len(math_scores)}")
print(f"英语最低分：{min(english_scores)}，最高分：{max(english_scores)}，平均分：{sum(english_scores)/len(english_scores)}")
#3.查找成绩优秀（平均分大于90）的学生，并输出
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    if avg>90:
        print(f"平均分大于90的学生姓名：{name},平均分为{avg:.1f}")


