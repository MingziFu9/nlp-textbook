"""实验 2-3（第 3 部分）：检查清洗效果"""
import pandas as pd

raw = pd.read_csv("reviews_raw.csv")
clean = pd.read_csv("reviews_clean.csv")

# 用正则统计清洗前后各类“噪声”还剩多少条
checks = {"含HTML标签": r"<[^>]+>",
          "含网址": r"https?://",
          "含表情": "[\U0001F300-\U0001FAFF]",
          "含繁体(示例字)": "[這說個時沒還發麼覺東]",
          "含全角数字字母": "[０-９ａ-ｚＡ-Ｚ]"}
print(f"{'检查项':<10}{'清洗前':>6}{'清洗后':>6}")
for name, p in checks.items():
    print(f"{name:<10}{raw['review'].str.contains(p).sum():>6}"
          f"{clean['clean'].str.contains(p).sum():>6}")
print("平均长度：", round(raw["review"].str.len().mean(), 1), "→",
      round(clean["clean"].str.len().mean(), 1))

# 随机抽 5 条人工检查（random_state 固定随机数，保证每次抽到同样的样本）
for t in clean.sample(5, random_state=7)["clean"]:
    print("  ·", t)
