# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class JobCategory(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "active_status": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobCategoryBuilder":
        return JobCategoryBuilder()


class JobCategoryBuilder(object):
    def __init__(self, job_category: JobCategory = JobCategory({})) -> None:
        self._job_category: JobCategory = job_category

    def id(self, id: str) -> "JobCategoryBuilder":
        self._job_category.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobCategoryBuilder":
        self._job_category.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobCategoryBuilder":
        self._job_category.en_name = en_name
        return self

    def active_status(self, active_status: int) -> "JobCategoryBuilder":
        self._job_category.active_status = active_status
        return self

    def build(self) -> "JobCategory":
        return self._job_category