"""Media Use Case"""

from typing import Optional
import uuid

from pymongo.results import InsertOneResult
from app.core.constants import LOG_USECASE
from app.core.logger_custom import log
from app.solution.models.media_model import MediaDB
from app.solution.models.s3_model import S3DB
from app.solution.repositories.media_repository import MediaRepository


class MediaUseCase:
    """Media Use Case Class"""

    def __init__(self, media_repository: MediaRepository):
        self.media_repository = media_repository

    async def get_preasigned_url(self, media: MediaDB) -> Optional[S3DB]:
        """Get preasigned url"""
        log.info(f"{LOG_USECASE} Get preasigned url")
        folder = "images/" if media.type == "IMAGE" else "videos/"
        content_type = "image/jpeg" if media.type == "IMAGE" else "video/mp4"
        extension = media.filename_original.split(".")[-1]
        unique_key = f"{uuid.uuid4()}.{extension}"
        result = await self.media_repository.get_preasigned_url(
            folder, unique_key, content_type
        )
        return result if result else None

    async def create(self, media: MediaDB) -> Optional[InsertOneResult]:
        """Create media"""
        log.info(f"{LOG_USECASE} Create media")
        result = await self.media_repository.create(media)
        return result if result else None
