"""Media Router"""

from fastapi import APIRouter, Depends, Request
from app.core.constants import LOG_FINOK, LOG_INIT, LOG_DATA
from app.core.utils import execution_time
from app.core.logger_custom import log
from app.solution.handlers.media_handler import MediaHandler
from app.solution.models.media_model import MediaDB, MediaPublishTrigger
from app.container import media_handler
from app.config.config import CustomAPIResponse

router = APIRouter()

@router.post(
    "/get_preasigned_url",
    summary="Get preasigned url",
    description="Get preasigned url",
    tags=["media"]
)
@execution_time
async def get_preasigned_url(rq: Request, payload: MediaDB, media_handler: MediaHandler = Depends(media_handler)):
    """Get preasigned url"""
    log.info(f"{LOG_INIT}")
    log.info(f"{rq.url}", extra=f"{rq.method}: {str(payload)}")
    response = await media_handler.get_preasigned_url(payload)
    log.info(f"{LOG_DATA}", extra=response)
    log.info(f"{LOG_FINOK}")
    return CustomAPIResponse(status_code=200, message="Preasigned url created", data=response)


@router.post(
    "/update_generic",
    summary="Update generic",
    description="Update generic",
    tags=["media"]
)
@execution_time
async def update_generic(rq: Request, payload: dict, media_handler: MediaHandler = Depends(media_handler)):
    """Update generic"""
    log.info(f"{LOG_INIT}")
    log.info(f"{rq.url}", extra=f"{rq.method}: {str(payload)}")
    response = await media_handler.update_generic(payload)
    log.info(f"{LOG_DATA}", extra=response)
    log.info(f"{LOG_FINOK}")
    return CustomAPIResponse(status_code=200, message="Media updated", data=response)


@router.post(
    "/trigger_publish",
    summary="Trigger publish",
    description="Trigger publish",
    tags=["media"]
)
@execution_time
async def trigger_publish(rq: Request, payload: MediaPublishTrigger, media_handler: MediaHandler = Depends(media_handler)):
    """Trigger publish"""
    log.info(f"{LOG_INIT}")
    log.info(f"{rq.url}", extra=f"{rq.method}: {str(payload)}")
    response = await media_handler.trigger_publish(payload)
    log.info(f"{LOG_DATA}", extra=response)
    log.info(f"{LOG_FINOK}")
    return CustomAPIResponse(status_code=200, message="Publish triggered", data=response)