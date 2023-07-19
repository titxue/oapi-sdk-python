# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .exteranl_instance_check import ExteranlInstanceCheck


class CheckExternalInstanceRequestBody(object):
    _types = {
        "instances": List[ExteranlInstanceCheck],
    }

    def __init__(self, d):
        self.instances: Optional[List[ExteranlInstanceCheck]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CheckExternalInstanceRequestBodyBuilder":
        return CheckExternalInstanceRequestBodyBuilder()


class CheckExternalInstanceRequestBodyBuilder(object):
    def __init__(self,
                 check_external_instance_request_body: CheckExternalInstanceRequestBody = CheckExternalInstanceRequestBody(
                     {})) -> None:
        self._check_external_instance_request_body: CheckExternalInstanceRequestBody = check_external_instance_request_body

    def instances(self, instances: List[ExteranlInstanceCheck]) -> "CheckExternalInstanceRequestBodyBuilder":
        self._check_external_instance_request_body.instances = instances
        return self

    def build(self) -> "CheckExternalInstanceRequestBody":
        return self._check_external_instance_request_body