import asyncio
import logging
import random
import tempfile
from asyncio import sleep
from typing import Sequence, Generator, Callable, List, Tuple

import edge_tts
from edge_tts import VoicesManager
from pydub import AudioSegment
from pydub.playback import play

VOICE = "en-GB-SoniaNeural"


class NumberMode:
    @staticmethod
    def num_ty() -> Generator[int, None, None]:
        yield random.choice([20, 30, 40, 50, 60, 70, 80, 90])

    @staticmethod
    def num_teen() -> Generator[int, None, None]:
        yield random.choice([13, 14, 15, 16, 17, 18, 19])

    @staticmethod
    def num_11_12() -> Generator[int, None, None]:
        yield random.choice([11, 12])

    @staticmethod
    def num_10_99() -> Generator[int, None, None]:
        yield random.randint(10, 99)

    @staticmethod
    def num_hundred_and_sth() -> Generator[int, None, None]:
        """
        生成 100-999以内的中间是0的数字
        :return:
        """
        yield int(str(random.randint(1, 9)) + "0" + str(random.randint(0, 9)))

    @staticmethod
    def num_100_1000() -> Generator[int, None, None]:
        yield random.randint(100, 1000)

    @staticmethod
    def num_thousand_and_sth() -> Generator[int, None, None]:
        """
        2030
        :return:
        """
        yield int(str(next(NumberMode.num_10_99())) + "0" + str(next(NumberMode.num_10_99())))

    @staticmethod
    def num_1000_10000() -> Generator[int, None, None]:
        yield random.randint(1000, 10000)

    @staticmethod
    def num_10000_100000() -> Generator[int, None, None]:
        yield random.randint(10000, 100000)

    @staticmethod
    def num_100000_1000000() -> Generator[int, None, None]:
        yield random.randint(100000, 1000000)


# async def gen_voice_cache(cache, gened):
#     async for voice, num in generate_num_voice_List(gened):
#         cache.append((AudioSegment.from_mp3(voice), num))
#     cache.append(-1)


async def play_ToTest(cache: List[Tuple[AudioSegment, str] | int]):
    while True:
        if len(cache) == 0:
            print("等待语音生成中")
            await sleep(1)
            continue
        if cache[0] == -1:
            return
        sgm = cache[0][0]
        num = cache[0][1]
        cache.pop(0)
        while True:
            play(sgm)
            inp = input().strip().replace(",", "")
            # inp = await ainput()
            if inp == num.replace(",", ""):
                print(num)
                break


def generate_num(
        numberModeList: Sequence[Callable[[], Generator[int, None, None]] | int],
        *,
        num: int = 100) -> list[str]:
    """
    生成数字
    :param numberModeList: 传入可以生成数字的函数列表, 例如 [NumberMode.num_10_100], 会从中随机选择一个
    :param num: 生成数字的数量
    :return:
    """
    ret = []
    for _ in range(num):
        if len(numberModeList) == 0:
            raise ValueError("numberModeList 不能为空")
        now_mode = random.choice(numberModeList)
        if isinstance(now_mode, int):
            ret.append("{:,}".format(now_mode))
        else:
            ret.append("{:,}".format(next(now_mode())))
        # for random_integer in now_mode():
        #     n = "{:,}".format(random_integer)
        #     ret.append(n)
    return ret


async def generate_num_voice_List(textList: List[str], cache: List[Tuple[AudioSegment, str] | int]):
    """
    生成文本的语音
    :param cache:
    :param textList:
    :return: 文件绝对路径
    """

    async def F(t: str):
        # print(t)
        communicate = edge_tts.Communicate(t, voice=random.choice(voice)['Name'], rate="-10%")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            await communicate.save(tmp_file.name)
            logging.info(f"已生成{tmp_file.name}")
            cache.append((AudioSegment.from_mp3(tmp_file.name), t))

    voices = await VoicesManager.create()
    voice = voices.find(Language="en")
    await asyncio.gather(*[F(t) for t in textList])
    cache.append(-1)


async def _main():
    # generate_num后面传入列表,列表中是各种生成数字的函数
    gened = generate_num([
        NumberMode.num_ty,
        NumberMode.num_teen,
        NumberMode.num_100_1000,
        NumberMode.num_hundred_and_sth,
        *[NumberMode.num_1000_10000 for _ in range(3)],
        *[NumberMode.num_10000_100000 for _ in range(3)],
        6773,
        43527
    ], num=100)

    cache = []
    task1 = asyncio.create_task(generate_num_voice_List(gened, cache))
    task2 = asyncio.create_task(play_ToTest(cache))
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    print(NumberMode.num_thousand_and_sth())
    asyncio.run(_main())
