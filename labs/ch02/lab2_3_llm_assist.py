"""实验 2-3（第 2 部分）：让大模型辅助处理规则搞不定的疑难样本
使用前请先在 DeepSeek 开放平台（platform.deepseek.com）申请 API Key，
并设置环境变量 DEEPSEEK_API_KEY。其他兼容 OpenAI 接口的国产大模型
（如阿里云百炼、智谱、Kimi）只需修改 base_url 和 model 即可。"""
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")

PROMPT = """你是一名数据清洗员。请把下面这条外卖评论改写成规范的书面中文：
1. 网络用语、拼音缩写改成普通说法；
2. 删除无意义的重复词语；
3. 不要改变原意，不要添加原文没有的信息；
4. 只输出改写后的评论，不要输出其他内容。
评论：{review}"""

hard_samples = ["yyds!绝绝子,下次还点",
                "送餐太慢了,菜都凉透了,差评差评差评差评",
                "两个小时后送来的,鱼早冷了,简直腥哭 详情见"]

for review in hard_samples:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT.format(review=review)}],
        temperature=0,          # 温度设为 0，让输出尽量稳定
    )
    print(f"原文：{review}\n改写：{resp.choices[0].message.content.strip()}\n")
