import logging
import tempfile
from typing import Literal

import dotenv
import elevenlabs

dotenv.load_dotenv()


async def tts(text: str, *,
              elevenlab_token: str = "",
              voice: str = 'Adam',
              model: str = Literal["eleven_multilingual_v2", "eleven_monolingual_v1"],
              ):
    logging.info(f"使用ElevenLab TTS: {text}")
    if elevenlab_token == "":
        raise ValueError("elevenlab_token is empty")
    elevenlabs.set_api_key(elevenlab_token)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as file:
        b = elevenlabs.generate(
            text=text,
            voice=voice,
            # voice=elevenlabs.Voice(
            #     voice_id='pNInz6obpgDQGcFmaJgB',
            #     name="Adam",
            #     settings=elevenlabs.VoiceSettings(
            #         stability=0.5,
            #         similarity_boost=0.75,
            #         style=0,
            #         use_speaker_boost=True,
            #     )
            # ),
            model=model,
        )

        file.write(b)
    print(file)
    return file.name


if __name__ == '__main__':
    print(tts("He barely touched his food and left the restaurant.."))
