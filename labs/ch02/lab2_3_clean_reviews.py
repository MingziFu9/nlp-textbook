"""实验 2-3：中文评论数据清洗"""
import re
import pandas as pd
from opencc import OpenCC

df = pd.read_csv("reviews_raw.csv")
print("原始数据：", df.shape[0], "条")

cc = OpenCC("t2s")                                   # 繁体转简体
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")  # 常见表情符号的编码范围

def to_halfwidth(s):
    """全角字符转半角：全角字符的编码比半角大 0xFEE0，全角空格单独处理"""
    out = []
    for ch in s:
        code = ord(ch)
        if code == 0x3000:
            code = 0x20
        elif 0xFF01 <= code <= 0xFF5E:
            code -= 0xFEE0
        out.append(chr(code))
    return "".join(out)

def clean(text):
    text = str(text)
    text = re.sub(r"<[^>]+>", "", text)              # ① 去 HTML 标签
    text = re.sub(r"https?://\S+", "", text)          # ② 去网址
    text = re.sub(r"@\S+\s?", "", text)               # ③ 去 @用户名
    text = re.sub(r"#[^#]+#", "", text)               # ④ 去 #话题#
    text = EMOJI.sub("", text)                        # ⑤ 去表情符号
    text = to_halfwidth(text)                         # ⑥ 全角转半角
    text = cc.convert(text)                           # ⑦ 繁体转简体
    text = re.sub(r"([，。！？!?,.])\1+", r"\1", text)  # ⑧ 连续重复标点只留一个
    text = re.sub(r"\s+", " ", text).strip()          # ⑨ 合并多余空白
    return text

df["clean"] = df["review"].apply(clean)

# 对比几条清洗前后的效果
for i in [0, 3, 6, 9, 5]:
    print(f"\n[{df.id[i]}] 清洗前：{df.review[i]!r}\n     清洗后：{df.clean[i]!r}")

# ⑩ 删除清洗后过短的评论（少于 2 个字）
before = len(df)
df = df[df["clean"].str.len() >= 2]
print(f"\n删除过短评论：{before - len(df)} 条")

# ⑪ 去重
before = len(df)
df = df.drop_duplicates(subset="clean")
print(f"删除重复评论：{before - len(df)} 条")

df[["id", "label", "clean"]].to_csv("reviews_clean.csv", index=False, encoding="utf-8")
print("清洗完成，剩余", len(df), "条，已保存到 reviews_clean.csv")

# 规则处理不了的“疑难样本”：网络用语、语义重复
print("\n规则处理不了的样本：")
for t in df["clean"].tail(2):
    print("  ", t)
