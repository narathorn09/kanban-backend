from beanie import Document
from pydantic import EmailStr
from datetime import datetime
from typing import Optional

class User(Document):
    email: EmailStr
    password_hash: Optional[str] = None   # null if Google login
    auth_provider: str = "local"          # local | google
    google_id: Optional[str] = None
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "users"   # MongoDB collection name
