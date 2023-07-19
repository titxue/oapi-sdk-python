# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.bitable.v1.model.create_app_table_field_request import CreateAppTableFieldRequest
from lark_oapi.api.bitable.v1.model.create_app_table_field_response import CreateAppTableFieldResponse
from lark_oapi.api.bitable.v1.model.delete_app_table_field_request import DeleteAppTableFieldRequest
from lark_oapi.api.bitable.v1.model.delete_app_table_field_response import DeleteAppTableFieldResponse
from lark_oapi.api.bitable.v1.model.list_app_table_field_request import ListAppTableFieldRequest
from lark_oapi.api.bitable.v1.model.list_app_table_field_response import ListAppTableFieldResponse
from lark_oapi.api.bitable.v1.model.update_app_table_field_request import UpdateAppTableFieldRequest
from lark_oapi.api.bitable.v1.model.update_app_table_field_response import UpdateAppTableFieldResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class AppTableField(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateAppTableFieldRequest,
               option: RequestOption = RequestOption()) -> CreateAppTableFieldResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateAppTableFieldResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteAppTableFieldRequest,
               option: RequestOption = RequestOption()) -> DeleteAppTableFieldResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteAppTableFieldResponse)
        response.raw = resp

        return response

    def list(self, request: ListAppTableFieldRequest,
             option: RequestOption = RequestOption()) -> ListAppTableFieldResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAppTableFieldResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateAppTableFieldRequest,
               option: RequestOption = RequestOption()) -> UpdateAppTableFieldResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateAppTableFieldResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateAppTableFieldResponse)
        response.raw = resp

        return response