# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .field_variable_value_to_for_review import FieldVariableValueToForReview


class FieldVariableSubVlaueForReview(object):
    _types = {
        "key": str,
        "value": FieldVariableValueToForReview,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[FieldVariableValueToForReview] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FieldVariableSubVlaueForReviewBuilder":
        return FieldVariableSubVlaueForReviewBuilder()


class FieldVariableSubVlaueForReviewBuilder(object):
    def __init__(self) -> None:
        self._field_variable_sub_vlaue_for_review = FieldVariableSubVlaueForReview()

    def key(self, key: str) -> "FieldVariableSubVlaueForReviewBuilder":
        self._field_variable_sub_vlaue_for_review.key = key
        return self

    def value(self, value: FieldVariableValueToForReview) -> "FieldVariableSubVlaueForReviewBuilder":
        self._field_variable_sub_vlaue_for_review.value = value
        return self

    def build(self) -> "FieldVariableSubVlaueForReview":
        return self._field_variable_sub_vlaue_for_review
