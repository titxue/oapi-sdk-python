# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SkillCall(object):
    _types = {
        "skill_call_id": str,
        "input": str,
        "waiting_type": str,
        "input_dsl": str,
    }

    def __init__(self, d=None):
        self.skill_call_id: Optional[str] = None
        self.input: Optional[str] = None
        self.waiting_type: Optional[str] = None
        self.input_dsl: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SkillCallBuilder":
        return SkillCallBuilder()


class SkillCallBuilder(object):
    def __init__(self) -> None:
        self._skill_call = SkillCall()

    def skill_call_id(self, skill_call_id: str) -> "SkillCallBuilder":
        self._skill_call.skill_call_id = skill_call_id
        return self

    def input(self, input: str) -> "SkillCallBuilder":
        self._skill_call.input = input
        return self

    def waiting_type(self, waiting_type: str) -> "SkillCallBuilder":
        self._skill_call.waiting_type = waiting_type
        return self

    def input_dsl(self, input_dsl: str) -> "SkillCallBuilder":
        self._skill_call.input_dsl = input_dsl
        return self

    def build(self) -> "SkillCall":
        return self._skill_call