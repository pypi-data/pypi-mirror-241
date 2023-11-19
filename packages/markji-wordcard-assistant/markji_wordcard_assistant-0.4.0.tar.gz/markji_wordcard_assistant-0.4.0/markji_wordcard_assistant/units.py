import sys

from dotenv import load_dotenv

from markji_wordcard_assistant.markji_api import api
from markji_wordcard_assistant.voice import edge, markji_native, youdao, openai_tts
from markji_wordcard_assistant.voice.tts_method import TTS_method

load_dotenv()


@DeprecationWarning
async def request_audio_id_old(word: str, locale: str = "en-GB", by: str = "default", speed: str = "+0%") -> str:
    """

    :param speed:
    :param word:
    :param locale:
        - en-GB or en-US
    :param by:
        - default 使用Markji自带的tts
          youdao 使用有道的发音api
    :return:
    """
    try:
        if by == "default":
            return f"[Audio#ID/{api.getIdFromUrl(markji_native.tts(word, locale))}#]"
        if by == "youdao":
            codes = {"en-GB": 1, "en-US": 2}
            return f"[Audio#ID/{api.upload_voice_old(youdao.tts(word, codes[locale]))}#]"
        if by == "edge":
            return f"[Audio#ID/{api.upload_voice_old(await edge.tts(word, rate=speed))}#]"

    except ValueError as e:
        print(e)
        sys.exit(1)


async def request_audio_id(*, word: str,
                           markji_token: str,
                           by: TTS_method,
                           tts_token: str = "",
                           locale: str = "en-GB",
                           speed: float) -> str:
    def combin(s: str):
        return f"[Audio#ID/{s}#]"

    if by == TTS_method.default:
        return combin(api.getIdFromUrl(markji_native.tts(word, locale)))
    if by == TTS_method.youdao:
        codes = {"en-GB": 1, "en-US": 2}
        return combin(api.upload_voice(youdao.tts(word, types=codes[locale]),
                                       markji_token=markji_token))
    if by == TTS_method.edge_tts:
        speed = int(speed * 100 - 100)
        _speed: str = ""
        if speed >= 0:
            _speed = f"+{speed}%"
        elif speed < 0:
            _speed = f"{speed}%"
        return combin(api.upload_voice(await edge.tts(word, rate=_speed),
                                       markji_token=markji_token))

    if by == TTS_method.openai:
        return combin(api.upload_voice(await openai_tts.tts(word,
                                                            openai_token=tts_token,
                                                            rate=speed),
                                       markji_token=markji_token))
