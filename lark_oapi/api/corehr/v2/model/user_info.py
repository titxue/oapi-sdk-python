# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class UserInfo(object):
    _types = {
        "user_id": str,
        "name": str,
        "zh_name": str,
        "en_name": str,
        "mobile": str,
        "employee_no": str,
        "email": str,
        "is_resigned": bool,
        "resign_time": int,
        "resign_date": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.name: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.mobile: Optional[str] = None
        self.employee_no: Optional[str] = None
        self.email: Optional[str] = None
        self.is_resigned: Optional[bool] = None
        self.resign_time: Optional[int] = None
        self.resign_date: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserInfoBuilder":
        return UserInfoBuilder()


class UserInfoBuilder(object):
    def __init__(self) -> None:
        self._user_info = UserInfo()

    def user_id(self, user_id: str) -> "UserInfoBuilder":
        self._user_info.user_id = user_id
        return self

    def name(self, name: str) -> "UserInfoBuilder":
        self._user_info.name = name
        return self

    def zh_name(self, zh_name: str) -> "UserInfoBuilder":
        self._user_info.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "UserInfoBuilder":
        self._user_info.en_name = en_name
        return self

    def mobile(self, mobile: str) -> "UserInfoBuilder":
        self._user_info.mobile = mobile
        return self

    def employee_no(self, employee_no: str) -> "UserInfoBuilder":
        self._user_info.employee_no = employee_no
        return self

    def email(self, email: str) -> "UserInfoBuilder":
        self._user_info.email = email
        return self

    def is_resigned(self, is_resigned: bool) -> "UserInfoBuilder":
        self._user_info.is_resigned = is_resigned
        return self

    def resign_time(self, resign_time: int) -> "UserInfoBuilder":
        self._user_info.resign_time = resign_time
        return self

    def resign_date(self, resign_date: str) -> "UserInfoBuilder":
        self._user_info.resign_date = resign_date
        return self

    def build(self) -> "UserInfo":
        return self._user_info