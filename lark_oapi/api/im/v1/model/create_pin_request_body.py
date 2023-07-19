# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreatePinRequestBody(object):
    _types = {
        "message_id": str,
    }

    def __init__(self, d):
        self.message_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreatePinRequestBodyBuilder":
        return CreatePinRequestBodyBuilder()


class CreatePinRequestBodyBuilder(object):
    def __init__(self, create_pin_request_body: CreatePinRequestBody = CreatePinRequestBody({})) -> None:
        self._create_pin_request_body: CreatePinRequestBody = create_pin_request_body

    def message_id(self, message_id: str) -> "CreatePinRequestBodyBuilder":
        self._create_pin_request_body.message_id = message_id
        return self

    def build(self) -> "CreatePinRequestBody":
        return self._create_pin_request_body