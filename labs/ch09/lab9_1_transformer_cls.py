"""实验 9-1 第 4 部分：用 PyTorch 搭建小型 Transformer 情感分类器（与实验 8-2 的 LSTM 比较）"""
import time
import torch
import torch.nn as nn
from lab8_2_lstm import load_data, encode, MAX_LEN


class TinyTransformer(nn.Module):
    def __init__(self, vocab_size, d_model=128, n_heads=4, n_layers=2):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, d_model, padding_idx=0)   # 词嵌入
        self.pos_emb = nn.Embedding(MAX_LEN, d_model)                     # 位置嵌入：第 0~39 个位置各一个向量
        layer = nn.TransformerEncoderLayer(d_model, n_heads, dim_feedforward=256,
                                           dropout=0.1, batch_first=True)
        self.encoder = nn.TransformerEncoder(layer, n_layers, enable_nested_tensor=False)  # 2 层编码器
        self.fc = nn.Linear(d_model, 2)

    def forward(self, ids):
        pos = torch.arange(ids.size(1)).unsqueeze(0)                     # [[0, 1, 2, ..., 39]]
        x = self.tok_emb(ids) + self.pos_emb(pos)                        # 词向量 + 位置向量
        pad_mask = ids == 0                                              # 填充位置不参与注意力
        h = self.encoder(x, src_key_padding_mask=pad_mask)
        h = h.masked_fill(pad_mask.unsqueeze(-1), 0).sum(1) / (~pad_mask).sum(1, keepdim=True)
        return self.fc(h)                                                # 所有真实词的平均向量做分类


train_tokens, test_tokens, y_train, y_test, vocab = load_data()
Xtr, _ = encode(train_tokens, vocab)
Xte, _ = encode(test_tokens, vocab)
ytr, yte = torch.tensor(y_train), torch.tensor(y_test)

torch.manual_seed(42)
model = TinyTransformer(len(vocab))
print("模型参数量：", sum(p.numel() for p in model.parameters()))
opt = torch.optim.AdamW(model.parameters(), lr=5e-4)
loss_fn = nn.CrossEntropyLoss()
start = time.time()
for epoch in range(1, 7):
    model.train()
    perm = torch.randperm(len(Xtr))
    for i in range(0, len(Xtr), 64):
        idx = perm[i:i + 64]
        opt.zero_grad()
        loss = loss_fn(model(Xtr[idx]), ytr[idx])
        loss.backward()
        opt.step()
    model.eval()
    with torch.no_grad():
        acc = (model(Xte).argmax(1) == yte).float().mean().item()
    print(f"第 {epoch} 轮  测试集准确率 {acc:.4f}")
print(f"用时 {time.time() - start:.1f} 秒")
