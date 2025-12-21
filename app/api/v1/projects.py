from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.project_service import ProjectService
from app.schemas.project import ProjectCreate, ProjectOut

router = APIRouter()


@router.post("/", response_model=ProjectOut)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
):
    service = ProjectService(db)
    return service.create_project(name=project.name)
