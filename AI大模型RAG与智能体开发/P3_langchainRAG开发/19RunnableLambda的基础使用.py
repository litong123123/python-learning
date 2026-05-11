from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from openai.lib import streaming

#创建所需的解析器
str_parser=StrOutputParser()

#创建模型
model=ChatTongyi(model="qwen3-max",streaming=True)

#创建提示词
first_prompt=PromptTemplate.from_template("我邻居姓：{lastname}，刚生了{gender}，请帮忙取一个名字,只生成一个名字，不要其他内容")

second_prompt=PromptTemplate.from_template("姓名：{name}，请帮我解析含义")

#函数的入参：AIMessage-->dic  ({"name":"xxxx"})

my_func=RunnableLambda(lambda ai_msg:{"name":ai_msg.content})  #自己定义函数

chain=first_prompt|model|my_func|second_prompt|model|str_parser

for chunk in chain.stream({"lastname":"张","gender":"男"}):
    print(chunk,end="",flush=True)