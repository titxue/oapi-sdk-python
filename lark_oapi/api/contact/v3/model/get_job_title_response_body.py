# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_title import JobTitle


class GetJobTitleResponseBody(object):
    _types = {
        "job_title": JobTitle,
    }

    def __init__(self, d):
        self.job_title: Optional[JobTitle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetJobTitleResponseBodyBuilder":
        return GetJobTitleResponseBodyBuilder()


class GetJobTitleResponseBodyBuilder(object):
    def __init__(self, get_job_title_response_body: GetJobTitleResponseBody = GetJobTitleResponseBody({})) -> None:
        self._get_job_title_response_body: GetJobTitleResponseBody = get_job_title_response_body

    def job_title(self, job_title: JobTitle) -> "GetJobTitleResponseBodyBuilder":
        self._get_job_title_response_body.job_title = job_title
        return self

    def build(self) -> "GetJobTitleResponseBody":
        return self._get_job_title_response_body