from langchain_ollama.embeddings import OllamaEmbeddings

#创建模型对象 不传model默认用的是text-embedding-v1
model=OllamaEmbeddings(model="qwen3-embedding:4b")

#不用invoke stream
#embed_query, embed_documents

print(model.embed_query("你好"))
print(model.embed_documents(["你好","我很好","你好不好"]))
