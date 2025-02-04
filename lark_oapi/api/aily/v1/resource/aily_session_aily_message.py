# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.create_aily_session_aily_message_request import CreateAilySessionAilyMessageRequest
from ..model.create_aily_session_aily_message_response import CreateAilySessionAilyMessageResponse
from ..model.get_aily_session_aily_message_request import GetAilySessionAilyMessageRequest
from ..model.get_aily_session_aily_message_response import GetAilySessionAilyMessageResponse
from ..model.list_aily_session_aily_message_request import ListAilySessionAilyMessageRequest
from ..model.list_aily_session_aily_message_response import ListAilySessionAilyMessageResponse


class AilySessionAilyMessage(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateAilySessionAilyMessageRequest,
               option: Optional[RequestOption] = None) -> CreateAilySessionAilyMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAilySessionAilyMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        CreateAilySessionAilyMessageResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateAilySessionAilyMessageRequest,
                      option: Optional[RequestOption] = None) -> CreateAilySessionAilyMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateAilySessionAilyMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        CreateAilySessionAilyMessageResponse)
        response.raw = resp

        return response

    def get(self, request: GetAilySessionAilyMessageRequest,
            option: Optional[RequestOption] = None) -> GetAilySessionAilyMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetAilySessionAilyMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     GetAilySessionAilyMessageResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetAilySessionAilyMessageRequest,
                   option: Optional[RequestOption] = None) -> GetAilySessionAilyMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetAilySessionAilyMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     GetAilySessionAilyMessageResponse)
        response.raw = resp

        return response

    def list(self, request: ListAilySessionAilyMessageRequest,
             option: Optional[RequestOption] = None) -> ListAilySessionAilyMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAilySessionAilyMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      ListAilySessionAilyMessageResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListAilySessionAilyMessageRequest,
                    option: Optional[RequestOption] = None) -> ListAilySessionAilyMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListAilySessionAilyMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      ListAilySessionAilyMessageResponse)
        response.raw = resp

        return response
