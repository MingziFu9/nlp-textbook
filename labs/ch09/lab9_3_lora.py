"""实验 9-3：用 LoRA 微调小型开源大模型，打造“校园助手”
需要：pip install peft accelerate
模型文件 1GB 多。国内下载请先设置 HF_ENDPOINT=https://hf-mirror.com，
或改用魔搭社区：from modelscope import snapshot_download; MODEL = snapshot_download("Qwen/Qwen3-0.6B")
"""
import json
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

MODEL = os.environ.get("MODEL", "Qwen/Qwen3-0.6B")
torch.manual_seed(42)
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.float32)


def chat(question, max_new_tokens=80):
    messages = [{"role": "user", "content": question}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True,
                                           enable_thinking=False)   # 关闭“深度思考”，直接回答
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    return tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()


TESTS = ["你是谁？", "图书馆几点关门？", "考试没过怎么办？", "今天天气怎么样？"]

# ===== 第 1 部分：微调前，先问几个问题 =====
print("=== 微调前 ===")
for q in TESTS:
    print(f"问：{q}\n答：{chat(q)}\n")

# ===== 第 2 部分：给模型装上 LoRA“插件” =====
lora_config = LoraConfig(
    r=8,                                   # 低秩矩阵的秩，越大可学的东西越多
    lora_alpha=16,                         # 缩放系数，一般取 r 的 2 倍
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],   # 只在注意力的四个投影矩阵旁加 LoRA
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()          # 看看只训练了多少参数

# ===== 第 3 部分：准备训练数据 =====
data = json.load(open("school_qa.json", encoding="utf-8"))
examples = []
for item in data:
    messages = [{"role": "user", "content": item["instruction"]}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False,
                                           add_generation_prompt=True, enable_thinking=False)
    prompt_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    # 回答后面加上结束符，模型才知道答完要停下
    answer_ids = tokenizer(item["output"] + tokenizer.eos_token, add_special_tokens=False)["input_ids"]
    full_ids = prompt_ids + answer_ids
    labels = [-100] * len(prompt_ids) + answer_ids    # -100 表示不计算损失：只让模型学习“回答”部分
    examples.append((torch.tensor([full_ids]), torch.tensor([labels])))
print("训练样本数：", len(examples))

# ===== 第 4 部分：训练（训练五步法，和第 8 章完全一样） =====
optimizer = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=2e-4)
model.train()
for epoch in range(1, 6):
    total = 0.0
    for input_ids, labels in examples:
        optimizer.zero_grad()
        loss = model(input_ids=input_ids, labels=labels).loss
        loss.backward()
        optimizer.step()
        total += loss.item()
    print(f"第 {epoch} 轮  平均损失 {total / len(examples):.4f}")

# ===== 第 5 部分：微调后，再问同样的问题 =====
model.eval()
print("\n=== 微调后 ===")
for q in TESTS:
    print(f"问：{q}\n答：{chat(q)}\n")

model.save_pretrained("lora_xiaoxing")      # 只保存 LoRA 参数，只有几 MB
