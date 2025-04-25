from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from auth.views import router as auth_router
from employee.views import router as employee_router
from call.views import router as call_router
from employee_result.views import router as result_router
from employee_session.views import router as session_router
from organization.views import router as organization_router


class ErrorMessage(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

api_router.include_router(
    employee_router,
    prefix="/employee",
    tags=["employee"]
)

api_router.include_router(
    organization_router,
    prefix="/organization",
    tags=["organization"]
)

api_router.include_router(
    session_router,
    prefix="/session",
    tags=["session"]
)

api_router.include_router(
    result_router,
    prefix="/result",
    tags=["result"]
)

api_router.include_router(
    call_router,
    prefix="/call",
    tags=["call"]
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)


@api_router.get("/isalive", include_in_schema=False)
async def is_alive() -> dict:
    return {"alive": True}
