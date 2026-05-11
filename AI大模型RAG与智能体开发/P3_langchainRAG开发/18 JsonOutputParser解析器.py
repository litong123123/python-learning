from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from openai.lib import streaming

#创建所需的解析器
str_parser=StrOutputParser()
json_parser=JsonOutputParser()

#创建模型
model=ChatTongyi(model="qwen3-max",streaming=True)

#创建提示词
first_prompt=PromptTemplate.from_template("我邻居姓：{lastname}，刚生了{gender}，请帮忙取一个名字"
                                          "并封装为JSON格式返回给我。要求key为name，value为你起的名字")

second_prompt=PromptTemplate.from_template("姓名：{name}，请帮我解析含义")

#创建链

chain=first_prompt|model|json_parser|second_prompt|model|str_parser

for chunk in chain.stream({"lastname":"张","gender":"男"}):
    print(chunk,end="",flush=True)


