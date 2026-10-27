---
title: 学习图谱
description: 全书 176 个核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解“检索增强生成”，得先懂“语义搜索”和“提示工程”；要理解“语义搜索”，又得先懂“文本嵌入”……顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="1300" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从第 11、12 章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

图谱共有 **176 个概念、238 条先修关系**，概念按章排列，颜色表示 10 个类别（基础概念、文本处理、语言分析、文本表示、机器学习与评价、神经网络、Transformer 与大模型、生成与解码、应用系统、安全与伦理）。概念的定义都来自[附录 E 术语表](../appendix/e-glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 绪论（6 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [自然语言处理](../appendix/e-glossary.md#g-自然语言处理) | 基础概念 | — |
    | [自然语言理解](../appendix/e-glossary.md#g-自然语言理解) | 基础概念 | [自然语言处理](../appendix/e-glossary.md#g-自然语言处理) |
    | [自然语言生成](../appendix/e-glossary.md#g-自然语言生成) | 基础概念 | [自然语言处理](../appendix/e-glossary.md#g-自然语言处理) |
    | [歧义](../appendix/e-glossary.md#g-歧义) | 基础概念 | [自然语言处理](../appendix/e-glossary.md#g-自然语言处理) |
    | [语料库](../appendix/e-glossary.md#g-语料库) | 基础概念 | [自然语言处理](../appendix/e-glossary.md#g-自然语言处理) |
    | [大语言模型](../appendix/e-glossary.md#g-大语言模型) | 基础概念 | [自然语言处理](../appendix/e-glossary.md#g-自然语言处理) |

??? note "第 2 章 文本预处理（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [文本预处理](../appendix/e-glossary.md#g-文本预处理) | 文本处理 | [语料库](../appendix/e-glossary.md#g-语料库) |
    | [字符编码](../appendix/e-glossary.md#g-字符编码) | 文本处理 | [文本预处理](../appendix/e-glossary.md#g-文本预处理) |
    | [Unicode 规范化](../appendix/e-glossary.md#g-Unicode-规范化) | 文本处理 | [字符编码](../appendix/e-glossary.md#g-字符编码) |
    | [正则表达式](../appendix/e-glossary.md#g-正则表达式) | 文本处理 | [文本预处理](../appendix/e-glossary.md#g-文本预处理) |
    | [数据清洗](../appendix/e-glossary.md#g-数据清洗) | 文本处理 | [正则表达式](../appendix/e-glossary.md#g-正则表达式)、[字符编码](../appendix/e-glossary.md#g-字符编码) |
    | [近似重复](../appendix/e-glossary.md#g-近似重复) | 文本处理 | [数据清洗](../appendix/e-glossary.md#g-数据清洗) |
    | [词元化 / 分词](../appendix/e-glossary.md#g-词元化-分词) | 文本处理 | [文本预处理](../appendix/e-glossary.md#g-文本预处理) |
    | [停用词](../appendix/e-glossary.md#g-停用词) | 文本处理 | [词元化 / 分词](../appendix/e-glossary.md#g-词元化-分词) |
    | [词干提取](../appendix/e-glossary.md#g-词干提取) | 文本处理 | [词元化 / 分词](../appendix/e-glossary.md#g-词元化-分词) |
    | [词形还原](../appendix/e-glossary.md#g-词形还原) | 文本处理 | [词干提取](../appendix/e-glossary.md#g-词干提取) |

??? note "第 3 章 词法分析（11 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [词法分析](../appendix/e-glossary.md#g-词法分析) | 语言分析 | [词元化 / 分词](../appendix/e-glossary.md#g-词元化-分词) |
    | [中文分词](../appendix/e-glossary.md#g-中文分词) | 语言分析 | [词法分析](../appendix/e-glossary.md#g-词法分析)、[歧义](../appendix/e-glossary.md#g-歧义) |
    | [最大匹配法](../appendix/e-glossary.md#g-最大匹配法) | 语言分析 | [中文分词](../appendix/e-glossary.md#g-中文分词) |
    | [切分歧义](../appendix/e-glossary.md#g-切分歧义) | 语言分析 | [中文分词](../appendix/e-glossary.md#g-中文分词)、[歧义](../appendix/e-glossary.md#g-歧义) |
    | [未登录词](../appendix/e-glossary.md#g-未登录词) | 语言分析 | [中文分词](../appendix/e-glossary.md#g-中文分词) |
    | [N 元语法](../appendix/e-glossary.md#g-N-元语法) | 语言分析 | [语料库](../appendix/e-glossary.md#g-语料库) |
    | [隐马尔可夫模型](../appendix/e-glossary.md#g-隐马尔可夫模型) | 语言分析 | [N 元语法](../appendix/e-glossary.md#g-N-元语法)、[中文分词](../appendix/e-glossary.md#g-中文分词) |
    | [词性标注](../appendix/e-glossary.md#g-词性标注) | 语言分析 | [词法分析](../appendix/e-glossary.md#g-词法分析) |
    | [子词](../appendix/e-glossary.md#g-子词) | 文本处理 | [词元化 / 分词](../appendix/e-glossary.md#g-词元化-分词)、[未登录词](../appendix/e-glossary.md#g-未登录词) |
    | [字节对编码](../appendix/e-glossary.md#g-字节对编码) | 文本处理 | [子词](../appendix/e-glossary.md#g-子词) |
    | [词元](../appendix/e-glossary.md#g-词元) | 文本处理 | [字节对编码](../appendix/e-glossary.md#g-字节对编码) |

??? note "第 4 章 句法与语义分析（11 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [句法分析](../appendix/e-glossary.md#g-句法分析) | 语言分析 | [词性标注](../appendix/e-glossary.md#g-词性标注) |
    | [成分句法](../appendix/e-glossary.md#g-成分句法) | 语言分析 | [句法分析](../appendix/e-glossary.md#g-句法分析) |
    | [上下文无关文法](../appendix/e-glossary.md#g-上下文无关文法) | 语言分析 | [成分句法](../appendix/e-glossary.md#g-成分句法) |
    | [句法树](../appendix/e-glossary.md#g-句法树) | 语言分析 | [上下文无关文法](../appendix/e-glossary.md#g-上下文无关文法) |
    | [结构歧义](../appendix/e-glossary.md#g-结构歧义) | 语言分析 | [句法树](../appendix/e-glossary.md#g-句法树)、[歧义](../appendix/e-glossary.md#g-歧义) |
    | [依存句法](../appendix/e-glossary.md#g-依存句法) | 语言分析 | [句法分析](../appendix/e-glossary.md#g-句法分析) |
    | [依存关系](../appendix/e-glossary.md#g-依存关系) | 语言分析 | [依存句法](../appendix/e-glossary.md#g-依存句法) |
    | [语义分析](../appendix/e-glossary.md#g-语义分析) | 语言分析 | [句法分析](../appendix/e-glossary.md#g-句法分析) |
    | [词义消歧](../appendix/e-glossary.md#g-词义消歧) | 语言分析 | [语义分析](../appendix/e-glossary.md#g-语义分析)、[歧义](../appendix/e-glossary.md#g-歧义) |
    | [语义角色标注](../appendix/e-glossary.md#g-语义角色标注) | 语言分析 | [语义分析](../appendix/e-glossary.md#g-语义分析)、[依存关系](../appendix/e-glossary.md#g-依存关系) |
    | [指代消解](../appendix/e-glossary.md#g-指代消解) | 语言分析 | [语义分析](../appendix/e-glossary.md#g-语义分析) |

??? note "第 5 章 文本表示（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [文本表示](../appendix/e-glossary.md#g-文本表示) | 文本表示 | [词元化 / 分词](../appendix/e-glossary.md#g-词元化-分词) |
    | [独热编码](../appendix/e-glossary.md#g-独热编码) | 文本表示 | [文本表示](../appendix/e-glossary.md#g-文本表示) |
    | [词袋模型](../appendix/e-glossary.md#g-词袋模型) | 文本表示 | [独热编码](../appendix/e-glossary.md#g-独热编码) |
    | [TF-IDF](../appendix/e-glossary.md#g-TF-IDF) | 文本表示 | [词袋模型](../appendix/e-glossary.md#g-词袋模型)、[停用词](../appendix/e-glossary.md#g-停用词) |
    | [BM25](../appendix/e-glossary.md#g-BM25) | 文本表示 | [TF-IDF](../appendix/e-glossary.md#g-TF-IDF) |
    | [余弦相似度](../appendix/e-glossary.md#g-余弦相似度) | 文本表示 | [词袋模型](../appendix/e-glossary.md#g-词袋模型) |
    | [分布式假设](../appendix/e-glossary.md#g-分布式假设) | 文本表示 | [文本表示](../appendix/e-glossary.md#g-文本表示) |
    | [词向量 / 词嵌入](../appendix/e-glossary.md#g-词向量-词嵌入) | 文本表示 | [分布式假设](../appendix/e-glossary.md#g-分布式假设)、[独热编码](../appendix/e-glossary.md#g-独热编码) |
    | [Word2Vec](../appendix/e-glossary.md#g-Word2Vec) | 文本表示 | [词向量 / 词嵌入](../appendix/e-glossary.md#g-词向量-词嵌入) |
    | [自监督学习](../appendix/e-glossary.md#g-自监督学习) | 机器学习与评价 | [Word2Vec](../appendix/e-glossary.md#g-Word2Vec) |
    | [文本嵌入](../appendix/e-glossary.md#g-文本嵌入) | 文本表示 | [词向量 / 词嵌入](../appendix/e-glossary.md#g-词向量-词嵌入)、[余弦相似度](../appendix/e-glossary.md#g-余弦相似度) |
    | [向量数据库](../appendix/e-glossary.md#g-向量数据库) | 应用系统 | [文本嵌入](../appendix/e-glossary.md#g-文本嵌入) |
    | [语义搜索](../appendix/e-glossary.md#g-语义搜索) | 应用系统 | [文本嵌入](../appendix/e-glossary.md#g-文本嵌入)、[向量数据库](../appendix/e-glossary.md#g-向量数据库) |
    | [混合检索](../appendix/e-glossary.md#g-混合检索) | 应用系统 | [BM25](../appendix/e-glossary.md#g-BM25)、[语义搜索](../appendix/e-glossary.md#g-语义搜索) |

??? note "第 6 章 文本分类与情感分析（18 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [监督学习](../appendix/e-glossary.md#g-监督学习) | 机器学习与评价 | [语料库](../appendix/e-glossary.md#g-语料库) |
    | [训练集](../appendix/e-glossary.md#g-训练集) | 机器学习与评价 | [监督学习](../appendix/e-glossary.md#g-监督学习) |
    | [测试集](../appendix/e-glossary.md#g-测试集) | 机器学习与评价 | [训练集](../appendix/e-glossary.md#g-训练集) |
    | [文本分类](../appendix/e-glossary.md#g-文本分类) | 应用系统 | [监督学习](../appendix/e-glossary.md#g-监督学习)、[文本表示](../appendix/e-glossary.md#g-文本表示) |
    | [朴素贝叶斯](../appendix/e-glossary.md#g-朴素贝叶斯) | 机器学习与评价 | [文本分类](../appendix/e-glossary.md#g-文本分类)、[词袋模型](../appendix/e-glossary.md#g-词袋模型) |
    | [逻辑回归](../appendix/e-glossary.md#g-逻辑回归) | 机器学习与评价 | [文本分类](../appendix/e-glossary.md#g-文本分类) |
    | [阈值](../appendix/e-glossary.md#g-阈值) | 机器学习与评价 | [逻辑回归](../appendix/e-glossary.md#g-逻辑回归) |
    | [混淆矩阵](../appendix/e-glossary.md#g-混淆矩阵) | 机器学习与评价 | [文本分类](../appendix/e-glossary.md#g-文本分类)、[测试集](../appendix/e-glossary.md#g-测试集) |
    | [准确率](../appendix/e-glossary.md#g-准确率) | 机器学习与评价 | [混淆矩阵](../appendix/e-glossary.md#g-混淆矩阵) |
    | [精确率](../appendix/e-glossary.md#g-精确率) | 机器学习与评价 | [混淆矩阵](../appendix/e-glossary.md#g-混淆矩阵) |
    | [召回率](../appendix/e-glossary.md#g-召回率) | 机器学习与评价 | [混淆矩阵](../appendix/e-glossary.md#g-混淆矩阵) |
    | [F1 值](../appendix/e-glossary.md#g-F1-值) | 机器学习与评价 | [精确率](../appendix/e-glossary.md#g-精确率)、[召回率](../appendix/e-glossary.md#g-召回率) |
    | [交叉验证](../appendix/e-glossary.md#g-交叉验证) | 机器学习与评价 | [测试集](../appendix/e-glossary.md#g-测试集) |
    | [类别不平衡](../appendix/e-glossary.md#g-类别不平衡) | 机器学习与评价 | [准确率](../appendix/e-glossary.md#g-准确率) |
    | [情感分析](../appendix/e-glossary.md#g-情感分析) | 应用系统 | [文本分类](../appendix/e-glossary.md#g-文本分类) |
    | [情感词典](../appendix/e-glossary.md#g-情感词典) | 应用系统 | [情感分析](../appendix/e-glossary.md#g-情感分析) |
    | [方面级情感分析](../appendix/e-glossary.md#g-方面级情感分析) | 应用系统 | [情感分析](../appendix/e-glossary.md#g-情感分析) |
    | [零样本学习](../appendix/e-glossary.md#g-零样本学习) | Transformer 与大模型 | [大语言模型](../appendix/e-glossary.md#g-大语言模型)、[文本分类](../appendix/e-glossary.md#g-文本分类) |

??? note "第 7 章 信息抽取（11 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [信息抽取](../appendix/e-glossary.md#g-信息抽取) | 应用系统 | [自然语言理解](../appendix/e-glossary.md#g-自然语言理解) |
    | [命名实体识别](../appendix/e-glossary.md#g-命名实体识别) | 应用系统 | [信息抽取](../appendix/e-glossary.md#g-信息抽取) |
    | [序列标注](../appendix/e-glossary.md#g-序列标注) | 机器学习与评价 | [词性标注](../appendix/e-glossary.md#g-词性标注) |
    | [BIO 标注](../appendix/e-glossary.md#g-BIO-标注) | 机器学习与评价 | [序列标注](../appendix/e-glossary.md#g-序列标注)、[命名实体识别](../appendix/e-glossary.md#g-命名实体识别) |
    | [条件随机场](../appendix/e-glossary.md#g-条件随机场) | 机器学习与评价 | [序列标注](../appendix/e-glossary.md#g-序列标注)、[隐马尔可夫模型](../appendix/e-glossary.md#g-隐马尔可夫模型) |
    | [实体链接](../appendix/e-glossary.md#g-实体链接) | 应用系统 | [命名实体识别](../appendix/e-glossary.md#g-命名实体识别) |
    | [关系抽取](../appendix/e-glossary.md#g-关系抽取) | 应用系统 | [命名实体识别](../appendix/e-glossary.md#g-命名实体识别)、[依存关系](../appendix/e-glossary.md#g-依存关系) |
    | [三元组](../appendix/e-glossary.md#g-三元组) | 应用系统 | [关系抽取](../appendix/e-glossary.md#g-关系抽取) |
    | [事件抽取](../appendix/e-glossary.md#g-事件抽取) | 应用系统 | [关系抽取](../appendix/e-glossary.md#g-关系抽取) |
    | [知识图谱](../appendix/e-glossary.md#g-知识图谱) | 应用系统 | [三元组](../appendix/e-glossary.md#g-三元组)、[实体链接](../appendix/e-glossary.md#g-实体链接) |
    | [数据标注](../appendix/e-glossary.md#g-数据标注) | 机器学习与评价 | [监督学习](../appendix/e-glossary.md#g-监督学习) |

??? note "第 8 章 深度学习基础（20 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [深度学习](../appendix/e-glossary.md#g-深度学习) | 神经网络 | [监督学习](../appendix/e-glossary.md#g-监督学习) |
    | [神经元](../appendix/e-glossary.md#g-神经元) | 神经网络 | [深度学习](../appendix/e-glossary.md#g-深度学习) |
    | [权重 / 偏置](../appendix/e-glossary.md#g-权重-偏置) | 神经网络 | [神经元](../appendix/e-glossary.md#g-神经元) |
    | [感知机](../appendix/e-glossary.md#g-感知机) | 神经网络 | [神经元](../appendix/e-glossary.md#g-神经元) |
    | [线性不可分](../appendix/e-glossary.md#g-线性不可分) | 神经网络 | [感知机](../appendix/e-glossary.md#g-感知机) |
    | [多层感知机](../appendix/e-glossary.md#g-多层感知机) | 神经网络 | [感知机](../appendix/e-glossary.md#g-感知机)、[线性不可分](../appendix/e-glossary.md#g-线性不可分) |
    | [激活函数](../appendix/e-glossary.md#g-激活函数) | 神经网络 | [神经元](../appendix/e-glossary.md#g-神经元) |
    | [Softmax](../appendix/e-glossary.md#g-Softmax) | 神经网络 | [激活函数](../appendix/e-glossary.md#g-激活函数) |
    | [损失函数](../appendix/e-glossary.md#g-损失函数) | 神经网络 | [监督学习](../appendix/e-glossary.md#g-监督学习) |
    | [交叉熵](../appendix/e-glossary.md#g-交叉熵) | 神经网络 | [损失函数](../appendix/e-glossary.md#g-损失函数)、[Softmax](../appendix/e-glossary.md#g-Softmax) |
    | [梯度下降](../appendix/e-glossary.md#g-梯度下降) | 神经网络 | [损失函数](../appendix/e-glossary.md#g-损失函数) |
    | [学习率](../appendix/e-glossary.md#g-学习率) | 神经网络 | [梯度下降](../appendix/e-glossary.md#g-梯度下降) |
    | [反向传播](../appendix/e-glossary.md#g-反向传播) | 神经网络 | [梯度下降](../appendix/e-glossary.md#g-梯度下降)、[多层感知机](../appendix/e-glossary.md#g-多层感知机) |
    | [过拟合](../appendix/e-glossary.md#g-过拟合) | 机器学习与评价 | [训练集](../appendix/e-glossary.md#g-训练集) |
    | [词嵌入层](../appendix/e-glossary.md#g-词嵌入层) | 神经网络 | [词向量 / 词嵌入](../appendix/e-glossary.md#g-词向量-词嵌入)、[深度学习](../appendix/e-glossary.md#g-深度学习) |
    | [循环神经网络](../appendix/e-glossary.md#g-循环神经网络) | 神经网络 | [多层感知机](../appendix/e-glossary.md#g-多层感知机)、[词嵌入层](../appendix/e-glossary.md#g-词嵌入层) |
    | [隐藏状态](../appendix/e-glossary.md#g-隐藏状态) | 神经网络 | [循环神经网络](../appendix/e-glossary.md#g-循环神经网络) |
    | [梯度消失 / 梯度爆炸](../appendix/e-glossary.md#g-梯度消失-梯度爆炸) | 神经网络 | [反向传播](../appendix/e-glossary.md#g-反向传播)、[循环神经网络](../appendix/e-glossary.md#g-循环神经网络) |
    | [长短期记忆网络](../appendix/e-glossary.md#g-长短期记忆网络) | 神经网络 | [梯度消失 / 梯度爆炸](../appendix/e-glossary.md#g-梯度消失-梯度爆炸) |
    | [门控循环单元](../appendix/e-glossary.md#g-门控循环单元) | 神经网络 | [长短期记忆网络](../appendix/e-glossary.md#g-长短期记忆网络) |

??? note "第 9 章 Transformer 与大模型（23 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [注意力机制](../appendix/e-glossary.md#g-注意力机制) | Transformer 与大模型 | [循环神经网络](../appendix/e-glossary.md#g-循环神经网络)、[Softmax](../appendix/e-glossary.md#g-Softmax) |
    | [自注意力](../appendix/e-glossary.md#g-自注意力) | Transformer 与大模型 | [注意力机制](../appendix/e-glossary.md#g-注意力机制) |
    | [查询 / 键 / 值](../appendix/e-glossary.md#g-查询-键-值) | Transformer 与大模型 | [自注意力](../appendix/e-glossary.md#g-自注意力) |
    | [多头注意力](../appendix/e-glossary.md#g-多头注意力) | Transformer 与大模型 | [查询 / 键 / 值](../appendix/e-glossary.md#g-查询-键-值) |
    | [位置编码](../appendix/e-glossary.md#g-位置编码) | Transformer 与大模型 | [自注意力](../appendix/e-glossary.md#g-自注意力) |
    | [残差连接](../appendix/e-glossary.md#g-残差连接) | Transformer 与大模型 | [多层感知机](../appendix/e-glossary.md#g-多层感知机) |
    | [层归一化](../appendix/e-glossary.md#g-层归一化) | Transformer 与大模型 | [多层感知机](../appendix/e-glossary.md#g-多层感知机) |
    | [Transformer](../appendix/e-glossary.md#g-Transformer) | Transformer 与大模型 | [多头注意力](../appendix/e-glossary.md#g-多头注意力)、[位置编码](../appendix/e-glossary.md#g-位置编码)、[残差连接](../appendix/e-glossary.md#g-残差连接)、[层归一化](../appendix/e-glossary.md#g-层归一化) |
    | [编码器 / 解码器](../appendix/e-glossary.md#g-编码器-解码器) | Transformer 与大模型 | [Transformer](../appendix/e-glossary.md#g-Transformer) |
    | [因果掩码](../appendix/e-glossary.md#g-因果掩码) | Transformer 与大模型 | [自注意力](../appendix/e-glossary.md#g-自注意力) |
    | [预训练](../appendix/e-glossary.md#g-预训练) | Transformer 与大模型 | [自监督学习](../appendix/e-glossary.md#g-自监督学习)、[Transformer](../appendix/e-glossary.md#g-Transformer) |
    | [微调](../appendix/e-glossary.md#g-微调) | Transformer 与大模型 | [预训练](../appendix/e-glossary.md#g-预训练) |
    | [掩码语言模型](../appendix/e-glossary.md#g-掩码语言模型) | Transformer 与大模型 | [预训练](../appendix/e-glossary.md#g-预训练) |
    | [BERT](../appendix/e-glossary.md#g-BERT) | Transformer 与大模型 | [掩码语言模型](../appendix/e-glossary.md#g-掩码语言模型)、[编码器 / 解码器](../appendix/e-glossary.md#g-编码器-解码器) |
    | [GPT](../appendix/e-glossary.md#g-GPT) | Transformer 与大模型 | [预训练](../appendix/e-glossary.md#g-预训练)、[因果掩码](../appendix/e-glossary.md#g-因果掩码) |
    | [指令微调](../appendix/e-glossary.md#g-指令微调) | Transformer 与大模型 | [微调](../appendix/e-glossary.md#g-微调)、[GPT](../appendix/e-glossary.md#g-GPT) |
    | [人类反馈强化学习](../appendix/e-glossary.md#g-人类反馈强化学习) | Transformer 与大模型 | [指令微调](../appendix/e-glossary.md#g-指令微调) |
    | [规模定律](../appendix/e-glossary.md#g-规模定律) | Transformer 与大模型 | [GPT](../appendix/e-glossary.md#g-GPT) |
    | [涌现能力](../appendix/e-glossary.md#g-涌现能力) | Transformer 与大模型 | [规模定律](../appendix/e-glossary.md#g-规模定律) |
    | [混合专家模型](../appendix/e-glossary.md#g-混合专家模型) | Transformer 与大模型 | [Transformer](../appendix/e-glossary.md#g-Transformer) |
    | [幻觉](../appendix/e-glossary.md#g-幻觉) | 生成与解码 | [GPT](../appendix/e-glossary.md#g-GPT) |
    | [参数高效微调](../appendix/e-glossary.md#g-参数高效微调) | Transformer 与大模型 | [微调](../appendix/e-glossary.md#g-微调) |
    | [低秩适配](../appendix/e-glossary.md#g-低秩适配) | Transformer 与大模型 | [参数高效微调](../appendix/e-glossary.md#g-参数高效微调) |

??? note "第 10 章 机器翻译与文本生成（18 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [机器翻译](../appendix/e-glossary.md#g-机器翻译) | 应用系统 | [自然语言生成](../appendix/e-glossary.md#g-自然语言生成) |
    | [平行语料](../appendix/e-glossary.md#g-平行语料) | 应用系统 | [机器翻译](../appendix/e-glossary.md#g-机器翻译)、[语料库](../appendix/e-glossary.md#g-语料库) |
    | [统计机器翻译](../appendix/e-glossary.md#g-统计机器翻译) | 应用系统 | [平行语料](../appendix/e-glossary.md#g-平行语料)、[N 元语法](../appendix/e-glossary.md#g-N-元语法) |
    | [序列到序列模型](../appendix/e-glossary.md#g-序列到序列模型) | 生成与解码 | [循环神经网络](../appendix/e-glossary.md#g-循环神经网络)、[编码器 / 解码器](../appendix/e-glossary.md#g-编码器-解码器) |
    | [神经机器翻译](../appendix/e-glossary.md#g-神经机器翻译) | 应用系统 | [统计机器翻译](../appendix/e-glossary.md#g-统计机器翻译)、[序列到序列模型](../appendix/e-glossary.md#g-序列到序列模型) |
    | [BLEU](../appendix/e-glossary.md#g-BLEU) | 机器学习与评价 | [机器翻译](../appendix/e-glossary.md#g-机器翻译)、[N 元语法](../appendix/e-glossary.md#g-N-元语法) |
    | [简短惩罚](../appendix/e-glossary.md#g-简短惩罚) | 机器学习与评价 | [BLEU](../appendix/e-glossary.md#g-BLEU) |
    | [文本生成](../appendix/e-glossary.md#g-文本生成) | 生成与解码 | [自然语言生成](../appendix/e-glossary.md#g-自然语言生成) |
    | [自回归生成](../appendix/e-glossary.md#g-自回归生成) | 生成与解码 | [文本生成](../appendix/e-glossary.md#g-文本生成)、[GPT](../appendix/e-glossary.md#g-GPT) |
    | [解码策略](../appendix/e-glossary.md#g-解码策略) | 生成与解码 | [自回归生成](../appendix/e-glossary.md#g-自回归生成)、[Softmax](../appendix/e-glossary.md#g-Softmax) |
    | [贪心搜索](../appendix/e-glossary.md#g-贪心搜索) | 生成与解码 | [解码策略](../appendix/e-glossary.md#g-解码策略) |
    | [束搜索](../appendix/e-glossary.md#g-束搜索) | 生成与解码 | [贪心搜索](../appendix/e-glossary.md#g-贪心搜索) |
    | [温度](../appendix/e-glossary.md#g-温度) | 生成与解码 | [解码策略](../appendix/e-glossary.md#g-解码策略) |
    | [Top-k / Top-p 采样](../appendix/e-glossary.md#g-Top-k-Top-p-采样) | 生成与解码 | [温度](../appendix/e-glossary.md#g-温度) |
    | [文本摘要](../appendix/e-glossary.md#g-文本摘要) | 应用系统 | [文本生成](../appendix/e-glossary.md#g-文本生成) |
    | [TextRank](../appendix/e-glossary.md#g-TextRank) | 应用系统 | [文本摘要](../appendix/e-glossary.md#g-文本摘要)、[余弦相似度](../appendix/e-glossary.md#g-余弦相似度) |
    | [ROUGE](../appendix/e-glossary.md#g-ROUGE) | 机器学习与评价 | [文本摘要](../appendix/e-glossary.md#g-文本摘要)、[BLEU](../appendix/e-glossary.md#g-BLEU) |
    | [深度合成](../appendix/e-glossary.md#g-深度合成) | 安全与伦理 | [文本生成](../appendix/e-glossary.md#g-文本生成) |

??? note "第 11 章 问答、RAG 与智能体（20 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [问答系统](../appendix/e-glossary.md#g-问答系统) | 应用系统 | [自然语言理解](../appendix/e-glossary.md#g-自然语言理解) |
    | [FAQ 问答](../appendix/e-glossary.md#g-FAQ-问答) | 应用系统 | [问答系统](../appendix/e-glossary.md#g-问答系统)、[余弦相似度](../appendix/e-glossary.md#g-余弦相似度) |
    | [知识图谱问答](../appendix/e-glossary.md#g-知识图谱问答) | 应用系统 | [问答系统](../appendix/e-glossary.md#g-问答系统)、[知识图谱](../appendix/e-glossary.md#g-知识图谱) |
    | [机器阅读理解](../appendix/e-glossary.md#g-机器阅读理解) | 应用系统 | [问答系统](../appendix/e-glossary.md#g-问答系统)、[BERT](../appendix/e-glossary.md#g-BERT) |
    | [检索器 / 阅读器](../appendix/e-glossary.md#g-检索器-阅读器) | 应用系统 | [机器阅读理解](../appendix/e-glossary.md#g-机器阅读理解)、[BM25](../appendix/e-glossary.md#g-BM25) |
    | [提示词 / 提示工程](../appendix/e-glossary.md#g-提示词-提示工程) | Transformer 与大模型 | [大语言模型](../appendix/e-glossary.md#g-大语言模型) |
    | [系统提示](../appendix/e-glossary.md#g-系统提示) | Transformer 与大模型 | [提示词 / 提示工程](../appendix/e-glossary.md#g-提示词-提示工程) |
    | [零样本提示](../appendix/e-glossary.md#g-零样本提示) | Transformer 与大模型 | [提示词 / 提示工程](../appendix/e-glossary.md#g-提示词-提示工程)、[零样本学习](../appendix/e-glossary.md#g-零样本学习) |
    | [少样本提示](../appendix/e-glossary.md#g-少样本提示) | Transformer 与大模型 | [零样本提示](../appendix/e-glossary.md#g-零样本提示) |
    | [思维链](../appendix/e-glossary.md#g-思维链) | Transformer 与大模型 | [少样本提示](../appendix/e-glossary.md#g-少样本提示) |
    | [应用程序编程接口](../appendix/e-glossary.md#g-应用程序编程接口) | 应用系统 | [大语言模型](../appendix/e-glossary.md#g-大语言模型) |
    | [上下文长度](../appendix/e-glossary.md#g-上下文长度) | Transformer 与大模型 | [词元](../appendix/e-glossary.md#g-词元)、[自注意力](../appendix/e-glossary.md#g-自注意力) |
    | [检索增强生成](../appendix/e-glossary.md#g-检索增强生成) | 应用系统 | [检索器 / 阅读器](../appendix/e-glossary.md#g-检索器-阅读器)、[语义搜索](../appendix/e-glossary.md#g-语义搜索)、[提示词 / 提示工程](../appendix/e-glossary.md#g-提示词-提示工程)、[幻觉](../appendix/e-glossary.md#g-幻觉) |
    | [切块](../appendix/e-glossary.md#g-切块) | 应用系统 | [检索增强生成](../appendix/e-glossary.md#g-检索增强生成)、[上下文长度](../appendix/e-glossary.md#g-上下文长度) |
    | [向量检索](../appendix/e-glossary.md#g-向量检索) | 应用系统 | [文本嵌入](../appendix/e-glossary.md#g-文本嵌入)、[向量数据库](../appendix/e-glossary.md#g-向量数据库) |
    | [重排序](../appendix/e-glossary.md#g-重排序) | 应用系统 | [向量检索](../appendix/e-glossary.md#g-向量检索) |
    | [函数调用](../appendix/e-glossary.md#g-函数调用) | 应用系统 | [应用程序编程接口](../appendix/e-glossary.md#g-应用程序编程接口) |
    | [智能体](../appendix/e-glossary.md#g-智能体) | 应用系统 | [函数调用](../appendix/e-glossary.md#g-函数调用)、[提示词 / 提示工程](../appendix/e-glossary.md#g-提示词-提示工程) |
    | [ReAct](../appendix/e-glossary.md#g-ReAct) | 应用系统 | [智能体](../appendix/e-glossary.md#g-智能体)、[思维链](../appendix/e-glossary.md#g-思维链) |
    | [模型上下文协议](../appendix/e-glossary.md#g-模型上下文协议) | 应用系统 | [函数调用](../appendix/e-glossary.md#g-函数调用) |

??? note "第 12 章 伦理、安全与法律（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [人工智能伦理](../appendix/e-glossary.md#g-人工智能伦理) | 安全与伦理 | [大语言模型](../appendix/e-glossary.md#g-大语言模型) |
    | [偏见](../appendix/e-glossary.md#g-偏见) | 安全与伦理 | [人工智能伦理](../appendix/e-glossary.md#g-人工智能伦理)、[词向量 / 词嵌入](../appendix/e-glossary.md#g-词向量-词嵌入) |
    | [反事实测试](../appendix/e-glossary.md#g-反事实测试) | 安全与伦理 | [偏见](../appendix/e-glossary.md#g-偏见) |
    | [个人信息](../appendix/e-glossary.md#g-个人信息) | 安全与伦理 | [人工智能伦理](../appendix/e-glossary.md#g-人工智能伦理) |
    | [敏感个人信息](../appendix/e-glossary.md#g-敏感个人信息) | 安全与伦理 | [个人信息](../appendix/e-glossary.md#g-个人信息) |
    | [去标识化](../appendix/e-glossary.md#g-去标识化) | 安全与伦理 | [个人信息](../appendix/e-glossary.md#g-个人信息) |
    | [匿名化](../appendix/e-glossary.md#g-匿名化) | 安全与伦理 | [去标识化](../appendix/e-glossary.md#g-去标识化) |
    | [数据脱敏](../appendix/e-glossary.md#g-数据脱敏) | 安全与伦理 | [个人信息](../appendix/e-glossary.md#g-个人信息)、[正则表达式](../appendix/e-glossary.md#g-正则表达式)、[命名实体识别](../appendix/e-glossary.md#g-命名实体识别) |
    | [越狱](../appendix/e-glossary.md#g-越狱) | 安全与伦理 | [系统提示](../appendix/e-glossary.md#g-系统提示) |
    | [提示注入](../appendix/e-glossary.md#g-提示注入) | 安全与伦理 | [系统提示](../appendix/e-glossary.md#g-系统提示)、[智能体](../appendix/e-glossary.md#g-智能体) |
    | [纵深防御](../appendix/e-glossary.md#g-纵深防御) | 安全与伦理 | [提示注入](../appendix/e-glossary.md#g-提示注入) |
    | [最小权限原则](../appendix/e-glossary.md#g-最小权限原则) | 安全与伦理 | [纵深防御](../appendix/e-glossary.md#g-纵深防御)、[函数调用](../appendix/e-glossary.md#g-函数调用) |
    | [红队测试](../appendix/e-glossary.md#g-红队测试) | 安全与伦理 | [越狱](../appendix/e-glossary.md#g-越狱) |
    | [内容标识](../appendix/e-glossary.md#g-内容标识) | 安全与伦理 | [深度合成](../appendix/e-glossary.md#g-深度合成) |
