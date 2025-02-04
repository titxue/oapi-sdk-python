# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrProcessApproverUpdatedV2Data(object):
    _types = {
        "process_id": str,
        "approver_id": str,
        "type": int,
        "status": int,
        "biz_type": str,
        "flow_definition_id": str,
        "node_definition_id": str,
        "node_id": str,
    }

    def __init__(self, d=None):
        self.process_id: Optional[str] = None
        self.approver_id: Optional[str] = None
        self.type: Optional[int] = None
        self.status: Optional[int] = None
        self.biz_type: Optional[str] = None
        self.flow_definition_id: Optional[str] = None
        self.node_definition_id: Optional[str] = None
        self.node_id: Optional[str] = None
        init(self, d, self._types)


class P2CorehrProcessApproverUpdatedV2(EventContext):
    _types = {
        "event": P2CorehrProcessApproverUpdatedV2Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrProcessApproverUpdatedV2Data] = None
        init(self, d, self._types)
