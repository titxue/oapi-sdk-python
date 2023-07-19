# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.vc.v1.model.get_meeting_list_request import GetMeetingListRequest
from lark_oapi.api.vc.v1.model.get_meeting_list_response import GetMeetingListResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class MeetingList(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetMeetingListRequest, option: RequestOption = RequestOption()) -> GetMeetingListResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetMeetingListResponse = JSON.unmarshal(str(resp.content, UTF_8), GetMeetingListResponse)
        response.raw = resp

        return response