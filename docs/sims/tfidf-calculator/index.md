---
title: TF-IDF 计算器
description: 修改小语料，实时计算 TF-IDF；拖动参数，看 BM25 的词频饱和与长度惩罚（第 5 章）
---

# TF-IDF 计算器

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="TF-IDF 计算器"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[5.4.2 计算方法](../../chapters/05-representation/index.md#542)、[5.4.4 从 TF-IDF 到 BM25](../../chapters/05-representation/index.md#544-tf-idf-bm25)

## 教学说明

**学习目标**

1. 能按公式算出一个词的 TF、IDF 和 TF-IDF（应用）；
2. 能解释“的”这类词 TF-IDF 低的原因（理解）；
3. 能说明 BM25 词频饱和与长度惩罚的作用（分析）。

**画面与操作**

- 上方 6 篇已分好词的短文可以直接编辑，单选按钮选择要分析的一篇。
- 表格按 TF-IDF 从高到低排列，黄色是前 3 个关键词。可以切换教材公式和 scikit-learn 的平滑公式。
- 下方曲线是 BM25 的词频得分（蓝线）与按比例增长（橙色虚线）的对比，红点是当前词频。

**数据来源**：6 篇短文由编者编写。BM25 部分的公式和参数与 5.4.4 节一致，k₁ = 1.2、b = 0.75、长度等于平均时，tf = 1、2、5、10 的得分与教材表格一致。

**课堂用法建议**

1. 让学生在文章 2 里把“好吃”重复三遍，观察 TF-IDF 的变化。
2. 把 b 拖到 0，再改变文章长度，说明长度惩罚的作用。
