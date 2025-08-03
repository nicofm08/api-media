"""Media Handler"""


from typing import Optional
from app.core.constants import LOG_HANDLER
from app.solution.services.media_service import MediaService
from app.core.logger_custom import log
from app.solution.models.media_model import MediaDB


class MediaHandler:
    """Media Handler Class"""

    def __init__(self, service: MediaService):
        self.media_service = service

    async def get_preasigned_url(self, media_file: MediaDB) -> Optional[MediaDB]:
        """Get preasigned url"""
        log.info(f"{LOG_HANDLER} Get preasigned url")
        response = await self.media_service.get_preasigned_url(media_file)
        return response