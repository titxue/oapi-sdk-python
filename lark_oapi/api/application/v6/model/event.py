# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Event(object):
    _types = {
        "event_type": str,
        "event_name": str,
        "event_description": str,
    }

    def __init__(self, d=None):
        self.event_type: Optional[str] = None
        self.event_name: Optional[str] = None
        self.event_description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventBuilder":
        return EventBuilder()


class EventBuilder(object):
    def __init__(self) -> None:
        self._event = Event()

    def event_type(self, event_type: str) -> "EventBuilder":
        self._event.event_type = event_type
        return self

    def event_name(self, event_name: str) -> "EventBuilder":
        self._event.event_name = event_name
        return self

    def event_description(self, event_description: str) -> "EventBuilder":
        self._event.event_description = event_description
        return self

    def build(self) -> "Event":
        return self._event