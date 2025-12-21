import enum
import sqlalchemy as sa
from sqlalchemy import Enum, ForeignKey, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class TaskStatus(str, enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(Base):
    __tablename__ = "tasks"
    
    __table_args__ = (
        Index("ix_tasks_project_id", "project_id"),
        Index("ix_tasks_assignee_id", "assignee_id"),
        Index("ix_tasks_status", "status"),
)

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    
    status: Mapped[TaskStatus] = mapped_column(
        sa.Enum(
            TaskStatus,
            name="task_status",
            values_callable=lambda enum: [e.value for e in enum],
        ),
        default=TaskStatus.TODO,
        nullable=False,
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )

    assignee_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )