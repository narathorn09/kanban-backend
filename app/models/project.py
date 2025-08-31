from beanie import Document, Link
from datetime import datetime
from typing import Optional
from app.models.user import User

class Project(Document):
    name: str
    description: Optional[str] = None
    owner: Link[User]   # relationship to User
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "projects"
