from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi

prompt=PromptTemplate.from_template("你是一个AI助手")
model=ChatTongyi(model="qwen-max")

chain=prompt| model

print(type(chain))