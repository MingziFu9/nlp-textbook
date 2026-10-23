---
title: 附录 E 术语表
description: 本书主要术语的中英文名称与简明定义，按章节顺序排列
---

# 附录 E 术语表

本表按章节顺序列出本书的主要术语，每个术语给出英文名称和简明定义。括号中的数字表示该术语主要出现的章节。

## 第 1 章 自然语言处理概述

| 术语 | 英文 | 定义 |
|---|---|---|
| 自然语言 | Natural Language | 人类在日常交流中自然形成和使用的语言，如汉语、英语，区别于编程语言等人工语言 |
| 自然语言处理 | Natural Language Processing, NLP | 研究让计算机理解、处理和生成人类语言的理论与技术 |
| 自然语言理解 | Natural Language Understanding, NLU | 让计算机读懂语言含义的技术，如分类、抽取、问答 |
| 自然语言生成 | Natural Language Generation, NLG | 让计算机产生自然语言文本的技术，如翻译、摘要、写作 |
| 歧义 | Ambiguity | 同一个语言表达可以有多种理解的现象，是 NLP 的核心难点 |
| 语料库 | Corpus | 为语言研究和模型训练而收集、整理的大规模文本集合 |
| 大语言模型 | Large Language Model, LLM | 参数规模巨大、在海量文本上预训练、具有通用语言理解与生成能力的模型 |

## 第 2 章 文本预处理

| 术语 | 英文 | 定义 |
|---|---|---|
| 文本预处理 | Text Preprocessing | 在分析或建模前对原始文本进行清洗、规范化、切分等处理的过程 |
| 字符编码 | Character Encoding | 把字符映射为计算机中二进制数据的规则，如 UTF-8、GBK |
| 正则表达式 | Regular Expression | 用特定语法描述字符串模式，用于查找、替换和校验文本 |
| 分句 | Sentence Segmentation | 把一段文本切分为句子 |
| 词元化 / 分词 | Tokenization | 把文本切分为词、子词或字等基本单位（词元） |
| 停用词 | Stop Words | 出现频率高但对任务贡献小的词，如“的”“了”“the” |
| 词干提取 | Stemming | 用规则去掉英文单词的词缀，得到词干，如 running → run |
| 词形还原 | Lemmatization | 借助词典把英文单词还原为原形，如 better → good |
| 繁简转换 | Traditional-Simplified Conversion | 在繁体中文与简体中文之间转换 |
| 数据清洗 | Data Cleaning | 去除噪声、重复、无效数据，提高数据质量的过程 |

## 第 3 章 词法分析

| 术语 | 英文 | 定义 |
|---|---|---|
| 词法分析 | Lexical Analysis | 以词为单位的分析，包括分词、词性标注等 |
| 中文分词 | Chinese Word Segmentation | 把没有空格分隔的中文句子切分为词序列 |
| 最大匹配法 | Maximum Matching | 基于词典、每次取最长匹配词的分词方法，分正向、逆向和双向 |
| 切分歧义 | Segmentation Ambiguity | 同一字串可以有多种切分方式的现象，分交集型和组合型 |
| 未登录词 | Out-of-Vocabulary Word, OOV | 词典或词表中没有收录的词，如新词、人名 |
| 词性标注 | Part-of-Speech Tagging | 为句子中的每个词标注名词、动词等词性 |
| N 元语法 | N-gram | 由连续 N 个词（或字）组成的片段；N 元语言模型据此估计句子概率 |
| 隐马尔可夫模型 | Hidden Markov Model, HMM | 用隐藏状态序列生成观测序列的概率模型，曾广泛用于分词和词性标注 |
| 子词 | Subword | 介于字符和词之间的切分单位，可以组合出罕见词 |
| 字节对编码 | Byte Pair Encoding, BPE | 反复合并出现最频繁的相邻符号对来构建子词词表的算法 |
| 词元 | Token | 模型处理文本的最小单位；大模型按 Token 计费和限制长度 |
| 分词器 | Tokenizer | 把文本转换为 Token 编号序列（以及反向转换）的组件 |
| 词表 | Vocabulary | 模型或分词器所认识的全部词元及其编号 |

## 第 4 章 句法分析

| 术语 | 英文 | 定义 |
|---|---|---|
| 句法分析 | Syntactic Parsing | 分析句子的语法结构 |
| 成分句法 | Constituency Parsing | 把句子分析为层层嵌套的短语结构（句法树） |
| 上下文无关文法 | Context-Free Grammar, CFG | 用“左边一个符号 → 右边符号串”形式的规则描述句子结构的文法 |
| 句法树 | Parse Tree | 表示句子成分结构的树形图 |
| 依存句法 | Dependency Parsing | 分析句子中词与词之间支配与被支配关系的方法 |
| 核心词 / 中心词 | Head | 依存关系中起支配作用的词 |
| 依存关系 | Dependency Relation | 两个词之间的语法关系，如主谓、动宾、定中 |
| 语义角色标注 | Semantic Role Labeling | 识别句子中谓词的施事、受事、时间、地点等语义角色 |

## 第 5 章 文本表示

| 术语 | 英文 | 定义 |
|---|---|---|
| 文本表示 | Text Representation | 把文本转换为计算机可以计算的数值向量 |
| 独热编码 | One-hot Encoding | 用只有一个位置为 1、其余为 0 的向量表示词 |
| 词袋模型 | Bag of Words | 只统计词出现次数、忽略词序的文本表示方法 |
| 词频-逆文档频率 | TF-IDF | 用词在文档中的频率与其在整个语料中的稀有程度的乘积衡量词的重要性 |
| 余弦相似度 | Cosine Similarity | 用两个向量夹角的余弦值衡量其相似程度，取值 -1 到 1 |
| 分布式假设 | Distributional Hypothesis | 上下文相似的词，意义也相似 |
| 词向量 / 词嵌入 | Word Embedding | 用低维稠密向量表示词，语义相近的词向量相近 |
| Word2Vec | Word2Vec | 通过预测上下文（Skip-gram）或中心词（CBOW）学习词向量的方法 |
| 上下文相关词向量 | Contextual Embedding | 同一个词在不同语境中得到不同向量的表示方法，如 BERT 的输出 |
| 文本嵌入 | Text Embedding | 把整句或整段文本表示为一个向量，用于语义检索和匹配 |
| 语义搜索 | Semantic Search | 根据含义而非字面匹配进行的检索 |

## 第 6 章 文本分类与情感分析

| 术语 | 英文 | 定义 |
|---|---|---|
| 文本分类 | Text Classification | 把文本归入预先定义的类别 |
| 情感分析 | Sentiment Analysis | 识别文本表达的情感倾向（正面、负面等）或情绪 |
| 方面级情感分析 | Aspect-Based Sentiment Analysis | 识别文本中针对各个具体方面（如价格、服务）的情感 |
| 情感词典 | Sentiment Lexicon | 收录词语及其情感倾向和强度的词典 |
| 训练集 / 测试集 | Training Set / Test Set | 分别用于训练模型和评估模型效果的数据 |
| 朴素贝叶斯 | Naive Bayes | 基于贝叶斯定理、假设特征相互独立的分类算法 |
| 逻辑回归 | Logistic Regression | 用 Sigmoid 函数输出类别概率的线性分类模型 |
| 支持向量机 | Support Vector Machine, SVM | 寻找使两类间隔最大的分隔超平面的分类算法 |
| 混淆矩阵 | Confusion Matrix | 按真实类别和预测类别交叉统计样本数量的表格 |
| 准确率 | Accuracy | 预测正确的样本占全部样本的比例 |
| 精确率 | Precision | 预测为某类的样本中真正属于该类的比例 |
| 召回率 | Recall | 某类的全部样本中被正确预测出来的比例 |
| F1 值 | F1 Score | 精确率与召回率的调和平均数 |
| 类别不平衡 | Class Imbalance | 各类别样本数量差异很大的情况 |
| 零样本学习 | Zero-shot Learning | 不提供任何示例，仅凭任务描述完成任务 |

## 第 7 章 命名实体识别与信息抽取

| 术语 | 英文 | 定义 |
|---|---|---|
| 信息抽取 | Information Extraction, IE | 从非结构化文本中抽取指定类型的信息并整理成结构化数据 |
| 命名实体识别 | Named Entity Recognition, NER | 识别文本中人名、地名、机构名等实体的位置和类型 |
| 序列标注 | Sequence Labeling | 为序列中的每个元素分配一个标签的任务，如分词、词性标注、NER |
| BIO 标注 | BIO Tagging | 用 B（开始）、I（内部）、O（外部）标注实体边界的方法 |
| 条件随机场 | Conditional Random Field, CRF | 考虑相邻标签之间依赖关系的序列标注模型 |
| 关系抽取 | Relation Extraction | 判断文本中两个实体之间的语义关系 |
| 三元组 | Triple | （头实体，关系，尾实体）形式的知识表示 |
| 事件抽取 | Event Extraction | 识别事件类型、触发词和事件论元（时间、地点、参与者等） |
| 知识图谱 | Knowledge Graph | 以实体为节点、关系为边组织知识的图结构 |
| 实体链接 | Entity Linking | 把文本中的实体指称对应到知识库中唯一实体的任务 |
| 数据标注 | Data Annotation | 按照规范为数据添加标签，供模型训练和评估使用 |

## 第 8 章 深度学习基础

| 术语 | 英文 | 定义 |
|---|---|---|
| 深度学习 | Deep Learning | 使用多层神经网络从数据中自动学习特征的机器学习方法 |
| 表示学习 | Representation Learning | 让模型自动学习数据的有用表示，而非依赖人工特征 |
| 神经元 | Neuron | 对输入加权求和、加上偏置后经激活函数输出的计算单元 |
| 权重 / 偏置 | Weight / Bias | 神经元中由训练学习得到的参数 |
| 感知机 | Perceptron | 只有一个神经元、使用阶跃激活函数的最简单神经网络 |
| 多层感知机 | Multi-Layer Perceptron, MLP | 含一个或多个隐藏层的全连接前馈神经网络 |
| 激活函数 | Activation Function | 为神经网络引入非线性的函数，如 Sigmoid、Tanh、ReLU |
| Softmax | Softmax | 把一组得分转换为和为 1 的概率分布的函数 |
| 损失函数 | Loss Function | 衡量模型预测与真实答案之间差距的函数 |
| 交叉熵 | Cross-Entropy | 分类任务常用的损失函数，等于正确类别预测概率的负对数 |
| 梯度 | Gradient | 损失函数对参数的偏导数，指示参数调整的方向和幅度 |
| 反向传播 | Backpropagation | 利用链式法则从输出层向输入层逐层计算梯度的算法 |
| 梯度下降 | Gradient Descent | 沿梯度反方向更新参数以减小损失的优化方法 |
| 学习率 | Learning Rate | 每次参数更新的步长，是最重要的超参数之一 |
| 优化器 | Optimizer | 根据梯度更新参数的算法，如 SGD、Adam、AdamW |
| 轮次 / 批 | Epoch / Batch | 完整使用一遍训练数据称为一轮；每次更新所用的一小组样本称为一批 |
| 超参数 | Hyperparameter | 训练前由人设定、不由模型学习的参数 |
| 过拟合 | Overfitting | 模型在训练集上表现好、在新数据上表现差的现象 |
| 随机失活 | Dropout | 训练时随机关闭部分神经元以减轻过拟合的方法 |
| 张量 | Tensor | 深度学习框架中的多维数组，可在 GPU 上计算并自动求导 |
| 词嵌入层 | Embedding Layer | 把词的编号映射为可训练词向量的查找表 |
| 循环神经网络 | Recurrent Neural Network, RNN | 通过隐藏状态在时间步之间传递信息、处理序列数据的网络 |
| 隐藏状态 | Hidden State | 循环网络中保存已读内容信息的向量 |
| 梯度消失 / 梯度爆炸 | Vanishing / Exploding Gradient | 反向传播中梯度逐层变得极小或极大，导致训练困难的现象 |
| 长短期记忆网络 | Long Short-Term Memory, LSTM | 用记忆细胞和遗忘门、输入门、输出门控制信息流动的循环网络 |
| 门控循环单元 | Gated Recurrent Unit, GRU | 只有更新门和重置门的简化版 LSTM |
| 双向循环网络 | Bidirectional RNN | 分别从左向右和从右向左读取序列并拼接结果的循环网络 |
| 状态空间模型 | State Space Model, SSM | 以固定大小状态递推处理长序列的模型，如 Mamba |

## 第 9 章 Transformer 与预训练大模型

| 术语 | 英文 | 定义 |
|---|---|---|
| 注意力机制 | Attention Mechanism | 根据相关程度为不同位置的信息分配权重并加权求和的机制 |
| 自注意力 | Self-Attention | 序列中每个位置关注同一序列所有位置的注意力 |
| 查询 / 键 / 值 | Query / Key / Value | 自注意力中分别用于发起匹配、被匹配和提供内容的三个向量 |
| 多头注意力 | Multi-Head Attention | 并行使用多组 Q、K、V 投影，从多个角度计算注意力 |
| Transformer | Transformer | 以自注意力为核心、可并行计算的神经网络架构，2017 年提出 |
| 编码器 / 解码器 | Encoder / Decoder | 分别负责理解输入和逐步生成输出的网络部分 |
| 位置编码 | Positional Encoding | 为输入加入位置信息，弥补自注意力不感知词序的缺陷 |
| 旋转位置编码 | Rotary Position Embedding, RoPE | 通过旋转 Q、K 向量表示相对位置的编码方法，大模型普遍采用 |
| 残差连接 | Residual Connection | 把层的输入直接加到输出上，使深层网络易于训练 |
| 层归一化 | Layer Normalization | 把每个向量的数值调整到稳定范围，使训练更稳定 |
| 因果掩码 | Causal Mask | 使每个位置只能看到其左侧内容的注意力掩码 |
| 预训练 | Pre-training | 在大规模通用数据上训练模型，学习一般语言规律和知识 |
| 微调 | Fine-tuning | 在预训练模型基础上用任务数据继续训练 |
| 自监督学习 | Self-supervised Learning | 从数据本身构造训练目标、无需人工标注的学习方式 |
| 掩码语言模型 | Masked Language Model, MLM | 遮住部分词让模型预测的预训练任务（BERT） |
| BERT | Bidirectional Encoder Representations from Transformers | 基于 Transformer 编码器、用掩码语言模型预训练的模型 |
| GPT | Generative Pre-trained Transformer | 基于 Transformer 解码器、以预测下一个词为预训练任务的生成式模型 |
| 规模定律 | Scaling Law | 模型效果随参数量、数据量、计算量增加而可预测地提升的规律 |
| 指令微调 | Supervised Fine-Tuning, SFT | 用“指令-回答”数据微调，使模型能遵循人类指令 |
| 人类反馈强化学习 | Reinforcement Learning from Human Feedback, RLHF | 利用人类对回答的偏好训练模型，使其更有帮助、更安全 |
| 推理模型 | Reasoning Model | 回答前先生成长思维链进行推理的大模型 |
| 混合专家模型 | Mixture of Experts, MoE | 由路由器为每个 Token 选择少数专家网络计算的模型结构 |
| 基座模型 | Base Model | 只经过预训练、尚未进行指令微调的模型 |
| 开放权重模型 | Open-weight Model | 公开模型参数、允许下载和本地运行的模型 |
| 量化 | Quantization | 用更少的比特存储模型参数，以降低内存和计算需求 |
| 幻觉 | Hallucination | 模型生成看似合理但与事实不符或无中生有的内容 |
| 参数高效微调 | Parameter-Efficient Fine-Tuning, PEFT | 冻结大部分参数、只训练少量参数的微调方法 |
| 低秩适配 | Low-Rank Adaptation, LoRA | 用两个低秩矩阵的乘积近似参数变化量的参数高效微调方法 |

## 第 10 章 机器翻译与文本生成

| 术语 | 英文 | 定义 |
|---|---|---|
| 机器翻译 | Machine Translation, MT | 用计算机把一种自然语言自动转换为另一种自然语言 |
| 平行语料 | Parallel Corpus | 原文与译文逐句对应的双语语料 |
| 统计机器翻译 | Statistical Machine Translation, SMT | 从平行语料中统计翻译规律，结合翻译模型与语言模型的翻译方法 |
| 词对齐 | Word Alignment | 找出双语句子中相互对应的词 |
| 神经机器翻译 | Neural Machine Translation, NMT | 用编码器-解码器神经网络端到端完成翻译 |
| 序列到序列模型 | Sequence-to-Sequence, Seq2Seq | 把一个序列转换为另一个序列的编码器-解码器模型 |
| 回译 | Back-Translation | 用反向翻译模型把目标语言单语数据译回源语言，生成伪平行数据 |
| 译后编辑 | Post-Editing | 人工修改机器翻译初稿的工作方式 |
| BLEU | Bilingual Evaluation Understudy | 基于 n 元精确率和简短惩罚的机器翻译自动评价指标 |
| 文本生成 | Text Generation | 由计算机自动产生自然语言文本 |
| 自回归生成 | Autoregressive Generation | 把已生成内容作为输入、逐个生成下一个 Token 的方式 |
| 解码策略 | Decoding Strategy | 根据模型输出的概率分布选择下一个词的方法 |
| 贪心搜索 | Greedy Search | 每一步选择概率最大的词的解码方法 |
| 束搜索 | Beam Search | 每一步保留概率最高的若干候选序列的解码方法 |
| 温度 | Temperature | 调节概率分布尖锐程度、从而控制生成随机性的参数 |
| Top-k / Top-p 采样 | Top-k / Top-p (Nucleus) Sampling | 只在概率最高的 k 个词 / 累计概率达到 p 的词中采样 |
| 文本摘要 | Text Summarization | 把长文本浓缩为保留主要信息的短文本，分抽取式和生成式 |
| TextRank | TextRank | 借鉴 PageRank、基于句子（或词）相似度图进行排序的摘要与关键词提取算法 |
| ROUGE | Recall-Oriented Understudy for Gisting Evaluation | 以召回率为主的摘要自动评价指标 |
| 深度合成 | Deep Synthesis | 利用深度学习等技术生成或编辑文本、图像、音频、视频的技术 |

## 第 11 章 问答系统、RAG 与智能体

| 术语 | 英文 | 定义 |
|---|---|---|
| 问答系统 | Question Answering, QA | 理解自然语言问题并直接给出答案的系统 |
| 知识图谱问答 | Knowledge Base Question Answering, KBQA | 把问题转换为知识图谱查询来获取答案 |
| 机器阅读理解 | Machine Reading Comprehension, MRC | 根据给定文章回答问题，抽取式阅读理解预测答案的起止位置 |
| 应用程序编程接口 | Application Programming Interface, API | 程序之间相互调用的约定；大模型 API 让程序通过网络调用模型 |
| 系统提示 | System Prompt | 设定模型身份、规则和风格的消息，对整个对话生效 |
| 上下文长度 | Context Length | 模型一次能处理的最大 Token 数 |
| 提示词 / 提示工程 | Prompt / Prompt Engineering | 给模型的指令和输入 / 设计和优化提示词的方法 |
| 少样本提示 | Few-shot Prompting | 在提示中给出几个输入输出示例的方法 |
| 思维链 | Chain of Thought, CoT | 让模型先写出推理步骤再给出答案的方法 |
| 检索增强生成 | Retrieval-Augmented Generation, RAG | 先检索相关资料，再让大模型基于资料生成回答的技术 |
| 切块 | Chunking | 把长文档切分为适合检索的片段 |
| BM25 | BM25 | 考虑词频饱和与文档长度的关键词检索打分算法 |
| 向量检索 | Vector Retrieval | 基于文本嵌入向量相似度的检索 |
| 向量数据库 | Vector Database | 专门存储向量并支持快速相似度检索的数据库 |
| 混合检索 | Hybrid Retrieval | 结合关键词检索和向量检索的检索方式 |
| 重排序 | Reranking | 用更精确的模型对初步检索结果重新排序 |
| 智能体 | AI Agent | 以大模型为核心、能规划步骤、调用工具、自主完成任务的系统 |
| 函数调用 | Function Calling / Tool Calling | 模型输出结构化的工具调用请求、由程序执行并返回结果的机制 |
| ReAct | Reasoning and Acting | 让模型循环进行“思考—行动—观察”的智能体方法 |
| 模型上下文协议 | Model Context Protocol, MCP | 大模型应用连接外部工具和数据源的开放标准接口 |
| 工作流 | Workflow | 预先设计好的、由多个步骤组成的处理流程 |

## 第 12 章 NLP 的伦理、安全与法律

| 术语 | 英文 | 定义 |
|---|---|---|
| 人工智能伦理 | AI Ethics | 研究和规范人工智能研发与应用中道德问题的原则和准则 |
| 偏见 | Bias | 模型对某些群体系统性地产生不公平或不准确判断的现象 |
| 反事实测试 | Counterfactual Testing | 只改变与群体相关的词、观察模型输出变化的偏见检测方法 |
| 反事实数据增强 | Counterfactual Data Augmentation | 互换训练数据中的群体词生成新样本，以缓解偏见的方法 |
| 个人信息 | Personal Information | 与已识别或可识别的自然人有关的各种信息，不含匿名化处理后的信息 |
| 敏感个人信息 | Sensitive Personal Information | 一旦泄露或被非法使用，易导致人格尊严受损或人身、财产安全受危害的个人信息 |
| 去标识化 | De-identification | 使个人信息在不借助额外信息时无法识别特定个人的处理 |
| 匿名化 | Anonymization | 使个人信息无法识别特定个人且不能复原的处理 |
| 数据脱敏 | Data Masking | 对敏感信息进行替换、遮盖、泛化或删除的处理 |
| 越狱 | Jailbreak | 设法绕过模型安全限制、诱导其输出本应拒绝内容的行为 |
| 提示注入 | Prompt Injection | 把恶意指令伪装成数据混入模型输入以劫持模型行为的攻击，分直接与间接两类 |
| 纵深防御 | Defense in Depth | 设置多道相互补充的防线来降低安全风险的策略 |
| 最小权限原则 | Principle of Least Privilege | 只授予完成任务所必需的最少权限 |
| 红队测试 | Red Teaming | 模拟攻击者主动寻找系统漏洞的安全测试 |
| 内容标识 | Content Labeling | 对 AI 生成合成内容添加显式或隐式标记，以表明其来源 |
