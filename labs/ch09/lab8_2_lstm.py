"""实验 8-2：用 PyTorch 搭建 LSTM 情感分类器"""
from collections import Counter
import jieba
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

jieba.setLogLevel("WARN")
torch.manual_seed(42)
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "SimHei", "PingFang SC"]
MAX_LEN = 40          # 每条评论最多保留 40 个词


# ===== 第 1 部分：准备数据（分词、建词表、转成编号） =====
def load_data():
    df = pd.read_csv("waimai_10k.csv")
    # 与实验 6-2 完全相同的划分方式，方便比较
    X_train, X_test, y_train, y_test = train_test_split(
        df["review"], df["label"], test_size=0.2, random_state=42, stratify=df["label"])
    train_tokens = [jieba.lcut(t) for t in X_train]
    test_tokens = [jieba.lcut(t) for t in X_test]
    counter = Counter(w for ws in train_tokens for w in ws)
    # 0 号留给填充 <pad>，1 号留给未登录词 <unk>
    vocab = {"<pad>": 0, "<unk>": 1}
    for w, c in counter.items():
        if c >= 2:                               # 只保留出现 2 次以上的词
            vocab[w] = len(vocab)
    return train_tokens, test_tokens, list(y_train), list(y_test), vocab


def encode(tokens_list, vocab):
    """把分好词的句子转成等长的编号张量，并记录每句的真实长度"""
    ids = torch.zeros(len(tokens_list), MAX_LEN, dtype=torch.long)
    lengths = []
    for i, ws in enumerate(tokens_list):
        seq = [vocab.get(w, 1) for w in ws][:MAX_LEN]
        ids[i, :len(seq)] = torch.tensor(seq)
        lengths.append(max(len(seq), 1))
    return ids, torch.tensor(lengths)


# ===== 第 2 部分：定义模型 =====
class SentimentRNN(nn.Module):
    def __init__(self, vocab_size, cell="LSTM", emb_dim=128, hidden=128):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, emb_dim, padding_idx=0)   # 词嵌入层
        rnn_class = {"RNN": nn.RNN, "LSTM": nn.LSTM, "GRU": nn.GRU}[cell]
        self.rnn = rnn_class(emb_dim, hidden, batch_first=True)              # 循环层
        self.fc = nn.Linear(hidden, 2)                                       # 输出层：2 个类别

    def forward(self, ids, lengths):
        x = self.embedding(ids)                  # [批大小, 40] -> [批大小, 40, 128]
        # pack：告诉循环层每句的真实长度，跳过末尾的填充
        packed = nn.utils.rnn.pack_padded_sequence(
            x, lengths, batch_first=True, enforce_sorted=False)
        _, h = self.rnn(packed)
        if isinstance(h, tuple):                 # LSTM 返回 (h, c)，只取 h
            h = h[0]
        return self.fc(h[-1])                    # 用读完整句后的隐藏状态做分类


# ===== 第 3 部分：训练与评估 =====
def evaluate(model, ids, lengths, labels):
    model.eval()
    with torch.no_grad():
        pred = model(ids, lengths).argmax(dim=1)
    return (pred == labels).float().mean().item()


def train_model(cell, data, epochs=6, batch_size=64, verbose=True):
    train_tokens, test_tokens, y_train, y_test, vocab = data
    Xtr, Ltr = encode(train_tokens, vocab)
    Xte, Lte = encode(test_tokens, vocab)
    ytr, yte = torch.tensor(y_train), torch.tensor(y_test)

    torch.manual_seed(42)
    model = SentimentRNN(len(vocab), cell)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    history = {"loss": [], "train_acc": [], "test_acc": []}
    for epoch in range(1, epochs + 1):
        model.train()
        perm = torch.randperm(len(Xtr))           # 每轮打乱训练数据
        total_loss = 0.0
        for i in range(0, len(Xtr), batch_size):
            idx = perm[i:i + batch_size]
            optimizer.zero_grad()                 # 1. 清空上一批的梯度
            logits = model(Xtr[idx], Ltr[idx])    # 2. 前向传播
            loss = loss_fn(logits, ytr[idx])      # 3. 计算损失
            loss.backward()                       # 4. 反向传播求梯度
            optimizer.step()                      # 5. 更新参数
            total_loss += loss.item() * len(idx)
        history["loss"].append(total_loss / len(Xtr))
        history["train_acc"].append(evaluate(model, Xtr, Ltr, ytr))
        history["test_acc"].append(evaluate(model, Xte, Lte, yte))
        if verbose:
            print(f"第 {epoch} 轮  损失 {history['loss'][-1]:.4f}  "
                  f"训练集准确率 {history['train_acc'][-1]:.4f}  "
                  f"测试集准确率 {history['test_acc'][-1]:.4f}")
    return model, history


if __name__ == "__main__":
    data = load_data()
    print("训练集", len(data[0]), "条，测试集", len(data[1]), "条，词表大小", len(data[4]))
    model, history = train_model("LSTM", data)
    print("模型参数量：", sum(p.numel() for p in model.parameters()))

    # 画训练曲线
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    epochs = range(1, len(history["loss"]) + 1)
    ax1.plot(epochs, history["loss"], marker="o")
    ax1.set_title("训练损失"); ax1.set_xlabel("轮次")
    ax2.plot(epochs, history["train_acc"], marker="o", label="训练集")
    ax2.plot(epochs, history["test_acc"], marker="s", label="测试集")
    ax2.set_title("准确率"); ax2.set_xlabel("轮次"); ax2.legend()
    plt.tight_layout(); plt.savefig("lstm_curve.png", dpi=150)

    # ===== 第 4 部分：用训练好的模型预测新评论 =====
    vocab = data[4]
    samples = ["送餐很快，味道也不错", "等了两个小时，饭都凉了",
               "不是很难吃", "价格不便宜，但是真的好吃"]
    ids, lengths = encode([jieba.lcut(s) for s in samples], vocab)
    model.eval()
    with torch.no_grad():
        probs = torch.softmax(model(ids, lengths), dim=1)[:, 1]
    for s, p in zip(samples, probs):
        print(f"{s:<16} 正面概率 {p:.3f}  -> {'正面' if p > 0.5 else '负面'}")
