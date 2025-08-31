from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.setup import init_db
from app.api import users, projects, tasks

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await init_db()
    yield
    # shutdown (if needed)
    # await client.close()

app = FastAPI(
    title="Kanban Task Manager",
    description="API documentation for the Kanban Task Manager backend.",
    version="1.0.0",
    docs_url="/docs",           # Swagger UI
    redoc_url="/redoc",         # ReDoc UI
    openapi_url="/openapi.json", # OpenAPI schema
    lifespan=lifespan            # Ensure DB is initialized
)

# Register routes
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(projects.router, prefix="/api", tags=["Projects"])
app.include_router(tasks.router, prefix="/api", tags=["Tasks"])
