---
title: ReAct 执行回放
description: 回放智能体“思考—行动—观察”的全过程，同时看到背后的对话历史（第 11 章）
---

# ReAct 执行回放

<iframe class="sim-frame" src="main.html" height="720" loading="lazy" title="ReAct 执行回放"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[11.5.3 ReAct：边想边做](../../chapters/11-qa-rag-agent/index.md#1153-react)、[实验 11-3](../../chapters/11-qa-rag-agent/index.md#11-3)

## 教学说明

**学习目标**

1. 能说出 ReAct 循环的三个环节（记忆）；
2. 能解释工具调用请求和工具结果在对话历史中的顺序（理解）；
3. 能分析智能体在检索失败后怎样调整行动（分析）。

**画面与操作**

- 上方选择问题，工具栏中高亮的是当前调用的工具。
- 左侧：思考链。右侧：messages 列表，包括 system、user、assistant 的工具调用请求和 tool 结果。

**数据来源**：第 1 个问题的过程与 11.5.3 节相同；第 2 个问题来自实验 11-3；工具结果取自实验 11-2 的学生手册。思考内容是编者按 ReAct 思路编写的示意，不是真实模型的输出。

**课堂用法建议**

1. 回放第 2 个问题，让学生指出：如果模型跳过检索直接回答金额，会有什么风险？
2. 回放第 3 个问题，讨论 max_steps 的作用：如果第二次检索仍然失败，智能体应该怎样回答？
