
from datetime import date,datetime

from pydantic import BaseModel,ConfigDict, model_validator

from app.schemas.enums import TaskType, Priority, RecurrenceType


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    task_type: TaskType
    priority: Priority
    start_date: date
    due_date: date
    recurrence_type: RecurrenceType

    @model_validator(mode="after")
    def validate_task(self):

        if self.due_date < self.start_date:
            raise ValueError(
                "due_date cannot be earlier than start_date"
            )

        if (
            self.task_type == TaskType.NON_ROUTINE
            and self.recurrence_type != RecurrenceType.NONE
        ):
            raise ValueError(
                "Non-routine tasks cannot have recurrence."
            )

        return self



class TaskUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str | None = None
    description: str | None = None
    task_type: TaskType | None = None
    priority: Priority | None = None
    start_date: date | None = None
    due_date: date | None = None
    recurrence_type: RecurrenceType | None = None



class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    task_type: TaskType
    priority: Priority
    completed: bool
    start_date: date
    due_date: date
    recurrence_type: RecurrenceType
    created_at: datetime
    updated_at: datetime


