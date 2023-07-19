# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .content_paragraph_element import ContentParagraphElement
from .content_paragraph_style import ContentParagraphStyle


class ContentParagraph(object):
    _types = {
        "style": ContentParagraphStyle,
        "elements": List[ContentParagraphElement],
    }

    def __init__(self, d):
        self.style: Optional[ContentParagraphStyle] = None
        self.elements: Optional[List[ContentParagraphElement]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentParagraphBuilder":
        return ContentParagraphBuilder()


class ContentParagraphBuilder(object):
    def __init__(self, content_paragraph: ContentParagraph = ContentParagraph({})) -> None:
        self._content_paragraph: ContentParagraph = content_paragraph

    def style(self, style: ContentParagraphStyle) -> "ContentParagraphBuilder":
        self._content_paragraph.style = style
        return self

    def elements(self, elements: List[ContentParagraphElement]) -> "ContentParagraphBuilder":
        self._content_paragraph.elements = elements
        return self

    def build(self) -> "ContentParagraph":
        return self._content_paragraph