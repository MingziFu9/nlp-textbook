# 实验数据说明

| 文件 | 内容 | 规模 | 来源 | 使用章节 |
|---|---|---|---|---|
| `waimai_10k.csv` | 外卖平台用户评论，`label` 为 1 表示正面、0 表示负面 | 11987 条（正面 4000，负面 7987） | ChineseNlpCorpus 项目（github.com/SophonPlus/ChineseNlpCorpus） | 第 2、3、6、8、9、10、12 章 |
| `online_shopping_10_cats.zip` | 10 类商品的网购评论，字段为 `cat`（类别）、`label`、`review` | 62773 条 | ChineseNlpCorpus 项目 | 第 2、5、6、8 章 |
| `cn_stopwords.txt` | 中文停用词表 | 746 个词 | goto456/stopwords 项目（github.com/goto456/stopwords） | 第 2、3、5、10、11 章 |
| `reviews_raw.csv` | 含有噪声（网址、表情、繁体字、重复、空白等）的评论，用于练习清洗 | 306 条 | 由 `make_noisy_reviews.py` 从 `waimai_10k.csv` 生成 | 第 2 章 |
| `news_samples.csv` | 8 条短新闻，类别为科技、体育、财经、教育 | 8 条 | 教材编写，内容为虚构 | 第 5 章 |

各章目录中还有本章专用的数据文件，均为教材编写的虚构材料：

| 文件 | 内容 | 章节 |
|---|---|---|
| `ch07/news_ner.txt`、`ch07/relations_sample.json` | 虚构的企业新闻及编者整理的关系三元组 | 第 7 章 |
| `ch09/school_qa.json` | 30 条关于虚构的“星海职业学院”的问答 | 第 9 章 |
| `ch10/article.txt`、`ch10/reference_summary.txt` | 介绍智能客服的短文及参考摘要 | 第 10 章 |
| `ch11/student_handbook.md` | 虚构的《星海职业学院学生手册（节选）》，12 章 | 第 11 章 |
| `ch12/records.txt` | 4 条虚构的客服工单，身份证号使用不存在的地区码 99 | 第 12 章 |

**使用说明**：公开数据集仅用于教学和研究，请遵守原项目的许可说明，不得用于商业用途。虚构材料中出现的人名、机构、电话、证件号码均不对应真实的人和机构。
