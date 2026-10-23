"""实验 6-3（第 1 部分）：大模型零样本情感分类，并与逻辑回归对比
需要设置环境变量 DEEPSEEK_API_KEY（或其他兼容 OpenAI 接口的大模型）"""
import os
import time
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")

PROMPT = """判断下面这条外卖评论的情感倾向。
只回答一个字：“好”表示好评，“差”表示差评。
评论：{review}"""

def llm_classify(review):
    resp = client.chat.completions.create(
        model=MODEL, temperature=0, max_tokens=2,
        messages=[{"role": "user", "content": PROMPT.format(review=review)}])
    answer = resp.choices[0].message.content.strip()
    return 1 if answer.startswith("好") else 0

# 为节省费用，只取 100 条评论测试（好评、差评各 50 条）
df = pd.read_csv("waimai_10k.csv")
sample = pd.concat([df[df.label == 1].sample(50, random_state=7),
                    df[df.label == 0].sample(50, random_state=7)])
start = time.time()
sample["llm"] = [llm_classify(r) for r in sample["review"]]
print(f"大模型准确率：{(sample['llm'] == sample['label']).mean():.2%}，"
      f"用时 {time.time() - start:.1f} 秒")
wrong = sample[sample["llm"] != sample["label"]]
print("大模型判断错误的评论：")
for _, r in wrong.iterrows():
    print(f"  真实:{'好评' if r.label else '差评'} | {r.review}")
