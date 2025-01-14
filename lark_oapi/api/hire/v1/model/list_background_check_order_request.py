# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListBackgroundCheckOrderRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.application_id: Optional[str] = None
        self.update_start_time: Optional[str] = None
        self.update_end_time: Optional[str] = None

    @staticmethod
    def builder() -> "ListBackgroundCheckOrderRequestBuilder":
        return ListBackgroundCheckOrderRequestBuilder()


class ListBackgroundCheckOrderRequestBuilder(object):

    def __init__(self) -> None:
        list_background_check_order_request = ListBackgroundCheckOrderRequest()
        list_background_check_order_request.http_method = HttpMethod.GET
        list_background_check_order_request.uri = "/open-apis/hire/v1/background_check_orders"
        list_background_check_order_request.token_types = {AccessTokenType.TENANT}
        self._list_background_check_order_request: ListBackgroundCheckOrderRequest = list_background_check_order_request

    def user_id_type(self, user_id_type: str) -> "ListBackgroundCheckOrderRequestBuilder":
        self._list_background_check_order_request.user_id_type = user_id_type
        self._list_background_check_order_request.add_query("user_id_type", user_id_type)
        return self

    def page_token(self, page_token: str) -> "ListBackgroundCheckOrderRequestBuilder":
        self._list_background_check_order_request.page_token = page_token
        self._list_background_check_order_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListBackgroundCheckOrderRequestBuilder":
        self._list_background_check_order_request.page_size = page_size
        self._list_background_check_order_request.add_query("page_size", page_size)
        return self

    def application_id(self, application_id: str) -> "ListBackgroundCheckOrderRequestBuilder":
        self._list_background_check_order_request.application_id = application_id
        self._list_background_check_order_request.add_query("application_id", application_id)
        return self

    def update_start_time(self, update_start_time: str) -> "ListBackgroundCheckOrderRequestBuilder":
        self._list_background_check_order_request.update_start_time = update_start_time
        self._list_background_check_order_request.add_query("update_start_time", update_start_time)
        return self

    def update_end_time(self, update_end_time: str) -> "ListBackgroundCheckOrderRequestBuilder":
        self._list_background_check_order_request.update_end_time = update_end_time
        self._list_background_check_order_request.add_query("update_end_time", update_end_time)
        return self

    def build(self) -> ListBackgroundCheckOrderRequest:
        return self._list_background_check_order_request
