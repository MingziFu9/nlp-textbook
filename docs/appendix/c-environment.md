---
title: 附录 C 实验环境、模型与数据说明
description: 实验环境的软硬件要求、安装与镜像配置、所用模型清单、数据集说明，以及需要联网的实验清单和教师准备建议
---

# 附录 C 实验环境、模型与数据说明

## C.1 软硬件要求

| 项目 | 最低要求 | 推荐配置 |
|---|---|---|
| 操作系统 | Windows 10 / macOS 12 / 主流 Linux | Windows 11 / macOS 14 及以上 |
| 内存 | 8GB | 16GB（实验 9-3、10-3 运行本地大模型时需要） |
| 硬盘可用空间 | 10GB | 20GB 以上（存放模型文件） |
| 显卡 | 不需要 | 有 NVIDIA 显卡可以加快第 8、9 章的训练，但不是必需的 |
| Python | 3.10 – 3.12 | 3.11（教材编写时使用 3.11.17） |
| 网络 | 能访问国内网站 | 能访问 Hugging Face 镜像站、魔搭社区和大模型 API |

!!! warning "关于 Python 版本"
    请不要使用刚发布的最新 Python 版本。部分库（如 jieba）在最新版本的 Python 上可能安装失败。如果已经安装了较新的版本，可以用 Anaconda 或 uv 另外创建一个 Python 3.11 的环境：
    `conda create -n nlp python=3.11` 或 `uv venv -p 3.11`。

本书全部实验都可以在 CPU 上完成。没有合适电脑的同学，可以使用**魔搭社区**提供的免费在线 Notebook 环境（modelscope.cn，登录后进入“我的 Notebook”），它预装了常用的深度学习库，下载国内模型速度快，还提供一定时长的免费 GPU。

## C.2 安装工具库

配套资源的 `labs/requirements.txt` 中列出了教材编写时实测通过的各库版本。推荐使用清华大学的 PyPI 镜像安装：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

也可以按章节逐步安装，各实验的“实验环境”中写明了需要额外安装的库。

| 库 | 教材编写时的版本 | 首次用到的章节 |
|---|---|---|
| jieba | 0.42.1 | 第 1 章 |
| nltk | 3.10.4 | 第 1 章 |
| spacy | 3.8.16 | 第 1 章 |
| scikit-learn | 1.9.1 | 第 1 章 |
| torch | 2.14.1 | 第 1 章 |
| transformers | 5.20.2 | 第 1 章 |
| pandas / numpy / matplotlib | 3.1.0 / 2.4.6 / 3.11.2 | 第 2 章 |
| opencc | 1.4.2 | 第 2 章 |
| openai | 3.36.1 | 第 2 章 |
| wordcloud | 1.9.6 | 第 3 章 |
| dashscope | 2.0.1 | 第 3 章 |
| gensim | 4.4.0 | 第 5 章 |
| sentence-transformers | 6.2.0 | 第 5 章 |
| gradio | 6.30.0 | 第 6 章 |
| networkx | 3.6.1 | 第 7 章 |
| datasets / accelerate / peft | 5.1.0 / – / 0.21.2 | 第 9 章 |

各库更新很快。如果你安装的版本更新，绝大多数代码可以直接运行；遇到接口变化导致的报错，可以查看该库的更新说明，或者安装与上表相同的版本，例如 `pip install transformers==5.20.2`。

**spaCy 模型与 NLTK 数据包**：

```bash
python -m spacy download zh_core_web_sm
python -m spacy download en_core_web_sm
python -c "import nltk; [nltk.download(p) for p in ['punkt_tab','averaged_perceptron_tagger_eng','vader_lexicon','stopwords','wordnet']]"
```

spaCy 模型从 GitHub 下载，网络不稳定时容易失败。教师可以提前下载模型的 `.whl` 安装文件，学生用 `pip install 文件名.whl` 离线安装。NLTK 数据包下载失败时，可以由教师下载 `nltk_data` 文件夹后拷贝到学生电脑的用户目录下。

## C.3 预训练模型的下载

### 设置 Hugging Face 镜像

```bash
# Windows（Anaconda Prompt 或 cmd）
set HF_ENDPOINT=https://hf-mirror.com
# Windows（PowerShell）
$env:HF_ENDPOINT = "https://hf-mirror.com"
# macOS / Linux
export HF_ENDPOINT=https://hf-mirror.com
```

设置后，**在同一个命令行窗口中**运行 Python 程序或启动 Jupyter，模型就会从镜像站下载。模型下载后保存在本机的缓存目录中（默认为用户目录下的 `.cache/huggingface`），以后再用就不需要重新下载。

也可以先用命令行把模型下载到指定文件夹，再在代码中把模型名称换成文件夹路径：

```bash
hf download BAAI/bge-small-zh-v1.5 --local-dir ./models/bge-small-zh
```

### 从魔搭社区下载

主流国产模型在魔搭社区都有官方发布，国内下载速度快：

```bash
pip install modelscope
modelscope download --model Qwen/Qwen3-0.6B --local_dir ./models/Qwen3-0.6B
```

### 本书使用的模型

| 模型 | 用途 | 大小（约） | 章节 |
|---|---|---|---|
| `zh_core_web_sm` / `en_core_web_sm` | spaCy 中、英文流水线 | 50MB / 15MB | 第 1–4、7、12 章 |
| `google-bert/bert-base-chinese` | 中文 BERT，完形填空 | 400MB | 第 9、12 章 |
| `uer/roberta-base-finetuned-jd-binary-chinese` | 中文情感分类 | 400MB | 第 1、9 章 |
| `uer/roberta-base-finetuned-cluener2020-chinese` | 中文命名实体识别 | 400MB | 第 7 章 |
| `hfl/rbt3` | 3 层中文 RoBERTa，用于微调 | 150MB | 第 9 章 |
| `BAAI/bge-small-zh-v1.5` | 中文文本嵌入 | 100MB | 第 5、11 章 |
| `Helsinki-NLP/opus-mt-zh-en` | 中译英翻译 | 300MB | 第 10 章 |
| `Qwen/Qwen3-0.6B` | 小型开源大模型，LoRA 微调 | 1GB 多 | 第 9 章 |
| `qwen3:1.7b`（Ollama） | 本地运行的量化大模型 | 1.4GB | 第 10 章 |

!!! tip "给教师的建议"
    开课前，教师可以在一台能联网的电脑上把上表中的模型全部下载好，复制到 U 盘或校内共享文件夹中。学生把模型文件夹拷贝到本机，在代码中用文件夹路径代替模型名称即可，例如 `pipeline("fill-mask", model="D:/models/bert-base-chinese")`。这样上课时不再依赖网络。

## C.4 数据集

本书使用的数据集放在配套资源的 `labs/data/` 目录中，详细说明见该目录下的 `README.md`。

| 文件 | 内容 | 规模 | 来源 |
|---|---|---|---|
| `waimai_10k.csv` | 外卖评论情感数据 | 11987 条 | ChineseNlpCorpus 开源项目 |
| `online_shopping_10_cats.zip` | 10 类商品网购评论 | 62773 条 | ChineseNlpCorpus 开源项目 |
| `cn_stopwords.txt` | 中文停用词表 | 746 个词 | goto456/stopwords 开源项目 |
| `reviews_raw.csv` | 含噪声的评论，用于清洗练习 | 306 条 | 由脚本从外卖评论生成 |
| `news_samples.csv` | 短新闻样例 | 8 条 | 教材编写（虚构） |

各章目录中还有本章专用的虚构材料，如第 7 章的企业新闻、第 9 章的校园问答、第 11 章的学生手册、第 12 章的客服工单。这些材料中的人名、机构、电话、证件号码均为虚构。

公开数据集仅用于教学和研究，请遵守原项目的许可说明。

## C.5 需要联网的实验

为了保证实验结果真实可信，本书中每个实验的运行结果都是编者在实验环境中实际运行得到的。由于编写环境的网络限制，部分需要下载模型或调用在线服务的实验内容无法实际运行，在书中以“**待实测**”标出，没有给出运行结果，并提供了记录表供学生填写。这些内容的代码都经过了检查：能离线验证的部分（如数据处理、评价指标、训练流程）已用离线方式运行过。

| 实验 | 需要联网的内容 | 需要的资源 |
|---|---|---|
| 实验 1-2 | Transformers 部分 | 下载中文情感分类模型 |
| 实验 2-3 | 大模型辅助清洗 | 大模型 API |
| 实验 4-3 | 大模型句法分析 | 大模型 API |
| 实验 5-3 | 嵌入模型语义搜索 | 下载 BGE 模型 |
| 实验 6-3 | 大模型零样本分类 | 大模型 API |
| 实验 7-2 | Transformers 中文 NER | 下载 NER 模型 |
| 实验 7-3 | 大模型结构化抽取 | 大模型 API |
| 实验 9-2 | 完形填空、情感模型、微调 | 下载 3 个模型 |
| 实验 9-3 | LoRA 微调 | 下载 Qwen3-0.6B |
| 实验 10-1 | 翻译模型与大模型翻译 | 下载翻译模型、大模型 API |
| 实验 10-2 | 大模型生成式摘要 | 大模型 API |
| 实验 10-3 | Ollama 本地部署 | 下载 Ollama 及模型 |
| 实验 11-1 | 全部 | 大模型 API |
| 实验 11-2 | 大模型生成、向量检索 | 大模型 API、下载 BGE 模型 |
| 实验 11-3 | 低代码平台、函数调用 | 在线平台账号、大模型 API |
| 实验 12-2 | 第 4 部分完形填空探测 | 下载 BERT 模型 |
| 实验 12-3 | 第 2 部分攻防测试 | 大模型 API |

**教师可以在开课前完成这些实验的实测**，把运行结果补充到讲义中，并根据实际情况调整实验要求。

## C.6 课时安排建议

本书共 12 章、36 个实验，课程大纲规定实验 12 学时。教师可以根据学生基础、机房条件和网络条件，从每章中选择 1–2 个实验在课内完成，其余作为课后练习或拓展项目。下表给出一种参考方案（每个实验约 1 学时）：

| 章节 | 课内实验（建议） | 课后或拓展 |
|---|---|---|
| 第 1 章 | 1-1 搭建环境 | 1-2、1-3 |
| 第 2 章 | 2-1 正则与编码 | 2-2、2-3 |
| 第 3 章 | 3-2 jieba 与 spaCy | 3-1、3-3 |
| 第 4 章 | 4-2 依存句法 | 4-1、4-3 |
| 第 5 章 | 5-2 Word2Vec | 5-1、5-3 |
| 第 6 章 | 6-2 情感分类与评估 | 6-1、6-3 |
| 第 7 章 | 7-1 BIO 与规则抽取 | 7-2、7-3 |
| 第 8 章 | 8-2 LSTM 情感分类 | 8-1、8-3 |
| 第 9 章 | 9-1 手算注意力 | 9-2、9-3 |
| 第 10 章 | 10-2 TextRank 摘要 | 10-1、10-3 |
| 第 11 章 | 11-2 RAG 问答系统 | 11-1、11-3 |
| 第 12 章 | 12-1 个人信息脱敏 | 12-2、12-3 |

如果机房网络和 API 额度允许，建议把第 9–11 章的课内实验换成 9-2、11-1 等需要使用预训练模型和大模型的实验，让学生体验最新的技术。
