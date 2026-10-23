"""实验 5-2：训练 Word2Vec 词向量"""
import zipfile
import jieba
import pandas as pd
from gensim.models import Word2Vec

jieba.setLogLevel("WARN")

# ===== 第 1 部分：准备语料：6 万多条网购评论，每条评论分词后是一个词列表 =====
with zipfile.ZipFile("online_shopping_10_cats.zip") as z:
    df = pd.read_csv(z.open("online_shopping_10_cats.csv"))
reviews = df["review"].dropna().astype(str)
sentences = [jieba.lcut(r) for r in reviews]
print("评论数：", len(sentences), " 示例：", sentences[1][:12])

# ===== 第 2 部分：训练模型 =====
model = Word2Vec(sentences,
                 vector_size=100,   # 每个词用 100 个数字表示
                 window=5,          # 看前后各 5 个词
                 min_count=5,       # 出现少于 5 次的词忽略
                 sg=1,              # 1 = Skip-gram，0 = CBOW
                 workers=4, epochs=5, seed=42)
print("词表大小：", len(model.wv))
print("“手机”的词向量（前 8 维）：", model.wv["手机"][:8].round(3))

# ===== 第 3 部分：找近义词 =====
for w in ["手机", "快递", "好吃", "酒店", "差"]:
    sims = model.wv.most_similar(w, topn=6)
    print(f"与“{w}”最相似：", "、".join(f"{x}({s:.2f})" for x, s in sims))

# ===== 第 4 部分：计算相似度与类比 =====
for a, b in [("手机", "电脑"), ("手机", "苹果"), ("手机", "洗发水"), ("满意", "失望")]:
    print(f"相似度({a}, {b}) = {model.wv.similarity(a, b):.3f}")
# 类比：手机 - 电池 + 酒店 ≈ ?
print("手机 - 电池 + 酒店 ≈", model.wv.most_similar(positive=["酒店", "电池"],
                                                 negative=["手机"], topn=3))
print("不合群的词：", model.wv.doesnt_match(["香蕉", "苹果", "橙子", "键盘"]))

model.save("shopping_w2v.model")      # 保存模型，下次用 Word2Vec.load() 加载

# ===== 第 5 部分：降维可视化 =====
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "SimHei", "PingFang SC"]
words = ["手机", "电脑", "屏幕", "电池", "键盘", "酒店", "房间", "早餐",
         "香蕉", "苹果", "橙子", "水果", "好", "不错", "满意", "差", "失望", "垃圾"]
vecs = PCA(n_components=2, random_state=0).fit_transform([model.wv[w] for w in words])
plt.figure(figsize=(7, 5))
plt.scatter(vecs[:, 0], vecs[:, 1])
for w, (x, y) in zip(words, vecs):
    plt.annotate(w, (x, y), fontsize=12)
plt.title("词向量降维到二维后的分布")
plt.savefig("w2v_pca.png", dpi=150, bbox_inches="tight")
print("图片已保存为 w2v_pca.png")
