import os
import qualtop_llmapi.docs as docs
from qualtop_llmapi.api.router import api_router

import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.logger import logger as fastapi_logger
from starlette.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)

app = FastAPI(title=docs.title, description=docs.desc)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/v1')
#app.add_event_handler('startup', events.startup_event_handler(app))
#app.add_exception_handler(HTTPException, events.on_http_error)

#@app.get("/")
#async def root():
#    return {"message": "Hello World"}

if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
    gunicorn_error_logger = logging.getLogger("gunicorn.error")
    gunicorn_logger = logging.getLogger("gunicorn")

    root_logger = logging.getLogger()
    fastapi_logger.setLevel(gunicorn_logger.level)
    fastapi_logger.handlers = gunicorn_error_logger.handlers
    root_logger.setLevel(gunicorn_logger.level)

    uvicorn_logger = logging.getLogger("uvicorn.access")
    uvicorn_logger.handlers = gunicorn_error_logger.handlers
else:
    # https://github.com/tiangolo/fastapi/issues/2019
    LOG_FORMAT2 = (
        "[%(asctime)s %(process)d:%(threadName)s] %(name)s - %(levelname)s - %(message)s | %(filename)s:%(lineno)d"
    )
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT2)
