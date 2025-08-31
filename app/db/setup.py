import motor.motor_asyncio
from beanie import init_beanie
from app.models.user import User
from app.models.project import Project
from app.models.task import Task

# Load environment variables from .env file
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGODB_DB", "kanban_db")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

async def init_db():
    await init_beanie(
        database=client[DB_NAME],
        document_models=[User, Project, Task]
    )
