"""实验 3-2（第 4 部分）：差评高频词统计与词云"""
from collections import Counter
import jieba
import pandas as pd
from wordcloud import WordCloud

jieba.setLogLevel("WARN")             # 不显示加载词典的提示信息
df = pd.read_csv("waimai_10k.csv")
bad = df[df["label"] == 0]["review"]  # 只取差评
stopwords = set(open("cn_stopwords.txt", encoding="utf-8").read().split())

words = []
for review in bad:
    for w in jieba.cut(review):
        if len(w) >= 2 and w not in stopwords:   # 去掉单字和停用词
            words.append(w)

freq = Counter(words)
print("差评共分出", len(words), "个词，不同的词有", len(freq), "个")
print("出现最多的 15 个词：")
for w, c in freq.most_common(15):
    print(f"  {w}\t{c}")

# 生成词云：Windows 可用 font_path="C:/Windows/Fonts/simhei.ttf"
# macOS 可用 "/System/Library/Fonts/PingFang.ttc"
wc = WordCloud(font_path="/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
               width=800, height=450, background_color="white", max_words=100)
wc.generate_from_frequencies(freq)
wc.to_file("bad_reviews_wordcloud.png")
print("词云已保存为 bad_reviews_wordcloud.png")
