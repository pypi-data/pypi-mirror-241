import asyncio
import logging
import tempfile

import edge_tts

cnt = 0


async def tts(text: str, *, voice: str = 'random', rate: float = 1.0, **kwargs) -> str:

    logging.info(f"使用Edge TTS: {text}")
    random_en = ["en-GB-LibbyNeural", "en-GB-RyanNeural", "en-GB-SoniaNeural",
                 "en-GB-SoniaNeural", "en-GB-ThomasNeural",
                 "en-US-AriaNeural", "en-US-ChristopherNeural", "en-US-EricNeural",
                 "en-US-GuyNeural", "en-US-JennyNeural", "en-US-RogerNeural", "en-US-SteffanNeural"]
    if voice == 'random':
        global cnt
        voice = random_en[cnt % len(random_en)]
        cnt += 1

    def trans_rate(r):
        if r >= 1.0:
            return f"+{int(r * 100 - 100)}%"
        else:
            return f"-{int(100 - r * 100)}%"

    communicate = edge_tts.Communicate(text=text,
                                       voice=voice,
                                       rate=trans_rate(rate),
                                       volume="+20%")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        await communicate.save(tmp_file.name)
        # filename = _handle_kbps(tmp_file.name)
    logging.info(f"使用Edge TTS: {text} -> 保存在 {tmp_file.name}")
    return tmp_file.name


def _handle_kbps(filename: str):
    from pydub import AudioSegment
    sound = AudioSegment.from_file(filename)

    if sound.channels == 1:
        sound = sound.set_channels(2)
    sound.export(filename, format="mp3", parameters=["-b:a", "60k"])
    return filename


if __name__ == '__main__':
    asyncio.run(tts("Its popularity barely decreases over the years and it was recently renovated."))
