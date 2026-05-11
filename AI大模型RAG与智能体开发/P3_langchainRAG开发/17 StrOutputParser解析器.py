from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from  langchain_core.messages import AIMessage

parser=StrOutputParser()
model=ChatTongyi(model="qwen3-max")
prompt=PromptTemplate.from_template("我的邻居姓{lastname}，她生了个{gender}，请起个名字,仅告知我名字无需其他内容")

chain=prompt|model|parser|model| parser

#model输出的是AIMessage通过parser转换成str，因为model要求输入的是Str
res:str=chain.invoke({"lastname":"张","gender":"女儿"})

print(res)

print(type(res))
