from starlette.requests import Request
from starlette.responses import JSONResponse

from markji_wordcard_assistant.open_api.controller.result import *


class Auth_exception(Exception):
    message = ""

    def __init__(self, message: str):
        self.message = message


def configure_exceptions(app):
    @app.exception_handler(Auth_exception)
    async def http_exception_handler(request: Request, exc: Auth_exception):
        # 自定义异常处理
        return JSONResponse(
            status_code=200,
            content=R.fail(message=exc.message,
                           data={}).model_dump()
        )
