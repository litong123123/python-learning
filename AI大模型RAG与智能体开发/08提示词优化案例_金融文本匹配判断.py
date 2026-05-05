from openai import OpenAI
import os

client = OpenAI(
    #api_key="ollama",
    #base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com"
    #base_url="http://localhost:11434/v1"
)
examples_data = {
    "是": [
        ("公司ABC发布了季度财报，显示盈利增长。", "财报披露，公司ABC利润上升。"),
        ("公司ITCAST发布了年度财报，显示盈利大幅度增长。", "财报披露，公司ITCAST更赚钱了。")
    ],
    "不是": [
        ("黄金价格下跌，投资者抄售。", "外汇市场交易额创下新高。"),
        ("央行降息，刺激经济增长。", "新能源技术的创新。")
    ]
}

questions = [
    ("利率上升，影响房地产市场。", "高利率对房地产有一定冲击。"),
    ("油价大幅度下跌，能源公司面临挑战。", "未来智能城市的建设趋势越加明显。"),
    ("股票市场今日大涨，投资者乐观。", "持续上涨的市场让投资者感到满意。")
]

"""
{"role": "system", "content": "f你帮我完成文本匹配，我给你2个句子，被[]包围，你判断它们是否匹配，回答是或不是，请参考如下示例："},
{"role": "user", "content": "句子1: [公司ABC发布了季度财报，显示盈利增长。] 句子2: [财报披露，公司ABC利润上升。]"},
{"role": "assistant", "content": "是"},
{"role": "user", "content": "句子1: [公司ITCAST发布了年度财报，显示盈利大幅度增长。] 句子2: [财报披露，公司ITCAST更赚钱了。]"},
{"role": "assistant", "content": "是"},
{"role": "user", "content": "句子1: [黄金价格下跌，投资者抄售。] 句子2: [外汇市场交易额创下新高。]"},
{"role": "assistant", "content": "不是"},
{"role": "user", "content": "句子1: [央行降息，刺激经济增长。] 句子2: [新能源技术的创新。]"},
{"role": "assistant", "content": "不是"},
{"role": "user", "content": "f按照上述示例，回答这2个句子的情况。句子1: [...], 句子2: [...]"}
"""

# ================== 构建messages ==================
messages = [
    {
        "role": "system", "content": "f你帮我完成文本匹配，我给你2个句子，被[]包围，你判断它们是否匹配，回答是或不是，请参考如下示例："
    }
]

# 加入示例（few-shot）
for key, value in examples_data.items():
    for example in value:
        messages.append({
            "role": "user",
            "content": f"句子1: [{example[0]}] 句子2: [{example[1]}]"
        })
        messages.append({
            "role": "assistant",
            "content": key
        })
#输入问题
for q in questions:
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages + [
            {
                "role": "user",
                "content": f"句子1: [{q[0]}] 句子2: [{q[1]}]"
            }
        ]
    )
    result = response.choices[0].message.content
    print(result)