"""术语表锚点与正文术语链接工具。

用法：
    python tools/glossary_links.py anchors          # 给附录 E 每个术语加锚点（可重复运行）
    python tools/glossary_links.py link 06          # 把第 6 章正文中本章术语的首次加粗出现改成术语链接

术语链接的效果：虚线下划线，鼠标悬停显示定义，点击跳到术语表。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "docs/appendix/e-glossary.md"
CHAPTERS = ROOT / "docs/chapters"
SPAN = re.compile(r'<span id="(g-[^"]+)"></span>')


def anchor_id(term):
    return "g-" + re.sub(r"[\s/（）()、，,]+", "-", term).strip("-")


def parse():
    """返回 {章号: [(术语, 锚点, 定义), ...]}"""
    result, chap = {}, None
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        m = re.match(r"## 第 (\d+) 章", line)
        if m:
            chap = int(m.group(1))
            result[chap] = []
            continue
        if chap and line.startswith("| ") and not line.startswith("| 术语") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            term = SPAN.sub("", cells[0]).strip()
            result[chap].append((term, anchor_id(term), cells[2]))
    return result


def add_anchors():
    out = []
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ") and not line.startswith("| 术语") and not SPAN.search(line):
            cells = line.split("|")
            term = cells[1].strip()
            cells[1] = f' <span id="{anchor_id(term)}"></span>{term} '
            line = "|".join(cells)
        out.append(line)
    GLOSSARY.write_text("\n".join(out) + "\n", encoding="utf-8")


def link_chapter(num):
    path = next(CHAPTERS.glob(f"{num:02d}-*/index.md"))
    text = path.read_text(encoding="utf-8")
    # 只处理“情景导入”到“本章小结”之间的正文，跳过代码块
    start = text.index("## 情景导入")
    end = text.index("## 本章小结")
    body = text[start:end]
    parts = re.split(r"(```.*?```)", body, flags=re.S)
    linked, missing = [], []
    for term, aid, definition in parse().get(num, []):
        target = f"**{term}**"
        done = False
        for i, part in enumerate(parts):
            if part.startswith("```"):
                continue
            pos = part.find(target)
            # 已经是链接的跳过
            if pos >= 0 and not part[max(0, pos - 1):pos] == "[":
                title = definition.replace('"', "“")
                link = f'[**{term}**](../../appendix/e-glossary.md#{aid} "{title}"){{ .term }}'
                parts[i] = part[:pos] + link + part[pos + len(target):]
                done = True
                break
            if pos >= 0:
                done = True
                break
        (linked if done else missing).append(term)
    path.write_text(text[:start] + "".join(parts) + text[end:], encoding="utf-8")
    print(f"已链接 {len(linked)} 个术语；正文中没有找到加粗形式的：{'、'.join(missing) or '无'}")


if __name__ == "__main__":
    if sys.argv[1] == "anchors":
        add_anchors()
    elif sys.argv[1] == "link":
        link_chapter(int(sys.argv[2]))
