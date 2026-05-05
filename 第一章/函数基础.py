#函数定义
#函数定义的时候并不会执行，只有在调用的时候才会执行，函数必须先定义在调用
# def uno_123():
#     print("-------------")
#
# #函数调用
# uno_123()
# uno_123()



#函数的参数与返回值
#函数1：计算函数的面积
def yuan(r):
    mianji=3.14*r*r
    return mianji
area=yuan(5)
print(area)
#函数2：计算长方形的面积
def changfangxing(x,y):
    mianji=x*y
    return mianji
area=changfangxing(3,4)
print(area)
#计算圆的面积，周长====半径
def yuan(r):
    """
    计算圆的周长以及面积
    :param r: 圆的半径
    :return: 面积 周长
    """
    mianji=3.14*r*r
    zhaouchang=2*r*3.14
    return mianji,round(zhaouchang,1)
print(yuan(10))
help(yuan)