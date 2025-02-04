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
from ..model.batch_get_department_request import BatchGetDepartmentRequest
from ..model.batch_get_department_response import BatchGetDepartmentResponse
from ..model.parents_department_request import ParentsDepartmentRequest
from ..model.parents_department_response import ParentsDepartmentResponse
from ..model.query_multi_timeline_department_request import QueryMultiTimelineDepartmentRequest
from ..model.query_multi_timeline_department_response import QueryMultiTimelineDepartmentResponse
from ..model.query_timeline_department_request import QueryTimelineDepartmentRequest
from ..model.query_timeline_department_response import QueryTimelineDepartmentResponse
from ..model.search_department_request import SearchDepartmentRequest
from ..model.search_department_response import SearchDepartmentResponse


class Department(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_get(self, request: BatchGetDepartmentRequest,
                  option: Optional[RequestOption] = None) -> BatchGetDepartmentResponse:
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
        response: BatchGetDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchGetDepartmentResponse)
        response.raw = resp

        return response

    async def abatch_get(self, request: BatchGetDepartmentRequest,
                         option: Optional[RequestOption] = None) -> BatchGetDepartmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: BatchGetDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchGetDepartmentResponse)
        response.raw = resp

        return response

    def parents(self, request: ParentsDepartmentRequest,
                option: Optional[RequestOption] = None) -> ParentsDepartmentResponse:
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
        response: ParentsDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ParentsDepartmentResponse)
        response.raw = resp

        return response

    async def aparents(self, request: ParentsDepartmentRequest,
                       option: Optional[RequestOption] = None) -> ParentsDepartmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ParentsDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ParentsDepartmentResponse)
        response.raw = resp

        return response

    def query_multi_timeline(self, request: QueryMultiTimelineDepartmentRequest,
                             option: Optional[RequestOption] = None) -> QueryMultiTimelineDepartmentResponse:
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
        response: QueryMultiTimelineDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        QueryMultiTimelineDepartmentResponse)
        response.raw = resp

        return response

    async def aquery_multi_timeline(self, request: QueryMultiTimelineDepartmentRequest,
                                    option: Optional[RequestOption] = None) -> QueryMultiTimelineDepartmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: QueryMultiTimelineDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        QueryMultiTimelineDepartmentResponse)
        response.raw = resp

        return response

    def query_timeline(self, request: QueryTimelineDepartmentRequest,
                       option: Optional[RequestOption] = None) -> QueryTimelineDepartmentResponse:
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
        response: QueryTimelineDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   QueryTimelineDepartmentResponse)
        response.raw = resp

        return response

    async def aquery_timeline(self, request: QueryTimelineDepartmentRequest,
                              option: Optional[RequestOption] = None) -> QueryTimelineDepartmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: QueryTimelineDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   QueryTimelineDepartmentResponse)
        response.raw = resp

        return response

    def search(self, request: SearchDepartmentRequest,
               option: Optional[RequestOption] = None) -> SearchDepartmentResponse:
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
        response: SearchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchDepartmentResponse)
        response.raw = resp

        return response

    async def asearch(self, request: SearchDepartmentRequest,
                      option: Optional[RequestOption] = None) -> SearchDepartmentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: SearchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchDepartmentResponse)
        response.raw = resp

        return response
