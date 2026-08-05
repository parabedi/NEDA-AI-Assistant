from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskStatusUpdate
)
from app.services import task_service


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return task_service.create_task(db, task)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    status: str | None = Query(
        default=None
    ),
    priority: str | None = Query(
        default=None
    ),
    db: Session = Depends(get_db)
):
    return task_service.get_filtered_tasks(
        db,
        status,
        priority
    )

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = task_service.get_task_by_id(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_task_status(
    task_id: int,
    status_update: TaskStatusUpdate,
    db: Session = Depends(get_db)
):
    task = task_service.get_task_by_id(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task_service.update_task_status(
        db,
        task,
        status_update.status
    )


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskCreate,
    db: Session = Depends(get_db)
):
    task = task_service.get_task_by_id(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task_service.update_task(
    db,
    task,
    task_update.model_dump()
)


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = task_service.get_task_by_id(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task_service.delete_task(
        db,
        task
    )

    return {
        "message": "Task deleted successfully"
    }