from pydantic import BaseModel
from typing import Any, Optional

class ErrorResponse(BaseModel):
    code: int
    message: str

class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[ErrorResponse] = None

