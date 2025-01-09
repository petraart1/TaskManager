from fastapi import APIRouter

from src.database import database


__all__ = [
    "delete_task_router"
]

delete_task_router = APIRouter()

@delete_task_router.get("/delete_task/{task_id}")
async def delete_task(task_id: int):
    return database.remove_task(task_id)