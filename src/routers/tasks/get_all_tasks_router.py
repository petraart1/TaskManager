from fastapi import APIRouter
from database import database

__all__ = [
    "get_all_tasks_router"
]

get_all_tasks_router = APIRouter()

@get_all_tasks_router.get("/tasks")
async def get_all_tasks():
    return database.get_all_tasks()