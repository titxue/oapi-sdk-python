# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .signature_template_brief_info import SignatureTemplateBriefInfo
from .signature_template_content_info import SignatureTemplateContentInfo


class SignatureTemplate(object):
    _types = {
        "id": str,
        "brief_info": SignatureTemplateBriefInfo,
        "content_info": SignatureTemplateContentInfo,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.brief_info: Optional[SignatureTemplateBriefInfo] = None
        self.content_info: Optional[SignatureTemplateContentInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SignatureTemplateBuilder":
        return SignatureTemplateBuilder()


class SignatureTemplateBuilder(object):
    def __init__(self) -> None:
        self._signature_template = SignatureTemplate()

    def id(self, id: str) -> "SignatureTemplateBuilder":
        self._signature_template.id = id
        return self

    def brief_info(self, brief_info: SignatureTemplateBriefInfo) -> "SignatureTemplateBuilder":
        self._signature_template.brief_info = brief_info
        return self

    def content_info(self, content_info: SignatureTemplateContentInfo) -> "SignatureTemplateBuilder":
        self._signature_template.content_info = content_info
        return self

    def build(self) -> "SignatureTemplate":
        return self._signature_template
