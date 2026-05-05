import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models.tongyi import ChatTongyi
import dashscope
from dashscope import TextEmbedding
import os
from typing import List

# ==================== 读取 API Key ====================
api_key = os.environ.get("DASHSCOPE_API_KEY", "")
if "DASHSCOPE_API_KEY" in st.secrets:
    api_key = str(st.secrets["DASHSCOPE_API_KEY"])
    os.environ["DASHSCOPE_API_KEY"] = api_key

# 全局设置 dashscope API Key（最可靠的方式）
dashscope.api_key = api_key

# ==================== 页面配置 ====================
st.set_page_config(page_title="文档问答助手", page_icon="📄")
st.title("📄 基于文档的 RAG 问答系统")

# 诊断：检查 API Key
if api_key:
    st.sidebar.success(f"✅ API Key 已加载 ({api_key[:4]}...{api_key[-4:]})")
else:
    st.sidebar.error("❌ 未检测到 DASHSCOPE_API_KEY，请在 Settings → Secrets 添加")
    st.stop()

# 诊断：测试 Embedding API 连通性
try:
    _test = TextEmbedding.call(model="text-embedding-v2", input=["连通测试"])
    if _test.status_code == 200:
        st.sidebar.success("✅ Embedding API 连接正常")
    else:
        st.sidebar.error(f"❌ Embedding API 错误: code={_test.status_code}, msg={_test.message}")
        st.stop()
except Exception as e:
    st.sidebar.error(f"❌ Embedding API 异常: {type(e).__name__}: {e}")
    st.stop()


# ==================== 自定义 Embedding（直接调 dashscope SDK）====================
class DirectDashScopeEmbeddings(Embeddings):
    """绕过 langchain_community 的 DashScopeEmbeddings（有 bug），直接调用 dashscope SDK"""

    def __init__(self, model: str = "text-embedding-v2"):
        self.model = model

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        all_embeddings = []
        # DashScope 单次最多 25 条
        batch_size = 25
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            resp = TextEmbedding.call(
                model=self.model, input=batch, text_type="document"
            )
            if resp.status_code != 200:
                raise ValueError(
                    f"Embedding 失败: code={resp.status_code}, msg={resp.message}"
                )
            for item in resp.output["embeddings"]:
                all_embeddings.append(item["embedding"])
        return all_embeddings

    def embed_query(self, text: str) -> List[float]:
        resp = TextEmbedding.call(
            model=self.model, input=[text], text_type="query"
        )
        if resp.status_code != 200:
            raise ValueError(
                f"Embedding 失败: code={resp.status_code}, msg={resp.message}"
            )
        return resp.output["embeddings"][0]["embedding"]


# ==================== 初始化模型 ====================
@st.cache_resource
-def init_llm():
+def init_llm(_api_key: str):
    return ChatTongyi(model="qwen-turbo", temperature=0, dashscope_api_key=_api_key)


@st.cache_resource
def init_embeddings():
    return DirectDashScopeEmbeddings(model="text-embedding-v2")


llm = init_llm(api_key)
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
    with st.spinner("正在建立向量索引，请稍候..."):
        try:
            vectorstore = FAISS.from_documents(split_docs, embeddings)
            retriever = vectorstore.as_retriever()
            st.sidebar.success("文档处理完成！现在可以开始提问了。")
        except Exception as e:
            st.error(f"❌ 建立向量索引失败: {type(e).__name__}: {e}")
            st.stop()

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
                try:
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
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response.content}
                    )
                except Exception as e:
                    st.error(f"❌ 回答失败: {type(e).__name__}: {e}")

else:
    st.info("👈 请先在左侧上传一个 PDF 文件以开始使用。")
