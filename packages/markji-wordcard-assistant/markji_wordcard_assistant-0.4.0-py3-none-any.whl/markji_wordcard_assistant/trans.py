import tempfile

import pyperclip

from . import units


async def trans(filepath: str, locale: str = "en-GB", by: str = "default", speed: str = "+0%"):
    # transed = []
    _, tmpPath = tempfile.mkstemp(suffix=".txt", prefix="OUT_", text=True)
    print(f"保存在 {tmpPath}")
    tmpFile = open(tmpPath, "w")
    with open(filepath, "r") as f:
        for line in f:
            if line[0:3] == "###":
                tmpFile.write(line + "\n")
                tmpFile.flush()
                print(line)
                continue
            splitChar = '\t' if '#' not in line else '#'
            line = [i.strip() for i in line.split(splitChar)]
            word = line[0]
            if (word == ""):
                continue
            while word.isdigit():
                line.pop(0)
                word = line[0]
            tmp = [await units.request_audio_id_old(word=word, locale=locale, by=by, speed=speed), "---", "\n".join(line)]
            s = "\n".join(tmp)
            tmpFile.write(f"{s}\n\n")
            tmpFile.flush()
            print(f"{s}\n")
    # result = "\n\n".join(transed)
    # pyperclip.copy(result)
    pyperclip.copy(open(tmpPath, "r").read())

    print("\n完成！已复制到剪切板")
    print(f"保存在 {tmpPath}")
