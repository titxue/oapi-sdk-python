# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_role import AppRole


class UpdateAppRoleResponseBody(object):
    _types = {
        "role": AppRole,
    }

    def __init__(self, d):
        self.role: Optional[AppRole] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateAppRoleResponseBodyBuilder":
        return UpdateAppRoleResponseBodyBuilder()


class UpdateAppRoleResponseBodyBuilder(object):
    def __init__(self,
                 update_app_role_response_body: UpdateAppRoleResponseBody = UpdateAppRoleResponseBody({})) -> None:
        self._update_app_role_response_body: UpdateAppRoleResponseBody = update_app_role_response_body

    def role(self, role: AppRole) -> "UpdateAppRoleResponseBodyBuilder":
        self._update_app_role_response_body.role = role
        return self

    def build(self) -> "UpdateAppRoleResponseBody":
        return self._update_app_role_response_body