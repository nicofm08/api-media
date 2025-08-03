"""Custom Exceptions."""

from typing import Any, Optional
from fastapi import HTTPException

from app.solution.models.response_model import APIResponse, ErrorResponse


class CustomAPIResponse(HTTPException):
    """Custom API Response."""

    def __init__(
        self,
        status_code: int,
        message: str = "",
        data: Optional[Any] = None,
    ):
        """Initialize Custom API Response."""
        detail = APIResponse(
            success=False,
            data=data,
            error=ErrorResponse(code=status_code, message=message),
        ).dict()

        super().__init__(status_code=status_code, detail=detail)
