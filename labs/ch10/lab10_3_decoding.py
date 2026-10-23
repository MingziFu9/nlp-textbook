"""实验 10-3 第 1 部分：训练一个字级语言模型，体验贪心、温度、Top-k、Top-p 解码"""
from collections import Counter, defaultdict
import numpy as np
import pandas as pd

reviews = pd.read_csv("waimai_10k.csv")["review"].astype(str)

# ===== 第 1 步：统计“前两个字 → 下一个字”的次数（三元字模型） =====
BOS, EOS = "^", "$"                      # 句首、句尾标记
counts = defaultdict(Counter)
for r in reviews:
    s = BOS * 2 + r + EOS
    for i in range(len(s) - 2):
        counts[s[i:i + 2]][s[i + 2]] += 1
print("模型记住的“两字上下文”数量：", len(counts))


def next_char_probs(context, temperature=1.0):
    """根据前两个字，给出下一个字的概率分布；温度用来调节分布的“尖锐”程度"""
    c = counts[context[-2:]]
    chars = list(c)
    logits = np.log(np.array([c[ch] for ch in chars], dtype=float))
    p = np.exp(logits / temperature)
    return chars, p / p.sum()


# ===== 第 2 步：看看温度如何改变概率分布 =====
for T in [0.5, 1.0, 2.0]:
    chars, p = next_char_probs("味道", T)
    top = sorted(zip(chars, p), key=lambda t: -t[1])[:5]
    print(f"温度 {T}：“味道”后面最可能的字 " + "  ".join(f"{c}:{q:.2f}" for c, q in top))


# ===== 第 3 步：四种解码方法生成评论 =====
def generate(prefix, method="greedy", temperature=1.0, k=5, p_top=0.9, max_len=30, rng=None):
    text = BOS * 2 + prefix
    for _ in range(max_len):
        chars, p = next_char_probs(text, temperature)
        if method == "greedy":                       # 贪心：永远选概率最大的字
            ch = chars[int(np.argmax(p))]
        else:
            order = np.argsort(-p)
            if method == "top_k":                    # Top-k：只在概率最高的 k 个字里抽
                keep = order[:k]
            elif method == "top_p":                  # Top-p：在累计概率达到 p 的最小集合里抽
                cum = np.cumsum(p[order])
                keep = order[:np.searchsorted(cum, p_top) + 1]
            else:                                    # 纯随机采样：按概率在全部字里抽
                keep = order
            q = p[keep] / p[keep].sum()
            ch = chars[rng.choice(keep, p=q)]
        if ch == EOS:
            break
        text += ch
    return text[2:]


rng = np.random.default_rng(2026)
print("\n贪心解码：")
for prefix in ["送餐", "味道", "下次"]:
    print("  ", generate(prefix, "greedy"))
for name, kw in [("随机采样 温度0.7", dict(method="sample", temperature=0.7)),
                 ("随机采样 温度1.5", dict(method="sample", temperature=1.5)),
                 ("Top-k (k=5)", dict(method="top_k")),
                 ("Top-p (p=0.9)", dict(method="top_p"))]:
    print(f"\n{name}：")
    for _ in range(3):
        print("  ", generate("味道", rng=rng, **kw))
