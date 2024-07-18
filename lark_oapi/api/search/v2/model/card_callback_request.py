# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .callback_action import CallbackAction


class CardCallbackRequest(object):
    _types = {
        "open_chat_id": str,
        "open_message_id": str,
        "token": str,
        "action": CallbackAction,
    }

    def __init__(self, d=None):
        self.open_chat_id: Optional[str] = None
        self.open_message_id: Optional[str] = None
        self.token: Optional[str] = None
        self.action: Optional[CallbackAction] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CardCallbackRequestBuilder":
        return CardCallbackRequestBuilder()


class CardCallbackRequestBuilder(object):
    def __init__(self) -> None:
        self._card_callback_request = CardCallbackRequest()

    def open_chat_id(self, open_chat_id: str) -> "CardCallbackRequestBuilder":
        self._card_callback_request.open_chat_id = open_chat_id
        return self

    def open_message_id(self, open_message_id: str) -> "CardCallbackRequestBuilder":
        self._card_callback_request.open_message_id = open_message_id
        return self

    def token(self, token: str) -> "CardCallbackRequestBuilder":
        self._card_callback_request.token = token
        return self

    def action(self, action: CallbackAction) -> "CardCallbackRequestBuilder":
        self._card_callback_request.action = action
        return self

    def build(self) -> "CardCallbackRequest":
        return self._card_callback_request