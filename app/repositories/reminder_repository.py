from sqlalchemy.orm import Session

from app.models.reminder import Reminder
from app.schemas.reminder import ReminderCreate


def create_reminder(
    db: Session,
    reminder: ReminderCreate
):
    db_reminder = Reminder(
        task_id=reminder.task_id,
        remind_at=reminder.remind_at
    )

    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)

    return db_reminder


def get_reminders_by_task(
    db: Session,
    task_id: int
):
    return (
        db.query(Reminder)
        .filter(Reminder.task_id == task_id)
        .all()
    )