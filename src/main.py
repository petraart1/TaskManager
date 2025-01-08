from fastapi import FastAPI
from task import Task
from user import User
from database import database

app = FastAPI()
tasks = [Task("a", "b")]
users = {}

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@app.get("/register")
async def registration(username: str, password: str) -> dict[str, str]:
    user = User(username, password)
    users[username] = user
    user_id = database.register(username, password)
    return {"username": user.username, "password": user.password}

@app.get("/users")
async def get_users():
    return database.get_all_users()

'''@app.get("/me")
async def get_me():
    return'''

@app.get("/auth")
async def authentication(username: str, password: str) -> str:
    user = User(username, password)
    return database.auth(username, password)

@app.get("/tasks/{user_id}")
async def get_tasks(user_id: int):
    return database.get_all_tasks(user_id)


@app.get("/task")
async def add_task(username: str, password: str, name: str, description: str = "empty") -> str:
    user = User(username, password)
    task = Task(name, description)
    users = database.get_all_users()
    # костыль
    for i in users:
        if i["username"] == username:
            user.set_id(i["id"])
    return database.add_task(user, task)