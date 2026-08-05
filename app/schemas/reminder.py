from datetime import datetime
from pydantic import BaseModel


class ReminderBase(BaseModel):
    remind_at: datetime


class ReminderCreate(ReminderBase):
    task_id: int


class ReminderResponse(ReminderBase):
    id: int
    task_id: int
    is_sent: bool
    created_at: datetime

    class Config:
        from_attributes = True