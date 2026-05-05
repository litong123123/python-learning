# ==================== 导入必要的库 ====================
# 从 langchain_community 导入 PDF 文档加载器，用于读取 PDF 文件
from langchain_community.document_loaders import PyPDFLoader

# 从 langchain_text_splitters 导入递归字符文本分割器，用于将长文本切分成小块
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 从 langchain_openai 导入 OpenAI 的嵌入模型（这里虽然导入了但实际未使用）
from langchain_openai import OpenAIEmbeddings

# 从 langchain_community 导入 FAISS 向量数据库，用于存储和检索向量
from langchain_community.vectorstores import FAISS

# 从 langchain_community 导入阿里云通义千问聊天模型
from langchain_community.chat_models.tongyi import ChatTongyi

# ==================== 第1步：读取 PDF 文档 ====================
# 创建 PDF 加载器实例，指定要读取的 PDF 文件路径
loader = PyPDFLoader("测试/测试文件.pdf")

# 调用 load() 方法加载 PDF 文件，返回文档列表（每个元素包含页面内容和元数据）
docs = loader.load()

# ==================== 第2步：文本切分 ====================
# 创建递归字符文本分割器实例
# chunk_size=500: 每个文本块的最大字符数为 500
# chunk_overlap=50: 相邻文本块之间重叠 50 个字符（避免信息被切断）
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# 将加载的文档按照设定的规则进行切分，返回切分后的文档列表
split_docs = text_splitter.split_documents(docs)

# ==================== 第3步：文本向量化（Embedding）====================
# 注意：如果使用阿里云模型，建议使用 DashScopeEmbeddings
# embeddings = OpenAIEmbeddings()   #把文本变成"数字向量"

# 从 langchain_community 导入阿里云 DashScope 的嵌入模型
from langchain_community.embeddings import DashScopeEmbeddings

# 创建阿里云嵌入模型实例，使用 text-embedding-v1 模型
# 作用：将文本转换为高维向量（数字数组），便于计算机理解和比较语义相似度
embeddings = DashScopeEmbeddings(model="text-embedding-v1")

# ==================== 第4步：存入向量数据库 ====================
# 使用 FAISS 向量数据库存储切分后的文档及其向量表示
# from_documents() 方法会自动调用 embeddings 将文本转换为向量并存入数据库
vectorstore = FAISS.from_documents(split_docs, embeddings)

# ==================== 第5步：创建检索器 ====================
# 将向量数据库转换为检索器对象
# as_retriever() 创建一个可以从向量数据库中检索相关文档的工具
retriever = vectorstore.as_retriever()

# ==================== 第6步：初始化大语言模型（LLM）====================
# 创建阿里云通义千问聊天模型实例
# model="qwen-max": 使用 qwen-max 模型（阿里云最强模型）
# temperature=0: 温度参数设为 0，使输出更加确定和一致（减少随机性）
llm = ChatTongyi(model="qwen-max", temperature=0)

# ==================== 第7步：定义问答函数（RAG 核心逻辑）====================
def ask(question):
    """
    RAG 问答函数
    参数 question: 用户提出的问题
    返回: AI 生成的答案
    """
    
    # 使用检索器查找与问题最相关的文档片段
    # invoke() 方法会根据问题的向量表示，在向量数据库中搜索相似度最高的文档
    docs = retriever.invoke(question)

    # 将检索到的所有文档内容拼接成一个字符串，用换行符分隔
    # doc.page_content 获取文档的文本内容
    context = "\n".join([doc.page_content for doc in docs])

    # 构建提示词（Prompt），包含检索到的上下文和用户问题
    # 这是一个典型的 RAG 提示词模板：先给背景知识，再提问题
    prompt = f"""
    你是一个文档助手，请基于以下内容回答问题：

    {context}

    问题：{question}
    """

    # 调用大语言模型生成回答
    # invoke() 方法将提示词发送给 LLM，并获取生成的回复
    response = llm.invoke(prompt)
    
    # 返回 AI 的回答内容
    return response


# ==================== 第8步：测试运行 ====================
# 进入无限循环，持续接收用户输入并回答问题
while True:
    # 等待用户输入问题，并将输入保存到变量 q 中
    q = input("请输入问题：")
    
    # 调用 ask() 函数获取 AI 的回答，并打印到控制台
    print(ask(q))

