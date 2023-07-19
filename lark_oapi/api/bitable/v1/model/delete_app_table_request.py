# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteAppTableRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAppTableRequestBuilder":
        return DeleteAppTableRequestBuilder()


class DeleteAppTableRequestBuilder(object):

    def __init__(self, delete_app_table_request: DeleteAppTableRequest = DeleteAppTableRequest()) -> None:
        delete_app_table_request.http_method = HttpMethod.DELETE
        delete_app_table_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id"
        delete_app_table_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_app_table_request: DeleteAppTableRequest = delete_app_table_request

    def app_token(self, app_token: str) -> "DeleteAppTableRequestBuilder":
        self._delete_app_table_request.app_token = app_token
        self._delete_app_table_request.paths["app_token"] = app_token
        return self

    def table_id(self, table_id: str) -> "DeleteAppTableRequestBuilder":
        self._delete_app_table_request.table_id = table_id
        self._delete_app_table_request.paths["table_id"] = table_id
        return self

    def build(self) -> DeleteAppTableRequest:
        return self._delete_app_table_request