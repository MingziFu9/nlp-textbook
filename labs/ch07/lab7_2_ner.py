"""实验 7-2：spaCy 与 Transformers 命名实体识别"""
import spacy
from spacy import displacy

text = open("news_ner.txt", encoding="utf-8").read()

# ===== 第 1 部分：spaCy 中文实体识别 =====
nlp = spacy.load("zh_core_web_sm")
doc = nlp(text)
print("spaCy 识别出的实体：")
for ent in doc.ents:
    print(f"  {ent.text:<12}{ent.label_:<10}{spacy.explain(ent.label_)}")

html = displacy.render(doc, style="ent", jupyter=False)   # 在 Jupyter 中用 jupyter=True 直接显示
open("ner_zh.html", "w", encoding="utf-8").write(html)

# ===== 第 2 部分：spaCy 英文实体识别 =====
nlp_en = spacy.load("en_core_web_sm")
en = ("On October 15, 2026, Xinghai Technology announced in Hangzhou that it will invest "
      "500 million yuan with Zhejiang University. CEO Li Zhiyuan attended the event.")
print("\n英文实体：", [(e.text, e.label_) for e in nlp_en(en).ents])

# ===== 第 3 部分：Transformers 预训练中文 NER 模型 =====
# 首次运行需下载约 400MB 模型，国内请先设置 HF_ENDPOINT=https://hf-mirror.com
from transformers import pipeline
ner = pipeline("token-classification",
               model="uer/roberta-base-finetuned-cluener2020-chinese",
               aggregation_strategy="simple")          # 把同一实体的多个字合并
print("\nTransformers 识别出的实体：")
for line in text.splitlines():
    for e in ner(line):
        print(f"  {e['word'].replace(' ', ''):<12}{e['entity_group']:<14}{e['score']:.2f}")
