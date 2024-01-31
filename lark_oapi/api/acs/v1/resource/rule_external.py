# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_rule_external_request import CreateRuleExternalRequest
from ..model.create_rule_external_response import CreateRuleExternalResponse
from ..model.delete_rule_external_request import DeleteRuleExternalRequest
from ..model.delete_rule_external_response import DeleteRuleExternalResponse
from ..model.device_bind_rule_external_request import DeviceBindRuleExternalRequest
from ..model.device_bind_rule_external_response import DeviceBindRuleExternalResponse
from ..model.get_rule_external_request import GetRuleExternalRequest
from ..model.get_rule_external_response import GetRuleExternalResponse


class RuleExternal(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateRuleExternalRequest,
               option: Optional[RequestOption] = None) -> CreateRuleExternalResponse:
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
        response: CreateRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateRuleExternalResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateRuleExternalRequest,
                      option: Optional[RequestOption] = None) -> CreateRuleExternalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateRuleExternalResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteRuleExternalRequest,
               option: Optional[RequestOption] = None) -> DeleteRuleExternalResponse:
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
        response: DeleteRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteRuleExternalResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeleteRuleExternalRequest,
                      option: Optional[RequestOption] = None) -> DeleteRuleExternalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeleteRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteRuleExternalResponse)
        response.raw = resp

        return response

    def device_bind(self, request: DeviceBindRuleExternalRequest,
                    option: Optional[RequestOption] = None) -> DeviceBindRuleExternalResponse:
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
        response: DeviceBindRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  DeviceBindRuleExternalResponse)
        response.raw = resp

        return response

    async def adevice_bind(self, request: DeviceBindRuleExternalRequest,
                           option: Optional[RequestOption] = None) -> DeviceBindRuleExternalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeviceBindRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  DeviceBindRuleExternalResponse)
        response.raw = resp

        return response

    def get(self, request: GetRuleExternalRequest, option: Optional[RequestOption] = None) -> GetRuleExternalResponse:
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
        response: GetRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8), GetRuleExternalResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetRuleExternalRequest,
                   option: Optional[RequestOption] = None) -> GetRuleExternalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetRuleExternalResponse = JSON.unmarshal(str(resp.content, UTF_8), GetRuleExternalResponse)
        response.raw = resp

        return response
