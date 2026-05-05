#csv操作  方式1：文件操作的原始方式
#写
# with open ("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名，年龄，性别，爱好\n")  #写入表头
#     f.write("小王，18，男，football\n")
#     f.write("小李，12，男，ball\n")
#     f.write("小王，14，男，足球\n")
#     f.write("小王，16，男，baseball\n")
#读

# with open ("csv_data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


#csv操作  方式2：csv（推荐）
import csv

#写
# with open ("csv_data/02.csv","w",encoding="utf-8",newline="") as f:
#     writer=csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
#     writer.writeheader()
#     writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"football"})
#     writer.writerow({"姓名":"小王","年龄":12,"性别":"男","爱好":"ball"})
#     writer.writerow({"姓名":"李哥","年龄":14,"性别":"男","爱好":"足球"})
#     writer.writerow({"姓名":"统哥","年龄":16,"性别":"男","爱好":"baseball"})

#写
with open ("csv_data/02.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row)


