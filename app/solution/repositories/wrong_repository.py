"""Wrong Validation Repository"""

from datetime import datetime
from app.solution.models.wrong_model import WrongDB
from typing import Optional
from app.core.constants import LOG_REPOSITORY
from app.core.logger_custom import log
from app.core.mongo import MongoClient
from app.core.utils import UtilsCore
from pymongo.results import InsertOneResult


class WrongRepository:
    """Wrong Repository Class"""

    def __init__(self):
        self.mongo = MongoClient("api-media", "wrong_validation")
        self.utils = UtilsCore()

    async def create(self, wrong) -> Optional[InsertOneResult]:
        """Create Wrong in MongoDB."""
        log.info(f"{LOG_REPOSITORY} Save wrong")
        log.info(f"{LOG_REPOSITORY}", extra={"extra": f"Wrong: {wrong}"})

        try:
            if isinstance(wrong, list):
                if not wrong:
                    log.warning(
                        f"{LOG_REPOSITORY} Empty list, nothing is saved"
                    )
                    return None
                wrong = wrong[0]

            if hasattr(wrong, "dict"):
                wrong = wrong.dict()

            if not isinstance(wrong, dict):
                raise ValueError(f"Expected dict, got {type(wrong)}")

            wrong["created_at"] = datetime.now()
            result = await self.mongo.insert_one(wrong)
            return result if result else None

        except Exception as e:
            log.error(f"{LOG_REPOSITORY} Error inserting wrong: {e}")
            return None
