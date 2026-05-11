from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

template=PromptTemplate.from_template( "我的邻居是：{lastname},最喜欢的食物是：{food}")

res=template.format(lastname="王明",food="烤牛排")#format是关键字传参,纯字符串形式
print(res,type(res))

res1=template.invoke({"lastname":"litong","food":"chigali"})#invoke是键值对传参
print(res1,type(res1))
