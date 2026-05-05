import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models.tongyi import ChatTongyi
import os

# ==================== 页面配置 ====================
st.set_page_config(page_title="文档问答助手", page_icon="📄")
st.title("📄 基于文档的 RAG 问答系统")


# ==================== 初始化模型 (利用缓存提高效率) ====================
@st.cache_resource
def init_llm():
    return ChatTongyi(model="qwen-turbo", temperature=0)


@st.cache_resource
def init_embeddings():
    return DashScopeEmbeddings(model="text-embedding-v1")


llm = init_llm()
embeddings = init_embeddings()

# ==================== 侧边栏：文件上传与处理 ====================
st.sidebar.header("1. 上传文档")
uploaded_file = st.sidebar.file_uploader("请上传 PDF 文件", type=["pdf"])

if uploaded_file is not None:
    # 保存上传的文件到本地临时目录
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success("文件上传成功！正在处理...")

    # 第1步：读取
    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    # 第2步：切分
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    # 第3步 & 4步：向量化并存入 FAISS
    with st.spinner('正在建立向量索引，请稍候...'):
        vectorstore = FAISS.from_documents(split_docs, embeddings)
        retriever = vectorstore.as_retriever()

    st.sidebar.success("文档处理完成！现在可以开始提问了。")

    # ==================== 主界面：问答交互 ====================
    st.header("2. 开始提问")

    # 初始化聊天历史
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 显示历史消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 用户输入框
    if prompt := st.chat_input("请输入你的问题..."):
        # 显示用户问题
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # RAG 核心逻辑：检索 + 生成
        with st.chat_message("assistant"):
            with st.spinner("思考中..."):
                # 检索相关文档
                retrieved_docs = retriever.invoke(prompt)
                context = "\n".join([doc.page_content for doc in retrieved_docs])

                # 构造提示词
                sys_prompt = f"""你是一个文档助手，请严格基于以下内容回答问题：
                {context}
                如果内容中没有答案，请如实回答"文档中未找到相关信息"。
                问题：{prompt}
                """

                # 调用大模型
                response = llm.invoke(sys_prompt)
                st.markdown(response.content)

        # 保存助手回复
        st.session_state.messages.append({"role": "assistant", "content": response.content})

else:
    st.info("👈 请先在左侧上传一个 PDF 文件以开始使用。")