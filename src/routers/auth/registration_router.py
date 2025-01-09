from fastapi import APIRouter

from src.models import User
from src.database import database


__all__ = [
    "registration_router"
]


registration_router = APIRouter()


@registration_router.get("/register")
async def registration(username: str, password: str) -> dict[str, int | str]:
    user = User(username, password)
    user_id = database.register(username, password)
    return {"user id" : user_id, "username": user.username, "password": user.password}