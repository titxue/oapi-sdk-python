# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .offer_apply_form import OfferApplyForm


class ListOfferApplicationFormResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[OfferApplyForm],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[OfferApplyForm]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListOfferApplicationFormResponseBodyBuilder":
        return ListOfferApplicationFormResponseBodyBuilder()


class ListOfferApplicationFormResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_offer_application_form_response_body = ListOfferApplicationFormResponseBody()

    def has_more(self, has_more: bool) -> "ListOfferApplicationFormResponseBodyBuilder":
        self._list_offer_application_form_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListOfferApplicationFormResponseBodyBuilder":
        self._list_offer_application_form_response_body.page_token = page_token
        return self

    def items(self, items: List[OfferApplyForm]) -> "ListOfferApplicationFormResponseBodyBuilder":
        self._list_offer_application_form_response_body.items = items
        return self

    def build(self) -> "ListOfferApplicationFormResponseBody":
        return self._list_offer_application_form_response_body
