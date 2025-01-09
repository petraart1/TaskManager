from fastapi import APIRouter
from database import database

remove_user_router = APIRouter()

@remove_user_router.get("remove_user")
async def remove_user():
    return database.re