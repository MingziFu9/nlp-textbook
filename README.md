# 自然语言处理导论

面向成人教育人工智能技术应用专业（专科）的自然语言处理入门教材，网页版：https://mingzifu9.github.io/nlp-textbook/

- 4 学分，72 学时（理论 60 + 实验 12），第 3 学期，期末开卷
- 12 章 + 5 个附录，每章 3 个动手实验，共 36 个
- 使用 NLTK、spaCy、Transformers、jieba、scikit-learn、PyTorch 与国产大模型 API
- 每章课后选择题、判断题可在网页上直接作答并查看解析；正文配有参考文献引用、先修要求和概念清单
- 配套 19 个交互动画（`docs/sims/`）、学习图谱（`docs/learning-graph/`）和常见问题（`docs/faq/`），首页“先玩一玩”轮播展示其中 5 个

本书是系列网络教材模板 ai-textbook-template 的来源，2026 年 11 月起改用与系列其他课程相同的模板结构：`course.yml` 统一配置，维护脚本、课件和教案生成器、Word/PDF 导出与其他课程通用。

## 目录结构

| 路径 | 内容 |
|---|---|
| `course.yml` | **课程配置**：书名、学分学时、章节、附录、首页轮播。改完运行 `python tools/course.py sync`，导航、首页、术语表小节等自动更新 |
| `编写规范.md` | 一章的结构、篇幅、实验、题型、文献、动画、术语表、首页轮播的统一要求 |
| `系列公共术语表.md` | 系列课程共用的术语，统一译名和定义 |
| `docs/` | 教材正文（MkDocs Material 格式） |
| `docs/sims/` | 交互动画，每个动画一个文件夹（`main.html` 为动画，`index.md` 为教学说明），公共样式在 `common/` |
| `docs/assets/showcase/` | 首页轮播的短视频和封面图（`python tools/showcase.py record` 生成） |
| `labs/` | 按章存放的实验代码与数据，`labs/requirements.txt` 为实验环境 |
| `slides/`、`lesson-plans/` | 课件底稿、教案底稿 |
| `tools/` | 维护脚本，见下文 |
| `大纲-自然语言处理导论-v4.md` | 章节大纲与成稿调整说明 |

## 维护脚本

```bash
python tools/glossary_links.py anchors     # 给术语表每个术语加锚点
python tools/glossary_links.py link 03     # 第 3 章正文中的术语改成悬停可见定义的链接
python tools/glossary_links.py concepts 03 # 生成第 3 章的“本章概念清单”
python tools/graph_text.py                 # 检查学习图谱并生成文字版
python tools/book_stats.py                 # 更新首页“全书概览”统计表
python tools/course.py sync                # 按 course.yml 更新导航、首页、章节骨架、首页轮播等
python tools/course.py new-sim 名称 3 "标题" # 新建第 3 章的交互动画骨架
python tools/export_docx.py --pdf          # 导出 Word 版和 PDF 版到 build/（需要 pandoc 和 LibreOffice）
python tools/showcase.py record            # 重录首页轮播的短视频（需要 npm ci、ffmpeg）
```

## 课件、教案和 Word/PDF 版

```bash
pip install -r requirements-tools.txt      # 第一次：Python 库
npm install && npx playwright install chromium   # 第一次：渲染配图用的 Node 库和浏览器
npm run figures                            # 把 Mermaid 图和交互动画渲染成图片（课件、Word 版要用）

python tools/make_slides.py draft 3        # 从第 3 章正文生成课件底稿 slides/ch03.md，精简后再 build
python tools/make_slides.py build 3        # → build/课件/第03章 章名.pptx（all 表示全部章节）
python tools/make_lesson_plan.py draft 3   # 生成教案底稿 lesson-plans/ch03.yml，补写“【待填】”后再 build
python tools/make_lesson_plan.py build 3   # → build/教案/第03章 章名 教案.docx
python tools/export_docx.py --pdf          # → build/书名.docx 和 .pdf，动画换成截图和二维码
```

本机不想装这些工具时，在 GitHub 仓库的 **Actions → 导出课件、教案和 Word/PDF → Run workflow** 运行一次，几分钟后在运行页面底部的 Artifacts 下载全部文件。底稿（`slides/`、`lesson-plans/`）要提交到仓库，生成的文件不提交。

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve          # 浏览器打开 http://127.0.0.1:8000
mkdocs build --strict # 提交前确认没有警告
```

## 说明

书中运行结果均为编者实测；需要 GPU、联网下载模型或调用大模型 API 的部分标为“待实测”，并附记录表。数据集来源与许可见 `labs/data/README.md`，仅用于教学。
