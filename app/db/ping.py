
import os
from dotenv import load_dotenv
import motor.motor_asyncio

load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGODB_DB", "kanban_db")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

async def test():
    print(await db.command("ping"))

import asyncio
asyncio.run(test())
