"""实验 12-1：个人信息识别与脱敏工具"""
import re
import jieba.posseg as pseg
import spacy

__import__("jieba").setLogLevel("WARN")
text = open("records.txt", encoding="utf-8").read()


# ===== 第 1 部分：用正则表达式 + 校验规则识别结构化的个人信息 =====
def check_id(s):
    """身份证号第 18 位是校验码，按国家标准 GB 11643 计算"""
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    total = sum(int(a) * w for a, w in zip(s[:17], weights))
    return "10X98765432"[total % 11] == s[17].upper()


def check_luhn(s):
    """银行卡号的最后一位是按 Luhn 算法计算的校验码"""
    total = 0
    for i, ch in enumerate(reversed(s)):
        d = int(ch)
        if i % 2 == 1:
            d = d * 2 - 9 if d * 2 > 9 else d * 2
        total += d
    return total % 10 == 0


PATTERNS = [   # (类型, 正则表达式, 额外校验函数)
    ("身份证号", r"(?<!\d)[1-9]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx](?!\d)", check_id),
    ("银行卡号", r"(?<!\d)62\d{14,17}(?!\d)", check_luhn),
    ("手机号", r"(?<!\d)1[3-9]\d[- ]?\d{4}[- ]?\d{4}(?!\d)", None),
    ("固定电话", r"(?<!\d)0\d{2,3}-\d{7,8}(?!\d)", None),
    ("电子邮箱", r"[\w.+-]+@[\w-]+\.[\w.]+", None),
]

found = []
for label, pattern, check in PATTERNS:
    for m in re.finditer(pattern, text):
        ok = check(m.group()) if check else True
        status = ("✔ 校验通过" if ok else "✘ 校验失败，不是" + label) if check else "✔ 格式匹配"
        print(f"{label:<6} {m.group():<22} {status}")
        if ok:
            found.append((m.start(), m.end(), label))

# ===== 第 2 部分：识别人名和地址——比较 spaCy 与 jieba =====
nlp = spacy.load("zh_core_web_sm")
spacy_names = sorted({e.text for e in nlp(text).ents if e.label_ == "PERSON"})
jieba_names = sorted({w for w, flag in pseg.lcut(text) if flag == "nr" and len(w) >= 2})   # 去掉单字
print("\nspaCy 识别的人名：", spacy_names)
print("jieba 识别的人名：", jieba_names)

for name in set(spacy_names) | set(jieba_names):
    for m in re.finditer(re.escape(name), text):
        found.append((m.start(), m.end(), "姓名"))
# 地址：用规则匹配“（××省）××市××区……号/室”的结构
for m in re.finditer(r"(?:[\u4e00-\u9fa5]{2}省)?[\u4e00-\u9fa5]{2}市[\u4e00-\u9fa5]{2}(?:区|县)[\u4e00-\u9fa5\d]+(?:号|室)", text):
    found.append((m.start(), m.end(), "地址"))


# ===== 第 3 部分：两种脱敏方式——替换为标签、部分遮盖 =====
def mask(s, label):
    if label in ("手机号", "身份证号", "银行卡号"):
        digits = re.sub(r"\D", "", s)
        return digits[:3] + "*" * (len(digits) - 7) + digits[-4:]    # 保留前 3 位和后 4 位
    if label == "姓名":
        return s[0] + "*" * (len(s) - 1)                             # 保留姓氏
    return f"[{label}]"


def apply(text, spans, mode):
    spans = sorted(set(spans), key=lambda x: (x[0], -x[1]))
    out, last = [], 0
    for start, end, label in spans:
        if start < last:            # 跳过与前一个重叠的片段
            continue
        out.append(text[last:start])
        out.append(f"[{label}]" if mode == "tag" else mask(text[start:end], label))
        last = end
    return "".join(out) + text[last:]


print("\n===== 替换为类型标签（适合交给大模型或做数据分析） =====")
print(apply(text, found, "tag"))
print("\n===== 部分遮盖（适合给客服人员查看） =====")
print(apply(text, found, "mask"))
