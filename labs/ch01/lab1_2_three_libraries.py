# ===== 第 1 部分：NLTK 处理英文 =====
import nltk
sentence = "Natural language processing makes computers understand human language."
words = nltk.word_tokenize(sentence)          # 分词
print("NLTK 分词：", words)
print("NLTK 词性：", nltk.pos_tag(words))      # 词性标注

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
print("NLTK 情感：", sia.polarity_scores("I really love this course!"))

# ===== 第 2 部分：spaCy 处理中文 =====
import spacy
nlp = spacy.load("zh_core_web_sm")
doc = nlp("国家统计局今天在北京发布了最新的经济数据。")
for token in doc:
    print(f"{token.text}\t{token.pos_}")
print("spaCy 实体：", [(ent.text, ent.label_) for ent in doc.ents])

# ===== 第 3 部分：Transformers 中文情感分析 =====
from transformers import pipeline
classifier = pipeline("sentiment-analysis",
                      model="uer/roberta-base-finetuned-jd-binary-chinese")
reviews = ["这款手机拍照效果太棒了，电池也很耐用！",
           "物流太慢了，包装还破了，非常失望。"]
for r in reviews:
    print(r, "→", classifier(r))
