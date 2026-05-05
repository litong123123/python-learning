import streamlit as st
#页面设置
st.set_page_config(
    page_title="浏览器表头位置",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#大标题
st.title("大阿达阿达是的")
st.header("一级标题")
st.subheader("二级标题")
import streamlit as st

st.button("两个标题")
if st.button("说你好"):
    st.write("为什么你好")
else:
    st.write("再见")

if st.button("Aloha"):
    st.write("Ciao")
genre=st.radio("你运动会得了第几名",["第一","第二","第三"],
               captions=["牛逼",
        "一般",
        "不行啊"],
               )

if genre == "第一":
    st.write("第一牛逼牛逼")
else:
    st.write("你也不行啊")