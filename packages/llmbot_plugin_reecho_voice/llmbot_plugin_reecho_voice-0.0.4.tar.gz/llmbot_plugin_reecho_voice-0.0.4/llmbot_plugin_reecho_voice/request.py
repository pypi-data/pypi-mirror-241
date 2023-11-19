# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 下午4:09
# @Author  : sudoskys
# @File    : request.py
# @Software: PyCharm
from pydantic import Field, BaseModel, model_validator


class ReechoResult(BaseModel):
    """
    {
    "status": 200, //状态码，失败时则为500
    "message": "OK", //状态消息
    "data": { //生成详情
        "id": "fb9bfcdd-754f-40b3-b93f-9f98967291a2", //本次生成的ID
        //本次生成结果的音频文件地址
        "audio": "https://r2-global.reecho-external.pro/generate/fb9bfcdd-754f-40b3-b93f-9f374878da2/fb9bfcdd-754f-40b3-b93f-effihie478d-simple-mkc16v.mp3",
        "credit_used": 15 //本次生成所消耗的点数
        }
    }
    """
    status: int = Field(..., title="状态码")
    message: str = Field(..., title="状态消息")
    data: dict = Field(..., title="生成详情")

    @model_validator(mode="after")
    def status_check(self):
        if self.status != 200:
            raise ValueError(f"失败！{self.message}")
        return self

    @property
    def audio_url(self):
        return self.data["audio"]
