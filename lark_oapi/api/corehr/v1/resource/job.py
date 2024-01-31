# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_job_request import CreateJobRequest
from ..model.create_job_response import CreateJobResponse
from ..model.delete_job_request import DeleteJobRequest
from ..model.delete_job_response import DeleteJobResponse
from ..model.get_job_request import GetJobRequest
from ..model.get_job_response import GetJobResponse
from ..model.list_job_request import ListJobRequest
from ..model.list_job_response import ListJobResponse
from ..model.patch_job_request import PatchJobRequest
from ..model.patch_job_response import PatchJobResponse


class Job(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateJobRequest, option: Optional[RequestOption] = None) -> CreateJobResponse:
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
        response: CreateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateJobRequest, option: Optional[RequestOption] = None) -> CreateJobResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteJobRequest, option: Optional[RequestOption] = None) -> DeleteJobResponse:
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
        response: DeleteJobResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeleteJobRequest, option: Optional[RequestOption] = None) -> DeleteJobResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeleteJobResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobResponse)
        response.raw = resp

        return response

    def get(self, request: GetJobRequest, option: Optional[RequestOption] = None) -> GetJobResponse:
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
        response: GetJobResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetJobRequest, option: Optional[RequestOption] = None) -> GetJobResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetJobResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobResponse)
        response.raw = resp

        return response

    def list(self, request: ListJobRequest, option: Optional[RequestOption] = None) -> ListJobResponse:
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
        response: ListJobResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListJobRequest, option: Optional[RequestOption] = None) -> ListJobResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListJobResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchJobRequest, option: Optional[RequestOption] = None) -> PatchJobResponse:
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
        response: PatchJobResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchJobResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchJobRequest, option: Optional[RequestOption] = None) -> PatchJobResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchJobResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchJobResponse)
        response.raw = resp

        return response
