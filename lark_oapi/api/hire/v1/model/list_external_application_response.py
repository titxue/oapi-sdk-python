# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_external_application_response_body import ListExternalApplicationResponseBody


class ListExternalApplicationResponse(BaseResponse):
    _types = {
        "data": ListExternalApplicationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListExternalApplicationResponseBody] = None
        init(self, d, self._types)
