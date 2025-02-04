# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .search_job_publish_record_request_body import SearchJobPublishRecordRequestBody


class SearchJobPublishRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.job_level_id_type: Optional[str] = None
        self.job_family_id_type: Optional[str] = None
        self.request_body: Optional[SearchJobPublishRecordRequestBody] = None

    @staticmethod
    def builder() -> "SearchJobPublishRecordRequestBuilder":
        return SearchJobPublishRecordRequestBuilder()


class SearchJobPublishRecordRequestBuilder(object):

    def __init__(self) -> None:
        search_job_publish_record_request = SearchJobPublishRecordRequest()
        search_job_publish_record_request.http_method = HttpMethod.POST
        search_job_publish_record_request.uri = "/open-apis/hire/v1/job_publish_records/search"
        search_job_publish_record_request.token_types = {AccessTokenType.TENANT}
        self._search_job_publish_record_request: SearchJobPublishRecordRequest = search_job_publish_record_request

    def page_token(self, page_token: str) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.page_token = page_token
        self._search_job_publish_record_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.page_size = page_size
        self._search_job_publish_record_request.add_query("page_size", page_size)
        return self

    def user_id_type(self, user_id_type: str) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.user_id_type = user_id_type
        self._search_job_publish_record_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.department_id_type = department_id_type
        self._search_job_publish_record_request.add_query("department_id_type", department_id_type)
        return self

    def job_level_id_type(self, job_level_id_type: str) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.job_level_id_type = job_level_id_type
        self._search_job_publish_record_request.add_query("job_level_id_type", job_level_id_type)
        return self

    def job_family_id_type(self, job_family_id_type: str) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.job_family_id_type = job_family_id_type
        self._search_job_publish_record_request.add_query("job_family_id_type", job_family_id_type)
        return self

    def request_body(self, request_body: SearchJobPublishRecordRequestBody) -> "SearchJobPublishRecordRequestBuilder":
        self._search_job_publish_record_request.request_body = request_body
        self._search_job_publish_record_request.body = request_body
        return self

    def build(self) -> SearchJobPublishRecordRequest:
        return self._search_job_publish_record_request
