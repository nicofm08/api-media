"""Wrong use case module."""

from typing import Optional
from app.core.constants import LOG_USECASE
from app.solution.repositories.wrong_repository import WrongRepository
from app.solution.models.wrong_model import WrongDB
from app.core.logger_custom import log
from app.solution.exceptions import errors_excepctions
from pymongo.results import InsertOneResult


class WrongUseCase:
    """Wrong Use Case Class."""

    def __init__(self, wrong_repository: WrongRepository):
        self.wrong_repository = wrong_repository
        self.exception = errors_excepctions.CustomAPIResponse

    async def create_wrong(self, wrong: dict) -> Optional[InsertOneResult]:
        """Create client in repository."""
        log.info(f"{LOG_USECASE} Save wrong")
        response = await self.wrong_repository.create(wrong)
        return response