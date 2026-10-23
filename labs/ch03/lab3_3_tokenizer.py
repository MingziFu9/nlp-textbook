"""实验 3-3：大模型分词器体验
使用通义千问（Qwen）的分词器。dashscope 安装包里自带了分词器文件，
不需要联网下载模型：pip install dashscope"""
from dashscope import get_tokenizer

tokenizer = get_tokenizer("qwen-turbo")

# ===== 第 1 部分：看看大模型是怎么“切词”的 =====
samples = ["自然语言处理", "我爱北京天安门", "Natural language processing",
           "unbelievable", "yyds绝绝子", "ChatGPT和DeepSeek", "2026年11月6日", "😂👍"]
for text in samples:
    ids = tokenizer.encode(text)
    pieces = [tokenizer.decode([i]) for i in ids]
    print(f"{text:<28} {len(ids):>2} 个 Token：{pieces}")

# ===== 第 2 部分：中英文的 Token 效率对比 =====
zh = "人工智能正在深刻改变我们的生活和工作方式。"
en = "Artificial intelligence is profoundly changing the way we live and work."
for name, text in [("中文", zh), ("英文", en)]:
    n = len(tokenizer.encode(text))
    print(f"{name}：{len(text)} 个字符 → {n} 个 Token，平均每个 Token {len(text)/n:.2f} 个字符")

# ===== 第 3 部分：估算 API 调用费用 =====
import pandas as pd
reviews = pd.read_csv("waimai_10k.csv")["review"]
total = sum(len(tokenizer.encode(r)) for r in reviews)
chars = reviews.str.len().sum()
print(f"\n{len(reviews)} 条评论共 {chars} 个字符，{total} 个 Token")

# 假设：输入单价 每百万 Token 2 元（请以各平台最新价格为准）
price_per_million = 2.0
prompt_tokens = 60                       # 每次调用附带的提示词大约 60 个 Token
cost = (total + prompt_tokens * len(reviews)) / 1_000_000 * price_per_million
print(f"逐条调用大模型做情感分析，输入部分费用约 {cost:.2f} 元")
