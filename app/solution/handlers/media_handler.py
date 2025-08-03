"""Media Handler"""


from typing import Optional
from app.core.constants import LOG_HANDLER
from app.solution.services.media_service import MediaService
from app.core.logger_custom import log
from app.solution.models.media_model import MediaDB, MediaPublishTrigger


class MediaHandler:
    """Media Handler Class"""

    def __init__(self, service: MediaService):
        self.media_service = service

    async def get_preasigned_url(self, media_file: MediaDB) -> Optional[MediaDB]:
        """Get preasigned url"""
        log.info(f"{LOG_HANDLER} Get preasigned url")
        response = await self.media_service.get_preasigned_url(media_file)
        return response

    async def update_generic(self, body: dict) -> Optional[int]:
        """Update generic"""
        log.info(f"{LOG_HANDLER} Update generic")
        response = await self.media_service.update_generic(body)
        return response

    async def trigger_publish(self, body: MediaPublishTrigger) -> Optional[int]:
        """Trigger publish"""
        log.info(f"{LOG_HANDLER} Trigger publish")
        response = await self.media_service.trigger_publish(body)
        return response