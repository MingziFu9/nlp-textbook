---
title: 附录 B NLP 工具库接口速查
description: jieba、NLTK、spaCy、scikit-learn、gensim、PyTorch、Transformers、OpenAI SDK 常用接口速查
---

# 附录 B NLP 工具库接口速查

本附录列出本书实验中用到的各工具库的常用接口。更多用法请查阅各库的官方文档。

## B.1 jieba（中文分词）

```python
import jieba
import jieba.posseg as pseg
import jieba.analyse

jieba.lcut("我来到北京清华大学")              # 精确模式 -> ['我', '来到', '北京', '清华大学']
jieba.lcut("我来到北京清华大学", cut_all=True)   # 全模式：列出所有可能的词
jieba.lcut_for_search("我来到北京清华大学")    # 搜索引擎模式：对长词再切分
jieba.add_word("大语言模型")                   # 临时添加一个词
jieba.load_userdict("userdict.txt")            # 加载用户词典（每行：词 [词频] [词性]）
jieba.setLogLevel("WARN")                      # 不显示加载提示
[(w, f) for w, f in pseg.lcut("小王在杭州工作")]   # 词性标注：nr 人名、ns 地名、v 动词……
jieba.analyse.extract_tags(text, topK=10)      # 基于 TF-IDF 提取关键词
jieba.analyse.textrank(text, topK=10)          # 基于 TextRank 提取关键词
```

## B.2 NLTK（英文处理）

```python
import nltk
nltk.download("punkt_tab"); nltk.download("stopwords"); nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")   # 首次使用前下载数据包

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

sent_tokenize("Hello world. How are you?")      # 分句
word_tokenize("I can't wait!")                  # 分词 -> ['I', 'ca', "n't", 'wait', '!']
nltk.pos_tag(["I", "love", "NLP"])              # 词性标注
stopwords.words("english")                      # 英文停用词表
PorterStemmer().stem("running")                 # 词干提取 -> 'run'
WordNetLemmatizer().lemmatize("better", pos="a")    # 词形还原 -> 'good'
nltk.FreqDist(tokens).most_common(10)           # 词频统计
list(nltk.ngrams(tokens, 2))                    # 生成二元组
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu   # BLEU 评价（第 10 章）
```

## B.3 spaCy（工业级 NLP 流水线）

```python
import spacy
from spacy import displacy
nlp = spacy.load("zh_core_web_sm")      # 中文模型；英文用 en_core_web_sm
doc = nlp("小王在杭州的星海科技工作。")

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)   # 词、词性、依存关系、中心词
[(ent.text, ent.label_) for ent in doc.ents]     # 命名实体
[sent.text for sent in doc.sents]                # 分句
token.lemma_                                     # 词形还原（英文）
displacy.render(doc, style="dep")                # 依存句法可视化（style="ent" 显示实体）
nlp.pipe_names                                   # 查看流水线中的组件
```

安装模型：`python -m spacy download zh_core_web_sm`（下载失败时见附录 C）。

## B.4 scikit-learn（传统机器学习）

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics.pairwise import cosine_similarity

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42, stratify=y)
vec = TfidfVectorizer(tokenizer=jieba.lcut, token_pattern=None, ngram_range=(1, 2), min_df=2)
Xtr = vec.fit_transform(X_train)     # 只在训练集上 fit
Xte = vec.transform(X_test)          # 测试集只 transform
model = LogisticRegression(max_iter=1000).fit(Xtr, y_train)
pred = model.predict(Xte)
model.predict_proba(Xte)             # 各类别的概率
print(classification_report(y_test, pred, digits=4))
vec.get_feature_names_out()          # 词表

import joblib
joblib.dump(model, "model.joblib"); model = joblib.load("model.joblib")   # 保存 / 加载模型
```

## B.5 gensim（词向量）

```python
from gensim.models import Word2Vec
model = Word2Vec(sentences, vector_size=100, window=5, min_count=2, sg=1, seed=42, workers=4)
model.wv["好吃"]                          # 词向量
model.wv.most_similar("好吃", topn=5)     # 最相似的词
model.wv.similarity("好吃", "美味")        # 两个词的相似度
model.wv.most_similar(positive=["国王", "女人"], negative=["男人"])   # 词向量类比
model.save("w2v.model"); model = Word2Vec.load("w2v.model")
```

## B.6 PyTorch（深度学习）

```python
import torch
import torch.nn as nn

x = torch.tensor([[1.0, 2.0]]); x.shape        # 张量与形状
torch.zeros(2, 3, dtype=torch.long)            # 整数张量（词编号必须是 long）
nn.Embedding(vocab_size, 128, padding_idx=0)   # 词嵌入层
nn.LSTM(128, 128, batch_first=True, bidirectional=False, num_layers=1)
nn.Linear(128, 2); nn.Dropout(0.5)
nn.CrossEntropyLoss()                          # 分类损失（内部含 Softmax）
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 训练五步法
optimizer.zero_grad(); out = model(x); loss = loss_fn(out, y); loss.backward(); optimizer.step()

model.eval()                                   # 评估模式
with torch.no_grad(): pred = model(x).argmax(dim=1)
torch.manual_seed(42)                          # 固定随机种子
torch.save(model.state_dict(), "m.pt"); model.load_state_dict(torch.load("m.pt"))
device = "cuda" if torch.cuda.is_available() else "cpu"; model.to(device)
```

## B.7 Transformers（预训练模型）

```python
from transformers import pipeline, AutoTokenizer, AutoModel, AutoModelForSequenceClassification

# pipeline：一行完成一个任务
pipeline("text-classification", model="...")      # 文本分类 / 情感分析
pipeline("token-classification", model="...", aggregation_strategy="simple")   # NER
pipeline("fill-mask", model="google-bert/bert-base-chinese")   # 完形填空
pipeline("question-answering", model="...")        # 抽取式问答
pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")   # 翻译
pipeline("summarization", model="...")             # 摘要
pipeline("text-generation", model="...")           # 文本生成

# Auto 类：自己控制每一步
tokenizer = AutoTokenizer.from_pretrained("hfl/rbt3")
inputs = tokenizer(["今天天气真好"], padding=True, truncation=True, max_length=64, return_tensors="pt")
tokenizer.tokenize("自然语言处理")                     # 查看切分结果
model = AutoModelForSequenceClassification.from_pretrained("hfl/rbt3", num_labels=2)
outputs = model(**inputs); outputs.logits

# 对话模型
messages = [{"role": "user", "content": "你好"}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
model.generate(**inputs, max_new_tokens=100, do_sample=True, temperature=0.7, top_p=0.9)
```

微调使用 `TrainingArguments` + `Trainer`（见实验 9-2），LoRA 使用 `peft` 库的 `LoraConfig` + `get_peft_model`（见实验 9-3）。

## B.8 sentence-transformers（文本嵌入）

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
vecs = model.encode(["句子一", "句子二"], normalize_embeddings=True)
vecs @ vecs.T                  # 归一化后，点积即余弦相似度
```

## B.9 OpenAI 兼容接口（调用大模型）

```python
import os
from openai import OpenAI
client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "system", "content": "你是……"},
              {"role": "user", "content": "……"}],
    temperature=0.3,                          # 随机性
    max_tokens=500,                           # 最大输出长度
    response_format={"type": "json_object"},  # JSON 模式（可选）
    tools=[...],                              # 函数调用（可选，见实验 11-3）
)
resp.choices[0].message.content               # 回答内容
resp.choices[0].message.tool_calls            # 工具调用请求
resp.usage.prompt_tokens, resp.usage.completion_tokens   # Token 用量

# 流式输出
for chunk in client.chat.completions.create(model="deepseek-chat", messages=messages, stream=True):
    print(chunk.choices[0].delta.content or "", end="")
```

## B.10 其他

| 库 | 用途 | 常用接口 | 章节 |
|---|---|---|---|
| `opencc` | 繁简转换 | `opencc.OpenCC("t2s").convert(text)` | 第 2 章 |
| `wordcloud` | 词云 | `WordCloud(font_path=..., ...).generate_from_frequencies(freq)` | 第 3 章 |
| `networkx` | 图与 PageRank | `nx.Graph()`、`add_edge`、`nx.pagerank`、`nx.draw` | 第 7、10 章 |
| `gradio` | 快速搭建网页演示 | `gr.Interface(fn, inputs, outputs).launch()` | 第 6 章 |
| `datasets` | 加载与处理数据集 | `Dataset.from_pandas(df)`、`.map(fn, batched=True)` | 第 9 章 |
| `peft` | 参数高效微调 | `LoraConfig`、`get_peft_model`、`print_trainable_parameters` | 第 9 章 |
