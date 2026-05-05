#langchain_ollama
from langchain_ollama import OllamaLLM

model=OllamaLLM(model="deepseek-r1:8b")
res=model.invoke(input="你是谁 能做什么")
print(res)