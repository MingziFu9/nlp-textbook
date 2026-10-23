"""实验 10-2：TextRank 抽取式摘要 vs. 大模型生成式摘要，并用 ROUGE 评价"""
import os
import math
import re
import jieba
import jieba.analyse
import networkx as nx

jieba.setLogLevel("WARN")
text = open("article.txt", encoding="utf-8").read().strip()
reference = open("reference_summary.txt", encoding="utf-8").read().strip()
stopwords = set(open("cn_stopwords.txt", encoding="utf-8").read().split())

# ===== 第 1 部分：TextRank 抽取关键词 =====
print("关键词：", jieba.analyse.textrank(text, topK=8, allowPOS=("n", "vn", "v")))

# ===== 第 2 部分：TextRank 抽取关键句 =====
sentences = [s for s in re.split(r"(?<=[。！？])", text) if s.strip()]
words = [set(w for w in jieba.lcut(s) if w not in stopwords and len(w) > 1) for s in sentences]


def similarity(a, b):
    """两句话的相似度：共同词的数量，除以两句长度的对数之和（TextRank 原论文的公式）"""
    if len(a) < 2 or len(b) < 2:
        return 0.0
    return len(a & b) / (math.log(len(a)) + math.log(len(b)))


G = nx.Graph()
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        w = similarity(words[i], words[j])
        if w > 0:
            G.add_edge(i, j, weight=w)          # 句子是节点，相似度是边的权重
scores = nx.pagerank(G, weight="weight")        # 和网页排名一样：被越多重要句子“推荐”的句子越重要

print(f"\n共 {len(sentences)} 句，各句得分：")
for i, s in enumerate(sentences):
    print(f"  [{i:2d}] {scores.get(i, 0):.3f}  {s[:24]}…")
top = sorted(sorted(scores, key=scores.get, reverse=True)[:2])   # 取得分最高的 2 句，按原文顺序排列
textrank_summary = "".join(sentences[i] for i in top)
print("\nTextRank 摘要：", textrank_summary)


# ===== 第 3 部分：用 ROUGE 评价摘要 =====
def rouge_n(cand, ref, n):
    """按字计算 ROUGE-N 的召回率：参考摘要中的 n 元组，有多少出现在候选摘要中"""
    clean = lambda s: re.sub(r"[^一-鿿\w]", "", s)
    cand, ref = clean(cand), clean(ref)
    c = [cand[i:i + n] for i in range(len(cand) - n + 1)]
    r = [ref[i:i + n] for i in range(len(ref) - n + 1)]
    hit = sum(min(c.count(g), r.count(g)) for g in set(r))
    return hit / len(r)


def report(name, summary):
    print(f"{name}（{len(summary)} 字）ROUGE-1 = {rouge_n(summary, reference, 1):.3f}  "
          f"ROUGE-2 = {rouge_n(summary, reference, 2):.3f}")


print("\n参考摘要：", reference)
report("TextRank 摘要", textrank_summary)
report("首句摘要（基线）", sentences[0])

# ===== 第 4 部分：大模型生成式摘要（需要 API Key，见附录 D） =====
if os.environ.get("DEEPSEEK_API_KEY"):
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                    base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
    resp = client.chat.completions.create(
        model=os.environ.get("LLM_MODEL", "deepseek-chat"), temperature=0,
        messages=[{"role": "user", "content": f"用一句话（不超过 70 字）概括下面文章的主要内容：\n{text}"}])
    llm_summary = resp.choices[0].message.content.strip()
    print("\n大模型摘要：", llm_summary)
    report("大模型摘要", llm_summary)
else:
    print("\n未设置 DEEPSEEK_API_KEY，跳过第 4 部分")
