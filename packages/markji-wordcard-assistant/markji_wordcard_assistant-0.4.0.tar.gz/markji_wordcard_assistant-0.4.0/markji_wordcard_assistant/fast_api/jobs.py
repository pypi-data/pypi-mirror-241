import asyncio
import logging
from asyncio import Queue
from typing import Dict, Callable, Any, Literal
from uuid import UUID, uuid4

from pydantic import Field, BaseModel

tasks = set()


class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    job_func: Any = Field(exclude=True, default=None)
    args: list = Field(exclude=True, default=[])
    kwargs: dict = Field(exclude=True, default={})
    status: Literal["in_progress", "complete", "error"] = "in_progress"
    progress: float = 0
    result: str = None

    async def start(self):
        queue = Queue()
        task = asyncio.create_task(self.job_func(queue, *self.args, **self.kwargs))
        tasks.add(task)

        while info := await queue.get():
            logging.info(f"JOB[{self.uid}]队列获取数据" + str(info))
            if len(info) == 0:
                break
            assert len(info) == 2
            assert isinstance(info[0], float)
            assert isinstance(info[1], str)
            if info[0] < 0:
                logging.error(f"JOB[{self.uid}]错误{info[1]}")
                self.status = "error"
                raise Exception(info[1])
            else:
                logging.info(f"JOB[{self.uid}]已完成{info[0] * 100:.2f}%")
            self.progress, self.result = info

        self.status = "complete"


jobs: Dict[UUID, Job] = {}


def new_job(job_func: Callable, *args, **kwargs) -> Job:
    job = Job()
    job.job_func = job_func
    job.args = args
    job.kwargs = kwargs
    jobs[job.uid] = job
    return job
