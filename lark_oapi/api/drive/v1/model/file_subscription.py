# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FileSubscription(object):
    _types = {
        "subscription_id": str,
        "subscription_type": str,
        "is_subcribe": bool,
        "file_type": str,
    }

    def __init__(self, d):
        self.subscription_id: Optional[str] = None
        self.subscription_type: Optional[str] = None
        self.is_subcribe: Optional[bool] = None
        self.file_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileSubscriptionBuilder":
        return FileSubscriptionBuilder()


class FileSubscriptionBuilder(object):
    def __init__(self, file_subscription: FileSubscription = FileSubscription({})) -> None:
        self._file_subscription: FileSubscription = file_subscription

    def subscription_id(self, subscription_id: str) -> "FileSubscriptionBuilder":
        self._file_subscription.subscription_id = subscription_id
        return self

    def subscription_type(self, subscription_type: str) -> "FileSubscriptionBuilder":
        self._file_subscription.subscription_type = subscription_type
        return self

    def is_subcribe(self, is_subcribe: bool) -> "FileSubscriptionBuilder":
        self._file_subscription.is_subcribe = is_subcribe
        return self

    def file_type(self, file_type: str) -> "FileSubscriptionBuilder":
        self._file_subscription.file_type = file_type
        return self

    def build(self) -> "FileSubscription":
        return self._file_subscription