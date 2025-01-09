from fastapi import APIRouter
from database import database


__all__ = [
    "get_all_users_router"
]

get_all_users_router = APIRouter()

@get_all_users_router.get("/users")
async def get_users():
    return database.get_all_users()