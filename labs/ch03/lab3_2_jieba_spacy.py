"""实验 3-2：jieba 与 spaCy 分词和词性标注"""
import jieba
import jieba.posseg as pseg

# ===== 第 1 部分：jieba 的三种分词模式 =====
s = "我在人工智能技术应用专业学习自然语言处理"
print("精确模式：", "/".join(jieba.cut(s)))
print("全模式：  ", "/".join(jieba.cut(s, cut_all=True)))
print("搜索引擎：", "/".join(jieba.cut_for_search(s)))

# ===== 第 2 部分：自定义词典 =====
s2 = "大模型智能体可以调用工具，这个外卖小哥送餐真是绝绝子"
print("\n添加词典前：", "/".join(jieba.cut(s2)))
for w in ["大模型", "智能体", "外卖小哥", "绝绝子"]:
    jieba.add_word(w)                 # 也可以用 jieba.load_userdict("文件名") 批量加载
print("添加词典后：", "/".join(jieba.cut(s2)))

# ===== 第 3 部分：词性标注 =====
s3 = "这家店的牛肉面味道很好，但是送餐速度太慢了"
print("\njieba 词性：", " ".join(f"{w}/{f}" for w, f in pseg.cut(s3)))
nouns = [w for w, f in pseg.cut(s3) if f.startswith("n")]
adjs = [w for w, f in pseg.cut(s3) if f.startswith("a")]
print("名词：", nouns, " 形容词：", adjs)

import spacy
nlp = spacy.load("zh_core_web_sm")
print("spaCy 词性：", " ".join(f"{t.text}/{t.pos_}" for t in nlp(s3)))
