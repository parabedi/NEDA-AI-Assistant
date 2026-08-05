from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.repositories.reminder_repository import (
    create_reminder,
    get_reminders_by_task
)
from app.repositories.task_repository import get_task_by_id
from app.schemas.reminder import ReminderCreate


def create_reminder_service(
    db: Session,
    reminder: ReminderCreate
):
    # Business Rule 1
    task = get_task_by_id(db, reminder.task_id)

    if task is None:
        raise ValueError("Task not found")

    # Business Rule 2
    if reminder.remind_at < datetime.now(timezone.utc):
        raise ValueError("Reminder time cannot be in the past")

    return create_reminder(db, reminder)


def get_task_reminders_service(
    db: Session,
    task_id: int
):
    return get_reminders_by_task(db, task_id)

from app.repositories.reminder_repository import (
    create_reminder,
    get_reminders_by_task
)

from app.repositories.task_repository import (
    get_task_by_id
)


from app.schemas.reminder import ReminderCreate


def create_reminder_service(
    db: Session,
    reminder: ReminderCreate
):
    # Check parent task exists
    task = get_task_by_id(
        db,
        reminder.task_id
    )

    if task is None:
        raise ValueError(
            "Task not found"
        )

    # Validate reminder time
    if reminder.remind_at < datetime.now(timezone.utc):
        raise ValueError(
            "Reminder time cannot be in the past"
        )

    return create_reminder(
        db,
        reminder
    )


def get_task_reminders_service(
    db: Session,
    task_id: int
):
    task = get_task_by_id(
        db,
        task_id
    )

    if task is None:
        raise ValueError(
            "Task not found"
        )

    return get_reminders_by_task(
        db,
        task_id
    )