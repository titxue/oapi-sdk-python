# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .patch_tag_request_body import PatchTagRequestBody


class PatchTagRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.tag_id: Optional[str] = None
        self.request_body: Optional[PatchTagRequestBody] = None

    @staticmethod
    def builder() -> "PatchTagRequestBuilder":
        return PatchTagRequestBuilder()


class PatchTagRequestBuilder(object):

    def __init__(self) -> None:
        patch_tag_request = PatchTagRequest()
        patch_tag_request.http_method = HttpMethod.PATCH
        patch_tag_request.uri = "/open-apis/im/v2/tags/:tag_id"
        patch_tag_request.token_types = {AccessTokenType.TENANT}
        self._patch_tag_request: PatchTagRequest = patch_tag_request

    def tag_id(self, tag_id: str) -> "PatchTagRequestBuilder":
        self._patch_tag_request.tag_id = tag_id
        self._patch_tag_request.paths["tag_id"] = str(tag_id)
        return self

    def request_body(self, request_body: PatchTagRequestBody) -> "PatchTagRequestBuilder":
        self._patch_tag_request.request_body = request_body
        self._patch_tag_request.body = request_body
        return self

    def build(self) -> PatchTagRequest:
        return self._patch_tag_request