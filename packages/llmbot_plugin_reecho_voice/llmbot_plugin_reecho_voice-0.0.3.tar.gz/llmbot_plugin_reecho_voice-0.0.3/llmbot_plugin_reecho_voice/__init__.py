# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 下午4:09
# @Author  : sudoskys
# @File    : __init__.py
# @Software: PyCharm


__package__name__ = "llmbot_plugin_reecho_voice"
__plugin_name__ = "speaking_chinese"
__openapi_version__ = "20231111"

from llmkira.sdk.func_calling import verify_openapi_version

verify_openapi_version(__package__name__, __openapi_version__)

import re
from aiohttp import ClientTimeout
from llmkira.sdk import resign_plugin_executor
from llmkira.sdk.utils import aiohttp_download_file, Ffmpeg
from pydantic import field_validator, ConfigDict, Field
from llmkira.sdk.schema import Function, File
from loguru import logger
from pydantic import BaseModel
from llmkira.schema import RawMessage
from llmkira.sdk.func_calling import PluginMetadata, BaseTool
from llmkira.sdk.func_calling.schema import FuncPair
from llmkira.task import Task, TaskHeader
from typing import TYPE_CHECKING, List

from .request import ReechoResult

if TYPE_CHECKING:
    from llmkira.sdk.schema import TaskBatch

import aiohttp


# function verification class
class SpeakChinese(BaseModel):
    """
    朗诵/朗读中文文本，并发送语音消息
    """
    short_text: str = Field(..., description="聊天内容,内容为中文,内容少于50字,不包含英文字符")
    model_config = ConfigDict(extra="allow")

    @field_validator("short_text")
    def delay_validator(cls, v):
        if len(v) > 80:
            return v[:100]
        return v


speak_chinese = Function.parse_from_pydantic(schema_model=SpeakChinese, plugin_name=__plugin_name__)


@resign_plugin_executor(function=speak_chinese, handle_exceptions=(Exception,))
async def generate_speech(text: str, *,
                          api_key: str = None,
                          voice_id: str = "e91ee8b1",
                          model: str = "reecho-neural-voice-001"
                          ) -> ReechoResult:
    """
    生成语音
    :param api_key: api_key
    :param text: 要生成语音的文本，必须为中文
    :param voice_id: 语音id
    :param model: 语音模型
    :return: 语音链接
    """
    if not api_key:
        raise LookupError("env `REECHO_KEY` not found")
    if voice_id is None:
        voice_id = "e91ee8b1-11ac-4e5e-b381-5978e184f055"
    if model is None:
        model = "reecho-neural-voice-001"
    chinese = re.findall('[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5]',
                         text)
    if not chinese:
        raise ValueError("内容必须为中文")
    chinese_text = ''.join(chinese)
    url = "https://v1.reecho.ai/api/tts/simple-generate"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model,
        "randomness": 97,
        "stability_boost": 40,
        "voiceId": voice_id,
        "text": chinese_text
    }
    logger.debug(f"Plugin --payload {payload}")
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload,
                                timeout=ClientTimeout(total=60)) as response:
            response.raise_for_status()
            result = ReechoResult.model_validate(await response.json())
    return result


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

    def pre_check(self):
        return True

    def env_help_docs(self, empty_env: List[str]) -> str:
        """
        环境变量帮助文档
        :param empty_env: 未被配置的环境变量列表
        :return: 帮助文档/警告
        """
        assert isinstance(empty_env, list), "empty_env must be list"
        message = ""
        if empty_env:
            message = "Login https://dash.reecho.ai/ to get your api key"
        if "REECHO_KEY" in empty_env:
            message += "\n/env REECHO_KEY=xxx Is Required"
        if "REECHO_VOICE_ID" in empty_env:
            message += "\n/env REECHO_VOICE_ID=xxx Is Required"
        if "REECHO_MODEL" in empty_env:
            message += "\n/env REECHO_MODEL=xxx Is Required"
        return message

    def func_message(self, message_text, **kwargs):
        """
        如果合格则返回message，否则返回None，表示不处理
        """
        for i in self.keywords:
            if i in message_text:
                return self.function
        # 忽略过长的消息
        if len(message_text) > 100:
            return None
        # 正则匹配
        if self.pattern:
            match = self.pattern.match(message_text)
            if match:
                return self.function
        return None

    async def failed(self,
                     task: "TaskHeader", receiver: "TaskHeader.Location",
                     exception,
                     env: dict,
                     arg: dict, pending_task: "TaskBatch", refer_llm_result: dict = None,
                     **kwargs
                     ):
        _meta = task.task_meta.reply_message(
            plugin_name=__plugin_name__,
            callback=[TaskHeader.Meta.Callback.create(
                name=__plugin_name__,
                function_response=f"Run Failed: {exception}",
                tool_call_id=pending_task.get_batch_id()
            )
            ],
            write_back=True,
            release_chain=True
        )
        logger.error(f"Plugin:{__plugin_name__} Run Failed:{exception}")
        await Task.create_and_send(
            queue_name=receiver.platform,
            task=TaskHeader(
                sender=task.sender,
                receiver=receiver,
                task_meta=_meta,
                message=[
                    RawMessage(
                        user_id=receiver.user_id,
                        chat_id=receiver.chat_id,
                        text="Can't speak Chinese"
                    )
                ]
            )
        )

    async def callback(self,
                       task: "TaskHeader", receiver: "TaskHeader.Location",
                       env: dict,
                       arg: dict, pending_task: "TaskBatch", refer_llm_result: dict = None,
                       **kwargs
                       ):
        return None

    async def run(self,
                  task: "TaskHeader", receiver: "TaskHeader.Location",
                  arg: dict, env: dict, pending_task: "TaskBatch", refer_llm_result: dict = None,
                  ):
        """
        处理message，返回message
        """
        _arg = SpeakChinese.model_validate(arg)
        _meta = task.task_meta.reply_message(
            plugin_name=__plugin_name__,
            callback=[
                TaskHeader.Meta.Callback.create(
                    name=__plugin_name__,
                    function_response="Run Success",
                    tool_call_id=pending_task.get_batch_id()
                )
            ]
        )
        logger.debug("Plugin --Reecho Generate Speech")
        generate_speech_result = await generate_speech(
            text=_arg.short_text,
            api_key=env.get("REECHO_KEY") or self.get_os_env("REECHO_KEY"),
            voice_id=env.get("REECHO_VOICE_ID"),
            model=env.get("REECHO_MODEL"),
        )
        generate_speech_result: ReechoResult
        audio = generate_speech_result.audio_url
        try:
            logger.debug(f"Plugin --Download Audio")
            file_data = await aiohttp_download_file(
                audio,
                timeout=20,
                size_limit=1024 * 1024 * 20,
            )
            logger.debug(f"Plugin --Convert Audio")
            ogg_data = Ffmpeg.convert(
                input_c="mp3",
                output_c="ogg",
                stream_data=file_data,
                quiet=True
            )
            logger.debug(f"Plugin --Upload Audio")
            file_list = [
                await File.upload_file(
                    file_name=f"generate.ogg",
                    file_data=ogg_data,
                    size_limit=1024 * 1024 * 3,
                    caption=_arg.short_text,
                    creator_uid=task.sender.uid,
                )
            ]
            only_file = True
        except Exception as e:
            logger.exception(f"Plugin:{__plugin_name__} Download Resource Failed:{e}")
            file_list = []
            only_file = False
        await Task.create_and_send(
            queue_name=receiver.platform,
            task=TaskHeader(
                sender=task.sender,
                receiver=receiver,
                task_meta=_meta,
                message=[
                    RawMessage(
                        user_id=receiver.user_id,
                        chat_id=receiver.chat_id,
                        file=file_list,
                        only_send_file=only_file,
                        text=_arg.short_text,
                    )
                ]
            )
        )


__plugin_meta__ = PluginMetadata(
    name=__plugin_name__,
    description="使用 reecho.ai 的语音合成功能",
    usage="直接指示，但是需要设置环境变量",
    openapi_version=__openapi_version__,
    function={
        FuncPair(function=speak_chinese, tool=ReechoSpeak)
    },
    homepage="https://www.reecho.ai/"
)
