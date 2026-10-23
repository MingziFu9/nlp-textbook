"""实验 6-1：基于情感词典的情感分析"""
import jieba
import pandas as pd

jieba.setLogLevel("WARN")

# 一个小型情感词典（真实词典有上万个词，如知网 HowNet、大连理工情感词汇本体库）
POSITIVE = {"好吃", "好", "不错", "满意", "快", "新鲜", "美味", "喜欢", "赞", "棒",
            "推荐", "热情", "准时", "实惠", "干净", "香", "划算", "周到", "好评", "可口"}
NEGATIVE = {"难吃", "差", "慢", "凉", "冷", "失望", "贵", "少", "咸", "淡", "差评",
            "糟糕", "恶心", "垃圾", "退款", "投诉", "硬", "腥", "坑", "难等"}
NEGATIONS = {"不", "没", "没有", "别", "无", "并非", "不是"}
DEGREE = {"太": 2.0, "很": 1.5, "非常": 2.0, "特别": 2.0, "超": 2.0, "有点": 0.5, "稍微": 0.5}


def sentiment_score(text, verbose=False):
    words = jieba.lcut(text)
    score = 0.0
    for i, w in enumerate(words):
        if w in POSITIVE or w in NEGATIVE:
            s = 1.0 if w in POSITIVE else -1.0
            # 往前看最多 3 个词：遇到程度副词就加权，遇到否定词就翻转
            for prev in words[max(0, i - 3):i]:
                if prev in DEGREE:
                    s *= DEGREE[prev]
                if prev in NEGATIONS:
                    s *= -1
            if verbose:
                print(f"    {w}: {s:+.1f}")
            score += s
    return score


examples = ["味道很好，送餐也快", "太难吃了，再也不点了", "不好吃，而且送得非常慢",
            "味道不错，就是有点贵", "包装没有破损，饭菜也没凉"]
for t in examples:
    print(t)
    sc = sentiment_score(t, verbose=True)
    print(f"  总分 {sc:+.1f} → {'好评' if sc > 0 else '差评' if sc < 0 else '中性'}")

# 在 2000 条真实评论上测试准确率
df = pd.read_csv("waimai_10k.csv").sample(2000, random_state=1)
df["score"] = df["review"].apply(sentiment_score)
df["pred"] = (df["score"] > 0).astype(int)        # 大于 0 判为好评(1)，否则差评(0)
acc = (df["pred"] == df["label"]).mean()
print(f"\n2000 条评论上的准确率：{acc:.1%}")
print("得分为 0（词典里一个词都没匹配上）的评论占比：", f"{(df['score'] == 0).mean():.1%}")
