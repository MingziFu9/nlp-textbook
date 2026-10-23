"""实验 6-2：电商评论情感分类与模型评估"""
import jieba
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay)

jieba.setLogLevel("WARN")
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "SimHei", "PingFang SC"]

# ===== 第 1 部分：准备数据 =====
df = pd.read_csv("waimai_10k.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["label"], test_size=0.2, random_state=42, stratify=df["label"])
print("训练集：", len(X_train), "条；测试集：", len(X_test), "条")

# 特征：TF-IDF，同时使用单个词和相邻两个词（N-gram）
vec = TfidfVectorizer(tokenizer=jieba.lcut, token_pattern=None, ngram_range=(1, 2), min_df=2)
Xtr = vec.fit_transform(X_train)        # 只在训练集上“学习”词表和 IDF
Xte = vec.transform(X_test)             # 测试集只做转换
print("特征维度：", Xtr.shape[1])

# ===== 第 2 部分：训练并比较三种模型 =====
models = {"朴素贝叶斯": MultinomialNB(),
          "逻辑回归": LogisticRegression(max_iter=1000),
          "支持向量机": LinearSVC()}
for name, clf in models.items():
    clf.fit(Xtr, y_train)
    print(f"{name} 准确率：{accuracy_score(y_test, clf.predict(Xte)):.4f}")

# ===== 第 3 部分：详细评估逻辑回归 =====
best = models["逻辑回归"]
pred = best.predict(Xte)
print("\n分类报告：")
print(classification_report(y_test, pred, target_names=["差评", "好评"], digits=4))
cm = confusion_matrix(y_test, pred)
print("混淆矩阵：\n", cm)
ConfusionMatrixDisplay(cm, display_labels=["差评", "好评"]).plot(cmap="Blues")
plt.title("逻辑回归混淆矩阵")
plt.savefig("confusion_matrix.png", dpi=150, bbox_inches="tight")

# ===== 第 4 部分：错误分析——看看模型错在哪里 =====
result = pd.DataFrame({"review": X_test, "label": y_test, "pred": pred})
wrong = result[result["label"] != result["pred"]]
print(f"\n判断错误 {len(wrong)} 条，随机展示 6 条：")
for _, r in wrong.sample(6, random_state=3).iterrows():
    print(f"  真实:{'好评' if r.label else '差评'} 预测:{'好评' if r.pred else '差评'} | {r.review}")

# ===== 第 5 部分：模型学到了什么——权重最大的词 =====
words = vec.get_feature_names_out()
coef = best.coef_[0]
top_pos = coef.argsort()[::-1][:10]
top_neg = coef.argsort()[:10]
print("\n最能代表好评的词：", "、".join(words[i] for i in top_pos))
print("最能代表差评的词：", "、".join(words[i] for i in top_neg))

# ===== 第 6 部分：预测新评论 =====
new = ["菜量很足，味道也正宗，下次还来", "等了两个小时，饭都凉了", "还行吧，一般般"]
for t, p in zip(new, best.predict_proba(vec.transform(new))):
    print(f"  {t} → 好评概率 {p[1]:.2f}")
