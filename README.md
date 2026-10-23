# 自然语言处理导论

面向成人教育人工智能技术应用专业（专科）的自然语言处理入门教材。

- 4 学分，72 学时（理论 60 + 实验 12）
- 12 章 + 5 个附录，每章 3 个动手实验，共 36 个
- 使用 NLTK、spaCy、Transformers、jieba、scikit-learn、PyTorch 与国产大模型 API

## 目录结构

| 路径 | 内容 |
|---|---|
| `docs/` | 教材正文（MkDocs Material 格式） |
| `labs/` | 按章存放的实验代码与数据，`labs/requirements.txt` 为实验环境 |
| `大纲-自然语言处理导论-v4.md` | 章节大纲与成稿调整说明 |

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

推送到 `main` 分支后，GitHub Actions 会自动构建并发布到 GitHub Pages（需在仓库 Settings → Pages 中把 Source 设为 GitHub Actions）。

## 说明

书中运行结果均为编者实测。需要联网下载模型或调用大模型 API 的部分标为“待实测”，并附记录表，见附录 C。数据集来源与许可见 `labs/data/README.md`，仅用于教学。
