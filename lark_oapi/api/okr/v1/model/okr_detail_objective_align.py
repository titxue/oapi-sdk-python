# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OkrDetailObjectiveAlign(object):
    _types = {
        "id": int,
        "okr_id": int,
        "user_id": str,
    }

    def __init__(self, d):
        self.id: Optional[int] = None
        self.okr_id: Optional[int] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrDetailObjectiveAlignBuilder":
        return OkrDetailObjectiveAlignBuilder()


class OkrDetailObjectiveAlignBuilder(object):
    def __init__(self, okr_detail_objective_align: OkrDetailObjectiveAlign = OkrDetailObjectiveAlign({})) -> None:
        self._okr_detail_objective_align: OkrDetailObjectiveAlign = okr_detail_objective_align

    def id(self, id: int) -> "OkrDetailObjectiveAlignBuilder":
        self._okr_detail_objective_align.id = id
        return self

    def okr_id(self, okr_id: int) -> "OkrDetailObjectiveAlignBuilder":
        self._okr_detail_objective_align.okr_id = okr_id
        return self

    def user_id(self, user_id: str) -> "OkrDetailObjectiveAlignBuilder":
        self._okr_detail_objective_align.user_id = user_id
        return self

    def build(self) -> "OkrDetailObjectiveAlign":
        return self._okr_detail_objective_align