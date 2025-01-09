from fastapi import APIRouter

__all__ = [
    "delete_task_router"
]

delete_task_router = APIRouter()

@delete_task_router.get("/delete_task")
async def delete_task():
    pass