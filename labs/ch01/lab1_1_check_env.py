"""实验 1-1：检查 NLP 实验环境是否安装成功"""
import sys
import importlib

print("Python 版本：", sys.version.split()[0])
if sys.version_info < (3, 9):
    print("⚠ 建议使用 Python 3.10 或 3.11")

packages = ["nltk", "jieba", "spacy", "sklearn", "transformers", "torch"]
ok = True
for name in packages:
    try:
        module = importlib.import_module(name)
        print(f"✔ {name:<13} 版本 {getattr(module, '__version__', '未知')}")
    except ImportError:
        ok = False
        print(f"✘ {name:<13} 未安装，请执行：pip install {'scikit-learn' if name == 'sklearn' else name}")

# 检查 spaCy 语言模型
try:
    import spacy
    for model in ["zh_core_web_sm", "en_core_web_sm"]:
        spacy.load(model)
        print(f"✔ spaCy 模型 {model} 可用")
except Exception as e:
    ok = False
    print("✘ spaCy 模型未安装：", e)

# 检查 NLTK 数据包
try:
    import nltk
    nltk.word_tokenize("Hello world.")
    print("✔ NLTK 数据包 punkt_tab 可用")
except LookupError:
    ok = False
    print("✘ NLTK 数据包缺失，请运行：nltk.download('punkt_tab')")

print("\n环境检查通过，可以开始学习了！" if ok else "\n请根据上面的提示补装缺少的组件。")
