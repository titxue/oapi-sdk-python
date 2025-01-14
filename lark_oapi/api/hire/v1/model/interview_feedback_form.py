# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .score_calculation_config import ScoreCalculationConfig
from .interview_feedback_form_module import InterviewFeedbackFormModule


class InterviewFeedbackForm(object):
    _types = {
        "id": str,
        "version": int,
        "name": I18n,
        "type": int,
        "score_calculation_config": ScoreCalculationConfig,
        "modules": List[InterviewFeedbackFormModule],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.version: Optional[int] = None
        self.name: Optional[I18n] = None
        self.type: Optional[int] = None
        self.score_calculation_config: Optional[ScoreCalculationConfig] = None
        self.modules: Optional[List[InterviewFeedbackFormModule]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewFeedbackFormBuilder":
        return InterviewFeedbackFormBuilder()


class InterviewFeedbackFormBuilder(object):
    def __init__(self) -> None:
        self._interview_feedback_form = InterviewFeedbackForm()

    def id(self, id: str) -> "InterviewFeedbackFormBuilder":
        self._interview_feedback_form.id = id
        return self

    def version(self, version: int) -> "InterviewFeedbackFormBuilder":
        self._interview_feedback_form.version = version
        return self

    def name(self, name: I18n) -> "InterviewFeedbackFormBuilder":
        self._interview_feedback_form.name = name
        return self

    def type(self, type: int) -> "InterviewFeedbackFormBuilder":
        self._interview_feedback_form.type = type
        return self

    def score_calculation_config(self,
                                 score_calculation_config: ScoreCalculationConfig) -> "InterviewFeedbackFormBuilder":
        self._interview_feedback_form.score_calculation_config = score_calculation_config
        return self

    def modules(self, modules: List[InterviewFeedbackFormModule]) -> "InterviewFeedbackFormBuilder":
        self._interview_feedback_form.modules = modules
        return self

    def build(self) -> "InterviewFeedbackForm":
        return self._interview_feedback_form
