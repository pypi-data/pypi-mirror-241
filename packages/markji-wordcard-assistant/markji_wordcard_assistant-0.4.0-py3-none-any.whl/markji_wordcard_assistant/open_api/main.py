from fastapi import FastAPI

from .controller import trans_controller, jobs_controller
from .exception import *

app = FastAPI()
configure_exceptions(app)

app.include_router(trans_controller.router, prefix="/trans", tags=['trans'])
app.include_router(jobs_controller.router, prefix="/jobs", tags=['jobs'])
