from typing import Optional

from lark_oapi.core.construct import init


class Term(object):
    _types = {
        "from": str,
        "to": str,
    }

    def __init__(self, d=None):
        self._from: Optional[str] = None
        self.to: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TermBuilder":
        return TermBuilder()


class TermBuilder(object):
    def __init__(self) -> None:
        self._term = Term()

    def from_(self, _from: str) -> "TermBuilder":
        setattr(self._term, "from", _from)
        return self

    def to(self, to: str) -> "TermBuilder":
        self._term.to = to
        return self

    def build(self) -> "Term":
        return self._term
