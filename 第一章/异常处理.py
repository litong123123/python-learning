#异常处理
try:
    print("======================")
    #print(s)
    # print(1/0)
    print("asdasd"[10])
    print("===========================")
except NameError as e:
    print("名字不存在，请联系管理员：~:异常信息：",e)
except ZeroDivisionError as e:
    print("0不能做被除数，请联系管理员：~:异常信息：", e)
except Exception as e:
    print("程序出错了，请联系管理员：~:异常信息：", e)
finally:#无论程序你是否正常运行，finally中的代码都会运行
    print("资源释放")

