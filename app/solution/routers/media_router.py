"""Media Router"""

from fastapi import APIRouter, Depends, Request
from app.core.constants import LOG_FINOK, LOG_INIT, LOG_DATA
from app.core.utils import execution_time
from app.core.logger_custom import log
from app.solution.handlers.media_handler import MediaHandler
from app.solution.models.media_model import MediaDB
from app.container import media_handler
from app.config.config import CustomAPIResponse

router = APIRouter()

@router.post(
    "/get_preasigned_url",
    summary="Get preasigned url",
    description="Get preasigned url"
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