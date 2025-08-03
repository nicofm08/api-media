"""Media Repository"""

from typing import Optional

from pymongo.results import InsertOneResult
from app.core.constants import LOG_REPOSITORY
from app.core.logger_custom import log
from app.core.mongo import MongoClient
from app.core.utils import UtilsCore
from app.core.s3_client import S3Client
from app.solution.models.media_model import MediaDB
from app.solution.models.s3_model import S3DB


class MediaRepository:
    """Media Repository Class"""

    def __init__(self):
        self.mongo = MongoClient("api-media", "media")
        self.utils = UtilsCore()
        self.s3_client = S3Client()

    async def get_preasigned_url(self, folder: str, key: str, content_type: str) -> Optional[S3DB]:
        """Get preasigned url"""
        log.info(f"{LOG_REPOSITORY} Get preasigned url")
        result = await self.s3_client.preasigned_url(folder, key, content_type)
        return result if result else None

    async def create(self, media: MediaDB) -> Optional[InsertOneResult]:
        """Create media"""
        log.info(f"{LOG_REPOSITORY} Create media")
        result = await self.mongo.insert_one(media.model_dump())
        return result if result else None
