# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Task(object):
    _types = {
        "task_id": str,
        "folded": bool,
    }

    def __init__(self, d=None):
        self.task_id: Optional[str] = None
        self.folded: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskBuilder":
        return TaskBuilder()


class TaskBuilder(object):
    def __init__(self) -> None:
        self._task = Task()

    def task_id(self, task_id: str) -> "TaskBuilder":
        self._task.task_id = task_id
        return self

    def folded(self, folded: bool) -> "TaskBuilder":
        self._task.folded = folded
        return self

    def build(self) -> "Task":
        return self._task
