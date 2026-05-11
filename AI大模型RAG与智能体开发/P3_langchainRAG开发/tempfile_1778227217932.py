from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda

# 1. 定义单个示例的展示模板 (Example Prompt)
# 作用：告诉模型，每一个示例都是由“评论”和“JSON结果”组成的
example_prompt = PromptTemplate.from_template(
    "评论: {comment}\n分析结果: {explain}"
)

# 2. 准备示例数据
example_data = [
    {
        "comment": "《星际穿越》太震撼了！诺兰把科幻和亲情融合得完美，看哭了三次。唯一遗憾是中间节奏稍慢。",
        "explain": '{"movie": "星际穿越", "sentiment": "正面", "confidence": 0.85, "keywords": "震撼", "科幻", "亲情", "summary": "对科幻与亲情的融合高度认可，但认为中段节奏偏慢"}'
    },
    {
        "comment": "《上海堡垒》剧情稀烂，特效五毛，鹿晗演军人毫无说服力。",
        "explain": '{"movie": "上海堡垒", "sentiment": "负面", "confidence": 0.95, "keywords": "剧情烂", "特效差", "summary": "对剧情、特效和选角全面否定"}'
    }
]

# 3. 创建 FewShotPromptTemplate (核心组件)
few_shot_prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,      # ✅ 必须传入上面的 example_prompt 对象
    examples=example_data,              # 传入示例数据列表
    prefix="你是一个电影评论分析专家。请分析用户输入的评论，并严格按 JSON 格式返回结果。参考以下示例：",
    suffix="现在请分析这条新评论：\n评论：{input_review}\n分析结果:",
    input_variables=["input_review"],   # ✅ 声明动态输入的变量名
)

# 4. 创建模型和解析器
model = ChatTongyi(model="qwen3-max")
json_parser = JsonOutputParser()

# 5. 定义默认值填充函数 (防止模型漏掉某些 key)
def fill_defaults(data):
    if not isinstance(data, dict):
        return {"movie": "未知", "sentiment": "未知", "confidence": 0.5, "keywords": [], "summary": ""}
    data.setdefault("movie", "未知")
    data.setdefault("sentiment", "未知")
    data.setdefault("confidence", 0.5)
    data.setdefault("keywords", [])
    data.setdefault("summary", "")
    return data

# 6. 构建链 (Chain)
# ✅ 核心修正：使用 few_shot_prompt 而不是简单的 template
chain = few_shot_prompt | model | json_parser | RunnableLambda(fill_defaults)

# 7. 执行
target_comment = "《功夫》真是周星驰的巅峰之作！那个如来神掌从天而降的镜头，小时候看得目瞪口呆。配角也个个出彩，包租公包租婆那段打戏太经典了。不过说实话，结尾黄圣依那段感情线有点突兀，感觉强行塞的。总体还是强推！"

# ✅ 注意：这里的 key "input_review" 必须和 suffix 里的 {input_review} 以及 input_variables 保持一致
result = chain.invoke({"input_review": target_comment})

print("分析结果类型:", type(result))
print("分析结果内容:", result)
