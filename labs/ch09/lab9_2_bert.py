"""实验 9-2：用 Transformers 体验预训练模型，并微调中文 BERT 做情感分类
首次运行需联网下载模型。国内请先设置镜像：
    Windows（PowerShell）：$env:HF_ENDPOINT = "https://hf-mirror.com"
    macOS / Linux：        export HF_ENDPOINT=https://hf-mirror.com
"""
import os
import numpy as np
import pandas as pd
from datasets import Dataset
from sklearn.model_selection import train_test_split
from transformers import (pipeline, AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer)

# ===== 第 1 部分：完形填空——看看 BERT 学到了什么 =====
fill = pipeline("fill-mask", model="google-bert/bert-base-chinese")
for text in ["今天天气很[MASK]，我们去公园玩吧。", "这家店的菜太[MASK]了，再也不来了。"]:
    print(text)
    for r in fill(text, top_k=5):
        print(f"   {r['token_str']}  {r['score']:.3f}")

# ===== 第 2 部分：直接使用别人微调好的情感模型 =====
clf = pipeline("text-classification", model="uer/roberta-base-finetuned-jd-binary-chinese")
for text in ["送餐很快，味道也不错", "不是很难吃", "价格不便宜，但是真的好吃"]:
    print(text, clf(text))

# ===== 第 3 部分：在外卖评论上微调一个小型中文预训练模型 =====
MODEL = os.environ.get("MODEL", "hfl/rbt3")     # 3 层的中文 RoBERTa，CPU 也能训练
df = pd.read_csv("waimai_10k.csv")
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["label"])
tokenizer = AutoTokenizer.from_pretrained(MODEL)


def tokenize(batch):
    # 中文 BERT 按字切分；超过 64 个字截断，不足的补齐
    return tokenizer(batch["review"], truncation=True, padding="max_length", max_length=64)


train_ds = Dataset.from_pandas(train_df.rename(columns={"label": "labels"}), preserve_index=False)
test_ds = Dataset.from_pandas(test_df.rename(columns={"label": "labels"}), preserve_index=False)
train_ds = train_ds.map(tokenize, batched=True)
test_ds = test_ds.map(tokenize, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL, num_labels=2, id2label={0: "负面", 1: "正面"}, label2id={"负面": 0, "正面": 1})
print("模型参数量：", sum(p.numel() for p in model.parameters()))


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    return {"accuracy": (np.argmax(logits, axis=-1) == labels).mean()}


args = TrainingArguments(
    output_dir="bert_waimai",
    num_train_epochs=2,               # 预训练模型通常微调 2~3 轮就够了
    per_device_train_batch_size=32,
    per_device_eval_batch_size=64,
    learning_rate=3e-5,               # 微调的学习率要小，避免“忘掉”预训练学到的知识
    eval_strategy="epoch",
    save_strategy="no",
    logging_steps=50,
    report_to="none",
    seed=42,
)
trainer = Trainer(model=model, args=args, train_dataset=train_ds,
                  eval_dataset=test_ds, compute_metrics=compute_metrics)
trainer.train()
print("测试集结果：", trainer.evaluate())

# 用微调好的模型预测新评论
trainer.save_model("bert_waimai/final")
tokenizer.save_pretrained("bert_waimai/final")
my_clf = pipeline("text-classification", model="bert_waimai/final")
for text in ["送餐很快，味道也不错", "等了两个小时，饭都凉了", "不是很难吃", "价格不便宜，但是真的好吃"]:
    print(text, my_clf(text))
