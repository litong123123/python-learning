# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#与AI大模型进行交互（参数）
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你的名字叫阿宝宝，你是一个温柔且活泼的智能体"},
        {"role": "user", "content": "你是谁，你能帮我做什么？"},
    ],
    stream=False
)

#输出大模型返回的结果
print(response.choices[0].message.content)