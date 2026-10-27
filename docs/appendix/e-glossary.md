---
title: 附录 E 术语表
description: 本书主要术语的中英文名称与简明定义，按章节顺序排列
---

# 附录 E 术语表

本表按章节顺序列出本书的主要术语，每个术语给出英文名称和简明定义，部分章节还给出了例子。正文中带虚线下划线的术语，把鼠标停在上面就能看到定义，点击可以跳到本表。

## 第 1 章 自然语言处理概述

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-自然语言"></span>自然语言 | Natural Language | 人类在日常交流中自然形成和使用的语言，如汉语、英语，区别于编程语言等人工语言 | 微信聊天、新闻稿、客户评论都是自然语言；Python 代码不是 |
| <span id="g-自然语言处理"></span>自然语言处理 | Natural Language Processing, NLP | 研究让计算机理解、处理和生成人类语言的理论与技术 | 机器翻译、智能客服、垃圾短信识别 |
| <span id="g-自然语言理解"></span>自然语言理解 | Natural Language Understanding, NLU | 让计算机读懂语言含义的技术，如分类、抽取、问答 | 判断“快递太慢了”是一条投诉 |
| <span id="g-自然语言生成"></span>自然语言生成 | Natural Language Generation, NLG | 让计算机产生自然语言文本的技术，如翻译、摘要、写作 | 根据会议录音自动写出会议纪要 |
| <span id="g-歧义"></span>歧义 | Ambiguity | 同一个语言表达可以有多种理解的现象，是 NLP 的核心难点 | “咬死了猎人的狗”有两种理解 |
| <span id="g-语料库"></span>语料库 | Corpus | 为语言研究和模型训练而收集、整理的大规模文本集合 | 实验用的 1 万条外卖评论 `waimai_10k.csv` |
| <span id="g-大语言模型"></span>大语言模型 | Large Language Model, LLM | 参数规模巨大、在海量文本上预训练、具有通用语言理解与生成能力的模型 | DeepSeek、通义千问、文心一言 |

## 第 2 章 文本预处理

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-文本预处理"></span>文本预处理 | Text Preprocessing | 在分析或建模前对原始文本进行清洗、规范化、切分等处理的过程 | 去掉评论里的 HTML 标签和表情，再分词 |
| <span id="g-字符编码"></span>字符编码 | Character Encoding | 把字符映射为计算机中二进制数据的规则，如 UTF-8、GBK | 用 UTF-8 读 GBK 文件会出现乱码 |
| <span id="g-正则表达式"></span>正则表达式 | Regular Expression | 用特定语法描述字符串模式，用于查找、替换和校验文本 | `1[3-9]\d{9}` 描述手机号 |
| <span id="g-分句"></span>分句 | Sentence Segmentation | 把一段文本切分为句子 | “好吃！下次还来。”切成两句 |
| <span id="g-词元化-分词"></span>词元化 / 分词 | Tokenization | 把文本切分为词、子词或字等基本单位（词元） | They're → They / 're |
| <span id="g-停用词"></span>停用词 | Stop Words | 出现频率高但对任务贡献小的词，如“的”“了”“the” | 做 TF-IDF 时去掉“的”“了”；情感分析要保留“不” |
| <span id="g-词干提取"></span>词干提取 | Stemming | 用规则去掉英文单词的词缀，得到词干 | studying → studi，结果不一定是真单词 |
| <span id="g-词形还原"></span>词形还原 | Lemmatization | 借助词典把英文单词还原为原形 | was → be，better → good |
| <span id="g-繁简转换"></span>繁简转换 | Traditional-Simplified Conversion | 在繁体中文与简体中文之间转换 | 用 OpenCC 把“這個東西”转成“这个东西” |
| <span id="g-数据清洗"></span>数据清洗 | Data Cleaning | 去除噪声、重复、无效数据，提高数据质量的过程 | 删除空评论、合并重复标点、去重 |
| <span id="g-Unicode-规范化"></span>Unicode 规范化 | Unicode Normalization | 把写法不同、意思相同的字符统一为同一种编码形式 | NFKC 把“ＡＢＣ１２３”变成“ABC123” |
| <span id="g-近似重复"></span>近似重复 | Near Duplicate | 内容几乎相同、只差个别字词或标点的文本 | “送餐太慢了，等了…”和“送餐太慢了,等了…” |
| <span id="g-合成数据"></span>合成数据 | Synthetic Data | 由大模型等程序按要求生成、而非真实采集的数据 | 让大模型写 200 种“催单”的说法 |

## 第 3 章 词法分析

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-词法分析"></span>词法分析 | Lexical Analysis | 以词为单位的分析，包括分词、词性标注等 | 把“我爱北京”切成“我 / 爱 / 北京”并标出词性 |
| <span id="g-中文分词"></span>中文分词 | Chinese Word Segmentation | 把没有空格分隔的中文句子切分为词序列 | “研究生命的起源”→ 研究 / 生命 / 的 / 起源 |
| <span id="g-最大匹配法"></span>最大匹配法 | Maximum Matching | 基于词典、每次取最长匹配词的分词方法，分正向、逆向和双向 | 正向把“研究生命”切成“研究生 / 命” |
| <span id="g-切分歧义"></span>切分歧义 | Segmentation Ambiguity | 同一字串可以有多种切分方式的现象，分交集型和组合型 | “乒乓球拍卖完了”有两种切法 |
| <span id="g-未登录词"></span>未登录词 | Out-of-Vocabulary Word, OOV | 词典或词表中没有收录的词，如新词、人名 | “卷饼”“催单”不在 jieba 通用词典中 |
| <span id="g-词性标注"></span>词性标注 | Part-of-Speech Tagging | 为句子中的每个词标注名词、动词等词性 | 味道/n 不错/a |
| <span id="g-N-元语法"></span>N 元语法 | N-gram | 由连续 N 个词（或字）组成的片段；N 元语言模型据此估计句子概率 | “今天天气很”后面最常跟“好” |
| <span id="g-隐马尔可夫模型"></span>隐马尔可夫模型 | Hidden Markov Model, HMM | 用隐藏状态序列生成观测序列的概率模型，曾广泛用于分词和词性标注 | 给“我爱北京”逐字标出 S S B E |
| <span id="g-子词"></span>子词 | Subword | 介于字符和词之间的切分单位，可以组合出罕见词 | unbelievable → un / belie / vable |
| <span id="g-字节对编码"></span>字节对编码 | Byte Pair Encoding, BPE | 反复合并出现最频繁的相邻符号对来构建子词词表的算法 | 先把“e s”合并为“es”，再合并为“est” |
| <span id="g-词元"></span>词元 | Token | 模型处理文本的最小单位；大模型按 Token 计费和限制长度 | “自然语言处理”被切成 自然 / 语言 / 处理 三个 Token |
| <span id="g-分词器"></span>分词器 | Tokenizer | 把文本转换为 Token 编号序列（以及反向转换）的组件 | 实验 3-3 中通义千问的分词器 |
| <span id="g-词表"></span>词表 | Vocabulary | 模型或分词器所认识的全部词元及其编号 | 大模型词表通常有十几万个 Token |
| <span id="g-新词发现"></span>新词发现 | New Word Discovery | 用凝固度、自由度等统计指标从大量文本中自动找出候选新词的方法 | 从外卖评论中找出“卷饼”“拌饭” |
| <span id="g-兼类词"></span>兼类词 | Multi-category Word | 在不同句子中可以属于不同词性的词 | “锁门”的“锁”是动词，“这把锁”的“锁”是名词 |

## 第 4 章 句法分析

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-句法分析"></span>句法分析 | Syntactic Parsing | 分析句子的语法结构，找出词与词怎样组成句子 | 分析出“物业拆除了车棚”中“物业”是主语、“车棚”是宾语 |
| <span id="g-成分句法"></span>成分句法 | Constituency Parsing | 把句子分析为层层嵌套的短语结构（句法树） | “我 / 吃 / 苹果”→ [NP 我] [VP 吃 [NP 苹果]] |
| <span id="g-上下文无关文法"></span>上下文无关文法 | Context-Free Grammar, CFG | 用“左边一个符号 → 右边符号串”形式的规则描述句子结构的文法 | S -> NP VP：句子 = 名词短语 + 动词短语 |
| <span id="g-句法树"></span>句法树 | Parse Tree | 表示句子成分结构的树形图 | 根节点 S 下分出 NP 和 VP 两棵子树 |
| <span id="g-树库"></span>树库 | Treebank | 人工为大量句子标注好句法结构的语料库，句法分析器从中学习 | 宾州中文树库（CTB） |
| <span id="g-结构歧义"></span>结构歧义 | Structural Ambiguity | 同一串词可以组成不止一种合法的句法结构，从而有不同的意思 | “咬死了猎人的狗”：狗被咬死，还是狗咬死了猎人 |
| <span id="g-概率上下文无关文法"></span>概率上下文无关文法 | Probabilistic CFG, PCFG | 给每条文法规则加上概率，用规则概率之积为句法树打分，选出最可能的树 | 规则“VP → V NP”的概率为 0.6 |
| <span id="g-依存句法"></span>依存句法 | Dependency Parsing | 分析句子中词与词之间支配与被支配关系的方法 | “吃”支配“我”和“苹果” |
| <span id="g-核心词-中心词"></span>核心词 / 中心词 | Head | 依存关系中起支配作用的词 | “红色的苹果”中，“苹果”是“红色”的中心词 |
| <span id="g-依存关系"></span>依存关系 | Dependency Relation | 两个词之间的语法关系，如主谓、动宾、定中 | 物业 ← nsubj ← 拆除 |
| <span id="g-语义分析"></span>语义分析 | Semantic Analysis | 研究如何让计算机理解词语、句子乃至篇章的含义 | 知道“车棚被物业拆除了”和“物业拆除了车棚”意思相同 |
| <span id="g-词义消歧"></span>词义消歧 | Word Sense Disambiguation | 根据上下文确定多义词在句子中的具体含义 | “打车”中的“打”是乘坐的意思 |
| <span id="g-语义角色标注"></span>语义角色标注 | Semantic Role Labeling | 识别句子中谓词的施事、受事、时间、地点等语义角色 | “拆除”的施事是物业，受事是车棚 |
| <span id="g-语义依存分析"></span>语义依存分析 | Semantic Dependency Parsing | 用“图”表示词与词的语义关系，允许一个词有多个中心词 | “我请他吃饭”中，“他”既是“请”的受事又是“吃”的施事 |
| <span id="g-指代消解"></span>指代消解 | Coreference Resolution | 找出代词或简称指的是前文中的哪个实体 | “小猫追老鼠，它跑累了”中“它”指小猫 |
| <span id="g-文本蕴含"></span>文本蕴含 | Textual Entailment / NLI | 判断由前提句能否推出假设句：蕴含、矛盾或中立 | “小王在杭州跑马拉松”蕴含“小王去过杭州” |

## 第 5 章 文本表示

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-文本表示"></span>文本表示 | Text Representation | 把文本转换为计算机可以计算的数值向量 |
| <span id="g-独热编码"></span>独热编码 | One-hot Encoding | 用只有一个位置为 1、其余为 0 的向量表示词 |
| <span id="g-词袋模型"></span>词袋模型 | Bag of Words | 只统计词出现次数、忽略词序的文本表示方法 |
| <span id="g-词频-逆文档频率"></span>词频-逆文档频率 | TF-IDF | 用词在文档中的频率与其在整个语料中的稀有程度的乘积衡量词的重要性 |
| <span id="g-余弦相似度"></span>余弦相似度 | Cosine Similarity | 用两个向量夹角的余弦值衡量其相似程度，取值 -1 到 1 |
| <span id="g-分布式假设"></span>分布式假设 | Distributional Hypothesis | 上下文相似的词，意义也相似 |
| <span id="g-词向量-词嵌入"></span>词向量 / 词嵌入 | Word Embedding | 用低维稠密向量表示词，语义相近的词向量相近 |
| <span id="g-Word2Vec"></span>Word2Vec | Word2Vec | 通过预测上下文（Skip-gram）或中心词（CBOW）学习词向量的方法 |
| <span id="g-上下文相关词向量"></span>上下文相关词向量 | Contextual Embedding | 同一个词在不同语境中得到不同向量的表示方法，如 BERT 的输出 |
| <span id="g-文本嵌入"></span>文本嵌入 | Text Embedding | 把整句或整段文本表示为一个向量，用于语义检索和匹配 |
| <span id="g-语义搜索"></span>语义搜索 | Semantic Search | 根据含义而非字面匹配进行的检索 |

## 第 6 章 文本分类与情感分析

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-文本分类"></span>文本分类 | Text Classification | 把文本自动归入预先定义好的一个或多个类别 | 把外卖评论分成好评、差评 |
| <span id="g-多标签分类"></span>多标签分类 | Multi-label Classification | 一条文本可以同时属于多个类别的分类任务 | 一条评论同时属于“口味”和“配送” |
| <span id="g-监督学习"></span>监督学习 | Supervised Learning | 从带有正确答案（标签）的样本中学习规律的机器学习方式 | 用 1 万条标好“好评 / 差评”的评论训练模型 |
| <span id="g-训练集"></span>训练集 | Training Set | 用来训练模型的数据，相当于“课本和练习题” | 全部评论中随机抽取的 80% |
| <span id="g-测试集"></span>测试集 | Test Set | 训练时不让模型看见、训练完成后用来评估模型的数据，相当于“期末考试卷” | 剩下的 20% 评论 |
| <span id="g-验证集"></span>验证集 | Validation Set | 训练过程中用来调整参数、选择阈值的数据，相当于“模拟考试” | 从训练数据中再分出 10% 用来选阈值 |
| <span id="g-欠拟合"></span>欠拟合 | Underfitting | 模型太简单、没学到规律，训练集和测试集成绩都差的现象 | 只用“好吃”一个词判断情感 |
| <span id="g-朴素贝叶斯"></span>朴素贝叶斯 | Naive Bayes | 基于贝叶斯定理、假设各个词相互独立的分类算法 | 把“好吃”“慢”在好评、差评中的概率相乘后比较 |
| <span id="g-拉普拉斯平滑"></span>拉普拉斯平滑 | Laplace Smoothing | 统计概率时给每个词的次数加 1，避免没出现过的词使概率变成 0 | “快”在差评中出现 0 次，平滑后概率为 1/12 |
| <span id="g-逻辑回归"></span>逻辑回归 | Logistic Regression | 给每个特征一个权重、加权求和后用 Sigmoid 函数输出类别概率的分类模型 | “味道好吃，送得也快”是好评的概率约 87% |
| <span id="g-阈值"></span>阈值 | Threshold | 把概率转换成类别时使用的分界值 | 概率大于等于 0.5 判为好评 |
| <span id="g-支持向量机"></span>支持向量机 | Support Vector Machine, SVM | 在两类样本之间寻找间隔最大的分界线的分类算法 | 实验 6-2 中的 `LinearSVC` |
| <span id="g-基线"></span>基线 | Baseline | 用简单方法得到的参照成绩，用来衡量复杂方法是否真的更好 | 先用 TF-IDF + 逻辑回归做到 88% |
| <span id="g-混淆矩阵"></span>混淆矩阵 | Confusion Matrix | 按“实际类别 × 预测类别”交叉统计样本数量的表格 | TP = 1528，FN = 70，FP = 221，TN = 579 |
| <span id="g-准确率"></span>准确率 | Accuracy | 预测正确的样本占全部样本的比例 | 2398 条中判对 2107 条，准确率约 87.9% |
| <span id="g-精确率"></span>精确率 | Precision | 预测为某类的样本中，真正属于该类的比例（判得准不准） | 判为差评的 1749 条中，1528 条真是差评 |
| <span id="g-召回率"></span>召回率 | Recall | 某类的全部样本中，被正确找出来的比例（找得全不全） | 1598 条差评中找出了 1528 条 |
| <span id="g-F1-值"></span>F1 值 | F1 Score | 精确率与召回率的调和平均数，综合衡量两者 | 精确率 87.4%、召回率 95.6% 时 F1 约 91.3% |
| <span id="g-宏平均"></span>宏平均 | Macro Average | 各类别指标的简单平均，每个类别同等重要 | 好评、差评的 F1 直接相加除以 2 |
| <span id="g-交叉验证"></span>交叉验证 | Cross Validation | 把数据分成几份、轮流做测试集，取多次成绩平均值的评价方法 | 5 折交叉验证平均准确率 88.62% |
| <span id="g-类别不平衡"></span>类别不平衡 | Class Imbalance | 各类别样本数量相差很大的情况 | 外卖评论中差评约占三分之二 |
| <span id="g-错误分析"></span>错误分析 | Error Analysis | 逐条阅读模型判错的样本、归纳错误类型，以找到改进方向的方法 | 40 条错误中 14 条是褒贬混合 |
| <span id="g-情感分析"></span>情感分析 | Sentiment Analysis | 分析文本表达的情感倾向、态度和观点的技术，也叫观点挖掘 | 判断一条评论是好评还是差评 |
| <span id="g-方面级情感分析"></span>方面级情感分析 | Aspect-Based Sentiment Analysis | 针对文本中每个评价对象（方面）分别判断情感 | 口味：正面；配送：负面 |
| <span id="g-情感词典"></span>情感词典 | Sentiment Lexicon | 收录词语及其情感倾向和强度的词典 | 知网 HowNet 情感词典、大连理工情感词汇本体库 |
| <span id="g-零样本学习"></span>零样本学习 | Zero-shot Learning | 不提供任何示例，仅凭任务描述让模型完成任务 | 提示词只写“判断这条评论是好评还是差评” |
| <span id="g-意图识别"></span>意图识别 | Intent Recognition | 判断用户一句话想要做什么的文本分类任务 | “我的外卖怎么还没到”→ 查询订单进度 |

## 第 7 章 命名实体识别与信息抽取

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-信息抽取"></span>信息抽取 | Information Extraction, IE | 从非结构化文本中抽取指定类型的信息并整理成结构化数据 |
| <span id="g-命名实体识别"></span>命名实体识别 | Named Entity Recognition, NER | 识别文本中人名、地名、机构名等实体的位置和类型 |
| <span id="g-序列标注"></span>序列标注 | Sequence Labeling | 为序列中的每个元素分配一个标签的任务，如分词、词性标注、NER |
| <span id="g-BIO-标注"></span>BIO 标注 | BIO Tagging | 用 B（开始）、I（内部）、O（外部）标注实体边界的方法 |
| <span id="g-条件随机场"></span>条件随机场 | Conditional Random Field, CRF | 考虑相邻标签之间依赖关系的序列标注模型 |
| <span id="g-关系抽取"></span>关系抽取 | Relation Extraction | 判断文本中两个实体之间的语义关系 |
| <span id="g-三元组"></span>三元组 | Triple | （头实体，关系，尾实体）形式的知识表示 |
| <span id="g-事件抽取"></span>事件抽取 | Event Extraction | 识别事件类型、触发词和事件论元（时间、地点、参与者等） |
| <span id="g-知识图谱"></span>知识图谱 | Knowledge Graph | 以实体为节点、关系为边组织知识的图结构 |
| <span id="g-实体链接"></span>实体链接 | Entity Linking | 把文本中的实体指称对应到知识库中唯一实体的任务 |
| <span id="g-数据标注"></span>数据标注 | Data Annotation | 按照规范为数据添加标签，供模型训练和评估使用 |

## 第 8 章 深度学习基础

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-深度学习"></span>深度学习 | Deep Learning | 使用多层神经网络从数据中自动学习特征的机器学习方法 |
| <span id="g-表示学习"></span>表示学习 | Representation Learning | 让模型自动学习数据的有用表示，而非依赖人工特征 |
| <span id="g-神经元"></span>神经元 | Neuron | 对输入加权求和、加上偏置后经激活函数输出的计算单元 |
| <span id="g-权重-偏置"></span>权重 / 偏置 | Weight / Bias | 神经元中由训练学习得到的参数 |
| <span id="g-感知机"></span>感知机 | Perceptron | 只有一个神经元、使用阶跃激活函数的最简单神经网络 |
| <span id="g-多层感知机"></span>多层感知机 | Multi-Layer Perceptron, MLP | 含一个或多个隐藏层的全连接前馈神经网络 |
| <span id="g-激活函数"></span>激活函数 | Activation Function | 为神经网络引入非线性的函数，如 Sigmoid、Tanh、ReLU |
| <span id="g-Softmax"></span>Softmax | Softmax | 把一组得分转换为和为 1 的概率分布的函数 |
| <span id="g-损失函数"></span>损失函数 | Loss Function | 衡量模型预测与真实答案之间差距的函数 |
| <span id="g-交叉熵"></span>交叉熵 | Cross-Entropy | 分类任务常用的损失函数，等于正确类别预测概率的负对数 |
| <span id="g-梯度"></span>梯度 | Gradient | 损失函数对参数的偏导数，指示参数调整的方向和幅度 |
| <span id="g-反向传播"></span>反向传播 | Backpropagation | 利用链式法则从输出层向输入层逐层计算梯度的算法 |
| <span id="g-梯度下降"></span>梯度下降 | Gradient Descent | 沿梯度反方向更新参数以减小损失的优化方法 |
| <span id="g-学习率"></span>学习率 | Learning Rate | 每次参数更新的步长，是最重要的超参数之一 |
| <span id="g-优化器"></span>优化器 | Optimizer | 根据梯度更新参数的算法，如 SGD、Adam、AdamW |
| <span id="g-轮次-批"></span>轮次 / 批 | Epoch / Batch | 完整使用一遍训练数据称为一轮；每次更新所用的一小组样本称为一批 |
| <span id="g-超参数"></span>超参数 | Hyperparameter | 训练前由人设定、不由模型学习的参数 |
| <span id="g-过拟合"></span>过拟合 | Overfitting | 模型在训练集上表现好、在新数据上表现差的现象 |
| <span id="g-随机失活"></span>随机失活 | Dropout | 训练时随机关闭部分神经元以减轻过拟合的方法 |
| <span id="g-张量"></span>张量 | Tensor | 深度学习框架中的多维数组，可在 GPU 上计算并自动求导 |
| <span id="g-词嵌入层"></span>词嵌入层 | Embedding Layer | 把词的编号映射为可训练词向量的查找表 |
| <span id="g-循环神经网络"></span>循环神经网络 | Recurrent Neural Network, RNN | 通过隐藏状态在时间步之间传递信息、处理序列数据的网络 |
| <span id="g-隐藏状态"></span>隐藏状态 | Hidden State | 循环网络中保存已读内容信息的向量 |
| <span id="g-梯度消失-梯度爆炸"></span>梯度消失 / 梯度爆炸 | Vanishing / Exploding Gradient | 反向传播中梯度逐层变得极小或极大，导致训练困难的现象 |
| <span id="g-长短期记忆网络"></span>长短期记忆网络 | Long Short-Term Memory, LSTM | 用记忆细胞和遗忘门、输入门、输出门控制信息流动的循环网络 |
| <span id="g-门控循环单元"></span>门控循环单元 | Gated Recurrent Unit, GRU | 只有更新门和重置门的简化版 LSTM |
| <span id="g-双向循环网络"></span>双向循环网络 | Bidirectional RNN | 分别从左向右和从右向左读取序列并拼接结果的循环网络 |
| <span id="g-状态空间模型"></span>状态空间模型 | State Space Model, SSM | 以固定大小状态递推处理长序列的模型，如 Mamba |

## 第 9 章 Transformer 与预训练大模型

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-注意力机制"></span>注意力机制 | Attention Mechanism | 根据相关程度为不同位置的信息分配权重并加权求和的机制 |
| <span id="g-自注意力"></span>自注意力 | Self-Attention | 序列中每个位置关注同一序列所有位置的注意力 |
| <span id="g-查询-键-值"></span>查询 / 键 / 值 | Query / Key / Value | 自注意力中分别用于发起匹配、被匹配和提供内容的三个向量 |
| <span id="g-多头注意力"></span>多头注意力 | Multi-Head Attention | 并行使用多组 Q、K、V 投影，从多个角度计算注意力 |
| <span id="g-Transformer"></span>Transformer | Transformer | 以自注意力为核心、可并行计算的神经网络架构，2017 年提出 |
| <span id="g-编码器-解码器"></span>编码器 / 解码器 | Encoder / Decoder | 分别负责理解输入和逐步生成输出的网络部分 |
| <span id="g-位置编码"></span>位置编码 | Positional Encoding | 为输入加入位置信息，弥补自注意力不感知词序的缺陷 |
| <span id="g-旋转位置编码"></span>旋转位置编码 | Rotary Position Embedding, RoPE | 通过旋转 Q、K 向量表示相对位置的编码方法，大模型普遍采用 |
| <span id="g-残差连接"></span>残差连接 | Residual Connection | 把层的输入直接加到输出上，使深层网络易于训练 |
| <span id="g-层归一化"></span>层归一化 | Layer Normalization | 把每个向量的数值调整到稳定范围，使训练更稳定 |
| <span id="g-因果掩码"></span>因果掩码 | Causal Mask | 使每个位置只能看到其左侧内容的注意力掩码 |
| <span id="g-预训练"></span>预训练 | Pre-training | 在大规模通用数据上训练模型，学习一般语言规律和知识 |
| <span id="g-微调"></span>微调 | Fine-tuning | 在预训练模型基础上用任务数据继续训练 |
| <span id="g-自监督学习"></span>自监督学习 | Self-supervised Learning | 从数据本身构造训练目标、无需人工标注的学习方式 |
| <span id="g-掩码语言模型"></span>掩码语言模型 | Masked Language Model, MLM | 遮住部分词让模型预测的预训练任务（BERT） |
| <span id="g-BERT"></span>BERT | Bidirectional Encoder Representations from Transformers | 基于 Transformer 编码器、用掩码语言模型预训练的模型 |
| <span id="g-GPT"></span>GPT | Generative Pre-trained Transformer | 基于 Transformer 解码器、以预测下一个词为预训练任务的生成式模型 |
| <span id="g-规模定律"></span>规模定律 | Scaling Law | 模型效果随参数量、数据量、计算量增加而可预测地提升的规律 |
| <span id="g-指令微调"></span>指令微调 | Supervised Fine-Tuning, SFT | 用“指令-回答”数据微调，使模型能遵循人类指令 |
| <span id="g-人类反馈强化学习"></span>人类反馈强化学习 | Reinforcement Learning from Human Feedback, RLHF | 利用人类对回答的偏好训练模型，使其更有帮助、更安全 |
| <span id="g-推理模型"></span>推理模型 | Reasoning Model | 回答前先生成长思维链进行推理的大模型 |
| <span id="g-混合专家模型"></span>混合专家模型 | Mixture of Experts, MoE | 由路由器为每个 Token 选择少数专家网络计算的模型结构 |
| <span id="g-基座模型"></span>基座模型 | Base Model | 只经过预训练、尚未进行指令微调的模型 |
| <span id="g-开放权重模型"></span>开放权重模型 | Open-weight Model | 公开模型参数、允许下载和本地运行的模型 |
| <span id="g-量化"></span>量化 | Quantization | 用更少的比特存储模型参数，以降低内存和计算需求 |
| <span id="g-幻觉"></span>幻觉 | Hallucination | 模型生成看似合理但与事实不符或无中生有的内容 |
| <span id="g-参数高效微调"></span>参数高效微调 | Parameter-Efficient Fine-Tuning, PEFT | 冻结大部分参数、只训练少量参数的微调方法 |
| <span id="g-低秩适配"></span>低秩适配 | Low-Rank Adaptation, LoRA | 用两个低秩矩阵的乘积近似参数变化量的参数高效微调方法 |

## 第 10 章 机器翻译与文本生成

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-机器翻译"></span>机器翻译 | Machine Translation, MT | 用计算机把一种自然语言自动转换为另一种自然语言 |
| <span id="g-平行语料"></span>平行语料 | Parallel Corpus | 原文与译文逐句对应的双语语料 |
| <span id="g-统计机器翻译"></span>统计机器翻译 | Statistical Machine Translation, SMT | 从平行语料中统计翻译规律，结合翻译模型与语言模型的翻译方法 |
| <span id="g-词对齐"></span>词对齐 | Word Alignment | 找出双语句子中相互对应的词 |
| <span id="g-神经机器翻译"></span>神经机器翻译 | Neural Machine Translation, NMT | 用编码器-解码器神经网络端到端完成翻译 |
| <span id="g-序列到序列模型"></span>序列到序列模型 | Sequence-to-Sequence, Seq2Seq | 把一个序列转换为另一个序列的编码器-解码器模型 |
| <span id="g-回译"></span>回译 | Back-Translation | 用反向翻译模型把目标语言单语数据译回源语言，生成伪平行数据 |
| <span id="g-译后编辑"></span>译后编辑 | Post-Editing | 人工修改机器翻译初稿的工作方式 |
| <span id="g-BLEU"></span>BLEU | Bilingual Evaluation Understudy | 基于 n 元精确率和简短惩罚的机器翻译自动评价指标 |
| <span id="g-文本生成"></span>文本生成 | Text Generation | 由计算机自动产生自然语言文本 |
| <span id="g-自回归生成"></span>自回归生成 | Autoregressive Generation | 把已生成内容作为输入、逐个生成下一个 Token 的方式 |
| <span id="g-解码策略"></span>解码策略 | Decoding Strategy | 根据模型输出的概率分布选择下一个词的方法 |
| <span id="g-贪心搜索"></span>贪心搜索 | Greedy Search | 每一步选择概率最大的词的解码方法 |
| <span id="g-束搜索"></span>束搜索 | Beam Search | 每一步保留概率最高的若干候选序列的解码方法 |
| <span id="g-温度"></span>温度 | Temperature | 调节概率分布尖锐程度、从而控制生成随机性的参数 |
| <span id="g-Top-k-Top-p-采样"></span>Top-k / Top-p 采样 | Top-k / Top-p (Nucleus) Sampling | 只在概率最高的 k 个词 / 累计概率达到 p 的词中采样 |
| <span id="g-文本摘要"></span>文本摘要 | Text Summarization | 把长文本浓缩为保留主要信息的短文本，分抽取式和生成式 |
| <span id="g-TextRank"></span>TextRank | TextRank | 借鉴 PageRank、基于句子（或词）相似度图进行排序的摘要与关键词提取算法 |
| <span id="g-ROUGE"></span>ROUGE | Recall-Oriented Understudy for Gisting Evaluation | 以召回率为主的摘要自动评价指标 |
| <span id="g-深度合成"></span>深度合成 | Deep Synthesis | 利用深度学习等技术生成或编辑文本、图像、音频、视频的技术 |

## 第 11 章 问答系统、RAG 与智能体

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-问答系统"></span>问答系统 | Question Answering, QA | 理解自然语言问题并直接给出答案的系统 |
| <span id="g-知识图谱问答"></span>知识图谱问答 | Knowledge Base Question Answering, KBQA | 把问题转换为知识图谱查询来获取答案 |
| <span id="g-机器阅读理解"></span>机器阅读理解 | Machine Reading Comprehension, MRC | 根据给定文章回答问题，抽取式阅读理解预测答案的起止位置 |
| <span id="g-应用程序编程接口"></span>应用程序编程接口 | Application Programming Interface, API | 程序之间相互调用的约定；大模型 API 让程序通过网络调用模型 |
| <span id="g-系统提示"></span>系统提示 | System Prompt | 设定模型身份、规则和风格的消息，对整个对话生效 |
| <span id="g-上下文长度"></span>上下文长度 | Context Length | 模型一次能处理的最大 Token 数 |
| <span id="g-提示词-提示工程"></span>提示词 / 提示工程 | Prompt / Prompt Engineering | 给模型的指令和输入 / 设计和优化提示词的方法 |
| <span id="g-少样本提示"></span>少样本提示 | Few-shot Prompting | 在提示中给出几个输入输出示例的方法 |
| <span id="g-思维链"></span>思维链 | Chain of Thought, CoT | 让模型先写出推理步骤再给出答案的方法 |
| <span id="g-检索增强生成"></span>检索增强生成 | Retrieval-Augmented Generation, RAG | 先检索相关资料，再让大模型基于资料生成回答的技术 |
| <span id="g-切块"></span>切块 | Chunking | 把长文档切分为适合检索的片段 |
| <span id="g-BM25"></span>BM25 | BM25 | 考虑词频饱和与文档长度的关键词检索打分算法 |
| <span id="g-向量检索"></span>向量检索 | Vector Retrieval | 基于文本嵌入向量相似度的检索 |
| <span id="g-向量数据库"></span>向量数据库 | Vector Database | 专门存储向量并支持快速相似度检索的数据库 |
| <span id="g-混合检索"></span>混合检索 | Hybrid Retrieval | 结合关键词检索和向量检索的检索方式 |
| <span id="g-重排序"></span>重排序 | Reranking | 用更精确的模型对初步检索结果重新排序 |
| <span id="g-智能体"></span>智能体 | AI Agent | 以大模型为核心、能规划步骤、调用工具、自主完成任务的系统 |
| <span id="g-函数调用"></span>函数调用 | Function Calling / Tool Calling | 模型输出结构化的工具调用请求、由程序执行并返回结果的机制 |
| <span id="g-ReAct"></span>ReAct | Reasoning and Acting | 让模型循环进行“思考—行动—观察”的智能体方法 |
| <span id="g-模型上下文协议"></span>模型上下文协议 | Model Context Protocol, MCP | 大模型应用连接外部工具和数据源的开放标准接口 |
| <span id="g-工作流"></span>工作流 | Workflow | 预先设计好的、由多个步骤组成的处理流程 |

## 第 12 章 NLP 的伦理、安全与法律

| 术语 | 英文 | 定义 |
|---|---|---|
| <span id="g-人工智能伦理"></span>人工智能伦理 | AI Ethics | 研究和规范人工智能研发与应用中道德问题的原则和准则 |
| <span id="g-偏见"></span>偏见 | Bias | 模型对某些群体系统性地产生不公平或不准确判断的现象 |
| <span id="g-反事实测试"></span>反事实测试 | Counterfactual Testing | 只改变与群体相关的词、观察模型输出变化的偏见检测方法 |
| <span id="g-反事实数据增强"></span>反事实数据增强 | Counterfactual Data Augmentation | 互换训练数据中的群体词生成新样本，以缓解偏见的方法 |
| <span id="g-个人信息"></span>个人信息 | Personal Information | 与已识别或可识别的自然人有关的各种信息，不含匿名化处理后的信息 |
| <span id="g-敏感个人信息"></span>敏感个人信息 | Sensitive Personal Information | 一旦泄露或被非法使用，易导致人格尊严受损或人身、财产安全受危害的个人信息 |
| <span id="g-去标识化"></span>去标识化 | De-identification | 使个人信息在不借助额外信息时无法识别特定个人的处理 |
| <span id="g-匿名化"></span>匿名化 | Anonymization | 使个人信息无法识别特定个人且不能复原的处理 |
| <span id="g-数据脱敏"></span>数据脱敏 | Data Masking | 对敏感信息进行替换、遮盖、泛化或删除的处理 |
| <span id="g-越狱"></span>越狱 | Jailbreak | 设法绕过模型安全限制、诱导其输出本应拒绝内容的行为 |
| <span id="g-提示注入"></span>提示注入 | Prompt Injection | 把恶意指令伪装成数据混入模型输入以劫持模型行为的攻击，分直接与间接两类 |
| <span id="g-纵深防御"></span>纵深防御 | Defense in Depth | 设置多道相互补充的防线来降低安全风险的策略 |
| <span id="g-最小权限原则"></span>最小权限原则 | Principle of Least Privilege | 只授予完成任务所必需的最少权限 |
| <span id="g-红队测试"></span>红队测试 | Red Teaming | 模拟攻击者主动寻找系统漏洞的安全测试 |
| <span id="g-内容标识"></span>内容标识 | Content Labeling | 对 AI 生成合成内容添加显式或隐式标记，以表明其来源 |
