from sqlalchemy.orm import Session

from app.models.project import Project

class ProjectService:
  def __init__(self, db: Session):
    self.db = db
    
  def create_project(self, *, name: str) -> Project:
    project = Project(name=name)
    self.db.add(project)
    self.db.commit()
    self.db.refresh(project)
    return project