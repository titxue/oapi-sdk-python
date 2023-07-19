# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_reserve_response_body import UpdateReserveResponseBody


class UpdateReserveResponse(BaseResponse):
    _types = {
        "data": UpdateReserveResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UpdateReserveResponseBody] = None
        init(self, d, self._types)