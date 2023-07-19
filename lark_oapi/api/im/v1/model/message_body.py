# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class MessageBody(object):
    _types = {
        "content": str,
    }

    def __init__(self, d):
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessageBodyBuilder":
        return MessageBodyBuilder()


class MessageBodyBuilder(object):
    def __init__(self, message_body: MessageBody = MessageBody({})) -> None:
        self._message_body: MessageBody = message_body

    def content(self, content: str) -> "MessageBodyBuilder":
        self._message_body.content = content
        return self

    def build(self) -> "MessageBody":
        return self._message_body