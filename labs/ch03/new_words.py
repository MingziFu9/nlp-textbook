"""拓展：用凝固度和自由度从外卖评论中发现新词（3.3.5 节）"""
import math
import re
from collections import Counter, defaultdict
import jieba
import pandas as pd

jieba.setLogLevel("WARN")
jieba.dt.check_initialized()                     # 加载 jieba 词典，用来排除已收录的词

df = pd.read_csv("waimai_10k.csv")
pieces = []                                      # 去掉非汉字，切成连续的汉字片段
for t in df["review"].astype(str):
    pieces += re.sub(r"[^一-鿿]", " ", t).split()

cnt = Counter()                                  # 统计 1~3 字片段出现的次数
left, right = defaultdict(Counter), defaultdict(Counter)
for p in pieces:
    for n in (1, 2, 3):
        for i in range(len(p) - n + 1):
            w = p[i:i + n]
            cnt[w] += 1
            if n > 1:
                left[w][p[i - 1] if i > 0 else "^"] += 1     # 左边相邻的字（^ 表示开头）
                right[w][p[i + n] if i + n < len(p) else "$"] += 1
N = sum(v for w, v in cnt.items() if len(w) == 1)  # 总字数

def entropy(c):                                  # 自由度：左（右）邻字的信息熵
    s = sum(c.values())
    return -sum(v / s * math.log(v / s) for v in c.values())

def cohesion(w):                                 # 凝固度：所有切法中最小的“互信息”
    return min(math.log(cnt[w] * N / (cnt[w[:k]] * cnt[w[k:]])) for k in range(1, len(w)))

result = []
for w, f in cnt.items():
    if len(w) < 2 or f < 20 or w in jieba.dt.FREQ:   # 至少出现 20 次，且不在 jieba 词典中
        continue
    c, le, re_ = cohesion(w), entropy(left[w]), entropy(right[w])
    if c > 4 and min(le, re_) > 1.5:
        result.append((w, f, c, le, re_))

result.sort(key=lambda r: -r[1])
print(f"{'候选词':<6}{'次数':>5}{'凝固度':>8}{'左自由度':>8}{'右自由度':>8}")
for w, f, c, le, re_ in result[:20]:
    print(f"{w:<6}{f:>6}{c:>9.2f}{le:>10.2f}{re_:>10.2f}")
