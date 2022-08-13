import enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: Optional[str] = None
    user_id: int
    title: str
    description: Optional[str]
    is_active: bool
    end_time: datetime
    created_at: datetime

class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    end_time: datetime