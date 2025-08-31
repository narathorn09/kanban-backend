from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing   import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str  # only for local auth

class UserResponse(UserBase):
    id: str
    auth_provider: str = "local"   # local | google
    google_id: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
