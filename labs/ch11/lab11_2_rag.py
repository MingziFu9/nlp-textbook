"""实验 11-2：从零搭建一个“学生手册问答”RAG 系统"""
import math
import os
import re
from collections import Counter
import jieba

jieba.setLogLevel("WARN")
stopwords = set(open("cn_stopwords.txt", encoding="utf-8").read().split())

# ===== 第 1 步：切块——按章节把手册切成知识片段 =====
doc = open("student_handbook.md", encoding="utf-8").read()
chunks = []
for part in re.split(r"\n## ", doc)[1:]:               # 跳过标题和说明
    title, body = part.split("\n", 1)
    chunks.append({"title": title.strip(), "text": body.strip()})


# ===== 第 2 步：建立 BM25 检索索引 =====
def tokenize(text):
    return [w for w in jieba.lcut(text) if w.strip() and w not in stopwords]


docs = [tokenize(c["title"] + c["text"]) for c in chunks]
avgdl = sum(len(d) for d in docs) / len(docs)
df = Counter(w for d in docs for w in set(d))
N = len(docs)


def bm25(query, k1=1.5, b=0.75):
    """BM25：TF-IDF 的改进版，对词频做了“饱和”处理，并考虑文档长度"""
    q = tokenize(query)
    scores = []
    for d in docs:
        tf = Counter(d)
        s = 0.0
        for w in q:
            if w not in tf:
                continue
            idf = math.log((N - df[w] + 0.5) / (df[w] + 0.5) + 1)
            s += idf * tf[w] * (k1 + 1) / (tf[w] + k1 * (1 - b + b * len(d) / avgdl))
        scores.append(s)
    return scores


def retrieve(query, top_k=3):
    scores = bm25(query)
    order = sorted(range(N), key=lambda i: -scores[i])[:top_k]
    return [(i, scores[i]) for i in order]


# ===== 第 3 步：检索效果评估 =====
tests = [   # (问题, 正确答案所在的章节)
    ("一次最多能借几本书？", "七、图书馆"),
    ("奖学金需要什么条件？", "六、奖学金与资助"),
    ("选修课最多可以选几门？", "三、选课"),
    ("宿舍几点关门？", "八、宿舍管理"),
    ("挂科了怎么办？", "四、考试与成绩"),
    ("寝室里能用电饭锅吗？", "八、宿舍管理"),
    ("上网的账号是什么？", "九、校园网络"),
    ("被处分了不服可以找谁？", "十二、违纪处分"),
]


# ===== 第 4 步：把检索结果拼进提示词 =====
def build_prompt(question, top_k=3):
    context = "\n\n".join(f"【{chunks[i]['title']}】{chunks[i]['text']}" for i, _ in retrieve(question, top_k))
    return f"""你是星海职业学院的学生事务助手。请只根据下面的【参考资料】回答问题。
如果参考资料中没有相关信息，就回答“手册中没有找到相关规定，请咨询辅导员”，不要编造。
回答要简洁，并在最后注明依据的章节。

【参考资料】
{context}

【问题】{question}"""


if __name__ == "__main__":
    print(f"共切分出 {len(chunks)} 个片段，平均 {sum(len(c['text']) for c in chunks) // len(chunks)} 字")
    hit1 = hit3 = 0
    print("\n问题                      检索到的前 3 个片段（得分）")
    for q, answer in tests:
        result = retrieve(q)
        titles = [chunks[i]["title"] for i, _ in result]
        hit1 += titles[0] == answer
        hit3 += answer in titles
        mark = "✔" if titles[0] == answer else ("△" if answer in titles else "✘")
        print(f"{mark} {q:<16}" + "  ".join(f"{t}({s:.1f})" for t, (_, s) in zip(titles, result)))
    print(f"\n第 1 名命中率 {hit1}/{len(tests)}，前 3 名命中率 {hit3}/{len(tests)}")

    question = "补考没过会怎样？"
    prompt = build_prompt(question, top_k=2)
    print("\n===== 发送给大模型的提示词 =====")
    print(prompt)

    # ===== 第 5 步：调用大模型生成回答（需要 API Key，见附录 D） =====
    if os.environ.get("DEEPSEEK_API_KEY"):
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                        base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
        for q in [question, "寝室里能用电饭锅吗？", "学院有没有游泳馆？"]:
            resp = client.chat.completions.create(
                model=os.environ.get("LLM_MODEL", "deepseek-chat"), temperature=0,
                messages=[{"role": "user", "content": build_prompt(q)}])
            print(f"\n问：{q}\n答：{resp.choices[0].message.content}")
    else:
        print("\n未设置 DEEPSEEK_API_KEY，跳过第 5 步")
