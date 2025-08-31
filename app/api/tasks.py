from fastapi import APIRouter, HTTPException
from app.models.task import Task
from app.models.project import Project
from app.models.user import User

router = APIRouter()

@router.post("/tasks", response_model=Task)
async def create_task(title: str, project_id: str, assignee_id: str = None):
    project = await Project.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    assignee = None
    if assignee_id:
        assignee = await User.get(assignee_id)

    task = Task(title=title, project=project, assignee=assignee)
    await task.insert()
    return task

@router.get("/tasks/{project_id}", response_model=list[Task])
async def list_tasks(project_id: str):
    return await Task.find(Task.project.id == project_id).to_list()
