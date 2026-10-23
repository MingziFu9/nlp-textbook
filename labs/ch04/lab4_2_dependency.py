"""实验 4-2：依存句法分析与“主谓宾”提取"""
import spacy
from spacy import displacy

nlp_zh = spacy.load("zh_core_web_sm")
nlp_en = spacy.load("en_core_web_sm")

# ===== 第 1 部分：查看依存关系 =====
doc = nlp_zh("小明在图书馆认真阅读一本自然语言处理教材")
print(f"{'词':<8}{'词性':<7}{'依存关系':<10}{'中心词'}")
for t in doc:
    print(f"{t.text:<8}{t.pos_:<7}{t.dep_:<10}{t.head.text}")

# ===== 第 2 部分：可视化（在 Jupyter 中会直接显示图形）=====
svg = displacy.render(doc, style="dep", jupyter=False,
                      options={"compact": True, "distance": 110})
open("dep_zh.svg", "w", encoding="utf-8").write(svg)
print("依存图已保存为 dep_zh.svg，可用浏览器打开")


# ===== 第 3 部分：提取“主谓宾”三元组 =====
def extract_svo(doc):
    """找出每个动词的主语（nsubj）和宾语（dobj / obj），组成三元组"""
    triples = []
    for token in doc:
        if token.pos_ == "VERB":
            subj = [w for w in token.children if w.dep_ in ("nsubj", "nsubjpass")]
            obj = [w for w in token.children if w.dep_ in ("dobj", "obj")]
            if subj and obj:
                # 宾语带上它的修饰语，形成完整的短语
                obj_phrase = "".join(w.text_with_ws for w in obj[0].subtree).strip()
                triples.append((subj[0].text, token.text, obj_phrase))
    return triples

zh_sentences = ["小明在图书馆认真阅读一本自然语言处理教材",
                "华为发布了新款手机",
                "骑手把外卖送到了宿舍楼下"]
for s in zh_sentences:
    print(s, "→", extract_svo(nlp_zh(s)))

en_sentences = ["The students built a chatbot for the library.",
                "Alibaba released a new open-source model last week."]
for s in en_sentences:
    print(s, "→", extract_svo(nlp_en(s)))

# ===== 第 4 部分：添加自定义词典后再分析 =====
nlp_zh.tokenizer.pkuseg_update_user_dict(["自然语言处理"])
doc = nlp_zh(zh_sentences[0])
print("\n添加词典后：", " ".join(f"{t.text}/{t.dep_}" for t in doc))
print(zh_sentences[0], "→", extract_svo(doc))
