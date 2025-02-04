# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class VerificationDetail(object):
    _types = {
        "verification_type": int,
        "verification_source": int,
        "org_name": str,
        "usci": str,
        "org_type": int,
        "legal_person_name": str,
        "enterprise_license": str,
        "verification_letter": str,
    }

    def __init__(self, d=None):
        self.verification_type: Optional[int] = None
        self.verification_source: Optional[int] = None
        self.org_name: Optional[str] = None
        self.usci: Optional[str] = None
        self.org_type: Optional[int] = None
        self.legal_person_name: Optional[str] = None
        self.enterprise_license: Optional[str] = None
        self.verification_letter: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VerificationDetailBuilder":
        return VerificationDetailBuilder()


class VerificationDetailBuilder(object):
    def __init__(self) -> None:
        self._verification_detail = VerificationDetail()

    def verification_type(self, verification_type: int) -> "VerificationDetailBuilder":
        self._verification_detail.verification_type = verification_type
        return self

    def verification_source(self, verification_source: int) -> "VerificationDetailBuilder":
        self._verification_detail.verification_source = verification_source
        return self

    def org_name(self, org_name: str) -> "VerificationDetailBuilder":
        self._verification_detail.org_name = org_name
        return self

    def usci(self, usci: str) -> "VerificationDetailBuilder":
        self._verification_detail.usci = usci
        return self

    def org_type(self, org_type: int) -> "VerificationDetailBuilder":
        self._verification_detail.org_type = org_type
        return self

    def legal_person_name(self, legal_person_name: str) -> "VerificationDetailBuilder":
        self._verification_detail.legal_person_name = legal_person_name
        return self

    def enterprise_license(self, enterprise_license: str) -> "VerificationDetailBuilder":
        self._verification_detail.enterprise_license = enterprise_license
        return self

    def verification_letter(self, verification_letter: str) -> "VerificationDetailBuilder":
        self._verification_detail.verification_letter = verification_letter
        return self

    def build(self) -> "VerificationDetail":
        return self._verification_detail
