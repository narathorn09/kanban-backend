from beanie import Document, Link
from datetime import datetime
from typing import Optional
from app.models.user import User
from app.models.project import Project

class Task(Document):
    title: str
    description: Optional[str] = None
    status: str = "todo"     # todo | doing | done
    project: Link[Project]   # relationship to Project
    assignee: Optional[Link[User]] = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    class Settings:
        name = "tasks"
