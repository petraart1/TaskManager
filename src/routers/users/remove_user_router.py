from fastapi import APIRouter

from src.database import database


__all__ = [
    "remove_user_router"
]


remove_user_router = APIRouter()


@remove_user_router.get("/remove_user/{user_id}")
async def remove_user(user_id: int):
    return database.remove_user(user_id)