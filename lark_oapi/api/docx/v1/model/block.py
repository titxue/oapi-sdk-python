# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .add_ons import AddOns
from .bitable import Bitable
from .board import Board
from .callout import Callout
from .chat_card import ChatCard
from .diagram import Diagram
from .divider import Divider
from .file import File
from .grid import Grid
from .grid_column import GridColumn
from .iframe import Iframe
from .image import Image
from .isv import Isv
from .jira_issue import JiraIssue
from .mindnote import Mindnote
from .okr import Okr
from .okr_key_result import OkrKeyResult
from .okr_objective import OkrObjective
from .okr_progress import OkrProgress
from .quote_container import QuoteContainer
from .sheet import Sheet
from .table import Table
from .table_cell import TableCell
from .task import Task
from .text import Text
from .undefined import Undefined
from .view import View
from .wiki_catalog import WikiCatalog


class Block(object):
    _types = {
        "block_id": str,
        "parent_id": str,
        "children": List[str],
        "block_type": int,
        "page": Text,
        "text": Text,
        "heading1": Text,
        "heading2": Text,
        "heading3": Text,
        "heading4": Text,
        "heading5": Text,
        "heading6": Text,
        "heading7": Text,
        "heading8": Text,
        "heading9": Text,
        "bullet": Text,
        "ordered": Text,
        "code": Text,
        "quote": Text,
        "equation": Text,
        "todo": Text,
        "bitable": Bitable,
        "callout": Callout,
        "chat_card": ChatCard,
        "diagram": Diagram,
        "divider": Divider,
        "file": File,
        "grid": Grid,
        "grid_column": GridColumn,
        "iframe": Iframe,
        "image": Image,
        "isv": Isv,
        "add_ons": AddOns,
        "mindnote": Mindnote,
        "sheet": Sheet,
        "table": Table,
        "table_cell": TableCell,
        "view": View,
        "undefined": Undefined,
        "quote_container": QuoteContainer,
        "task": Task,
        "okr": Okr,
        "okr_objective": OkrObjective,
        "okr_key_result": OkrKeyResult,
        "okr_progress": OkrProgress,
        "comment_ids": List[str],
        "jira_issue": JiraIssue,
        "wiki_catalog": WikiCatalog,
        "board": Board,
    }

    def __init__(self, d=None):
        self.block_id: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.children: Optional[List[str]] = None
        self.block_type: Optional[int] = None
        self.page: Optional[Text] = None
        self.text: Optional[Text] = None
        self.heading1: Optional[Text] = None
        self.heading2: Optional[Text] = None
        self.heading3: Optional[Text] = None
        self.heading4: Optional[Text] = None
        self.heading5: Optional[Text] = None
        self.heading6: Optional[Text] = None
        self.heading7: Optional[Text] = None
        self.heading8: Optional[Text] = None
        self.heading9: Optional[Text] = None
        self.bullet: Optional[Text] = None
        self.ordered: Optional[Text] = None
        self.code: Optional[Text] = None
        self.quote: Optional[Text] = None
        self.equation: Optional[Text] = None
        self.todo: Optional[Text] = None
        self.bitable: Optional[Bitable] = None
        self.callout: Optional[Callout] = None
        self.chat_card: Optional[ChatCard] = None
        self.diagram: Optional[Diagram] = None
        self.divider: Optional[Divider] = None
        self.file: Optional[File] = None
        self.grid: Optional[Grid] = None
        self.grid_column: Optional[GridColumn] = None
        self.iframe: Optional[Iframe] = None
        self.image: Optional[Image] = None
        self.isv: Optional[Isv] = None
        self.add_ons: Optional[AddOns] = None
        self.mindnote: Optional[Mindnote] = None
        self.sheet: Optional[Sheet] = None
        self.table: Optional[Table] = None
        self.table_cell: Optional[TableCell] = None
        self.view: Optional[View] = None
        self.undefined: Optional[Undefined] = None
        self.quote_container: Optional[QuoteContainer] = None
        self.task: Optional[Task] = None
        self.okr: Optional[Okr] = None
        self.okr_objective: Optional[OkrObjective] = None
        self.okr_key_result: Optional[OkrKeyResult] = None
        self.okr_progress: Optional[OkrProgress] = None
        self.comment_ids: Optional[List[str]] = None
        self.jira_issue: Optional[JiraIssue] = None
        self.wiki_catalog: Optional[WikiCatalog] = None
        self.board: Optional[Board] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BlockBuilder":
        return BlockBuilder()


class BlockBuilder(object):
    def __init__(self) -> None:
        self._block = Block()

    def block_id(self, block_id: str) -> "BlockBuilder":
        self._block.block_id = block_id
        return self

    def parent_id(self, parent_id: str) -> "BlockBuilder":
        self._block.parent_id = parent_id
        return self

    def children(self, children: List[str]) -> "BlockBuilder":
        self._block.children = children
        return self

    def block_type(self, block_type: int) -> "BlockBuilder":
        self._block.block_type = block_type
        return self

    def page(self, page: Text) -> "BlockBuilder":
        self._block.page = page
        return self

    def text(self, text: Text) -> "BlockBuilder":
        self._block.text = text
        return self

    def heading1(self, heading1: Text) -> "BlockBuilder":
        self._block.heading1 = heading1
        return self

    def heading2(self, heading2: Text) -> "BlockBuilder":
        self._block.heading2 = heading2
        return self

    def heading3(self, heading3: Text) -> "BlockBuilder":
        self._block.heading3 = heading3
        return self

    def heading4(self, heading4: Text) -> "BlockBuilder":
        self._block.heading4 = heading4
        return self

    def heading5(self, heading5: Text) -> "BlockBuilder":
        self._block.heading5 = heading5
        return self

    def heading6(self, heading6: Text) -> "BlockBuilder":
        self._block.heading6 = heading6
        return self

    def heading7(self, heading7: Text) -> "BlockBuilder":
        self._block.heading7 = heading7
        return self

    def heading8(self, heading8: Text) -> "BlockBuilder":
        self._block.heading8 = heading8
        return self

    def heading9(self, heading9: Text) -> "BlockBuilder":
        self._block.heading9 = heading9
        return self

    def bullet(self, bullet: Text) -> "BlockBuilder":
        self._block.bullet = bullet
        return self

    def ordered(self, ordered: Text) -> "BlockBuilder":
        self._block.ordered = ordered
        return self

    def code(self, code: Text) -> "BlockBuilder":
        self._block.code = code
        return self

    def quote(self, quote: Text) -> "BlockBuilder":
        self._block.quote = quote
        return self

    def equation(self, equation: Text) -> "BlockBuilder":
        self._block.equation = equation
        return self

    def todo(self, todo: Text) -> "BlockBuilder":
        self._block.todo = todo
        return self

    def bitable(self, bitable: Bitable) -> "BlockBuilder":
        self._block.bitable = bitable
        return self

    def callout(self, callout: Callout) -> "BlockBuilder":
        self._block.callout = callout
        return self

    def chat_card(self, chat_card: ChatCard) -> "BlockBuilder":
        self._block.chat_card = chat_card
        return self

    def diagram(self, diagram: Diagram) -> "BlockBuilder":
        self._block.diagram = diagram
        return self

    def divider(self, divider: Divider) -> "BlockBuilder":
        self._block.divider = divider
        return self

    def file(self, file: File) -> "BlockBuilder":
        self._block.file = file
        return self

    def grid(self, grid: Grid) -> "BlockBuilder":
        self._block.grid = grid
        return self

    def grid_column(self, grid_column: GridColumn) -> "BlockBuilder":
        self._block.grid_column = grid_column
        return self

    def iframe(self, iframe: Iframe) -> "BlockBuilder":
        self._block.iframe = iframe
        return self

    def image(self, image: Image) -> "BlockBuilder":
        self._block.image = image
        return self

    def isv(self, isv: Isv) -> "BlockBuilder":
        self._block.isv = isv
        return self

    def add_ons(self, add_ons: AddOns) -> "BlockBuilder":
        self._block.add_ons = add_ons
        return self

    def mindnote(self, mindnote: Mindnote) -> "BlockBuilder":
        self._block.mindnote = mindnote
        return self

    def sheet(self, sheet: Sheet) -> "BlockBuilder":
        self._block.sheet = sheet
        return self

    def table(self, table: Table) -> "BlockBuilder":
        self._block.table = table
        return self

    def table_cell(self, table_cell: TableCell) -> "BlockBuilder":
        self._block.table_cell = table_cell
        return self

    def view(self, view: View) -> "BlockBuilder":
        self._block.view = view
        return self

    def undefined(self, undefined: Undefined) -> "BlockBuilder":
        self._block.undefined = undefined
        return self

    def quote_container(self, quote_container: QuoteContainer) -> "BlockBuilder":
        self._block.quote_container = quote_container
        return self

    def task(self, task: Task) -> "BlockBuilder":
        self._block.task = task
        return self

    def okr(self, okr: Okr) -> "BlockBuilder":
        self._block.okr = okr
        return self

    def okr_objective(self, okr_objective: OkrObjective) -> "BlockBuilder":
        self._block.okr_objective = okr_objective
        return self

    def okr_key_result(self, okr_key_result: OkrKeyResult) -> "BlockBuilder":
        self._block.okr_key_result = okr_key_result
        return self

    def okr_progress(self, okr_progress: OkrProgress) -> "BlockBuilder":
        self._block.okr_progress = okr_progress
        return self

    def comment_ids(self, comment_ids: List[str]) -> "BlockBuilder":
        self._block.comment_ids = comment_ids
        return self

    def jira_issue(self, jira_issue: JiraIssue) -> "BlockBuilder":
        self._block.jira_issue = jira_issue
        return self

    def wiki_catalog(self, wiki_catalog: WikiCatalog) -> "BlockBuilder":
        self._block.wiki_catalog = wiki_catalog
        return self

    def board(self, board: Board) -> "BlockBuilder":
        self._block.board = board
        return self

    def build(self) -> "Block":
        return self._block
