"""Wrong model module."""

from typing import Optional, Any, Dict
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from bson import ObjectId


class WrongDB(BaseModel):
    created_at: Optional[datetime] = None
    detail: Optional[str] = None
    link: Optional[str] = None
    status: Optional[str] = None
    
    model_config = ConfigDict(
        extra="allow",
        json_encoders={
            ObjectId: str,
            datetime: lambda v: v.isoformat()
        },
        arbitrary_types_allowed=True
    )