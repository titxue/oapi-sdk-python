# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchUpdateJobManagerRequestBody(object):
    _types = {
        "recruiter_id": str,
        "assistant_id_list": List[str],
        "hiring_manager_id_list": List[str],
        "update_option_list": List[int],
        "creator_id": str,
    }

    def __init__(self, d=None):
        self.recruiter_id: Optional[str] = None
        self.assistant_id_list: Optional[List[str]] = None
        self.hiring_manager_id_list: Optional[List[str]] = None
        self.update_option_list: Optional[List[int]] = None
        self.creator_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchUpdateJobManagerRequestBodyBuilder":
        return BatchUpdateJobManagerRequestBodyBuilder()


class BatchUpdateJobManagerRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_update_job_manager_request_body = BatchUpdateJobManagerRequestBody()

    def recruiter_id(self, recruiter_id: str) -> "BatchUpdateJobManagerRequestBodyBuilder":
        self._batch_update_job_manager_request_body.recruiter_id = recruiter_id
        return self

    def assistant_id_list(self, assistant_id_list: List[str]) -> "BatchUpdateJobManagerRequestBodyBuilder":
        self._batch_update_job_manager_request_body.assistant_id_list = assistant_id_list
        return self

    def hiring_manager_id_list(self, hiring_manager_id_list: List[str]) -> "BatchUpdateJobManagerRequestBodyBuilder":
        self._batch_update_job_manager_request_body.hiring_manager_id_list = hiring_manager_id_list
        return self

    def update_option_list(self, update_option_list: List[int]) -> "BatchUpdateJobManagerRequestBodyBuilder":
        self._batch_update_job_manager_request_body.update_option_list = update_option_list
        return self

    def creator_id(self, creator_id: str) -> "BatchUpdateJobManagerRequestBodyBuilder":
        self._batch_update_job_manager_request_body.creator_id = creator_id
        return self

    def build(self) -> "BatchUpdateJobManagerRequestBody":
        return self._batch_update_job_manager_request_body