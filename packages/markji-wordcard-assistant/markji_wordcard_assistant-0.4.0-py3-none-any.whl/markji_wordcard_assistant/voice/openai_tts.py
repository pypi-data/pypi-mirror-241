import logging
import tempfile
from typing import Literal

import openai


async def tts(text: str, *,
              openai_token: str,
              rate: float = 1.0,
              voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
              = "fable",
              model: Literal["tts-1", "tts-1-hd", "tts-1-1106", "tts-1-hd-1106"]
              = "tts-1-hd-1106",
              **kwargs
              ):
    client = openai.OpenAI(api_key=openai_token)
    logging.info(f"使用OpenAI TTS: {text}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text,
            speed=rate,
            response_format="mp3"
        )

        response.stream_to_file(tmp_file.name)
    logging.info(f"使用OpenAI TTS: {text} -> 保存在 {tmp_file.name}")
    return tmp_file.name
