"""实验 5-1：词袋模型、TF-IDF 关键词提取与相似文章推荐"""
import jieba
import jieba.analyse
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jieba.setLogLevel("WARN")
stopwords = set(open("cn_stopwords.txt", encoding="utf-8").read().split())

def tokenize(text):
    """分词并去掉停用词、单字和数字"""
    return [w for w in jieba.cut(text)
            if len(w) > 1 and w not in stopwords and not w.isdigit()]

# ===== 第 1 部分：词袋模型 =====
docs = ["我喜欢自然语言处理", "我喜欢机器学习", "自然语言处理和机器学习都很有趣"]
cv = CountVectorizer(tokenizer=jieba.lcut, token_pattern=None)
bow = cv.fit_transform(docs)
print("词表：", list(cv.get_feature_names_out()))
print("词袋矩阵：")
print(pd.DataFrame(bow.toarray(), columns=cv.get_feature_names_out()))

# ===== 第 2 部分：TF-IDF 关键词提取 =====
news = pd.read_csv("news_samples.csv")
tfidf = TfidfVectorizer(tokenizer=tokenize, token_pattern=None)
matrix = tfidf.fit_transform(news["content"])
words = tfidf.get_feature_names_out()
print(f"\n8 篇新闻共有 {len(words)} 个不同的词，TF-IDF 矩阵形状：{matrix.shape}")
for i in [0, 2, 6]:
    row = matrix[i].toarray()[0]
    top = row.argsort()[::-1][:5]                 # 权重最大的 5 个词
    print(f"《{news.title[i]}》关键词：",
          "、".join(f"{words[j]}({row[j]:.2f})" for j in top))

# jieba 自带的 TF-IDF 关键词提取（使用 jieba 内置的大语料 IDF）
print("\njieba.analyse 提取第 1 篇关键词：",
      jieba.analyse.extract_tags(news.content[0], topK=5))

# ===== 第 3 部分：余弦相似度与“猜你喜欢” =====
sim = cosine_similarity(matrix)
print("\n文章相似度矩阵（保留两位小数）：")
print(pd.DataFrame(sim, index=news.id, columns=news.id).round(2))

def recommend(article_id, k=2):
    i = article_id - 1
    order = sim[i].argsort()[::-1]
    order = [j for j in order if j != i][:k]       # 去掉文章自己
    return [(news.title[j], float(round(sim[i][j], 2))) for j in order]

for aid in [1, 6]:
    print(f"\n读了《{news.title[aid-1]}》的用户，猜你喜欢：", recommend(aid))
