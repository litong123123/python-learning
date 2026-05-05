from langchain_ollama import ChatOllama

#得到模型对象，qwen3-max就是聊天模型

model=ChatOllama(model="deepseek-r1:8b")

#准备消息列表

messages=[
    ("system","你是一个边塞诗人"),
    ("human","给我写一首唐诗"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human","按照以上实例，再写一首诗")
]

#调用Stream流式执行

res=model.stream(input=messages)

#for循环迭代打印输出，通过.content来获取到内容

for chunk in res:
    print(chunk.content,end="",flush=True)
