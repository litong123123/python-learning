#
# """
# 语法：
# {元素, ..., ..., 元素}
# """
# # 字面量
# {1, 2, 3, "itheima"}
#
# # 空集合
# s = set()       # 空集合只能这样写
# s = {}          # 这不能创建空集合，反而是空字典
# print(type(s))  # <class 'dict'>
#
# # 变量
# s = {1, 2, 3}
# print(type(s))  # <class 'set'>
#
# # 修改集合
# # 下标
# # s[0] = 10     # 集合没有下标
# print(s)
#
# # 去重
# s = {1, 1, 2, 2, 3, 3, "itheima", "itheima", "黑马", "黑马"}
# print(s)        # 去重了
#
#
# # add添加新元素
# s = {1, 2, 3}
# s.add(4)
# s.add(4)    # 多次添加4也只能加入1个因为去重
# print(s)
#
# # 移除元素
# s = {1, 2, 3}
# s.remove(2)
# # s.remove(4) 如果不存在数据被移除，则报错
# print(s)
#
# # pop取出元素
# s = {1, 2, 3}
# element = s.pop()     # 没有参数可以传 随机取
# print(f"取出元素{element}，集合内容：{s}")
#
# # 清空集合
# s = {1, 2, 3}
# s.clear()
# print(s)
# s = {1, 2, 3}
# s = set()       # 重新赋值为空集合也可以达到同样效果
# print(s)


# # 取出差集
# s1 = {1, 3, 5}
# s2 = {1, 3, 6}
# # 保留s1有的 s2没的 放入s3  s1和s2不变
# s3 = s1.difference(s2)
# print(f"s1:{s1}, s2:{s2}, s3:{s3}")
# # 保留s2有的 s1没的 放入s4  s1和s2不变
# s4 = s2.difference(s1)
# print(f"s1:{s1}, s2:{s2}, s4:{s4}")
#
# # 消除差集
# s1 = {1, 3, 5}
# s2 = {1, 3, 6}
# # 在s1内删除和s2相同的，即s1被修改，s2不变
# s1.difference_update(s2)
# print(f"s1:{s1}, s2:{s2}")
#
# s1 = {1, 3, 5}
# s2 = {1, 3, 6}
# # 在s2内删除和s1相同的，即s2被修改，s1不变
# s2.difference_update(s1)
# print(f"s1:{s1}, s2:{s2}")
#
# # 合并集合
# s1 = {1, 3, 5}
# s2 = {1, 3, 6}
# # s1 s2不变，合并为s3（会去重）
# s3 = s1.union(s2)
# print(f"s1:{s1}, s2:{s2}, s3:{s3}")
#
# # 查看集合元素个数
# s = {1, 2, 3, 4, 5}
# print(len(s))
#
# s = {1, 2, 3, 4, 5, 5, 5, 5, 1, 3, 1}
# # 集合支持遍历，但是顺序无法保证
# for i in s:
#     print(i)

# print("aaa" ,s[2]) 集合无法用下标

# 去重某list  list->set->list （顺序无法保证）
#-----------------------------------案例---------------------------------
# 选课篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"通天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# 补充：选修足球学生名单（代码中缺失，根据上下文补全）
football_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露", "许木"}

# 1. 找出同时选修了 法语 和 艺术 的学生
# 方式一：intersection() 方法
fa_set1=french_set.intersection(art_set)
print(f"同时选修了 法语 和 艺术 的学生：{fa_set1}")

# 方式二：& 运算符 交集
fa_set2=french_set&art_set
print(f"同时选修了 法语 和 艺术 的学生：{fa_set2}")

# 2. 找出同时选修了所有四门课程的学生
all_sets=french_set&art_set&football_set&basketball_set
print(f"同时选修了四门课的学生：{all_sets}")

# 3. 找出选修了足球，但是没有选修篮球的学生 - 差集
# 方式一：difference() 方法
fb_set1=football_set.difference(basketball_set)
print(f"选修了足球但没选修篮球的学生（方法一）：{fb_set1}")

# 方式二：- 运算符 差集
fb_set2 = football_set - basketball_set
print(f"选修了足球但没选修篮球的学生（方法二）：{fb_set2}")

#方式三：集合推导式----->快速构建集合，语法：{要往集合中添加的数据 for s in set1 if 条件}
fb_set3 ={s for s in basketball_set if s not in football_set}
print(f"选修了足球但没选修篮球的学生（方法三）：{fb_set3}")

# 4，统计每一个学生选修的课程数量
#4.1获取到学生名单
#all_set=basketball_set.union(football_set).union(art_set).union(french_set)
all_set=basketball_set|football_set|art_set|french_set
print(all_set)
#4.2获取每一个学生的选修的课程数量
all_list = [*basketball_set,*football_set,*art_set,*french_set]

for s in all_set:
    print(f"{s}选修了{all_list.count(s)}课程")




