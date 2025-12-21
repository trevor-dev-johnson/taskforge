from sqlalchemy.orm import Session

from app.models.task import Task, TaskStatus


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(
        self,
        *,
        title: str,
        project_id: int,
        assignee_id: int | None = None,
    ) -> Task:
        task = Task(
            title=title,
            project_id=project_id,
            assignee_id=assignee_id,
            status=TaskStatus.TODO,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def list_tasks_for_project(self, project_id: int) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.project_id == project_id)
            .order_by(Task.id)
            .all()
        )

    def update_task_status(
        self,
        *,
        task_id: int,
        status: TaskStatus,
    ) -> Task | None:
        task = self.db.get(Task, task_id)
        if not task:
            return None

        task.status = status
        self.db.commit()
        self.db.refresh(task)
        return task
