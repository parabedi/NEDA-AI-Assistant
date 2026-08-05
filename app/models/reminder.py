from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    task_id = Column(
        Integer,
        ForeignKey("tasks.id"),
        nullable=False
    )

    remind_at = Column(
        DateTime,
        nullable=False
    )

    is_sent = Column(
    Boolean,
    default=False,
    nullable=False
)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    task = relationship(
        "Task",
        back_populates="reminders"
    )