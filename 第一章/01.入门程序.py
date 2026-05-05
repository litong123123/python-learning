# # 需求：控制台中输出hello world,hello Python
# print("hello world")
# print("hello world")
# print("hello world")
# print("---------------")
# print(100)
# print(True)
# print("asdasdasdzxc")
# print("----------------")
# print(None)
# print(True+1)
# print(False-1)
# num,base=123,23
# print("总的和为:",num+base)
# a,b,c=100,200,300
# d=c
# c=a
# a=b
# b=d
# print(a,b,c)
from calendar import day_name
from os import name
from tokenize import endpats

# aa=1
# print(type("name"))
# print(type(True))
# print(type(None))
# print(isinstance(aa,int))
# 字符串的拼接
# s1="人生苦短""我用Python"
# print(s1)
# msg1="涛哥"
# age=18
# msg3=("软件工程")
# msg4=("Python,Java")
#
# print("\"大家好，我是"+msg1+" ,今年 "+str(int(age))+"岁,学习的专业是"+msg3+",爱好"+msg4+"\"")  #str(int(数字))---->将int类型的数字转为字符串
#字符串格式化1
# msg1="涛哥"
# age=18
# msg3=("软件工程")
# msg4=("Python,Java")
#
# print("\"大家好，我是%s ,今年%s岁,学习的专业是%s,爱好%s\""%(msg1,age,msg3,msg4))
#
# #字符串格式化2
# #f"内容{变量/表达式}"
# msg1="涛哥"
# age=18
# msg3=("软件工程")
# msg4=("Python,Java")
#
# print(f"\"大家好，我是{msg1} ,今年{age}岁,学习的专业是{msg3},爱好{msg4}\"")
# name=input("请输入你的名字：")
# print(f"欢迎您{name}")
# age=input("请输入你的年龄")
# print(f"您今年{age}岁了")

# s=10000
# password=input("请输入你的密码：")
# print(f"密码正确：{password}")
#
# age=input("输入取款金额")
#
# print(f"您的余额为{s-int(age)}元")

# x=float(input("请输入第一个数："))
# y=float(input("请输入第二个数："))
# print(f"x+y={x+y}，x-y={x-y}")

# score=int(input("请输入你的分数："))
# while score>0:
#     if score>650:
#         print("我可以去读河大")
#     else:
#         print("我去家里蹲")
# while score<0:
#     print("鉴定完毕，你是傻逼")

# zhanghao=int(input("请输入您的账号："))
# mima=int(input("请输入您的密码："))
# if zhanghao != 188 or mima != 456:
#     print('密码错误，验证失败')
# else:
#     print('密码正确准许进入')

# years=float(input("请输入年份"))
# if (years%4==0 and years%100!=0) or years%400==0:
#     print('此年份为闰年')
# else:
#     print('此年份为平年')

#
# ad=str(input('请输入您的用户名'))
# password=int(input('请输入您的密码'))
# if (ad=='admin'and password==666888)or (ad=='root'and password==547527) or (ad=='zhangsan'and password==123456) :
#     print('登录成功')
# else:
#     print('登陆失败')
# a=input('请输入三角形的三个边长:a边长为：')
# b=input('请输入三角形的三个边长:b边长为：')
# c=input('请输入三角形的三个边长:c边长为：')
# if a==b==c:
#     print('为等边三角形')
# elif a==b or b==c or c==a:
#     print('为等腰三角形')
# else:
#     print('为普通三角形')
'''match...case语法的学习'''
# day_name=input('请输入进入星期几：')
# match day_name:
#     case '1':print(11111)
#     case '2':print(22222)
#     case '3':print(33333)
#     case '4':print(44444)
#     case '5':print(55555)
#     case '6'|'7':print('周末休息')
#     case _ :print("输出错误")
# 计算器
#  '''while语句'''
# a=1
# while a<=10:
#     print('人生苦短，我用Python')
#     a=a+1
# print('循环停止，执行完毕')
# 计算1-100之间所有偶数的累加之和

'''计算1=100之间所有奇数之和，计算100-500之间左右3的倍数的数字之和'''
# total=0
# for i in range(1,101):
#    if i%2!=0:
#       total+=i
# print(total)
# total=0
# for i in range(100,501):
#    if i%3==0:
#       total+=i
# print(total)
# kuandu=int(input('请输入长方形的宽度'))
# changdu=int(input('请输入长方形的长度'))
# for i in range(kuandu):
#    for j in range(changdu):
#       print('*',end='')
#    print()  #print语句自动换行功能

#打印99乘法表
# j=1
# for i in range(1,10):
#    for j in range(1,j+1):
#       print(f"{j}*{i}={i*j}",end='\t')
#       j+=1
#    print()
#打印等腰直角三角形 打印数字金字塔 打印国际象棋棋盘
# a=int(input('请输入等腰直角三角形的边长'))
# for i in range(a):
#    for j in range(i+1):
#       print('*', end='\t')
#       j+=1
#    print()

#打印数字金字塔
# a=int(input('请输入数字金字塔的边长'))
# for i in range(a):
#    for j in range(i+1):
#       print(j+1, end='\t')
#       j+=1
#    print()
#打印国际象棋棋盘
# a=int(input('请输入棋盘的的边长'))
# for i in range(a):
#    if i%2==0:
#       for j in range(a):
#          if j % 2 == 0:
#             print('!', end='\t')
#             j += 1
#          else:
#             print('*', end='\t')
#    else:
#       for j in range(a):
#          if j % 2 == 0:
#             print('*', end='\t')
#             j += 1
#          else:
#             print('!', end='\t')
#
#    print()

# a=1
# while a:
#    mingzi = input('请输入您的用户名:')
#    password = input('请输入您的密码:')
#    if mingzi ==''or password =='':
#       print('输入的密码或者用户名不能为空，请重新输入')
#       continue
#    elif (mingzi=="lisi" and password=='666888') or (mingzi=='zhangsan' and password=='123456') or (mingzi=='taoge' and password=='888666'):
#       break
#    else :
#        print('验证失败，请继续输入')
#        continue
#
# print('登录成功，进入B站')
'''猜数字游戏'''
# import random
# random_number=random.randint(1,100)
# while 1 :
#     a = int(input('请您输入一个数字：'))
#     if a==random_number:
#         break
#     elif a>random_number:
#         print('您的数字太大了')
#     else :
#         print('您的数字太小了')
# print(f"恭喜您猜对了就是这个数字{random_number}")
'''数组里面的数据可以是重复的，并且有顺序性并且可以是不同类型的，比如数字和字符都能一起存。数组可以正向索引且可以反向索引 删除的话用del s[8]'''
# s=[1,2,3,4,5,6,7,8,9,0]
# print(s[3:5:2])
# print(type(s[3:5:2]))
'''append() --->在列表的尾部追加元素  s.append(10086)
   insert() --->在指定索引之前，插入该元素 s.insert(0,92)
   remove() --->移除列表中第一个匹配到的值 s.remove(75)
   pop()    --->删除列表中指定索引位置的元素（如果未指定索引，默认删除最后一个） s.pop()
   sort()   --->对列表进行排序（列表元素的数据类型一致，才可以排序） s.sort()
   reverse()--->反转列表元素 s.reverse()
   '''
s=[]
i=0
zonghe=0
for i in range(10):
    num = float(input('请输入十个数字'))
    s.append(num)
    zonghe+=num
    i += 1
s.sort()

print(f"数组的排序为{s}")
print(f"数组的最大值为{s[9]}")
print(f"数组的最小值为{s[0]}")
print(f"数组的平均值为{sum(s)/len(s)}")  #sum是数组求和，len是数组的个数，mix是数组获取最小值 max是数组获取最大值！！！！！！








