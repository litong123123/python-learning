#读文件
# #1.打开文件
#
# f=open("./resource/望庐山瀑布.txt", "r", encoding="utf-8")
# #2.读取文件内容
# # content=f.read()#读取所有内容
# # print(content)
# content_line=f.readlines()
# for line in content_line:
#     print(line.strip())
# #3.关闭文件
# f.close()


# #写文件
# #1.打开文件
#
# f=open("./resource/静夜思.txt", "w", encoding="utf-8")
# #2.写入文件内容
# f.write("静夜思（李白）\n")
# f.write("\n床前明月光，")
# f.write("疑似地上霜。")
# f.write("\n举头望明月，")
# f.write("低头思故乡。")
# #3.关闭文件
# f.close()
#===========================释放资源=========================
# #写文件
# #1.打开文件
#
# f=open("./resource/静夜思.txt", "w", encoding="utf-8")
# try :
# #2.写入文件内容
#     f.write("静夜思（李白）\n")
#     f.write("\n床前明月光，")
#     f.write("疑似地上霜。")
#     f.write("\n举头望明月，")
#     f.write("低头思故乡。")
# finally:
# #3.关闭文件
#     f.close()
#===========================with语句(释放资源的最佳实践)=========================
with open("./resource/静夜思.txt", "w", encoding="utf-8") as f:
    f.write("静夜思（李白）\n")
    f.write("\n床前明月光，")
    f.write("疑似地上霜。")
    f.write("\n举头望明月，")
    f.write("低头思故乡。")


"""
路径写法：从当前文件所在目录开始查找（推荐）
.  :当前目录-----》./resource/静夜思.txt  ./可以省略
.. :上一级目录-----------》../第一章/wozu.txt/

绝对路径：从文件系统根目录开始查找，文件位置的完整路径（注意：反斜杠 在字符串中表示的是转义字符）
方式一：E:\\python\\第一章\\wozu.txt
方式二：E:/python/第一章/wozu.txt



w,r,a:追加模式，新内容会被追加在原有内容之后；文件不存在则创建新文件
"""