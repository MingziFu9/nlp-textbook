"""实验 11-1：调用大模型 API 与提示工程
需要：pip install openai，并设置环境变量 DEEPSEEK_API_KEY（见附录 D）。
使用其他兼容 OpenAI 接口的大模型时，设置 LLM_BASE_URL 和 LLM_MODEL 即可。
"""
import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")


def ask(messages, **kwargs):
    resp = client.chat.completions.create(model=MODEL, messages=messages, **kwargs)
    return resp


# ===== 第 1 部分：第一次调用——角色与 Token 用量 =====
resp = ask([{"role": "system", "content": "你是一名耐心的高职院校计算机老师，回答通俗易懂，不超过 100 字。"},
            {"role": "user", "content": "什么是自然语言处理？"}], temperature=0.3)
print(resp.choices[0].message.content)
u = resp.usage
print(f"输入 {u.prompt_tokens} Token，输出 {u.completion_tokens} Token，合计 {u.total_tokens} Token")

# ===== 第 2 部分：多轮对话——模型的“记忆”是我们发给它的历史 =====
history = [{"role": "system", "content": "你是一个简洁的助手，每次回答不超过 50 字。"}]
for question in ["我叫小王，是人工智能专业的学生。", "推荐一本适合我的入门书。", "我叫什么名字？"]:
    history.append({"role": "user", "content": question})
    answer = ask(history, temperature=0.3).choices[0].message.content
    history.append({"role": "assistant", "content": answer})      # 把回答也加入历史
    print(f"\n用户：{question}\n助手：{answer}")

# ===== 第 3 部分：零样本 vs. 少样本——工单分类 =====
tickets = ["我的快递三天了还没更新物流", "发票抬头开错了，能重开吗", "收到的耳机左边没声音"]
zero_shot = "把客户留言分为【物流】【售后】【财务】三类之一，只输出类别名。\n留言：{}"
few_shot = """把客户留言分为【物流】【售后】【财务】三类之一，只输出类别名。
留言：包裹显示已签收但我没收到 → 物流
留言：想把订单改成公司报销用的专票 → 财务
留言：衣服洗了一次就掉色，要求退货 → 售后
留言：{} →"""
for t in tickets:
    a = ask([{"role": "user", "content": zero_shot.format(t)}], temperature=0).choices[0].message.content
    b = ask([{"role": "user", "content": few_shot.format(t)}], temperature=0).choices[0].message.content
    print(f"\n{t}\n  零样本：{a.strip()}  少样本：{b.strip()}")

# ===== 第 4 部分：思维链——让模型“一步一步想” =====
problem = ("食堂一份套餐原价 15 元，学生卡打八折，每月前 10 份再减 2 元。"
           "小明这个月吃了 25 份套餐，一共花了多少钱？")
for hint in ["直接给出最终答案，只输出数字。", "请一步一步列式计算，最后一行写“答案：xx 元”。"]:
    out = ask([{"role": "user", "content": problem + hint}], temperature=0).choices[0].message.content
    print(f"\n【{hint}】\n{out}")

# ===== 第 5 部分：结构化输出——JSON 模式 =====
review = "上周在你们店买的扫地机器人，吸力很强，但是噪音太大，APP 还老是断线，客服态度倒是挺好。"
resp = ask([{"role": "system", "content": "你是评论分析助手，以 JSON 格式输出。"},
            {"role": "user", "content": "分析下面评论中提到的产品方面及其情感（正面/负面），"
                                        "输出格式：{\"aspects\": [{\"aspect\": \"...\", \"sentiment\": \"...\"}]}\n"
                                        + review}],
           response_format={"type": "json_object"}, temperature=0)
data = json.loads(resp.choices[0].message.content)
for item in data["aspects"]:
    print(f"  {item['aspect']}：{item['sentiment']}")
