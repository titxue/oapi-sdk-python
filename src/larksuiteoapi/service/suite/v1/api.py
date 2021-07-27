# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import *

from ....api import Request, Response, set_timeout, set_tenant_key, set_user_access_token, set_path_params, \
    set_query_params, set_response_stream, set_is_response_stream, FormData, FormDataFile
from ....config import Config
from ....consts import ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER, ACCESS_TOKEN_TYPE_APP
from .model import *


class Service(object):
    def __init__(self, conf):
        # type: (Config) -> None
        self.conf = conf
        self.docs_apis = DocsApiService(self)
        



class DocsApiService(object):
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def meta(self, body, user_access_token=None, timeout=None):
        # type: (DocsApiMetaReqBody, str, int) -> DocsApiMetaReqCall

        request_opts = []   # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocsApiMetaReqCall(self, body, request_opts=request_opts)

    def search(self, body, user_access_token=None, timeout=None):
        # type: (DocsApiSearchReqBody, str, int) -> DocsApiSearchReqCall

        request_opts = []   # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocsApiSearchReqCall(self, body, request_opts=request_opts)



class DocsApiMetaReqCall(object):
    def __init__(self, service, body, request_opts=None):
        # type: (DocsApiService, DocsApiMetaReqBody, List[Any]) -> None

        self.service = service
        self.body = body

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> Response[DocsApiMetaResult]
        root_service = self.service.service

        conf = root_service.conf
        req = Request('/open-apis/suite/docs-api/meta', 'POST', [ACCESS_TOKEN_TYPE_USER],
                      self.body, output_class=DocsApiMetaResult, request_opts=self.request_opts)
        resp = req.do(conf)
        return resp


class DocsApiSearchReqCall(object):
    def __init__(self, service, body, request_opts=None):
        # type: (DocsApiService, DocsApiSearchReqBody, List[Any]) -> None

        self.service = service
        self.body = body

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> Response[DocsApiSearchResult]
        root_service = self.service.service

        conf = root_service.conf
        req = Request('/open-apis/suite/docs-api/search/object', 'POST', [ACCESS_TOKEN_TYPE_USER],
                      self.body, output_class=DocsApiSearchResult, request_opts=self.request_opts)
        resp = req.do(conf)
        return resp

