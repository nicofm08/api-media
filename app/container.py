"""Dependency Injection Container for FastAPI Application"""

from fastapi import Depends
from app.solution.repositories.media_repository import MediaRepository
from app.solution.use_cases.media_use_case import MediaUseCase
from app.solution.services.media_service import MediaService
from app.solution.repositories.wrong_repository import WrongRepository
from app.solution.handlers.media_handler import MediaHandler


def wrong_repository():
    """Wrong Repository Dependency Provider"""
    return WrongRepository()


def media_repository():
    """Media Repository Dependency Provider"""
    return MediaRepository()


def media_use_case(
    mr_repo_inject: MediaRepository = Depends(media_repository),
) -> MediaUseCase:
    """Media UseCase Dependency Provider"""
    return MediaUseCase(
        media_repository=mr_repo_inject,
    )


def media_service(
    mr_use_case_inject: MediaUseCase = Depends(media_use_case),
) -> MediaService:
    """Media Service Dependency Provider"""
    return MediaService(
        media_use_case=mr_use_case_inject,
    )


def media_handler(mr_service_inject: MediaService = Depends(media_service)):
    """Media Handler Dependency Provider"""
    return MediaHandler(
        service=mr_service_inject,
    )
