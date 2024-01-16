# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.search_basic_info_bank_branch_request import SearchBasicInfoBankBranchRequest
from ..model.search_basic_info_bank_branch_response import SearchBasicInfoBankBranchResponse


class BasicInfoBankBranch(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def search(self, request: SearchBasicInfoBankBranchRequest,
               option: Optional[RequestOption] = None) -> SearchBasicInfoBankBranchResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchBasicInfoBankBranchResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     SearchBasicInfoBankBranchResponse)
        response.raw = resp

        return response
