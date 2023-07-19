# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.authen.v1.model.create_refresh_access_token_request import CreateRefreshAccessTokenRequest
from lark_oapi.api.authen.v1.model.create_refresh_access_token_response import CreateRefreshAccessTokenResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class RefreshAccessToken(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateRefreshAccessTokenRequest,
               option: RequestOption = RequestOption()) -> CreateRefreshAccessTokenResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateRefreshAccessTokenResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    CreateRefreshAccessTokenResponse)
        response.raw = resp

        return response