# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OnboardingTask(object):
    _types = {
        "task_name": str,
        "task_status": str,
        "operator_id": str,
    }

    def __init__(self, d=None):
        self.task_name: Optional[str] = None
        self.task_status: Optional[str] = None
        self.operator_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OnboardingTaskBuilder":
        return OnboardingTaskBuilder()


class OnboardingTaskBuilder(object):
    def __init__(self) -> None:
        self._onboarding_task = OnboardingTask()

    def task_name(self, task_name: str) -> "OnboardingTaskBuilder":
        self._onboarding_task.task_name = task_name
        return self

    def task_status(self, task_status: str) -> "OnboardingTaskBuilder":
        self._onboarding_task.task_status = task_status
        return self

    def operator_id(self, operator_id: str) -> "OnboardingTaskBuilder":
        self._onboarding_task.operator_id = operator_id
        return self

    def build(self) -> "OnboardingTask":
        return self._onboarding_task