"""Media Service"""

from datetime import datetime
from typing import Optional
from app.core.constants import LOG_SERVICE
from app.core.logger_custom import log
from app.solution.models.media_model import MediaDB
from app.solution.use_cases.media_use_case import MediaUseCase
from app.solution.exceptions.errors_excepctions import CustomAPIResponse


class MediaService:
    """Media Service Class"""

    def __init__(self, media_use_case: MediaUseCase):
        self.media_use_case = media_use_case

    async def get_preasigned_url(self, media_file: MediaDB) -> Optional[MediaDB]:
        """Get preasigned url"""
        log.info(f"{LOG_SERVICE} Get preasigned url")
        response = await self.media_use_case.get_preasigned_url(media_file)
        if not response:
            raise CustomAPIResponse(status_code=400, message="Error getting presigned URL")
        media_file.s3_key = response.key
        media_file.s3_url = response.url
        media_file.s3_filename = response.filename
        media_file.upload_url_expires_at = response.expires_at
        media_file.s3_extra_info = response.extra_info
        media_file.status = "PENDING"
        media_file.uploaded_at = datetime.now()
        response = await self.media_use_case.create(media_file)
        if not response:
            raise CustomAPIResponse(status_code=400, message="Error creating media")
        media_file.id = str(response.inserted_id)
        return media_file
