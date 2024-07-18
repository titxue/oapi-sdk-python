# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_aily_session_run_response_body import ListAilySessionRunResponseBody


class ListAilySessionRunResponse(BaseResponse):
    _types = {
        "data": ListAilySessionRunResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAilySessionRunResponseBody] = None
        init(self, d, self._types)