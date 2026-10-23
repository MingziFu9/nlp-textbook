"""实验 11-3 第 2 部分（选做）：用函数调用（Function Calling）写一个迷你智能体
需要 DEEPSEEK_API_KEY（见附录 D），并与 lab11_2_rag.py、student_handbook.md 放在同一目录。
"""
import ast
import datetime
import json
import operator
import os
from openai import OpenAI
from lab11_2_rag import chunks, retrieve

client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")


# ===== 第 1 步：准备三个工具（就是普通的 Python 函数） =====
def search_handbook(query):
    """在学生手册中检索相关规定"""
    return "\n".join(f"【{chunks[i]['title']}】{chunks[i]['text']}" for i, _ in retrieve(query, 2))


def calculator(expression):
    """安全地计算四则运算表达式（不使用 eval，防止执行恶意代码）"""
    ops = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}

    def calc(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in ops:
            return ops[type(node.op)](calc(node.left), calc(node.right))
        raise ValueError("只支持加减乘除")
    return str(calc(ast.parse(expression, mode="eval").body))


def get_today():
    """获取今天的日期和星期"""
    d = datetime.date.today()
    return f"{d.isoformat()}，星期{'一二三四五六日'[d.weekday()]}"


TOOLS = {"search_handbook": search_handbook, "calculator": calculator, "get_today": get_today}

# ===== 第 2 步：用 JSON 格式向大模型“介绍”这些工具 =====
tool_specs = [
    {"type": "function", "function": {
        "name": "search_handbook", "description": "检索星海职业学院学生手册中的规章制度",
        "parameters": {"type": "object", "properties": {"query": {"type": "string", "description": "检索关键词"}},
                       "required": ["query"]}}},
    {"type": "function", "function": {
        "name": "calculator", "description": "计算加减乘除表达式，例如 3000*2+1000",
        "parameters": {"type": "object", "properties": {"expression": {"type": "string"}},
                       "required": ["expression"]}}},
    {"type": "function", "function": {
        "name": "get_today", "description": "获取今天的日期和星期",
        "parameters": {"type": "object", "properties": {}}}},
]


# ===== 第 3 步：智能体循环——思考、调用工具、观察结果，直到给出答案 =====
def run_agent(question, max_steps=5):
    messages = [{"role": "system", "content": "你是星海职业学院的学生助手。需要时调用工具获取信息，不要编造规定。"},
                {"role": "user", "content": question}]
    for step in range(1, max_steps + 1):
        msg = client.chat.completions.create(model=MODEL, messages=messages,
                                             tools=tool_specs, temperature=0).choices[0].message
        if not msg.tool_calls:                       # 模型认为信息已经足够，直接回答
            return msg.content
        messages.append(msg)                         # 记下模型“想调用工具”的这条消息
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments or "{}")
            result = TOOLS[call.function.name](**args)
            print(f"  [第 {step} 步] 调用 {call.function.name}({args}) -> {result[:40]}…")
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
    return "步骤太多，未能完成。"


for q in ["一等奖学金和三等奖学金加起来一共多少钱？",
          "今天星期几？图书馆今天几点关门？"]:
    print(f"\n问：{q}")
    print(f"答：{run_agent(q)}")
