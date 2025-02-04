# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .app_table_record import AppTableRecord


class BatchGetAppTableRecordResponseBody(object):
    _types = {
        "records": List[AppTableRecord],
        "forbidden_record_ids": List[str],
        "absent_record_ids": List[str],
    }

    def __init__(self, d=None):
        self.records: Optional[List[AppTableRecord]] = None
        self.forbidden_record_ids: Optional[List[str]] = None
        self.absent_record_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetAppTableRecordResponseBodyBuilder":
        return BatchGetAppTableRecordResponseBodyBuilder()


class BatchGetAppTableRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_app_table_record_response_body = BatchGetAppTableRecordResponseBody()

    def records(self, records: List[AppTableRecord]) -> "BatchGetAppTableRecordResponseBodyBuilder":
        self._batch_get_app_table_record_response_body.records = records
        return self

    def forbidden_record_ids(self, forbidden_record_ids: List[str]) -> "BatchGetAppTableRecordResponseBodyBuilder":
        self._batch_get_app_table_record_response_body.forbidden_record_ids = forbidden_record_ids
        return self

    def absent_record_ids(self, absent_record_ids: List[str]) -> "BatchGetAppTableRecordResponseBodyBuilder":
        self._batch_get_app_table_record_response_body.absent_record_ids = absent_record_ids
        return self

    def build(self) -> "BatchGetAppTableRecordResponseBody":
        return self._batch_get_app_table_record_response_body
