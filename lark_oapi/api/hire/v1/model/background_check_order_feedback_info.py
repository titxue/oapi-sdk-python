# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BackgroundCheckOrderFeedbackInfo(object):
    _types = {
        "id": str,
        "attachment_url": str,
        "result": str,
        "report_type": int,
        "create_time": str,
        "report_name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.attachment_url: Optional[str] = None
        self.result: Optional[str] = None
        self.report_type: Optional[int] = None
        self.create_time: Optional[str] = None
        self.report_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckOrderFeedbackInfoBuilder":
        return BackgroundCheckOrderFeedbackInfoBuilder()


class BackgroundCheckOrderFeedbackInfoBuilder(object):
    def __init__(self) -> None:
        self._background_check_order_feedback_info = BackgroundCheckOrderFeedbackInfo()

    def id(self, id: str) -> "BackgroundCheckOrderFeedbackInfoBuilder":
        self._background_check_order_feedback_info.id = id
        return self

    def attachment_url(self, attachment_url: str) -> "BackgroundCheckOrderFeedbackInfoBuilder":
        self._background_check_order_feedback_info.attachment_url = attachment_url
        return self

    def result(self, result: str) -> "BackgroundCheckOrderFeedbackInfoBuilder":
        self._background_check_order_feedback_info.result = result
        return self

    def report_type(self, report_type: int) -> "BackgroundCheckOrderFeedbackInfoBuilder":
        self._background_check_order_feedback_info.report_type = report_type
        return self

    def create_time(self, create_time: str) -> "BackgroundCheckOrderFeedbackInfoBuilder":
        self._background_check_order_feedback_info.create_time = create_time
        return self

    def report_name(self, report_name: str) -> "BackgroundCheckOrderFeedbackInfoBuilder":
        self._background_check_order_feedback_info.report_name = report_name
        return self

    def build(self) -> "BackgroundCheckOrderFeedbackInfo":
        return self._background_check_order_feedback_info