# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .forward_thread_request_body import ForwardThreadRequestBody


class ForwardThreadRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.receive_id_type: Optional[str] = None
        self.uuid: Optional[str] = None
        self.thread_id: Optional[str] = None
        self.request_body: Optional[ForwardThreadRequestBody] = None

    @staticmethod
    def builder() -> "ForwardThreadRequestBuilder":
        return ForwardThreadRequestBuilder()


class ForwardThreadRequestBuilder(object):

    def __init__(self) -> None:
        forward_thread_request = ForwardThreadRequest()
        forward_thread_request.http_method = HttpMethod.POST
        forward_thread_request.uri = "/open-apis/im/v1/threads/:thread_id/forward"
        forward_thread_request.token_types = {AccessTokenType.TENANT}
        self._forward_thread_request: ForwardThreadRequest = forward_thread_request

    def receive_id_type(self, receive_id_type: str) -> "ForwardThreadRequestBuilder":
        self._forward_thread_request.receive_id_type = receive_id_type
        self._forward_thread_request.add_query("receive_id_type", receive_id_type)
        return self

    def uuid(self, uuid: str) -> "ForwardThreadRequestBuilder":
        self._forward_thread_request.uuid = uuid
        self._forward_thread_request.add_query("uuid", uuid)
        return self

    def thread_id(self, thread_id: str) -> "ForwardThreadRequestBuilder":
        self._forward_thread_request.thread_id = thread_id
        self._forward_thread_request.paths["thread_id"] = str(thread_id)
        return self

    def request_body(self, request_body: ForwardThreadRequestBody) -> "ForwardThreadRequestBuilder":
        self._forward_thread_request.request_body = request_body
        self._forward_thread_request.body = request_body
        return self

    def build(self) -> ForwardThreadRequest:
        return self._forward_thread_request
