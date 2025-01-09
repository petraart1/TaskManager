from psycopg2.pool import SimpleConnectionPool

from .config import DATABASE

from src.models import User
from src.models import Task


__all__ = [
    "register",
    "auth",
    "remove_user",
    "get_all_users",
    "get_all_tasks",
    "add_task",
    "remove_task"
]

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    database=DATABASE["dbname"],
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"]
)

def register(username: str, password: str) -> int:
    users = "users"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                INSERT INTO {users} (username, password)
                VALUES (%s, %s)
                RETURNING id;
            """, (username, password))

            user_id = cursor.fetchone()[0]
            connection.commit()
            return user_id
    finally:
        pool.putconn(connection)


def auth(username: str, password: str) -> str:
    users = "users"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT username, password FROM {users} WHERE username = %s AND password = %s;", (username, password))
            result = cursor.fetchone()
            connection.commit()
            if result:
                return "Auth success"
            else:
                return "Wrong login or password"
    finally:
        pool.putconn(connection)


def remove_user(user_id: int):
    users = "users"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM {users} WHERE id = {user_id};")

            connection.commit()

    finally:
        pool.putconn(connection)

    return "User was removed"


def get_all_users() -> list:
    users = "users"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id, username, password FROM {users};")
            user_list = cursor.fetchall()

            connection.commit()

    finally:
        pool.putconn(connection)

    return [{"id": user[0], "username": user[1], "password": user[2]} for user in user_list]


def add_task(user: User, task: Task) -> str:
    tasks = "tasks"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO {tasks} (id, title, description, status) 
            VALUES (%s, %s, %s, %s);""", (str(user.id), task.title, task.description, task.status))

            connection.commit()
    finally:
        pool.putconn(connection)

    return "task was added"


def remove_task(task_id: int) -> str:
    tasks = "tasks"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM {tasks} WHERE id = {task_id};")

            connection.commit()

    finally:
        pool.putconn(connection)

    return "Task was removed"


def get_user_tasks(user_id: int) -> list:
    tasks = "tasks"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {tasks} WHERE id = {user_id};")
            task_list = cursor.fetchall()

            connection.commit()

    finally:
        pool.putconn(connection)

    return task_list


def get_all_tasks() -> list:
    tasks = "tasks"

    connection = pool.getconn()

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id, user_id, title, description, status FROM {tasks};")
            task_list = cursor.fetchall()

            connection.commit()

    finally:
        pool.putconn(connection)

    return [{"task_id": task[0], "user_id": task[1], "title": task[2], "description": task[3], "status": task[4]}
            for task in task_list]