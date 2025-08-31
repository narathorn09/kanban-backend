from fastapi import APIRouter, HTTPException
from app.models.project import Project
from app.models.user import User

router = APIRouter()

@router.post("/projects", response_model=Project)
async def create_project(name: str, owner_id: str):
    owner = await User.get(owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    project = Project(name=name, owner=owner)
    await project.insert()
    return project

@router.get("/projects", response_model=list[Project])
async def list_projects():
    return await Project.find_all().to_list()
