# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListTripartiteAgreementRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.application_id: Optional[str] = None
        self.tripartite_agreement_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListTripartiteAgreementRequestBuilder":
        return ListTripartiteAgreementRequestBuilder()


class ListTripartiteAgreementRequestBuilder(object):

    def __init__(self) -> None:
        list_tripartite_agreement_request = ListTripartiteAgreementRequest()
        list_tripartite_agreement_request.http_method = HttpMethod.GET
        list_tripartite_agreement_request.uri = "/open-apis/hire/v1/tripartite_agreements"
        list_tripartite_agreement_request.token_types = {AccessTokenType.TENANT}
        self._list_tripartite_agreement_request: ListTripartiteAgreementRequest = list_tripartite_agreement_request

    def page_size(self, page_size: int) -> "ListTripartiteAgreementRequestBuilder":
        self._list_tripartite_agreement_request.page_size = page_size
        self._list_tripartite_agreement_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListTripartiteAgreementRequestBuilder":
        self._list_tripartite_agreement_request.page_token = page_token
        self._list_tripartite_agreement_request.add_query("page_token", page_token)
        return self

    def application_id(self, application_id: str) -> "ListTripartiteAgreementRequestBuilder":
        self._list_tripartite_agreement_request.application_id = application_id
        self._list_tripartite_agreement_request.add_query("application_id", application_id)
        return self

    def tripartite_agreement_id(self, tripartite_agreement_id: str) -> "ListTripartiteAgreementRequestBuilder":
        self._list_tripartite_agreement_request.tripartite_agreement_id = tripartite_agreement_id
        self._list_tripartite_agreement_request.add_query("tripartite_agreement_id", tripartite_agreement_id)
        return self

    def build(self) -> ListTripartiteAgreementRequest:
        return self._list_tripartite_agreement_request
