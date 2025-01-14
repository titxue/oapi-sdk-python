# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .transit_task_pre_hire_request_body import TransitTaskPreHireRequestBody


class TransitTaskPreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.pre_hire_id: Optional[str] = None
        self.request_body: Optional[TransitTaskPreHireRequestBody] = None

    @staticmethod
    def builder() -> "TransitTaskPreHireRequestBuilder":
        return TransitTaskPreHireRequestBuilder()


class TransitTaskPreHireRequestBuilder(object):

    def __init__(self) -> None:
        transit_task_pre_hire_request = TransitTaskPreHireRequest()
        transit_task_pre_hire_request.http_method = HttpMethod.POST
        transit_task_pre_hire_request.uri = "/open-apis/corehr/v2/pre_hires/:pre_hire_id/transit_task"
        transit_task_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._transit_task_pre_hire_request: TransitTaskPreHireRequest = transit_task_pre_hire_request

    def pre_hire_id(self, pre_hire_id: str) -> "TransitTaskPreHireRequestBuilder":
        self._transit_task_pre_hire_request.pre_hire_id = pre_hire_id
        self._transit_task_pre_hire_request.paths["pre_hire_id"] = str(pre_hire_id)
        return self

    def request_body(self, request_body: TransitTaskPreHireRequestBody) -> "TransitTaskPreHireRequestBuilder":
        self._transit_task_pre_hire_request.request_body = request_body
        self._transit_task_pre_hire_request.body = request_body
        return self

    def build(self) -> TransitTaskPreHireRequest:
        return self._transit_task_pre_hire_request
