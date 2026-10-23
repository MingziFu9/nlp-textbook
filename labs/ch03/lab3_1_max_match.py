"""实验 3-1：动手实现最大匹配分词"""

# 一个很小的示例词典（真实词典有几十万个词）
DICT = {"南京", "南京市", "市长", "长江", "大桥", "长江大桥", "江大桥",
        "研究", "研究生", "生命", "命", "的", "起源",
        "结婚", "和", "和尚", "尚未", "未", "乒乓", "乒乓球", "乒乓球拍",
        "球拍", "拍卖", "卖", "完", "了", "卖完"}
MAX_LEN = max(len(w) for w in DICT)          # 词典中最长词的长度


def forward_max_match(text):
    """正向最大匹配：从左往右，每次先取最长的一段，查不到就去掉最后一个字再查"""
    words, i = [], 0
    while i < len(text):
        for size in range(min(MAX_LEN, len(text) - i), 0, -1):
            piece = text[i:i + size]
            if piece in DICT or size == 1:   # 查到了，或者只剩一个字
                words.append(piece)
                i += size
                break
    return words


def backward_max_match(text):
    """逆向最大匹配：从右往左，每次先取最长的一段，查不到就去掉最前面一个字再查"""
    words, j = [], len(text)
    while j > 0:
        for size in range(min(MAX_LEN, j), 0, -1):
            piece = text[j - size:j]
            if piece in DICT or size == 1:
                words.insert(0, piece)       # 从右往左切，所以插到最前面
                j -= size
                break
    return words


def bidirectional_match(text):
    """双向最大匹配：两种结果不同时，选词数更少的；词数相同时，选单字更少的"""
    f, b = forward_max_match(text), backward_max_match(text)
    if len(f) != len(b):
        return f if len(f) < len(b) else b
    single = lambda ws: sum(len(w) == 1 for w in ws)
    return f if single(f) < single(b) else b


for s in ["南京市长江大桥", "研究生命的起源", "结婚的和尚未结婚的", "乒乓球拍卖完了"]:
    print(s)
    print("  正向：", "/".join(forward_max_match(s)))
    print("  逆向：", "/".join(backward_max_match(s)))
    print("  双向：", "/".join(bidirectional_match(s)))
