# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.usage: Optional[str] = None

    @staticmethod
    def builder() -> "ListLocationRequestBuilder":
        return ListLocationRequestBuilder()


class ListLocationRequestBuilder(object):

    def __init__(self) -> None:
        list_location_request = ListLocationRequest()
        list_location_request.http_method = HttpMethod.GET
        list_location_request.uri = "/open-apis/hire/v1/locations"
        list_location_request.token_types = {AccessTokenType.TENANT}
        self._list_location_request: ListLocationRequest = list_location_request

    def page_token(self, page_token: str) -> "ListLocationRequestBuilder":
        self._list_location_request.page_token = page_token
        self._list_location_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListLocationRequestBuilder":
        self._list_location_request.page_size = page_size
        self._list_location_request.add_query("page_size", page_size)
        return self

    def usage(self, usage: str) -> "ListLocationRequestBuilder":
        self._list_location_request.usage = usage
        self._list_location_request.add_query("usage", usage)
        return self

    def build(self) -> ListLocationRequest:
        return self._list_location_request
