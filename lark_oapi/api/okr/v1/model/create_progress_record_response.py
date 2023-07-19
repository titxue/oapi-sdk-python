# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_progress_record_response_body import CreateProgressRecordResponseBody


class CreateProgressRecordResponse(BaseResponse):
    _types = {
        "data": CreateProgressRecordResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateProgressRecordResponseBody] = None
        init(self, d, self._types)