from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.task import TaskCreate, TaskOut, TaskStatusUpdate
from app.services.task_service import TaskService
from app.models.task import TaskStatus

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create_task(
  task:TaskCreate,
  db: Session = Depends(get_db),
):
  service = TaskService(db)
  try:
    return service.create_task(
      title=task.title,
      project_id=task.project_id,
      assignee_id=task.assignee_id,
    )
  except Exception:
    raise HTTPException(status_code=400, detail="Invalid project or assignee")
  
@router.get("/project/{project_id}", response_model=list[TaskOut])
def list_tasks_for_project(
  project_id: int,
  db: Session = Depends(get_db),
):
  service = TaskService(db)
  return service.list_tasks_for_project(project_id)

@router.patch("/{task_id}/status", response_model=TaskOut)
def update_task_status(
  task_id: int,
  update: TaskStatusUpdate,
  db: Session = Depends(get_db),
):
  service = TaskService(db)
  task = service.update_task_status(
    task_id=task_id,
    status=update.status,
  )
  
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  
  return task