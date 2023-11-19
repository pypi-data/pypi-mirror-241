<div align="center">
<a href="https://llmkira.github.io/Docs/plugin/basic">
    <img src="https://raw.githubusercontent.com/LlmKira/.github/main/llmbot/func_call_big.png">
</a>
<h2>llmbot_plugin_reecho_voice</h2>
</div>

适用于 [OpenaiBot](https://github.com/LlmKira/Openaibot) 的函数插件，可以提供中文语音合成功能。

## 📦 Install

```shell
pip install llmbot_plugin_reecho_voice -U
```

## 📄 Usage

`/env REECHO_MODEL=xxx;REECHO_KEY=xxx;REECHO_VOICE_ID=xxx`

模型 ID 可以在 [ReEcho](https://dash.reecho.ai/voices) 的控制台中找到。注意需要完整的模型
ID，例如 `9ede7186-f24b-4018-a907-c3927c5e596a`。

### 公共 API Key

可以额外配置 `PLUGIN_REECHO_KEY` 来指定默认公共 API Key。

默认参数如下

```python
voice_id = "4a632551-65d5-427e-b617-b2696c34587d"
model = "reecho-neural-voice-001"
```

也就是晓蕾 https://dash.reecho.ai/voice/4a632551-65d5-427e-b617-b2696c34587d

## 📝 Hook

```python
class ReechoSpeak(BaseTool):
    """
    语音工具
    """
    silent: bool = False
    function: Function = speak_chinese
    keywords: list = ["语音", "说", "读", "念", "回答", "骂", "唱", "朗读", "朗诵"]
    require_auth: bool = False
    repeatable: bool = False
    env_required: list = ["KEY", "VOICE_ID", "MODEL"]
    env_prefix: str = "REECHO_"
```