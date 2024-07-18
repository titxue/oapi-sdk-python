# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateAilySessionRequestBody(object):
    _types = {
        "channel_context": str,
        "metadata": str,
    }

    def __init__(self, d=None):
        self.channel_context: Optional[str] = None
        self.metadata: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAilySessionRequestBodyBuilder":
        return CreateAilySessionRequestBodyBuilder()


class CreateAilySessionRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_aily_session_request_body = CreateAilySessionRequestBody()

    def channel_context(self, channel_context: str) -> "CreateAilySessionRequestBodyBuilder":
        self._create_aily_session_request_body.channel_context = channel_context
        return self

    def metadata(self, metadata: str) -> "CreateAilySessionRequestBodyBuilder":
        self._create_aily_session_request_body.metadata = metadata
        return self

    def build(self) -> "CreateAilySessionRequestBody":
        return self._create_aily_session_request_body