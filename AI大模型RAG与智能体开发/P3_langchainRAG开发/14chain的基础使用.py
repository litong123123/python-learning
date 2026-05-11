from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import OllamaLLM
from langchain_community.llms import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi
chat_prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗")
    ]
)
history_data=[
    {"role":"human","content":"写一首诗吧"},
    {"role":"ai","content":"床前明月光，疑是地上霜。举头望明月，低头思故乡"},
    {"role":"human","content":"再来一首"},
    {"role":"ai","content":"锄禾日当午，汗滴禾当午。谁知盘中餐，粒粒皆辛苦"}
    ]
model=ChatTongyi(model="qwen3-max", streaming=True)
chain=chat_prompt_template | model
# res=chain.invoke({"history":history_data})
# print(res.content)
#通过流式输出
for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end="",flush=True)

