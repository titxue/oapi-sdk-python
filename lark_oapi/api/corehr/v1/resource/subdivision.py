# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_subdivision_request import GetSubdivisionRequest
from ..model.get_subdivision_response import GetSubdivisionResponse
from ..model.list_subdivision_request import ListSubdivisionRequest
from ..model.list_subdivision_response import ListSubdivisionResponse


class Subdivision(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetSubdivisionRequest, option: Optional[RequestOption] = None) -> GetSubdivisionResponse:
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
        response: GetSubdivisionResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSubdivisionResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetSubdivisionRequest,
                   option: Optional[RequestOption] = None) -> GetSubdivisionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetSubdivisionResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSubdivisionResponse)
        response.raw = resp

        return response

    def list(self, request: ListSubdivisionRequest, option: Optional[RequestOption] = None) -> ListSubdivisionResponse:
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
        response: ListSubdivisionResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSubdivisionResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListSubdivisionRequest,
                    option: Optional[RequestOption] = None) -> ListSubdivisionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListSubdivisionResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSubdivisionResponse)
        response.raw = resp

        return response
