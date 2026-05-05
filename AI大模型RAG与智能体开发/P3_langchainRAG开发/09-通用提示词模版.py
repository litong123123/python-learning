from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

#zero-shot(零提示回答)

prompt_template=PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我取一个名字，简单回答"
)
model=Tongyi(model="qwen-max")

#调用.format方法注入信息即可
# prompt_text=prompt_template.format(lastname="王",gender="男孩")
# res=model.invoke(input=prompt_text)
# print( res)

chain=prompt_template | model
res=chain.invoke(input={"lastname":"王","gender":"男孩"})
print( res)