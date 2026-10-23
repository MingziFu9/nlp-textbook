"""实验 5-3：用嵌入模型做语义搜索（与关键词搜索对比）"""
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jieba.setLogLevel("WARN")
faqs = ["商品出现质量问题如何申请退货？",
        "下单后多久发货？",
        "可以开具增值税发票吗？",
        "如何修改收货地址？",
        "会员积分可以兑换什么？",
        "快递一直没有更新物流信息怎么办？",
        "支持货到付款吗？",
        "优惠券为什么无法使用？",
        "怎样联系人工客服？",
        "退款多久能到账？"]
queries = ["东西坏了能退吗", "钱什么时候退回来", "我想找真人说话", "包裹好几天没动静"]

# ===== 第 1 部分：关键词搜索（TF-IDF）=====
tfidf = TfidfVectorizer(tokenizer=jieba.lcut, token_pattern=None)
faq_vec = tfidf.fit_transform(faqs)
print("【关键词搜索】")
for q in queries:
    scores = cosine_similarity(tfidf.transform([q]), faq_vec)[0]
    best = scores.argmax()
    print(f"  {q} → {faqs[best]}（相似度 {scores[best]:.2f}）")

# ===== 第 2 部分：语义搜索（文本嵌入模型）=====
# 首次运行会下载约 100MB 的模型；国内请先设置 HF_ENDPOINT=https://hf-mirror.com
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
faq_emb = model.encode(faqs, normalize_embeddings=True)       # 每个问题变成一个向量
print("\n每个句子被表示为", faq_emb.shape[1], "维的向量")
print("【语义搜索】")
for q in queries:
    q_emb = model.encode([q], normalize_embeddings=True)
    scores = (q_emb @ faq_emb.T)[0]                           # 归一化后，点积就是余弦相似度
    best = scores.argmax()
    print(f"  {q} → {faqs[best]}（相似度 {scores[best]:.2f}）")
