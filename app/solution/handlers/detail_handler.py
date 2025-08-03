"""Detail Handler Module."""

from typing import Optional
from app.core.constants import LOG_HANDLER
from app.solution.services.detail_service import DetailService
from app.core.logger_custom import log
from app.solution.models.detail_model import DetailDB
from pymongo.results import InsertOneResult


class DetailHandler:
    """Detail Handler Class."""

    def __init__(self, service: DetailService):
        self.detail_service = service

    async def create(self, detial: DetailDB) -> Optional[InsertOneResult]:
        """Receive request Detail and return homedb."""
        log.info(f"{LOG_HANDLER} create detail")
        response = await self.detail_service.create_detail(detial)
        return response

    async def get_all_filter(self, body: dict) -> Optional[dict]:
        """Receive request Detail and return homedb."""
        log.info(f"{LOG_HANDLER} {body}")
        response = await self.detail_service.get_all_filter(body)
        return response

    async def update_generic(self, body: dict) -> Optional[int]:
        """Receive request Detail and return homedb."""
        log.info(f"{LOG_HANDLER} {body}")
        response = await self.detail_service.update_generic(body)
        return response
