__all__ = [
    "Task"
]


class Task:
    _id: int
    _title: str
    _description: str
    _status: str

    def __init__(self, name: str, desc: str = "empty") -> None:
        self._title = name
        self._description = desc
        self._status = "none"

    def change_title(self, new_title: str) -> None:
        self._title = new_title

    def change_description(self, new_description: str) -> None:
        self._description = new_description

    def change_status(self, new_status: str) -> None:
        self._status = new_status

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def status(self) -> str:
        return self._status