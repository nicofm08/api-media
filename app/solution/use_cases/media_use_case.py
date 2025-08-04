"""Media Use Case"""

from typing import Optional
import uuid

from pymongo.results import InsertOneResult
from app.core.constants import LOG_USECASE
from app.core.logger_custom import log
from app.solution.exceptions.errors_excepctions import CustomAPIResponse
from app.solution.models.media_model import MediaDB, MediaPublishTrigger
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

    async def update_generic(self, body: dict) -> Optional[int]:
        """Update generic"""
        log.info(f"{LOG_USECASE} Update generic")
        result = await self.media_repository.update_generic(body)
        return result if result else None

    async def trigger_publish(self, body: MediaPublishTrigger) -> Optional[str]:
        """Trigger publish when media is in UPLOADED state"""
        log.info(f"{LOG_USECASE} Trigger publish")

        media = await self.media_repository.get_media_by_s3_filename(body.s3_filename)
        if not media:
            raise CustomAPIResponse(status_code=400, message="Media not found")

        if media.status != "UPLOADED":
            raise CustomAPIResponse(status_code=400, message="Media is not in 'UPLOADED' state")
        log.info(f"{LOG_USECASE} Trigger publish body {body}")
        result = await self.media_repository.process_media(body)
        log.info(f"{LOG_USECASE} Trigger publish result {result}")
        return result.id if result else None
