from uuid import UUID

from fastapi import APIRouter
from starlette.responses import FileResponse

from markji_wordcard_assistant.open_api.jobs import jobs
from .result import R

router = APIRouter()


@router.get("/progress/{uid}", tags=['jobs'])
async def job_progress(uid: str):
    j = jobs.get(UUID(uid), None)
    if j is None:
        return R.fail(message="Job not found")
    else:
        return R.success(j.model_dump())


@router.get("/download/{uid}", tags=['jobs'])
async def job_download(uid: str):
    j = jobs.get(UUID(uid), None)
    if j is None:
        return R.fail(message="Job not found")
    if j.status != "complete":
        return R.fail(message="Job not complete")
    return FileResponse(path=j.result, filename=j.uid.hex + ".txt")
