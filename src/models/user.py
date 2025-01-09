__all__ = [
    "User"
]


class User:
    _id: int
    _username: str
    _password: str
    _tasks: list #list of tasks id`s in database

    def __init__(self, username: str, password: str) -> None:
        self._username = username
        self._password = password

    def set_username(self, new_username: str) -> None:
        self._username = new_username

    def set_password(self, new_password: str) -> None:
        self._password = new_password

    def set_id(self, new_id: int) -> None:
        self._id = new_id

    '''def add_task_without_description(self, task_name: str) -> None:
        task = Task(task_name)
        self._tasks[task_name] = Task(task_name)

    def add_task_with_description(self, task_name: str, task_desc: str) -> None:
        self._tasks[task_name] = Task(task_name, task_desc)'''

    '''def get_all_tasks(self) -> list:
        return database.get_all_tasks(self._id)'''

    @property
    def id(self) -> int:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password