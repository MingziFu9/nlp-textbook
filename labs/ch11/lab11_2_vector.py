"""实验 11-2 第 6 步：用向量检索（文本嵌入）代替关键词检索，并做混合检索
需要：pip install sentence-transformers；首次运行下载 BAAI/bge-small-zh-v1.5（约 100MB），
国内请先设置 HF_ENDPOINT=https://hf-mirror.com
"""
import numpy as np
from sentence_transformers import SentenceTransformer
from lab11_2_rag import chunks, tests, bm25

model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
chunk_vecs = model.encode([c["title"] + c["text"] for c in chunks], normalize_embeddings=True)


def vector_scores(query):
    # BGE 模型建议在查询前加上这句指令，检索效果更好
    q = model.encode("为这个句子生成表示以用于检索相关文章：" + query, normalize_embeddings=True)
    return chunk_vecs @ q                       # 向量已归一化，点积就是余弦相似度


def hybrid_scores(query, alpha=0.5):
    """混合检索：把两种得分各自缩放到 0~1 后加权相加"""
    def norm(x):
        x = np.asarray(x, dtype=float)
        return (x - x.min()) / (x.max() - x.min() + 1e-9)
    return alpha * norm(vector_scores(query)) + (1 - alpha) * norm(bm25(query))


for name, fn in [("向量检索", vector_scores), ("混合检索", hybrid_scores)]:
    hit1 = 0
    print(f"\n===== {name} =====")
    for q, answer in tests:
        top = chunks[int(np.argmax(fn(q)))]["title"]
        hit1 += top == answer
        print(f"{'✔' if top == answer else '✘'} {q:<16} -> {top}")
    print(f"第 1 名命中率 {hit1}/{len(tests)}")
