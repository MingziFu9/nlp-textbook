"""实验 2-2：NLTK 英文预处理流水线"""
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

text = ("Dr. Smith loves teaching NLP! His students were studying the newest "
        "language models in 2026. They're running experiments and the results "
        "are surprisingly better than last year's.")

# 步骤 1：分句
sentences = nltk.sent_tokenize(text)
print("① 分句：")
for i, s in enumerate(sentences, 1):
    print(f"   {i}. {s}")

# 步骤 2：分词
tokens = nltk.word_tokenize(text)
print("② 分词：", tokens)

# 步骤 3：转小写并去掉标点
tokens = [t.lower() for t in tokens if t not in string.punctuation]
print("③ 小写、去标点：", tokens)

# 步骤 4：去停用词
stop_words = set(stopwords.words("english"))
tokens = [t for t in tokens if t not in stop_words]
print("④ 去停用词：", tokens)

# 步骤 5：词干提取 vs 词形还原
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print("⑤ 词干提取与词形还原对比：")
print(f"   {'原词':<12}{'词干提取':<12}{'词形还原'}")
for w in ["studying", "students", "running", "experiments", "surprisingly",
          "better", "models", "was"]:
    print(f"   {w:<14}{stemmer.stem(w):<14}{lemmatizer.lemmatize(w, pos='v')}")

# 词形还原需要知道词性：better 作形容词时还原为 good
print("   better 作形容词还原：", lemmatizer.lemmatize("better", pos="a"))

# 步骤 6：把上面的步骤封装成一个函数，方便复用
def preprocess(doc):
    words = nltk.word_tokenize(doc.lower())
    words = [w for w in words if w.isalpha() and w not in stop_words]
    return [lemmatizer.lemmatize(w) for w in words]

print("⑥ 封装后的结果：", preprocess("The cats are sitting on the mats."))
