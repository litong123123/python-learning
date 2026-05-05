
"""
语法：
{元素, 元素, ..., ..., 元素}
元素必须是： key:value   称之为键值对 KV对
key不能重复（如果重复，后面的值，会覆盖前面的值）key必须得是不可变类型（str,int,float,tuple） 不能为list,set,dict
value 可以是任意类型（可以是数据容器）
字典的值是可以修改的
无法用下标，可以用key找到对应的value
就像生活中查字典，用字 找到对应的 含义
"""
#
# # 空字典
# d = {}
# print(type(d))  # 打印结果：&lt;class 'dict'&gt;
# d = dict()
# print(type(d))
#
# # 字面量
# {"周杰轮": 99, "王力鸿":88, "林军杰": 77}
#
# # 变量
# d = {"周杰轮": 99, "王力鸿": 88, "林军杰": 77, 0: 66}
#
# # 没有下标 d[0] 本质是找0这个key  而不是找0这个下标
# # 访问元素的语法： 字典变量[key]   注意[]里面不是下标而是key的值
# print(d[0])
# print(d["周杰轮"])
#
# # 字典的key是不可以重复的
# d = {"周杰轮": 99, "王力鸿": 88, "林军杰": 77 }
# # 打印出来后 第二个林军杰覆盖第一个林军杰
# print(d)
#
# #验证字典的值是否是可以修改的
# d["林军杰"]=66
# print(d)
# ------------------------------ 字典 常见操作 ------------------------------
# dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["涛哥"]= 620
# print(dict1)
#
# # 查询
# print(dict1["涛哥"])  # 根据key获取value
# print(dict1.get("涛哥"))  # 根据key获取value
#
# print(dict1.keys())  # 获取所有的key
# print(dict1.values())  # 获取所有的value
# print(dict1.items())  # 获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("许立国")
# print(score) #可以获取到删除的值
# print(dict1)
#
# del dict1["韩立"]
# print(dict1) #获取不到删除的值
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
# for item in dict1.items():
#     print(f"{item[0]}:{item[1]}")
# for k,v in dict1.items():
#     print(f"{k}:{v}")
'''
案例：
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的购物车商品名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx，商品价格：xxx，商品数量：xxx”。
5. 退出购物车

    结构：shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
'''
shopping_cart = {}
#1.制作菜单
print("欢迎使用购物车管理系统~")

menu="""
###############购物车系统###############
#             1.添加购物车             #
#             2.修改购物车             #
#             3.删除购物车             #
#             4.查询购物车             #
#             5.退出购物车             #
#######################################
"""
print(menu)
#2.执行的具体操作
while True:
    choice = input("请选择要执行的操作（1-5）：")
    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = input("请输入商品数量：")
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕")
        case "2":  # 修改购物车
            goods_name = input("请输入要修改的商品名称：")
            # 如果商品不存在，则提示错误信息，请重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")

            else:
                goods_price = float(input("请输入最新的商品价格："))
                goods_num = input("请输入商品最新的数量：")
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕")
        case "3":  # 删除购物车
            # 如果商品不存在，则提示错误信息，请重新选择
            goods_name = input("请输入要删除的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")
            # shopping_cart.pop(goods_name)

        case "4":  # 查询购物车
            # goods_name = input("请输入要查询的商品名称：")
            # print(f"商品名称：{goods_name}，商品价格：{shopping_cart[goods_name[0]]}，商品数量：{shopping_cart[goods_name[1]]}")
            for goods_name in shopping_cart:
                num = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格:{num['price']},商品数量：{num['num']}")
        case "5":  # 退出购物车
            break
        case _:  # 匹配其他所有情况
            print('非法操作，不支持')