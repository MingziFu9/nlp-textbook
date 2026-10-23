"""实验 6-3（第 2 部分）：把情感分类模型做成网页小工具
pip install gradio joblib"""
import os
import jieba
import joblib
import pandas as pd
import gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

jieba.setLogLevel("WARN")
MODEL_FILE = "sentiment_model.joblib"


def cut(text):
    """分词函数。要保存模型，不能直接用 jieba.lcut，需要包装成自己定义的函数"""
    return jieba.lcut(text)


# 第一次运行时训练并保存模型，以后直接加载
if os.path.exists(MODEL_FILE):
    model = joblib.load(MODEL_FILE)
else:
    df = pd.read_csv("waimai_10k.csv")
    model = make_pipeline(   # 把“特征提取 + 分类器”打包成一个整体
        TfidfVectorizer(tokenizer=cut, token_pattern=None, ngram_range=(1, 2), min_df=2),
        LogisticRegression(max_iter=1000))
    model.fit(df["review"], df["label"])
    joblib.dump(model, MODEL_FILE)


def predict(review):
    prob = model.predict_proba([review])[0]
    return {"好评": float(prob[1]), "差评": float(prob[0])}


demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=3, label="请输入一条外卖评论"),
    outputs=gr.Label(label="情感分析结果"),
    title="外卖评论情感分析",
    examples=["味道很棒，骑手也很准时", "等了一个半小时，汤都洒了", "还行，就是有点咸"])

if __name__ == "__main__":
    demo.launch()            # 运行后在浏览器打开 http://127.0.0.1:7860
