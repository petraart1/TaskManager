from fastapi import APIRouter

from src.models import User
from src.database import database


__all__ = [
    "login_router"
]


login_router = APIRouter()


@login_router.get("/login")
async def login(username: str, password: str) -> str:
    user = User(username, password)
    return database.auth(username, password)