import os

import streamlit as st
from openai import OpenAI
import os

#这是一个标题
st.title("AI智能伴侣")

#logo
st.logo("😊")

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages =[]
    #遍历初始化列表
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

#创建一个与AI大模型交互的client对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#聊天框
prompt = st.chat_input("请输入你要问的问题")


#与AI大模型进行交互（参数）
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你的名字叫阿宝宝，你是一个温柔且活泼的智能体"},
            {"role": "user", "content":prompt },
        ],
        stream=False
    )
    st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})



#侧边栏
with st.sidebar:
    nick_name = st.text_input("昵称")
    nick_nature = st.text_area("性格")