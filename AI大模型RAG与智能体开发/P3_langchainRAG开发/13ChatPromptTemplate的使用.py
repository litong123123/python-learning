from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import OllamaLLM
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
prompt_text=chat_prompt_template.invoke({"history":history_data}).to_string()

model=OllamaLLM(model="deepseek-r1:8b")
res=model.invoke(prompt_text)
print(res)

