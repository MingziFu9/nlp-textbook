"""实验 8-1：用 NumPy 从零实现感知机与两层神经网络"""
import numpy as np

# ===== 第 1 部分：感知机学习“与”“或”运算 =====
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = {"与 AND": np.array([0, 0, 0, 1]),
           "或 OR": np.array([0, 1, 1, 1]),
           "异或 XOR": np.array([0, 1, 1, 0])}


def train_perceptron(X, y, lr=0.1, epochs=20):
    w = np.zeros(2)     # 两个权重
    b = 0.0             # 偏置
    for epoch in range(epochs):
        errors = 0
        for xi, yi in zip(X, y):
            pred = 1 if xi @ w + b > 0 else 0     # 阶跃激活函数
            update = lr * (yi - pred)             # 预测对了 update=0，不调整
            w += update * xi
            b += update
            errors += int(update != 0)
        if errors == 0:                            # 一轮全对，提前结束
            return w, b, epoch + 1
    return w, b, None


for name, y in targets.items():
    w, b, ep = train_perceptron(X, y)
    preds = [1 if xi @ w + b > 0 else 0 for xi in X]
    status = f"第 {ep} 轮收敛" if ep else "20 轮仍未收敛"
    print(f"{name}: w={np.round(w, 2)}, b={b:.2f}, 预测={preds}, 目标={y.tolist()}, {status}")

# ===== 第 2 部分：两层神经网络解决“异或” =====
np.random.seed(0)
y = targets["异或 XOR"].reshape(-1, 1)
W1, b1 = np.random.randn(2, 4), np.zeros((1, 4))   # 隐藏层 4 个神经元
W2, b2 = np.random.randn(4, 1), np.zeros((1, 1))   # 输出层 1 个神经元


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


lr = 1.0
for step in range(5001):
    # 前向传播
    h = np.tanh(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    loss = -np.mean(y * np.log(out) + (1 - y) * np.log(1 - out))   # 交叉熵损失
    # 反向传播：从输出往回，逐层求梯度
    d_out = (out - y) / len(X)
    dW2, db2 = h.T @ d_out, d_out.sum(axis=0, keepdims=True)
    d_h = (d_out @ W2.T) * (1 - h ** 2)        # tanh 的导数是 1 - tanh²
    dW1, db1 = X.T @ d_h, d_h.sum(axis=0, keepdims=True)
    # 梯度下降：参数沿梯度的反方向走一小步
    W1 -= lr * dW1; b1 -= lr * db1
    W2 -= lr * dW2; b2 -= lr * db2
    if step % 1000 == 0:
        print(f"第 {step:4d} 步  损失 = {loss:.4f}")

print("两层网络对异或的输出：", np.round(out.ravel(), 3))
print("四舍五入后的预测：  ", (out.ravel() > 0.5).astype(int), "目标：", y.ravel())
