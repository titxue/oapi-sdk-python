# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_aily_session_response_body import GetAilySessionResponseBody


class GetAilySessionResponse(BaseResponse):
    _types = {
        "data": GetAilySessionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetAilySessionResponseBody] = None
        init(self, d, self._types)
