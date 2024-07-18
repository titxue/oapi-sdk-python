# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .field_variable_value_to import FieldVariableValueTo


class FieldVariableSubVlaue(object):
    _types = {
        "key": str,
        "value": FieldVariableValueTo,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[FieldVariableValueTo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FieldVariableSubVlaueBuilder":
        return FieldVariableSubVlaueBuilder()


class FieldVariableSubVlaueBuilder(object):
    def __init__(self) -> None:
        self._field_variable_sub_vlaue = FieldVariableSubVlaue()

    def key(self, key: str) -> "FieldVariableSubVlaueBuilder":
        self._field_variable_sub_vlaue.key = key
        return self

    def value(self, value: FieldVariableValueTo) -> "FieldVariableSubVlaueBuilder":
        self._field_variable_sub_vlaue.value = value
        return self

    def build(self) -> "FieldVariableSubVlaue":
        return self._field_variable_sub_vlaue