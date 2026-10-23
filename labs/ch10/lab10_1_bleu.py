"""实验 10-1 第 1 部分：读懂 BLEU——机器翻译的自动评价"""
from collections import Counter
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

source = "人工智能正在改变我们学习和工作的方式。"
references = [   # 两位译者给出的参考译文
    "artificial intelligence is changing the way we learn and work .".split(),
    "ai is transforming how we study and work .".split(),
]
candidates = {   # 编者构造的 4 个待评价译文
    "A 意思对、措辞接近": "artificial intelligence is changing how we learn and work .",
    "B 意思对、换了说法": "ai has been reshaping our ways of studying and working .",
    "C 词都对、顺序乱": "work and learn we way the changing is intelligence artificial .",
    "D 太短": "artificial intelligence is changing .",
}


def ngram_precision(cand, refs, n):
    """修正的 n 元精确率：候选译文中有多少个 n 元组出现在参考译文里"""
    cand_ngrams = Counter(tuple(cand[i:i + n]) for i in range(len(cand) - n + 1))
    max_ref = Counter()
    for ref in refs:
        ref_ngrams = Counter(tuple(ref[i:i + n]) for i in range(len(ref) - n + 1))
        for g in ref_ngrams:
            max_ref[g] = max(max_ref[g], ref_ngrams[g])
    hit = sum(min(c, max_ref[g]) for g, c in cand_ngrams.items())   # 每个 n 元组最多算参考中出现的次数
    return hit, sum(cand_ngrams.values())


smooth = SmoothingFunction().method1
print("原文：", source)
for name, text in candidates.items():
    cand = text.split()
    precisions = []
    for n in range(1, 5):
        hit, total = ngram_precision(cand, references, n)
        precisions.append(f"{hit}/{total}")
    bleu = sentence_bleu(references, cand, smoothing_function=smooth)
    print(f"{name:<12} 1~4 元精确率 {' '.join(precisions):<22} BLEU = {bleu:.3f}")
