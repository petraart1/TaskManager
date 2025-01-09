from fastapi import APIRouter

from .auth.login_router import login_router
from .auth.registration_router import registration_router

from .tasks.get_all_tasks_router import get_all_tasks_router
from .tasks.get_user_tasks_router import get_user_tasks_router
from .tasks.add_task_router import add_task_router
from .tasks.delete_task_router import delete_task_router

from .users import get_all_users_router

__all__ = [
    "root_router"
]

root_router = APIRouter(prefix="/api")
root_router.include_router(login_router)

root_router.include_router(registration_router)
root_router.include_router(get_all_tasks_router)
root_router.include_router(get_user_tasks_router)
root_router.include_router(add_task_router)
root_router.include_router(delete_task_router)

root_router.include_router(get_all_users_router)