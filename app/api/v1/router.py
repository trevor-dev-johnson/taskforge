from fastapi import APIRouter

from app.api.v1 import projects, tasks

api_router = APIRouter()

api_router.include_router(
    projects.router,
    prefix="/projects",
    tags=["projects"],
)

api_router.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["tasks"],
)
