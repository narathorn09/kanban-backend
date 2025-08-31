from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_boards():
    return [{"id": 1, "name": "Sample Board"}]
