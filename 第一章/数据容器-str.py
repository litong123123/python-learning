#字符串 基本操作----->不可变的（无法修改）,有序性，可迭代性
# s="hello world"
# print(s[4])
# print(s[-8])
# #切片
# print(s[0:5:1])
# print(s[:5:])
# print(s[:5])
# print(s[6::1])
# #步长--->正数：从前往后截取；负数：从后往前截取
# print(s[-1:-7:-1])
# print(s[::-1])
#---------------------------字符串常用方法------------------------------

# s="     hello-python-hello-world    "
# #find()查找指定字符串第一次出现的索引位置
# index=s.find("-")
# print(index)
# #count()统计子字符串在指定字符串中出现的次数
# c=s.count("-")
# print(c)
# upper()转大写  lower()转小写
# daxie=s.upper()
# xiaoxie=s.lower()
# print(xiaoxie)
# print(daxie)
# #split()将字符串按照指定字符串切割-列表
# slist=s.split("-")
# print(slist)
# #strip()去除字符串两端的空格
# ss=s.strip()
# print(ss)
# #replace()将字符串中的指定字串替换成新的内容
# sr=s.replace("-","*")
# print(sr)
# #startswith()/endwith判断字符串是否是以指定的字符串开头/结尾，返回布尔值
# print(s.startswith("    "))
# print(s.endswith("phython"))
#-------------------------------字符串案例--------------------------------------------
#案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）如果输入正确，输出邮箱格式正确，否则输出邮箱格式错误
#方式1：------->
#1.接收用户输入的邮箱
# ema=input('请输入您的邮箱号：')
# #2.判断邮箱的格式是否正确
# if ema.count('@')==1 and ema.count('.')>=1:
#     print('邮箱格式正确')
# else:
#     print('邮箱格式错误')
#方式二：in 运算符---->判断子串是否存在字符串中，存在，返回True；否则，返回False
#1.接收用户输入的邮箱
# ema=input('请输入您的邮箱号：')
# #2.判断邮箱的格式是否正确
# if ema.count('@')==1 and '.'in ema:
#     print('邮箱格式正确')
# else:
#     print('邮箱格式错误')
#练习 1。输入一个字符串,判断该字符串是否是回文（两边对称）。
#2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来
zfc=input('请输入您的字符串')
if zfc[::]==zfc[-1::-1]:
    print('是回文')
else:
    print('不是')
daxie=zfc.upper()
fanzhuan=daxie[::-1]
for i in fanzhuan:
    print(i)





