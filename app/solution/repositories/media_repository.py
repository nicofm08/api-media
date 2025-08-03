"""Media Repository"""

from typing import Optional

from pymongo.results import InsertOneResult
from app.core.constants import LOG_REPOSITORY
from app.core.logger_custom import log
from app.core.mongo import MongoClient
from app.core.utils import UtilsCore
from app.core.s3_client import S3Client
from app.solution.models.media_model import MediaDB, MediaPublishTrigger
from app.solution.models.s3_model import S3DB
from app.core.redis import RedisClient


class MediaRepository:
    """Media Repository Class"""

    def __init__(self):
        self.mongo = MongoClient("api-media", "media")
        self.utils = UtilsCore()
        self.s3_client = S3Client()
        self.redis = RedisClient()

    async def get_preasigned_url(
        self, folder: str, key: str, content_type: str
    ) -> Optional[S3DB]:
        """Get preasigned url"""
        log.info(f"{LOG_REPOSITORY} Get preasigned url")
        result = await self.s3_client.preasigned_url(folder, key, content_type)
        return result if result else None

    async def create(self, media: MediaDB) -> Optional[InsertOneResult]:
        """Create media"""
        log.info(f"{LOG_REPOSITORY} Create media")
        result = await self.mongo.insert_one(media.model_dump())
        return result if result else None

    async def update_generic(self, body: dict) -> Optional[int]:
        """Generic update in MongoDB."""
        log.info(f"{LOG_REPOSITORY}  {body}")
        query = await self.utils.apply_filters_query({}, body.get("filter", []))
        update = await self.utils.build_update_query(body.get("update", []))
        log.info(f"{LOG_REPOSITORY}", extra=f"Query: {query}, Update: {update}")
        result = await self.mongo.update_many(query, update)
        return result if result else None

    async def trigger_publish(self, body: MediaPublishTrigger) -> Optional[int]:
        """Trigger publish"""
        log.info(f"{LOG_REPOSITORY}  {body}")
        result = await self.redis.publish(
            body.channel, {"s3_filename": body.s3_filename, "command": body.command}
        )
        return result if result else None

    async def get_media_by_s3_filename(self, s3_filename: str) -> Optional[MediaDB]:
        """Get media by s3 filename"""
        log.info(f"{LOG_REPOSITORY}  {s3_filename}")
        result = await self.mongo.find_one({"s3_filename": s3_filename})
        return result if result else None
