# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .master_location_info import MasterLocationInfo


class MasterLocationAddressInfo(object):
    _types = {
        "location_info": MasterLocationInfo,
        "address_info": MasterLocationInfo,
    }

    def __init__(self, d=None):
        self.location_info: Optional[MasterLocationInfo] = None
        self.address_info: Optional[MasterLocationInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MasterLocationAddressInfoBuilder":
        return MasterLocationAddressInfoBuilder()


class MasterLocationAddressInfoBuilder(object):
    def __init__(self) -> None:
        self._master_location_address_info = MasterLocationAddressInfo()

    def location_info(self, location_info: MasterLocationInfo) -> "MasterLocationAddressInfoBuilder":
        self._master_location_address_info.location_info = location_info
        return self

    def address_info(self, address_info: MasterLocationInfo) -> "MasterLocationAddressInfoBuilder":
        self._master_location_address_info.address_info = address_info
        return self

    def build(self) -> "MasterLocationAddressInfo":
        return self._master_location_address_info