from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Task(Base):
  __tablename__ = "tasks"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(255), nullable=False)
  status: Mapped[str] = mapped_column(String(50), default="todo")
  
  project_id: Mapped[int] = mapped_column(
    ForeignKey("projects.id", ondelete="CASCADE"),
    nullable=False,
  )
  
  assignee_id: Mapped[int | None] = mapped_column(
    ForeignKey("users.id", ondelete="SET NULL"),
    nullable=True
  )