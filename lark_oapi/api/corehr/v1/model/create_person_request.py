# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .person import Person


class CreatePersonRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[Person] = None

    @staticmethod
    def builder() -> "CreatePersonRequestBuilder":
        return CreatePersonRequestBuilder()


class CreatePersonRequestBuilder(object):

    def __init__(self) -> None:
        create_person_request = CreatePersonRequest()
        create_person_request.http_method = HttpMethod.POST
        create_person_request.uri = "/open-apis/corehr/v1/persons"
        create_person_request.token_types = {AccessTokenType.TENANT}
        self._create_person_request: CreatePersonRequest = create_person_request

    def client_token(self, client_token: str) -> "CreatePersonRequestBuilder":
        self._create_person_request.client_token = client_token
        self._create_person_request.add_query("client_token", client_token)
        return self

    def request_body(self, request_body: Person) -> "CreatePersonRequestBuilder":
        self._create_person_request.request_body = request_body
        self._create_person_request.body = request_body
        return self

    def build(self) -> CreatePersonRequest:
        return self._create_person_request
