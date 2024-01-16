# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .mention_event import MentionEvent


class EventMessage(object):
    _types = {
        "message_id": str,
        "root_id": str,
        "parent_id": str,
        "create_time": int,
        "update_time": int,
        "chat_id": str,
        "thread_id": str,
        "chat_type": str,
        "message_type": str,
        "content": str,
        "mentions": List[MentionEvent],
        "user_agent": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.root_id: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.chat_id: Optional[str] = None
        self.thread_id: Optional[str] = None
        self.chat_type: Optional[str] = None
        self.message_type: Optional[str] = None
        self.content: Optional[str] = None
        self.mentions: Optional[List[MentionEvent]] = None
        self.user_agent: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventMessageBuilder":
        return EventMessageBuilder()


class EventMessageBuilder(object):
    def __init__(self) -> None:
        self._event_message = EventMessage()

    def message_id(self, message_id: str) -> "EventMessageBuilder":
        self._event_message.message_id = message_id
        return self

    def root_id(self, root_id: str) -> "EventMessageBuilder":
        self._event_message.root_id = root_id
        return self

    def parent_id(self, parent_id: str) -> "EventMessageBuilder":
        self._event_message.parent_id = parent_id
        return self

    def create_time(self, create_time: int) -> "EventMessageBuilder":
        self._event_message.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "EventMessageBuilder":
        self._event_message.update_time = update_time
        return self

    def chat_id(self, chat_id: str) -> "EventMessageBuilder":
        self._event_message.chat_id = chat_id
        return self

    def thread_id(self, thread_id: str) -> "EventMessageBuilder":
        self._event_message.thread_id = thread_id
        return self

    def chat_type(self, chat_type: str) -> "EventMessageBuilder":
        self._event_message.chat_type = chat_type
        return self

    def message_type(self, message_type: str) -> "EventMessageBuilder":
        self._event_message.message_type = message_type
        return self

    def content(self, content: str) -> "EventMessageBuilder":
        self._event_message.content = content
        return self

    def mentions(self, mentions: List[MentionEvent]) -> "EventMessageBuilder":
        self._event_message.mentions = mentions
        return self

    def user_agent(self, user_agent: str) -> "EventMessageBuilder":
        self._event_message.user_agent = user_agent
        return self

    def build(self) -> "EventMessage":
        return self._event_message
