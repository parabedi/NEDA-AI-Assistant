from sqlalchemy import Integer, DateTime, String, Boolean, Column
from datetime import datetime

from app.database.database import Base

from app.schemas.enums import TaskType, Priority, RecurrenceType


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

    completed = Column(
        Boolean,
        default=False
    )

    start_date = Column(
        DateTime,
        nullable=False
    )

    due_date = Column(
        DateTime,
        nullable=False
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