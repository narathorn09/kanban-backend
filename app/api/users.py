from fastapi import APIRouter, HTTPException
from app.models.user import User

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(email: str):
    existing = await User.find_one(User.email == email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=email)
    await user.insert()
    return user

@router.get("/users", response_model=list[User])
async def list_users():
    return await User.find_all().to_list()
