from enum import Enum

from . import markji_native, edge, openai_tts, youdao


class TTS_method(Enum):
    default: str = "default"
    edge_tts: str = "edge_tts"
    youdao: str = "youdao"
    openai: str = "openai"

    @staticmethod
    def get_func(func: str):
        d = {
            "default": markji_native.tts,
            "edge_tts": edge.tts,
            "youdao": youdao.tts,
            "openai": openai_tts.tts
        }
        try:
            return d[func]
        except KeyError:
            raise ValueError("TTS_method参数错误")
