from sqlalchemy.orm import Session

from app.repositories import task_repository
from app.schemas.task import TaskCreate


def create_task(
    db: Session,
    task: TaskCreate
):
    return task_repository.create_task(
        db,
        task
    )


def get_tasks(
    db: Session
):
    return task_repository.get_tasks(db)


def get_task_by_id(
    db: Session,
    task_id: int
):
    return task_repository.get_task_by_id(
        db,
        task_id
    )


def delete_task(
    db: Session,
    task
):
    return task_repository.delete_task(
        db,
        task
    )


def update_task_status(
    db: Session,
    task,
    status
):
    return task_repository.update_task_status(
        db,
        task,
        status
    )


def get_filtered_tasks(
    db: Session,
    status=None,
    priority=None
):
    return task_repository.get_filtered_tasks(
        db,
        status,
        priority
    )

def update_task(
    db: Session,
    task,
    task_data: dict
):
    return task_repository.update_task(
        db,
        task,
        task_data
    )