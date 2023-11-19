from pydantic import BaseModel


class R(BaseModel):
    status: str = ""
    message: str = ""
    data: dict = {}

    @staticmethod
    def success(data: dict | str | None = None):
        if data is None:
            data = dict()
        elif isinstance(data, str):
            data = dict(message=data)
        return R(status="success", data=data)

    @staticmethod
    def fail(message: str = None, data: dict | str | None = None):
        if data is None:
            data = dict()
        elif isinstance(data, str):
            data = dict(message=data)
        return R(status="fail", message=message, data=data)
