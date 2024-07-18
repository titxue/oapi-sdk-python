# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListSubjectRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.subject_ids: Optional[List[str]] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListSubjectRequestBuilder":
        return ListSubjectRequestBuilder()


class ListSubjectRequestBuilder(object):

    def __init__(self) -> None:
        list_subject_request = ListSubjectRequest()
        list_subject_request.http_method = HttpMethod.GET
        list_subject_request.uri = "/open-apis/hire/v1/subjects"
        list_subject_request.token_types = {AccessTokenType.TENANT}
        self._list_subject_request: ListSubjectRequest = list_subject_request

    def user_id_type(self, user_id_type: str) -> "ListSubjectRequestBuilder":
        self._list_subject_request.user_id_type = user_id_type
        self._list_subject_request.add_query("user_id_type", user_id_type)
        return self

    def subject_ids(self, subject_ids: List[str]) -> "ListSubjectRequestBuilder":
        self._list_subject_request.subject_ids = subject_ids
        self._list_subject_request.add_query("subject_ids", subject_ids)
        return self

    def page_token(self, page_token: str) -> "ListSubjectRequestBuilder":
        self._list_subject_request.page_token = page_token
        self._list_subject_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListSubjectRequestBuilder":
        self._list_subject_request.page_size = page_size
        self._list_subject_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListSubjectRequest:
        return self._list_subject_request