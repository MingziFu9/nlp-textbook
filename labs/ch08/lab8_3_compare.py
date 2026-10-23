"""实验 8-3：RNN、LSTM、GRU 对比与“记忆力测试”"""
import time
import torch
import torch.nn as nn
from lab8_2_lstm import load_data, train_model

# ===== 第 1 部分：在外卖评论上比较三种循环网络 =====
data = load_data()
print("模型    参数量    最终测试准确率  最高测试准确率  用时(秒)")
for cell in ["RNN", "LSTM", "GRU"]:
    start = time.time()
    model, hist = train_model(cell, data, verbose=False)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"{cell:<6}{n_params:>8}{hist['test_acc'][-1]:>14.4f}"
          f"{max(hist['test_acc']):>16.4f}{time.time() - start:>10.1f}")


# ===== 第 2 部分：记忆力测试——答案藏在序列的第一个位置 =====
def make_memory_task(n, length):
    """随机生成 1~19 的数字序列，标签 = 第一个数字是否小于 10，后面的数字全是干扰"""
    x = torch.randint(1, 20, (n, length))
    y = (x[:, 0] < 10).long()
    return x, y


def build_rnn(cell, hidden=32):
    if cell == "LSTM(遗忘门打开)":
        rnn = nn.LSTM(16, hidden, batch_first=True)
        with torch.no_grad():
            # PyTorch 中 LSTM 偏置依次对应 输入门、遗忘门、候选记忆、输出门 各 hidden 个
            rnn.bias_ih_l0[hidden:2 * hidden].fill_(3.0)   # 遗忘门偏置设为 3，sigmoid(3)≈0.95
        return rnn
    return {"RNN": nn.RNN, "LSTM": nn.LSTM, "GRU": nn.GRU}[cell](16, hidden, batch_first=True)


class MemoryNet(nn.Module):
    def __init__(self, cell):
        super().__init__()
        self.emb = nn.Embedding(20, 16)
        self.rnn = build_rnn(cell)
        self.fc = nn.Linear(32, 2)

    def forward(self, x):
        out, _ = self.rnn(self.emb(x))
        return self.fc(out[:, -1])               # 只用最后一步的输出做判断


def memory_test(cell, length, steps=800):
    torch.manual_seed(0)
    x_train, y_train = make_memory_task(4000, length)
    x_test, y_test = make_memory_task(1000, length)
    model = MemoryNet(cell)
    opt = torch.optim.Adam(model.parameters(), lr=5e-3)
    for _ in range(steps):
        idx = torch.randint(0, 4000, (64,))
        loss = nn.functional.cross_entropy(model(x_train[idx]), y_train[idx])
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        return (model(x_test).argmax(1) == y_test).float().mean().item()


cells = ["RNN", "LSTM", "LSTM(遗忘门打开)"]
print("\n记忆力测试的测试集准确率（随机猜约为 0.5）")
for length in [10, 30, 60]:
    accs = [memory_test(c, length) for c in cells]
    print(f"序列长度 {length:>3}：" + "  ".join(f"{c} {a:.3f}" for c, a in zip(cells, accs)))


# ===== 第 3 部分：观察梯度消失——梯度能传回第一个词多少？ =====
print("\n第一个位置的梯度 ÷ 最后一个位置的梯度（越接近 0，说明梯度消失越严重）")
for cell in cells:
    ratios = []
    for length in [5, 20, 50]:
        torch.manual_seed(0)
        rnn = build_rnn(cell)
        x = torch.randn(32, length, 16, requires_grad=True)
        out, _ = rnn(x)
        out[:, -1].sum().backward()              # 只从最后一步的输出往回传梯度
        ratios.append((x.grad[:, 0].norm() / x.grad[:, -1].norm()).item())
    print(f"{cell:<16}" + "  ".join(f"长度{l}: {r:.1e}" for l, r in zip([5, 20, 50], ratios)))
