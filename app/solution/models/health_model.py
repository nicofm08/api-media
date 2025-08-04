"""Model for health check response."""

from typing import Dict
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Model for health check response."""

    message: str


class ConstantsResponse(BaseModel):
    """Model for constants response."""

    root: Dict[str, str]
