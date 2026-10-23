"""实验 4-3：传统句法分析工具与大模型对比
第 1 部分只需要 spaCy；第 2 部分需要大模型 API Key（设置环境变量 DEEPSEEK_API_KEY）。"""
import os
import spacy

nlp = spacy.load("zh_core_web_sm")
sentences = ["咬死了猎人的狗",
             "骑手把外卖送到了宿舍楼下",
             "我看见拿着望远镜的女孩",
             "这家店的面条我觉得还可以"]

# ===== 第 1 部分：spaCy 的分析结果 =====
for s in sentences:
    doc = nlp(s)
    print(s)
    print("   ", " ".join(f"{t.text}<-{t.dep_}-{t.head.text}" for t in doc))

# ===== 第 2 部分：让大模型分析同一组句子 =====
if os.environ.get("DEEPSEEK_API_KEY"):
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                    base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
    prompt = """请分析下面句子的句法结构：
1. 指出主语、谓语、宾语（没有的写“无”）；
2. 如果句子有歧义，列出所有可能的理解；
3. 用不超过 80 字回答。
句子：{s}"""
    for s in sentences:
        resp = client.chat.completions.create(
            model=os.environ.get("LLM_MODEL", "deepseek-chat"),
            messages=[{"role": "user", "content": prompt.format(s=s)}],
            temperature=0)
        print(f"\n【{s}】\n{resp.choices[0].message.content}")
else:
    print("\n未设置 DEEPSEEK_API_KEY，跳过第 2 部分")
