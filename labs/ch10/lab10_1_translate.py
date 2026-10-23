"""实验 10-1 第 2、3 部分：神经机器翻译模型 vs. 大模型翻译，并用 BLEU 评价
需要联网：第 2 部分下载 Helsinki-NLP/opus-mt-zh-en（约 300MB，国内先设置 HF_ENDPOINT=https://hf-mirror.com）；
第 3 部分需要大模型 API Key（见附录 D）。
"""
import os
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction
from transformers import pipeline
from openai import OpenAI

# 5 个中文句子及编者给出的参考译文
data = [
    ("人工智能正在改变我们学习和工作的方式。",
     "Artificial intelligence is changing the way we learn and work."),
    ("这家餐厅的菜味道不错，但是上菜太慢了。",
     "The food in this restaurant tastes good, but the service is too slow."),
    ("明天上午九点在三号教学楼举行期中考试。",
     "The midterm exam will be held in Teaching Building 3 at 9 a.m. tomorrow."),
    ("他这个人刀子嘴豆腐心，你别往心里去。",
     "He has a sharp tongue but a kind heart, so don't take it to heart."),
    ("这个项目八字还没一撇呢。",
     "This project hasn't even got off the ground yet."),
]


def tok(s):
    """简单的英文切分：转小写，标点前后加空格"""
    for p in ",.?!'":
        s = s.replace(p, f" {p} ")
    return s.lower().split()


# ===== 第 2 部分：专门的神经机器翻译模型 =====
mt = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
mt_out = [mt(src)[0]["translation_text"] for src, _ in data]

# ===== 第 3 部分：大模型翻译 =====
client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")


def llm_translate(text):
    resp = client.chat.completions.create(
        model=MODEL, temperature=0,
        messages=[{"role": "system", "content": "你是专业的中英翻译。把用户给出的中文翻译成地道的英文，只输出译文。"},
                  {"role": "user", "content": text}])
    return resp.choices[0].message.content.strip()


llm_out = [llm_translate(src) for src, _ in data]

for (src, ref), a, b in zip(data, mt_out, llm_out):
    print(f"原文：{src}\n参考：{ref}\nMT  ：{a}\nLLM ：{b}\n")

refs = [[tok(r)] for _, r in data]
smooth = SmoothingFunction().method1
print("opus-mt 的 BLEU：", round(corpus_bleu(refs, [tok(x) for x in mt_out], smoothing_function=smooth), 3))
print("大模型的 BLEU： ", round(corpus_bleu(refs, [tok(x) for x in llm_out], smoothing_function=smooth), 3))
