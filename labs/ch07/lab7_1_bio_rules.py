"""实验 7-1：BIO 标注实践与规则抽取"""
import re

# ===== 第 1 部分：读懂 BIO 标注 =====
chars = list("李志远在杭州创办了星海科技")
tags = ["B-PER", "I-PER", "I-PER", "O", "B-LOC", "I-LOC", "O", "O", "O",
        "B-ORG", "I-ORG", "I-ORG", "I-ORG"]
for c, t in zip(chars, tags):
    print(f"{c}\t{t}")


def bio_to_entities(chars, tags):
    """把逐字的 BIO 标签还原成 (实体, 类型) 列表"""
    entities, current, etype = [], "", None
    for c, t in zip(chars, tags):
        if t.startswith("B-"):                 # 新实体开始
            if current:
                entities.append((current, etype))
            current, etype = c, t[2:]
        elif t.startswith("I-") and current:   # 实体继续
            current += c
        else:                                  # O：实体结束
            if current:
                entities.append((current, etype))
            current, etype = "", None
    if current:
        entities.append((current, etype))
    return entities

print("还原出的实体：", bio_to_entities(chars, tags))

# ===== 第 2 部分：用规则抽取日期、金额和机构 =====
text = open("news_ner.txt", encoding="utf-8").read()
rules = {
    "日期": r"\d{4}年\d{1,2}月\d{1,2}日",
    "金额": r"\d+(?:\.\d+)?[万亿]?元",
    "机构": r"[一-龥]{2,8}(?:有限公司|大学|学院|银行|实验室)",
}
for label, pattern in rules.items():
    print(f"{label}：{re.findall(pattern, text)}")

# 词典法：用一份已知的机构名单进行匹配
ORG_DICT = ["星海科技", "浙江大学", "中国银行", "顺丰速运"]
found = sorted({org for org in ORG_DICT if org in text})
print("词典匹配到的机构：", found)
