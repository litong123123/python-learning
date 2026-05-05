# #合并两个容器的数据，并且去除重复数据
# num_list1=[112,3213,4,2,3,4,5,23,5,33,5,6]
# num_list2=[123,123,452,5,32,2,43,213,123,1,23]
# #普通遍历获得新容器加数据
# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
# #去除重复数据
# num_list=[]
# for num in num_list1:
#     if num not in num_list:
#         num_list.append(num)
# print(num_list)

# #合并两个容器的数据，并且去除重复数据
# num_list1=[112,3213,4,2,3,4,5,23,5,33,5,6]
# num_list2=[123,123,452,5,32,2,43,213,123,1,23]
# #解包：将列表这一类容器解开成一个一个独立的元素
# #组包：将多个值合并到一个容器
# num_list=[*num_list1,*num_list2]
# print(num_list)
# #去除重复数据
# new_list=[]
# for num in num_list:
#      if num not in new_list:
#          new_list.append(num)
# print(new_list)
#方式3：
#合并两个容器的数据，并且去除重复数据
# num_list1=[112,3213,4,2,3,4,5,23,5,33,5,6]
# num_list2=[123,123,452,5,32,2,43,213,123,1,23]
# #解包：将列表这一类容器解开成一个一个独立的元素
# #组包：将多个值合并到一个容器
# num_list=num_list1+num_list2
# print(num_list)
# #去除重复数据
# new_list=[]
# for num in num_list:
#      if num not in new_list:
#          new_list.append(num)
# print(new_list)

#1.生成1-20的平方列表。2.从如下数字列表中提取所有偶数，并计算平方，组成一个新的列表 num_list[22,32,5,2,35,2,35,2,32,6,34,6,34]
new=[]
# for i in range(1,21):
#     new.append(i**2)
#     i+=1
#列表推导式---->就是按照一定的规则快速生成一个列表的方法--->语法格式1：【要插入的值 for i in 序列/列表】
new=[i**2 for i in range(1,21)]

#2.从如下数字列表中提取所有偶数，并计算平方，组成一个新的列表 num_list[22,32,5,2,35,2,35,2,32,6,34,6,34]
#语法格式2：【要插入的值 for i in 序列/列表 if 条件】
num_list=[22,32,5,2,35,2,35,2,32,6,34,6,34]
new_list=[ i**2 for i in num_list if i%2==0]
print(new_list)


