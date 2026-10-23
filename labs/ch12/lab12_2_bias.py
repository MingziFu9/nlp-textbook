"""实验 12-2：发现并缓解情感分类模型中的性别偏见"""
import re
import jieba
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

jieba.setLogLevel("WARN")
df = pd.read_csv("waimai_10k.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["label"], test_size=0.2, random_state=42, stratify=df["label"])

# 成对的男性 / 女性称呼
PAIRS = [("小哥", "大姐"), ("大叔", "阿姨"), ("小伙子", "姑娘"), ("哥哥", "姐姐")]
TEMPLATES = ["送餐的{}迟到了半小时", "{}把汤洒了一半", "{}送得挺快的", "今天的{}态度一般"]


def train(texts, labels):
    vec = TfidfVectorizer(tokenizer=jieba.lcut, token_pattern=None, ngram_range=(1, 2), min_df=2)
    model = LogisticRegression(max_iter=1000).fit(vec.fit_transform(texts), labels)
    return vec, model


def audit(vec, model, title):
    """反事实测试：只把句子中的男性称呼换成女性称呼，看正面概率变化多少"""
    print(f"\n===== {title} =====")
    print(f"测试集准确率：{model.score(vec.transform(X_test), y_test):.4f}")
    gaps = []
    for m, f in PAIRS:
        for t in TEMPLATES:
            pm, pf = model.predict_proba(vec.transform([t.format(m), t.format(f)]))[:, 1]
            gaps.append(pm - pf)
        print(f"  {m} vs {f}：正面概率平均相差 {np.mean(gaps[-len(TEMPLATES):]):+.3f}")
    print(f"  全部 {len(gaps)} 组的平均差距：{np.mean(gaps):+.3f}（正数表示偏向男性称呼）")
    return gaps


# ===== 第 1 部分：训练模型，查看称呼词的权重和出现次数 =====
vec, model = train(X_train, y_train)
coef = dict(zip(vec.get_feature_names_out(), model.coef_[0]))
print("称呼词   权重    训练集中出现的评论数   其中正面评论占比")
for m, f in PAIRS:
    for w in (m, f):
        mask = X_train.str.contains(w)
        pos = y_train[mask].mean() if mask.sum() else float("nan")
        print(f"{w:<6}{coef.get(w, float('nan')):>+7.2f}{mask.sum():>14}{pos:>18.0%}")

# ===== 第 2 部分：反事实测试 =====
for m, f in PAIRS[:1]:
    for t in TEMPLATES:
        pm, pf = model.predict_proba(vec.transform([t.format(m), t.format(f)]))[:, 1]
        print(f"{t.format(m)}：{pm:.3f}    {t.format(f)}：{pf:.3f}")
audit(vec, model, "原始模型")

# ===== 第 3 部分：反事实数据增强——把训练数据中的称呼互换，再训练一次 =====
swap = {}
for m, f in PAIRS:
    swap[m], swap[f] = f, m
pattern = re.compile("|".join(sorted(swap, key=len, reverse=True)))
flipped = X_train[X_train.str.contains(pattern)]
augmented = flipped.str.replace(pattern, lambda mt: swap[mt.group()], regex=True)
print(f"\n含有称呼词的训练评论 {len(flipped)} 条，互换称呼后作为新样本加入训练集")
print("示例：", flipped.iloc[0], " ->", augmented.iloc[0])
vec2, model2 = train(pd.concat([X_train, augmented]), pd.concat([y_train, y_train[flipped.index]]))
audit(vec2, model2, "数据增强后的模型")
