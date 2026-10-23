"""实验 9-1：手算自注意力，并用 PyTorch 搭建小型 Transformer 分类器"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "SimHei", "PingFang SC"]
np.set_printoptions(precision=2, suppress=True)

# ===== 第 1 部分：一步一步计算自注意力 =====
words = ["小猫", "追", "老鼠", "，", "它", "跑", "累", "了"]
# 手工设计的 4 维词向量，四个维度大致表示：[动物, 动作, 代词, 标点/虚词]
X = np.array([
    [1.0, 0.0, 0.3, 0.0],   # 小猫
    [0.0, 1.0, 0.0, 0.0],   # 追
    [0.8, 0.0, 0.0, 0.0],   # 老鼠
    [0.0, 0.0, 0.0, 1.0],   # ，
    [0.6, 0.0, 1.0, 0.0],   # 它
    [0.0, 0.9, 0.0, 0.0],   # 跑
    [0.0, 0.7, 0.0, 0.2],   # 累
    [0.0, 0.0, 0.0, 0.8],   # 了
])
d = X.shape[1]
# 为了看清原理，这里让 Q、K、V 直接等于词向量（相当于 W_Q、W_K、W_V 都是单位矩阵）
Q, K, V = X, X, X

scores = Q @ K.T / np.sqrt(d)                   # ① 打分：每个词和所有词做点积，再除以 √d
def softmax(z):
    e = np.exp(z - z.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)
weights = softmax(scores)                        # ② 归一化：每一行变成和为 1 的权重
output = weights @ V                             # ③ 加权求和：按权重把所有词的 V 混合起来

i = words.index("它")
print("“它”对每个词的注意力权重：")
for w, a in sorted(zip(words, weights[i]), key=lambda t: -t[1]):
    print(f"  {w}\t{a:.3f}")
print("“它”的原始向量：  ", X[i])
print("“它”融合上下文后：", output[i])

plt.figure(figsize=(6, 5))
plt.imshow(weights, cmap="Blues")
plt.xticks(range(len(words)), words); plt.yticks(range(len(words)), words)
plt.xlabel("被关注的词（Key）"); plt.ylabel("当前词（Query）")
plt.colorbar(); plt.title("自注意力权重矩阵")
plt.tight_layout(); plt.savefig("attention_heatmap.png", dpi=150)

# ===== 第 2 部分：可学习的投影矩阵与多头注意力 =====
rng = np.random.default_rng(0)
n_heads, d_model = 2, 4
d_head = d_model // n_heads
heads = []
for h in range(n_heads):
    W_q, W_k, W_v = (rng.normal(size=(d_model, d_head)) for _ in range(3))
    q, k, v = X @ W_q, X @ W_k, X @ W_v          # 每个头有自己的 Q、K、V 投影
    a = softmax(q @ k.T / np.sqrt(d_head))
    heads.append(a @ v)
    print(f"第 {h + 1} 个头：“它”最关注的词是“{words[a[i].argmax()]}”")
multi = np.concatenate(heads, axis=-1)           # 拼接各个头的输出
print("每个头的输出形状：", heads[0].shape, " 拼接后：", multi.shape)

# ===== 第 3 部分：没有位置信息时，打乱词序结果不变 =====
perm = [4, 5, 6, 7, 0, 1, 2, 3]                  # 把句子前后两半对调
out_shuffled = softmax(X[perm] @ X[perm].T / np.sqrt(d)) @ X[perm]
print("打乱词序后，“它”的输出：", out_shuffled[perm.index(i)])
print("与原来是否完全相同：", np.allclose(out_shuffled[perm.index(i)], output[i]))
