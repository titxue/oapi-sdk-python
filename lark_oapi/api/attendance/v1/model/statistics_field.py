# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class StatisticsField(object):
    _types = {
        "field_id": str,
        "field_content": str,
        "title": str,
        "field_desc": str,
    }

    def __init__(self, d=None):
        self.field_id: Optional[str] = None
        self.field_content: Optional[str] = None
        self.title: Optional[str] = None
        self.field_desc: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StatisticsFieldBuilder":
        return StatisticsFieldBuilder()


class StatisticsFieldBuilder(object):
    def __init__(self) -> None:
        self._statistics_field = StatisticsField()

    def field_id(self, field_id: str) -> "StatisticsFieldBuilder":
        self._statistics_field.field_id = field_id
        return self

    def field_content(self, field_content: str) -> "StatisticsFieldBuilder":
        self._statistics_field.field_content = field_content
        return self

    def title(self, title: str) -> "StatisticsFieldBuilder":
        self._statistics_field.title = title
        return self

    def field_desc(self, field_desc: str) -> "StatisticsFieldBuilder":
        self._statistics_field.field_desc = field_desc
        return self

    def build(self) -> "StatisticsField":
        return self._statistics_field