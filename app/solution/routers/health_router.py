"""Health Router"""

import gc
from fastapi import APIRouter, Request
from app.core.constants import LOG_FINOK, LOG_INIT, LOG_DATA, get_constants
from app.core.utils import execution_time
from app.solution.models.health_model import HealthResponse
from app.core.logger_custom import log


router = APIRouter()


@router.get(
    "",
    summary="Receive and Response Health",
    description="Receive empty payload and check health status",
    response_model=None,
    tags=["health"]
)
@execution_time
async def health(rq: Request) -> HealthResponse:
    """Receive empty payload and check health status"""
    log.info(f"{LOG_INIT}")
    log.info(f"{rq.url}", extra=rq.method)
    try:
        response = HealthResponse(message="Health OK")
    finally:
        gc.collect()
    log.info(f"{LOG_DATA}", extra=response)
    log.info(f"{LOG_FINOK}")

    return response


@router.get(
    "/constants",
    summary="Receive and Response Constants",
    description="Receive empty payload and return constants",
    response_model=None,
    tags=["health"]
)
@execution_time
async def constants(rq: Request):
    """Receive empty payload and return constants"""
    log.info(f"{LOG_INIT}")
    log.info(f"{rq.url}", extra=rq.method)
    try:
        response = get_constants()
    finally:
        gc.collect()
    log.info(f"{LOG_DATA}", extra=response)
    log.info(f"{LOG_FINOK}")
    return response


@router.post(
    "/memory",
    summary="Receive and Clean Memory",
    description="Receive empty payload and clean Memory",
    response_model=None,
    tags=["health"]
)
@execution_time
async def memory(rq: Request) -> HealthResponse:
    """Receive empty payload and clean memory"""
    log.info(f"{LOG_INIT}")
    log.info(f"{rq.url}", extra=rq.method)
    try:
        gc.collect()
        response = HealthResponse(message="Memory Cleaned")
    finally:
        gc.collect()
    log.info(f"{LOG_DATA}", extra=response)
    log.info(f"{LOG_FINOK}")
    return response
