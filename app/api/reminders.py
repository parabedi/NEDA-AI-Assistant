from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.reminder import (
    ReminderCreate,
    ReminderResponse
)

from app.services.reminder_service import (
    create_reminder_service,
    get_task_reminders_service
)


router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


@router.post(
    "",
    response_model=ReminderResponse
)
def create_reminder(
    reminder: ReminderCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_reminder_service(
            db,
            reminder
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/task/{task_id}",
    response_model=list[ReminderResponse]
)
def get_task_reminders(
    task_id: int,
    db: Session = Depends(get_db)
):
    try:
        return get_task_reminders_service(
            db,
            task_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )