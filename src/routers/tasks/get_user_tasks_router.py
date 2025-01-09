from fastapi import APIRouter

from src.database import database


__all__ = [
    "get_user_tasks_router"
]


get_user_tasks_router = APIRouter()


@get_user_tasks_router.get("/tasks/{user_id}")
async def get_tasks(user_id: int):
    return database.get_user_tasks(user_id)