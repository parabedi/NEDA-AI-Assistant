from sqlalchemy import Integer, DateTime, String, Boolean, Column
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.database import Base

from app.schemas.enums import TaskType, Priority, RecurrenceType
from enum import Enum

class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCELLED = "CANCELLED"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    task_type = Column(
        String,
        nullable=False
    )

    priority = Column(
        String,
        nullable=False,
        default="medium"
    )


    start_date = Column(
        DateTime,
        nullable=True
    )

    due_date = Column(
        DateTime,
        nullable=True
    )

    recurrence_type = Column(
        String,
        nullable=False,
        default="none"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    status=Column(
       String, 
       nullable=False,
       default="TODO"   
    )
    reminders = relationship(
    "Reminder",
    back_populates="task",
    cascade="all, delete-orphan"
)