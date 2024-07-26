# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListExamMarkingTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id: Optional[str] = None
        self.activity_status: Optional[int] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListExamMarkingTaskRequestBuilder":
        return ListExamMarkingTaskRequestBuilder()


class ListExamMarkingTaskRequestBuilder(object):

    def __init__(self) -> None:
        list_exam_marking_task_request = ListExamMarkingTaskRequest()
        list_exam_marking_task_request.http_method = HttpMethod.GET
        list_exam_marking_task_request.uri = "/open-apis/hire/v1/exam_marking_tasks"
        list_exam_marking_task_request.token_types = {AccessTokenType.TENANT}
        self._list_exam_marking_task_request: ListExamMarkingTaskRequest = list_exam_marking_task_request

    def page_size(self, page_size: int) -> "ListExamMarkingTaskRequestBuilder":
        self._list_exam_marking_task_request.page_size = page_size
        self._list_exam_marking_task_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListExamMarkingTaskRequestBuilder":
        self._list_exam_marking_task_request.page_token = page_token
        self._list_exam_marking_task_request.add_query("page_token", page_token)
        return self

    def user_id(self, user_id: str) -> "ListExamMarkingTaskRequestBuilder":
        self._list_exam_marking_task_request.user_id = user_id
        self._list_exam_marking_task_request.add_query("user_id", user_id)
        return self

    def activity_status(self, activity_status: int) -> "ListExamMarkingTaskRequestBuilder":
        self._list_exam_marking_task_request.activity_status = activity_status
        self._list_exam_marking_task_request.add_query("activity_status", activity_status)
        return self

    def user_id_type(self, user_id_type: str) -> "ListExamMarkingTaskRequestBuilder":
        self._list_exam_marking_task_request.user_id_type = user_id_type
        self._list_exam_marking_task_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListExamMarkingTaskRequest:
        return self._list_exam_marking_task_request