# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AgentUser(object):
    _types = {
        "id": str,
        "avatar_url": str,
        "name": str,
        "email": str,
        "department": str,
        "company_name": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.avatar_url: Optional[str] = None
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.department: Optional[str] = None
        self.company_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgentUserBuilder":
        return AgentUserBuilder()


class AgentUserBuilder(object):
    def __init__(self, agent_user: AgentUser = AgentUser({})) -> None:
        self._agent_user: AgentUser = agent_user

    def id(self, id: str) -> "AgentUserBuilder":
        self._agent_user.id = id
        return self

    def avatar_url(self, avatar_url: str) -> "AgentUserBuilder":
        self._agent_user.avatar_url = avatar_url
        return self

    def name(self, name: str) -> "AgentUserBuilder":
        self._agent_user.name = name
        return self

    def email(self, email: str) -> "AgentUserBuilder":
        self._agent_user.email = email
        return self

    def department(self, department: str) -> "AgentUserBuilder":
        self._agent_user.department = department
        return self

    def company_name(self, company_name: str) -> "AgentUserBuilder":
        self._agent_user.company_name = company_name
        return self

    def build(self) -> "AgentUser":
        return self._agent_user