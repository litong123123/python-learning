#引入json模块
import json
# #写入json数据
# json_str = {"name": "李统",
#             "age": 18,
#             "gender": "男",
#             "hobbies":["看电影", "听音乐", "旅游"]}
# #写入json文件
# with open("./resource/json_data.json", "w", encoding="utf-8") as f:
#     #ensure_ascii:默认为True，确保所有的数据输出的数据都是ascii编码（非ASCII码会进行转义），False，非ASCII码保留原样输出
#     #indent:会在输出的json数据中添加缩进，方便阅读
#     json.dump(json_str, f, ensure_ascii=False, indent=2)

#读取json数据
with open("./resource/json_data.json", "r", encoding="utf-8") as f:
    user=json.load(f)
    print(user)
    print(type(user))