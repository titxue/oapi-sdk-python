# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .country_region import CountryRegion


class GetCountryRegionResponseBody(object):
    _types = {
        "country_region": CountryRegion,
    }

    def __init__(self, d):
        self.country_region: Optional[CountryRegion] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetCountryRegionResponseBodyBuilder":
        return GetCountryRegionResponseBodyBuilder()


class GetCountryRegionResponseBodyBuilder(object):
    def __init__(self, get_country_region_response_body: GetCountryRegionResponseBody = GetCountryRegionResponseBody(
        {})) -> None:
        self._get_country_region_response_body: GetCountryRegionResponseBody = get_country_region_response_body

    def country_region(self, country_region: CountryRegion) -> "GetCountryRegionResponseBodyBuilder":
        self._get_country_region_response_body.country_region = country_region
        return self

    def build(self) -> "GetCountryRegionResponseBody":
        return self._get_country_region_response_body