---
title: 附录 D 国产大模型 API 申请与使用指南
description: 国内主要大模型开放平台的 API Key 申请步骤、OpenAI 兼容接口地址、环境变量设置、费用估算与安全注意事项
---

# 附录 D 国产大模型 API 申请与使用指南

本书第 2、4、6、7、10、11、12 章的部分实验需要调用大模型 API。本附录介绍如何申请 API Key，以及如何让书中的代码切换到不同的平台。

!!! note "说明"
    各平台的网址、界面、模型名称和价格变化很快，本附录的信息以编写时为准。操作时如有出入，请以平台官方文档和控制台显示的信息为准。

## D.1 通用步骤

无论使用哪个平台，申请和使用 API 的流程都差不多：

1. **注册账号**：用手机号注册平台账号；
2. **实名认证**：按照国家规定，使用大模型 API 一般需要完成实名认证；
3. **获取额度**：新用户通常有一定的免费额度，用完后需要充值。本书实验的调用量很小，一般几元钱就足够完成全部实验；
4. **创建 API Key**：在控制台的“API Key”或“密钥管理”页面创建一个 Key，**复制后妥善保存**。很多平台只在创建时显示一次完整的 Key；
5. **记下三项配置**：**接口地址**（base_url）、**API Key** 和**模型名称**（model）。

## D.2 主要平台一览

下面这些平台都提供与 OpenAI 兼容的接口，本书的代码只需修改接口地址和模型名称即可使用。

| 平台 | 网址 | 接口地址（base_url） | 模型名称示例 |
|---|---|---|---|
| DeepSeek 开放平台 | platform.deepseek.com | `https://api.deepseek.com` | `deepseek-chat`（对话）、`deepseek-reasoner`（推理） |
| 阿里云百炼（通义千问） | bailian.console.aliyun.com | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus`、`qwen-turbo`、`qwen-max` |
| 智谱开放平台（GLM） | open.bigmodel.cn | `https://open.bigmodel.cn/api/paas/v4/` | 以控制台为准，平台提供部分可免费调用的模型 |
| 月之暗面（Kimi） | platform.moonshot.cn | `https://api.moonshot.cn/v1` | 以控制台为准 |
| 火山方舟（豆包） | console.volcengine.com/ark | `https://ark.cn-beijing.volces.com/api/v3` | 填写控制台中的模型 ID 或推理接入点 ID |
| 百度智能云千帆（文心） | console.bce.baidu.com/qianfan | `https://qianfan.baidubce.com/v2` | 以控制台为准 |
| 硅基流动 | cloud.siliconflow.cn | `https://api.siliconflow.cn/v1` | 提供 DeepSeek、Qwen、GLM 等多种开源模型，部分小模型可免费调用 |

本书的代码默认使用 DeepSeek。对于初学者，推荐以下两种选择：

- **DeepSeek 开放平台**：注册简单，价格低，模型能力强，是书中代码的默认配置；
- **硅基流动等模型聚合平台**：一个 Key 可以调用多家的开源模型，方便比较不同模型的效果，部分小模型免费。

## D.3 设置环境变量

为了不把 API Key 写在代码中，本书的代码统一从**环境变量**中读取三项配置：

| 环境变量 | 含义 | 默认值 |
|---|---|---|
| `DEEPSEEK_API_KEY` | API Key（使用其他平台时，也把那个平台的 Key 放在这个变量中） | 无，必须设置 |
| `LLM_BASE_URL` | 接口地址 | `https://api.deepseek.com` |
| `LLM_MODEL` | 模型名称 | `deepseek-chat` |

**临时设置**（只在当前命令行窗口中有效，关闭窗口后失效）：

```bash
# Windows（PowerShell）
$env:DEEPSEEK_API_KEY = "sk-xxxxxxxx"
$env:LLM_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"   # 使用 DeepSeek 时不用设置
$env:LLM_MODEL = "qwen-plus"                                              # 使用 DeepSeek 时不用设置

# Windows（Anaconda Prompt 或 cmd）
set DEEPSEEK_API_KEY=sk-xxxxxxxx

# macOS / Linux
export DEEPSEEK_API_KEY="sk-xxxxxxxx"
```

设置后，在**同一个窗口**中运行 `python 程序名.py` 或 `jupyter notebook`。

**长期设置**：

- Windows：在“设置 → 系统 → 系统信息 → 高级系统设置 → 环境变量”中，新建用户变量 `DEEPSEEK_API_KEY`。设置后需要**重新打开**命令行窗口和 Jupyter 才能生效；
- macOS：把 `export DEEPSEEK_API_KEY="sk-xxxxxxxx"` 这一行添加到用户目录下的 `.zshrc` 文件末尾，然后重新打开终端。

**在 Jupyter Notebook 中临时设置**（不推荐长期使用，提交作业前要删除这一行）：

```python
import os
os.environ["DEEPSEEK_API_KEY"] = "sk-xxxxxxxx"
```

## D.4 测试是否配置成功

把下面的代码保存为 `test_api.py` 并运行。如果看到模型的回答和 Token 用量，说明配置成功。

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url=os.environ.get("LLM_BASE_URL", "https://api.deepseek.com"))
resp = client.chat.completions.create(
    model=os.environ.get("LLM_MODEL", "deepseek-chat"),
    messages=[{"role": "user", "content": "用一句话介绍你自己。"}])
print(resp.choices[0].message.content)
print("本次消耗 Token：", resp.usage.total_tokens)
```

## D.5 费用估算

大模型 API 按 Token 计费，价格一般以“元/百万 Token”表示，输入和输出分别计价。估算方法如下：

$$
\text{费用} \approx \frac{\text{输入 Token 数}}{10^6} \times \text{输入单价} + \frac{\text{输出 Token 数}}{10^6} \times \text{输出单价}
$$

中文大约 1 个汉字对应 0.6–1 个 Token（不同模型的分词器不同，见第 3 章实验 3-3）。以实验 6-3 为例，对 100 条外卖评论做零样本情感分类，假设每条请求的输入（提示词 + 评论）约 100 Token、输出约 5 Token，总计约 1 万输入 Token 和 500 输出 Token。按照常见的价格水平，费用通常不到 1 角钱。

!!! tip "节省费用的方法"
    - 先用少量数据（如 10 条）调试程序，确认无误后再批量运行；
    - 选择满足需要的最小模型，简单的分类、抽取任务不需要最强的模型；
    - 在提示词中限制输出长度，比如“只输出类别名”；
    - 关注平台的免费额度、优惠活动和缓存折扣（重复的提示词前缀可能享受更低的价格）。

## D.6 安全注意事项

!!! danger "务必遵守"
    1. **API Key 就是钱**：不要写在代码里，不要截图发到群里，不要上传到网盘或代码仓库。一旦泄露，立即在控制台删除该 Key 并重新创建；
    2. **设置消费上限**：在控制台中设置每月的消费限额或余额提醒，防止程序出错或 Key 泄露造成大额扣费；
    3. **不要输入敏感信息**：不要把身份证号、银行卡号、他人的个人信息以及单位的保密资料发送给在线大模型（第 12 章）；
    4. **一人一 Key**：同学之间不要共用 Key，教师统一申请的 Key 也不要分发给学生。如果机房条件允许，可以由学校部署本地的开源模型（如通过 Ollama），供实验课统一使用，这样既不花钱，数据也不出校园。

## D.7 常见错误

| 错误 | 原因与解决办法 |
|---|---|
| `KeyError: 'DEEPSEEK_API_KEY'` | 环境变量没有设置，或设置后没有在同一个窗口中运行 |
| 401 `AuthenticationError` | Key 错误、已删除或复制不完整 |
| 402 / `Insufficient Balance` | 余额不足，需要充值 |
| 404 `model not found` | 模型名称写错，或该模型在这个平台上不存在；检查 `LLM_MODEL` |
| 429 `RateLimitError` | 调用太频繁，超过了每分钟的请求次数限制；在循环中加入 `time.sleep(1)` |
| 连接超时 / `APIConnectionError` | 网络问题；检查接口地址是否正确，校园网是否限制了访问 |
| 返回内容中有 `<think>` 等标记 | 使用了推理模型，思考过程混在了输出中；换用非推理模型，或在程序中去掉这部分内容 |
