"""实验 2-1：正则表达式与编码处理"""
import re

# ===== 第 1 部分：编码与乱码 =====
text = "自然语言处理"
utf8_bytes = text.encode("utf-8")       # 按 UTF-8 编码成字节
gbk_bytes = text.encode("gbk")          # 按 GBK 编码成字节
print("UTF-8 字节数：", len(utf8_bytes), utf8_bytes)
print("GBK   字节数：", len(gbk_bytes), gbk_bytes)

# 用错误的编码去解码，就会出现乱码
wrong = utf8_bytes.decode("gbk", errors="replace")
print("UTF-8 字节按 GBK 解码：", wrong)
# 修复：对原始字节换用正确的 UTF-8 解码
print("修复后：", utf8_bytes.decode("utf-8"))

# 模拟一个 GBK 编码的文件，并用不同编码读取
with open("gbk_demo.txt", "w", encoding="gbk") as f:
    f.write("这是一份用 GBK 编码保存的旧文件。")
for enc in ["utf-8", "gbk"]:
    try:
        with open("gbk_demo.txt", encoding=enc) as f:
            print(f"用 {enc} 读取成功：", f.read())
    except UnicodeDecodeError as e:
        print(f"用 {enc} 读取失败：", e.reason)

# ===== 第 2 部分：正则表达式提取信息 =====
msg = """【会议通知】各位同学：本周五（2026-11-06）下午 14:30 在 3 号楼 205 召开课程说明会。
联系人：王老师，电话 13812345678，备用电话 021-55667788；
邮箱 wang.teacher@example.edu.cn。资料下载：https://www.example.edu.cn/nlp/2026。
如有疑问也可联系助教 15900001111 或 ta_li@example.com。"""

patterns = {
    "手机号": r"1[3-9]\d{9}",
    "固定电话": r"0\d{2,3}-\d{7,8}",
    "邮箱": r"[\w.]+@[\w-]+(?:\.[\w-]+)+",
    "网址": r"https?://[^\s，。；]+",
    "日期": r"\d{4}-\d{1,2}-\d{1,2}",
    "时间": r"\d{1,2}:\d{2}",
}
for name, p in patterns.items():
    print(f"{name}：{re.findall(p, msg)}")

# 用 re.sub 给手机号打码：保留前 3 位和后 4 位
masked = re.sub(r"(1[3-9]\d)\d{4}(\d{4})", r"\1****\2", msg)
print(masked.splitlines()[1])
