import json

# 字典示例
d = {
    "name": "周杰轮",
    "age": 11,
    "gender": "男"
}

# Python字典 -> JSON字符串
s = json.dumps(d, ensure_ascii=False)
print("字典转JSON：", s)

# JSON字符串 -> Python字典
d_back = json.loads(s)
print("JSON转字典：", d_back)


# 列表示例（嵌套字典）
l = [
    {
        "name": "周杰轮",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "蔡依临",
        "age": 12,
        "gender": "女"
    },
    {
        "name": "小明",
        "age": 16,
        "gender": "男"
    }
]

# Python列表 -> JSON字符串
l_json = json.dumps(l, ensure_ascii=False)
print("列表转JSON：", l_json)

# JSON字符串 -> Python列表
l_back = json.loads(l_json)
print("JSON转列表：", l_back)