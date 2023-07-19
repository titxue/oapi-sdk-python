# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class OkrObjectiveProgressRate(object):
    _types = {
        "percent": int,
        "status": str,
    }

    def __init__(self, d):
        self.percent: Optional[int] = None
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrObjectiveProgressRateBuilder":
        return OkrObjectiveProgressRateBuilder()


class OkrObjectiveProgressRateBuilder(object):
    def __init__(self, okr_objective_progress_rate: OkrObjectiveProgressRate = OkrObjectiveProgressRate({})) -> None:
        self._okr_objective_progress_rate: OkrObjectiveProgressRate = okr_objective_progress_rate

    def percent(self, percent: int) -> "OkrObjectiveProgressRateBuilder":
        self._okr_objective_progress_rate.percent = percent
        return self

    def status(self, status: str) -> "OkrObjectiveProgressRateBuilder":
        self._okr_objective_progress_rate.status = status
        return self

    def build(self) -> "OkrObjectiveProgressRate":
        return self._okr_objective_progress_rate