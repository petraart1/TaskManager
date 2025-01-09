from fastapi import APIRouter

from src.models import User
from src.models import Task
from src.database import database


__all__ = [
    "add_task_router"
]

add_task_router = APIRouter()

@add_task_router.get("/task")
async def add_task(username: str, password: str, name: str, description: str = "empty") -> str:
    user = User(username, password)
    task = Task(name, description)
    users = database.get_all_users()
    # костыль
    for i in users:
        if i["username"] == username:
            user.set_id(i["id"])
    return database.add_task(user, task)