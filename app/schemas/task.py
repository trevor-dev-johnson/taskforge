from pydantic import BaseModel
from app.models.task import TaskStatus

class TaskCreate(BaseModel):
  title: str
  project_id: int
  assignee_id: int | None = None
  
class TaskOut(BaseModel):
  id: int
  title: str
  status: TaskStatus
  project_id: int
  assignee_id: int | None
  
  class Config:
    from_attributes = True
    
class TaskStatusUpdate(BaseModel):
    status: TaskStatus