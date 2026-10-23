"""实验 10-3 第 2 部分：用 Ollama 在本机运行开源大模型，观察温度和 Top-p 的影响
准备：安装 Ollama 后，在命令行执行  ollama pull qwen3:1.7b
"""
from openai import OpenAI

# Ollama 提供了与 OpenAI 兼容的接口，地址是本机的 11434 端口，API Key 可以随便填
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen3:1.7b"
prompt = "给一家新开的奶茶店写一句宣传语，不超过 20 个字。/no_think"   # /no_think 关闭 Qwen3 的思考过程

for temperature, top_p in [(0, 1.0), (0.7, 0.9), (1.5, 1.0)]:
    print(f"\n温度 = {temperature}，top_p = {top_p}")
    for i in range(3):          # 同样的设置生成 3 次，看看结果是否相同
        resp = client.chat.completions.create(
            model=MODEL, temperature=temperature, top_p=top_p,
            messages=[{"role": "user", "content": prompt}])
        print(f"  第 {i + 1} 次：{resp.choices[0].message.content.strip()}")
