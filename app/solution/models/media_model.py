"""Media model module."""

from typing import Dict, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from bson import ObjectId

class MediaDB(BaseModel):
    type: Optional[str] = "IMAGE"
    filename_original: Optional[str] = ""
    s3_key: Optional[str] = ""
    s3_url: Optional[str] = ""
    s3_filename: Optional[str] = ""
    upload_url_expires_at: Optional[datetime] = None
    s3_extra_info: Optional[Dict] = None

    model_config = ConfigDict(
        extra="allow",
        json_encoders={
            ObjectId: str,
            datetime: lambda v: v.isoformat()
        },
        arbitrary_types_allowed=True
    )

class MediaPublishTrigger(BaseModel):
    channel: Optional[str] = "media_uploaded"
    s3_filename: Optional[str] = ""
    command: Optional[str] = "PROCESS"