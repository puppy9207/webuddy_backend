import fastapi.openapi.utils as fu

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException
from app.router import common

from app.core.config import DESCRIPTION, PROJECT_NAME, VERSION
from app.core.events import create_start_app_handler, create_stop_app_handler


def create_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME,
                          version=VERSION, description=DESCRIPTION)

    application.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_origin_regex='^http://192\.168.*$',
    )

    
    application.add_event_handler("startup", create_start_app_handler())
    application.add_event_handler("shutdown", create_stop_app_handler())
    # application.add_exception_handler(RequestValidationError, http422_error_handler)
    
    # router 분리
    # 모든 router는 prefix기준으로 분리해서 사용한다.
    application.include_router(common.router, prefix='/common')
    
    return application


app = create_application()

fu.validation_error_response_definition = {
    "title": "HTTPValidationError",
    "type": "object",
    "properties": {
        "error": {"title": "Message", "type": "string"},
    },
}


@app.head(
    "/api/alive",
    tags=["common"],
    summary="health check",
    responses={204: {"description": "Alive Server"}},
    status_code=204,
)
def server_check():
    """
    check server alive
    """
    data = {"ping": "pong"}

    return JSONResponse(content=jsonable_encoder(data), status_code=204)