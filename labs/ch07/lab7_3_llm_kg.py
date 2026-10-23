"""实验 7-3：大模型结构化信息抽取与知识图谱可视化"""
import os
import json
import networkx as nx
import matplotlib.pyplot as plt

text = open("news_ner.txt", encoding="utf-8").read()

# ===== 第 1 部分：让大模型以 JSON 格式输出实体和关系 =====
PROMPT = """你是一名信息抽取助手。请从下面的新闻中抽取实体和实体之间的关系。
要求：
1. 实体类型只能是：人物、机构、地点、产品；
2. 关系用简短的词语表示，如“董事长”“合作”“位于”；
3. 严格按照下面的 JSON 格式输出，不要输出任何其他文字：
{{"entities": [{{"name": "实体名", "type": "类型"}}],
  "relations": [{{"head": "实体1", "relation": "关系", "tail": "实体2"}}]}}
新闻：
{text}"""

if os.environ.get("DEEPSEEK_API_KEY"):
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                    base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
    resp = client.chat.completions.create(
        model=os.environ.get("LLM_MODEL", "deepseek-chat"),
        messages=[{"role": "user", "content": PROMPT.format(text=text)}],
        response_format={"type": "json_object"},     # 要求模型只输出合法的 JSON
        temperature=0)
    data = json.loads(resp.choices[0].message.content)
    json.dump(data, open("relations_llm.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("大模型抽取结果已保存到 relations_llm.json")
else:
    print("未设置 DEEPSEEK_API_KEY，使用人工整理的示例数据 relations_sample.json")
    data = json.load(open("relations_sample.json", encoding="utf-8"))

print(f"实体 {len(data['entities'])} 个，关系 {len(data['relations'])} 条")
for r in data["relations"][:5]:
    print(f"  ({r['head']}) -[{r['relation']}]-> ({r['tail']})")

# ===== 第 2 部分：用 networkx 画出知识图谱 =====
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "SimHei", "PingFang SC"]
G = nx.DiGraph()                                         # 有方向的图
colors = {"人物": "#f4a582", "机构": "#92c5de", "地点": "#a6d96a", "产品": "#fdd49e"}
for e in data["entities"]:
    G.add_node(e["name"], color=colors.get(e["type"], "#dddddd"))
for r in data["relations"]:
    G.add_edge(r["head"], r["tail"], label=r["relation"])

pos = nx.spring_layout(G, k=2.0, seed=84)                # 自动计算每个节点的位置
plt.figure(figsize=(11, 8))
nx.draw_networkx_nodes(G, pos, node_size=2600,
                       node_color=[G.nodes[n].get("color", "#dddddd") for n in G])
nx.draw_networkx_labels(G, pos, font_size=10, font_family="WenQuanYi Zen Hei")
nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=18, node_size=2600, edge_color="#888888")
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "label"),
                             font_size=9, font_family="WenQuanYi Zen Hei")
plt.axis("off")
plt.savefig("knowledge_graph.png", dpi=150, bbox_inches="tight")
print("知识图谱已保存为 knowledge_graph.png")

# ===== 第 3 部分：在图谱上做简单查询 =====
print("\n与“星海科技有限公司”直接相连的实体：")
for _, tail, d in G.out_edges("星海科技有限公司", data=True):
    print(f"  {d['label']} → {tail}")
print("谁试用了客服大模型：", [h for h, _, d in G.in_edges("客服大模型", data=True)
                          if d["label"] == "试用"])
