from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate


def create_task(
    db: Session,
    task: TaskCreate
):
    db_task = Task(
        **task.model_dump()
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(
    db: Session
):
    return db.query(Task).all()


def get_task_by_id(
    db: Session,
    task_id: int
):
    return (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )


def update_task(
    db: Session,
    task: Task,
    task_data: dict
):
    for key, value in task_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


def update_task_status(
    db: Session,
    task: Task,
    status
):
    task.status = status

    db.commit()
    db.refresh(task)

    return task


def delete_task(
    db: Session,
    task: Task
):
    db.delete(task)
    db.commit()

    return True


def get_filtered_tasks(
    db: Session,
    status=None,
    priority=None
):
    query = db.query(Task)

    if status:
        query = query.filter(
            Task.status == status
        )

    if priority:
        query = query.filter(
            Task.priority == priority
        )

    return query.all()