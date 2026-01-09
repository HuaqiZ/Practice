from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class RunRecord(BaseModel):
    id: int
    job_name: str
    start_time: datetime
    status: str
    end_time: Optional[datetime]
    message: Optional[str] = None
