"""实验 4-1：编写上下文无关文法并画出句法树"""
import nltk

# ===== 第 1 部分：一个简单的中文文法 =====
# 规则左边是“成分”，右边是它可以由哪些成分组成；带引号的是具体的词
zh_grammar = nltk.CFG.fromstring("""
S  -> NP VP
NP -> N | Adj N | N N
VP -> V NP | Adv VP
N  -> '小明' | '同学' | '自然语言' | '处理' | '课程'
Adj -> '新'
V  -> '喜欢' | '学习'
Adv -> '非常'
""")
parser = nltk.ChartParser(zh_grammar)
sentence = ["小明", "非常", "喜欢", "自然语言", "处理"]   # 已经分好词的句子
for tree in parser.parse(sentence):
    print(tree)              # 括号形式
    tree.pretty_print()      # 树形图

# ===== 第 2 部分：结构歧义——一句话，两棵树 =====
en_grammar = nltk.CFG.fromstring("""
S  -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N  -> 'elephant' | 'pajamas'
V  -> 'shot'
P  -> 'in'
""")
parser = nltk.ChartParser(en_grammar)
sent = "I shot an elephant in my pajamas".split()
trees = list(parser.parse(sent))
print(f"共找到 {len(trees)} 种分析结果：")
for i, tree in enumerate(trees, 1):
    print(f"\n第 {i} 种：")
    tree.pretty_print()
