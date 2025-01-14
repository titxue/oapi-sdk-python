# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.admin.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListAuditInfoRequest = ListAuditInfoRequest.builder() \
        .user_id_type("user_id") \
        .latest(1668700799) \
        .oldest(1668528000) \
        .event_name("space_create_doc") \
        .operator_type("user") \
        .operator_value("55ed16fe") \
        .event_module(1) \
        .page_token(
        "LC39/f1%2B/Sz9Uv39Gf39/ew/cd5WY0gfGYFdixOW9cVk4bC79ituO/gx0qpPn1bYf92nz/kI0nNJOG3wCwDJKoNU%2BtyaXbpI8pV/9UNDMZT0BNeyanFH17Wv711Qh9anR3l2GjQfc2fUqXtxg1YPp63XyhYY4iRMv54ySRG7r%2BI89iS3zAoPzFuuU1MUJKsf") \
        .page_size(20) \
        .user_type(0) \
        .object_type(1) \
        .object_value("55ed16fe") \
        .ext_filter_object_by_ccm_token("55ed16fe") \
        .build()

    # 发起请求
    response: ListAuditInfoResponse = client.admin.v1.audit_info.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.admin.v1.audit_info.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListAuditInfoRequest = ListAuditInfoRequest.builder() \
        .user_id_type("user_id") \
        .latest(1668700799) \
        .oldest(1668528000) \
        .event_name("space_create_doc") \
        .operator_type("user") \
        .operator_value("55ed16fe") \
        .event_module(1) \
        .page_token(
        "LC39/f1%2B/Sz9Uv39Gf39/ew/cd5WY0gfGYFdixOW9cVk4bC79ituO/gx0qpPn1bYf92nz/kI0nNJOG3wCwDJKoNU%2BtyaXbpI8pV/9UNDMZT0BNeyanFH17Wv711Qh9anR3l2GjQfc2fUqXtxg1YPp63XyhYY4iRMv54ySRG7r%2BI89iS3zAoPzFuuU1MUJKsf") \
        .page_size(20) \
        .user_type(0) \
        .object_type(1) \
        .object_value("55ed16fe") \
        .ext_filter_object_by_ccm_token("55ed16fe") \
        .build()

    # 发起请求
    response: ListAuditInfoResponse = await client.admin.v1.audit_info.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.admin.v1.audit_info.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
