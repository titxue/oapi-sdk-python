# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryPreHireRequestBody(object):
    _types = {
        "pre_hire_ids": List[str],
        "fields": List[str],
    }

    def __init__(self, d=None):
        self.pre_hire_ids: Optional[List[str]] = None
        self.fields: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryPreHireRequestBodyBuilder":
        return QueryPreHireRequestBodyBuilder()


class QueryPreHireRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_pre_hire_request_body = QueryPreHireRequestBody()

    def pre_hire_ids(self, pre_hire_ids: List[str]) -> "QueryPreHireRequestBodyBuilder":
        self._query_pre_hire_request_body.pre_hire_ids = pre_hire_ids
        return self

    def fields(self, fields: List[str]) -> "QueryPreHireRequestBodyBuilder":
        self._query_pre_hire_request_body.fields = fields
        return self

    def build(self) -> "QueryPreHireRequestBody":
        return self._query_pre_hire_request_body
