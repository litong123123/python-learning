#电影评论智能分析器
#用 LangChain 构建一个命令行工具，输入一段电影评论，输出结构化分析结果。
from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableLambda

# 1. 定义单个示例的展示模板 (Example Prompt)
# 作用：告诉模型，每一个示例都是由“评论”和“JSON结果”组成的
example_prompt = PromptTemplate.from_template(
    "评论: {comment}\n分析结果: {explain}"
)

#示例的模版

few_shot_template=PromptTemplate.from_template("请对以下此电影评论{comment}进行结构化分析,参照{explain}")

example_data=[{"comment":"《星际穿越》太震撼了！诺兰把科幻和亲情融合得完美，看哭了三次。唯一遗憾是中间节奏稍慢。",
 "explain": '{"movie": "星际穿越", "sentiment": "正面", "confidence": 0.85, "keywords": ["震撼", "科幻", "亲情", "节奏慢"], "summary": "对科幻与亲情的融合高度认可，但认为中段节奏偏慢"}'
 },
              {
                  "comment": "《上海堡垒》剧情稀烂，特效五毛，鹿晗演军人毫无说服力。",
                  "explain": '{"movie": "上海堡垒", "sentiment": "负面", "confidence": 0.95, "keywords": ["剧情烂", "特效差", "选角失败"], "summary": "对剧情、特效和选角全面否定"}'
              },
              ]

json_parser = JsonOutputParser()

suffix = "请对以下评论进行结构化分析，严格按JSON格式返回：\n评论：{input_review}\n分析结果："

def fill_defaults(data):
 data.setdefault("movie", "未知")
 data.setdefault("sentiment", "未知")
 data.setdefault("confidence", 0.5)
 data.setdefault("keywords", [])
 data.setdefault("summary", "")
 return data
model=ChatTongyi(model="qwen3-max")
chain = few_shot_template | model | json_parser | RunnableLambda(fill_defaults)

if __name__ == '__main__':
    result = chain.invoke({"comment": "《功夫》真是周星驰的巅峰之作！...", "explain": "请参考示例格式"})
    print(result) # 直接是 dict



