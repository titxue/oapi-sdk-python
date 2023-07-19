# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserPosition(object):
    _types = {
        "position_code": str,
        "position_name": str,
        "department_id": str,
        "leader_user_id": str,
        "leader_position_code": str,
        "is_major": bool,
    }

    def __init__(self, d):
        self.position_code: Optional[str] = None
        self.position_name: Optional[str] = None
        self.department_id: Optional[str] = None
        self.leader_user_id: Optional[str] = None
        self.leader_position_code: Optional[str] = None
        self.is_major: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserPositionBuilder":
        return UserPositionBuilder()


class UserPositionBuilder(object):
    def __init__(self, user_position: UserPosition = UserPosition({})) -> None:
        self._user_position: UserPosition = user_position

    def position_code(self, position_code: str) -> "UserPositionBuilder":
        self._user_position.position_code = position_code
        return self

    def position_name(self, position_name: str) -> "UserPositionBuilder":
        self._user_position.position_name = position_name
        return self

    def department_id(self, department_id: str) -> "UserPositionBuilder":
        self._user_position.department_id = department_id
        return self

    def leader_user_id(self, leader_user_id: str) -> "UserPositionBuilder":
        self._user_position.leader_user_id = leader_user_id
        return self

    def leader_position_code(self, leader_position_code: str) -> "UserPositionBuilder":
        self._user_position.leader_position_code = leader_position_code
        return self

    def is_major(self, is_major: bool) -> "UserPositionBuilder":
        self._user_position.is_major = is_major
        return self

    def build(self) -> "UserPosition":
        return self._user_position