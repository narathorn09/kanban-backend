from fastapi import APIRouter
from app.api import board

api_router = APIRouter()
api_router.include_router(board.router, prefix="/boards", tags=["boards"])
