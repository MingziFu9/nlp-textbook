"""生成实验 2-3 使用的“脏”评论数据 reviews_raw.csv（教师备课用，学生直接使用生成好的文件）"""
import csv, random
random.seed(2026)
rows = list(csv.reader(open("waimai_10k.csv", encoding="utf-8")))[1:]
random.shuffle(rows)
rows = rows[:300]
noises = [
    lambda s: s + " 😂😂😂",
    lambda s: "<p>" + s + "</p><br/>",
    lambda s: s + " 详情见 http://t.cn/A6abcXyZ",
    lambda s: "@外卖小哥 " + s,
    lambda s: s.replace("，", "，，，") + "！！！！！",
    lambda s: s.replace("好", "ｈａｏ好").replace("1", "１"),
    lambda s: "  " + s + "\t\n",
    lambda s: s + "#吃货日常#",
]
trad = str.maketrans("这说个时没还发么觉东", "這說個時沒還發麼覺東")
out = []
for i, (label, review) in enumerate(rows):
    r = review
    if i % 3 == 0:
        r = random.choice(noises)(r)
    if i % 7 == 0:
        r = r.translate(trad)
    out.append([i + 1, label, r])
# 加入重复和空评论
out += [[301, "1", out[0][2]], [302, "1", out[5][2]], [303, "0", "   "], [304, "0", "😡😡"],
        [305, "1", "yyds！绝绝子，下次还点"], [306, "0", "送餐太慢了，菜都凉透了，差评差评差评差评"]]
with open("reviews_raw.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "label", "review"]); w.writerows(out)
print("已生成", len(out), "条")
