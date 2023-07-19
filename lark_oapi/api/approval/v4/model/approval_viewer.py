# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApprovalViewer(object):
    _types = {
        "type": str,
        "open_id": str,
        "user_id": str,
        "union_id": str,
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.open_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.union_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalViewerBuilder":
        return ApprovalViewerBuilder()


class ApprovalViewerBuilder(object):
    def __init__(self, approval_viewer: ApprovalViewer = ApprovalViewer({})) -> None:
        self._approval_viewer: ApprovalViewer = approval_viewer

    def type(self, type: str) -> "ApprovalViewerBuilder":
        self._approval_viewer.type = type
        return self

    def open_id(self, open_id: str) -> "ApprovalViewerBuilder":
        self._approval_viewer.open_id = open_id
        return self

    def user_id(self, user_id: str) -> "ApprovalViewerBuilder":
        self._approval_viewer.user_id = user_id
        return self

    def union_id(self, union_id: str) -> "ApprovalViewerBuilder":
        self._approval_viewer.union_id = union_id
        return self

    def build(self) -> "ApprovalViewer":
        return self._approval_viewer