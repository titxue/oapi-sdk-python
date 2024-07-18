# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_update_url_preview_request_body import BatchUpdateUrlPreviewRequestBody


class BatchUpdateUrlPreviewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[BatchUpdateUrlPreviewRequestBody] = None

    @staticmethod
    def builder() -> "BatchUpdateUrlPreviewRequestBuilder":
        return BatchUpdateUrlPreviewRequestBuilder()


class BatchUpdateUrlPreviewRequestBuilder(object):

    def __init__(self) -> None:
        batch_update_url_preview_request = BatchUpdateUrlPreviewRequest()
        batch_update_url_preview_request.http_method = HttpMethod.POST
        batch_update_url_preview_request.uri = "/open-apis/im/v2/url_previews/batch_update"
        batch_update_url_preview_request.token_types = {AccessTokenType.TENANT}
        self._batch_update_url_preview_request: BatchUpdateUrlPreviewRequest = batch_update_url_preview_request

    def request_body(self, request_body: BatchUpdateUrlPreviewRequestBody) -> "BatchUpdateUrlPreviewRequestBuilder":
        self._batch_update_url_preview_request.request_body = request_body
        self._batch_update_url_preview_request.body = request_body
        return self

    def build(self) -> BatchUpdateUrlPreviewRequest:
        return self._batch_update_url_preview_request