# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_permission_public_password_request import CreatePermissionPublicPasswordRequest
from ..model.create_permission_public_password_response import CreatePermissionPublicPasswordResponse
from ..model.delete_permission_public_password_request import DeletePermissionPublicPasswordRequest
from ..model.delete_permission_public_password_response import DeletePermissionPublicPasswordResponse
from ..model.update_permission_public_password_request import UpdatePermissionPublicPasswordRequest
from ..model.update_permission_public_password_response import UpdatePermissionPublicPasswordResponse


class PermissionPublicPassword(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreatePermissionPublicPasswordRequest,
               option: Optional[RequestOption] = None) -> CreatePermissionPublicPasswordResponse:
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
        response: CreatePermissionPublicPasswordResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          CreatePermissionPublicPasswordResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreatePermissionPublicPasswordRequest,
                      option: Optional[RequestOption] = None) -> CreatePermissionPublicPasswordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreatePermissionPublicPasswordResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          CreatePermissionPublicPasswordResponse)
        response.raw = resp

        return response

    def delete(self, request: DeletePermissionPublicPasswordRequest,
               option: Optional[RequestOption] = None) -> DeletePermissionPublicPasswordResponse:
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
        response: DeletePermissionPublicPasswordResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          DeletePermissionPublicPasswordResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeletePermissionPublicPasswordRequest,
                      option: Optional[RequestOption] = None) -> DeletePermissionPublicPasswordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeletePermissionPublicPasswordResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          DeletePermissionPublicPasswordResponse)
        response.raw = resp

        return response

    def update(self, request: UpdatePermissionPublicPasswordRequest,
               option: Optional[RequestOption] = None) -> UpdatePermissionPublicPasswordResponse:
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
        response: UpdatePermissionPublicPasswordResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          UpdatePermissionPublicPasswordResponse)
        response.raw = resp

        return response

    async def aupdate(self, request: UpdatePermissionPublicPasswordRequest,
                      option: Optional[RequestOption] = None) -> UpdatePermissionPublicPasswordResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: UpdatePermissionPublicPasswordResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          UpdatePermissionPublicPasswordResponse)
        response.raw = resp

        return response
