from config import DATABASE
import psycopg2


def get_connection():
    return psycopg2.connect(**DATABASE)

def register(username: str, password: str) -> int:
    users = "users"

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(f"""
            INSERT INTO {users} (username, password)
            VALUES (%s, %s)
            RETURNING user_id;
        """, (username, password))

        user_id = cursor.fetchone()[0]
        connection.commit()
        return user_id
    except psycopg2.IntegrityError as e:
        connection.rollback()
        raise ValueError("Username already exists.")
    finally:
        cursor.close()
        connection.close()

def auth(username: str, password: str) -> str:
    users = "users"

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT username, password FROM {users} WHERE username = %s AND password = %s;", (username, password))
        result = cursor.fetchone()
        if result:
            return "Auth success"
        else:
            return "Wrong login or password"
    finally:
        cursor.close()
        connection.close()


def get_all_users() -> list:
    users = "users"

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"SELECT user_id, username, password FROM {users};")
    users = cursor.fetchall()

    cursor.close()
    connection.close()
    return [{"id": user[0], "username": user[1], "password": user[2]} for user in users]

def add_task(user, task) -> str:
    users = "users"
    tasks = "tasks"

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO {tasks} (user_id, title, description, status) VALUES (%s, %s, %s, %s);",
                   (str(user.id), task.title, task.description, task.status))

    connection.commit()
    cursor.close()
    connection.close()

    return "task was added"

def get_all_tasks(user_id: int) -> list:
    users = "users"
    tasks = "tasks"

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {tasks} WHERE user_id = {user_id};")
    task_list = cursor.fetchall()

    cursor.close()
    connection.close()

    return task_list