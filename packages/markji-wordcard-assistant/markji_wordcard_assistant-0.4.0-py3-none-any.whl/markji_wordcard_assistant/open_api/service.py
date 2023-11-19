import logging
import tempfile
from asyncio import Queue
from typing import Callable, Coroutine

from markji_wordcard_assistant import units
from markji_wordcard_assistant.markji_api import api
from markji_wordcard_assistant.voice.tts_method import TTS_method

async def trans_file(q: Queue, *,
                     upload_file: str,
                     tts_func: Callable[..., Coroutine],
                     **kwargs):
    _, tmpPath = tempfile.mkstemp(suffix=".txt", prefix="OUT_", text=True)
    logging.info(f"保存在 {tmpPath}")
    try:
        with open(tmpPath, "w") as tmpFile:
            with upload_file.file as f:
                data = [i.decode("utf-8") for i in f.readlines()]
                total_len = len(data)
                now_line = 0
                for line in data:
                    now_line += 1
                    if line[0:3] == "###":
                        tmpFile.write(line + "\n")
                        tmpFile.flush()
                        await q.put((now_line * 1.0 / total_len, line))
                        continue
                    splitChar = '\t' if '#' not in line else '#'
                    line = [i.strip() for i in line.split(splitChar)]
                    word = line[0]
                    if (word == ""):
                        continue
                    while word.isdigit():
                        line.pop(0)
                        word = line[0]
                    # tmp = [await tts_func(word=word, **kwargs),
                    #        "---",
                    #        "\n".join(line)]
                    word = line[0]
                    tmp = [api.upload_voice(await tts_func(word=word, **kwargs), kwargs['markji_token']),
                           "---",
                           "\n".join(line)]
                    s = "\n".join(tmp)
                    tmpFile.write(f"{s}\n\n")
                    tmpFile.flush()
                    await q.put((now_line * 1.0 / total_len, f"{s}\n"))

        await q.put((1.0, tmpPath))
    except Exception as e:
        await q.put((-1.0, str(e)))
    else:
        await q.put(tuple())
