# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateMessageRequestBody(object):
    _types = {
        "receive_id": str,
        "msg_type": str,
        "content": str,
        "uuid": str,
    }

    def __init__(self, d):
        self.receive_id: Optional[str] = None
        self.msg_type: Optional[str] = None
        self.content: Optional[str] = None
        self.uuid: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMessageRequestBodyBuilder":
        return CreateMessageRequestBodyBuilder()


class CreateMessageRequestBodyBuilder(object):
    def __init__(self, create_message_request_body: CreateMessageRequestBody = CreateMessageRequestBody({})) -> None:
        self._create_message_request_body: CreateMessageRequestBody = create_message_request_body

    def receive_id(self, receive_id: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.receive_id = receive_id
        return self

    def msg_type(self, msg_type: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.msg_type = msg_type
        return self

    def content(self, content: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.content = content
        return self

    def uuid(self, uuid: str) -> "CreateMessageRequestBodyBuilder":
        self._create_message_request_body.uuid = uuid
        return self

    def build(self) -> "CreateMessageRequestBody":
        return self._create_message_request_body