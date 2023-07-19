# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.attendance.v1.model.modify_user_setting_request import ModifyUserSettingRequest
from lark_oapi.api.attendance.v1.model.modify_user_setting_response import ModifyUserSettingResponse
from lark_oapi.api.attendance.v1.model.query_user_setting_request import QueryUserSettingRequest
from lark_oapi.api.attendance.v1.model.query_user_setting_response import QueryUserSettingResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class UserSetting(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def modify(self, request: ModifyUserSettingRequest,
               option: RequestOption = RequestOption()) -> ModifyUserSettingResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ModifyUserSettingResponse = JSON.unmarshal(str(resp.content, UTF_8), ModifyUserSettingResponse)
        response.raw = resp

        return response

    def query(self, request: QueryUserSettingRequest,
              option: RequestOption = RequestOption()) -> QueryUserSettingResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryUserSettingResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryUserSettingResponse)
        response.raw = resp

        return response