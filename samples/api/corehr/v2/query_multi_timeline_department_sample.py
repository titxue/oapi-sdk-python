# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: QueryMultiTimelineDepartmentRequest = QueryMultiTimelineDepartmentRequest.builder() \
        .page_size(100) \
        .page_token("6891251722631890445") \
        .user_id_type("people_corehr_id") \
        .department_id_type("people_corehr_department_id") \
        .request_body(QueryMultiTimelineDepartmentRequestBody.builder()
                      .department_ids([])
                      .effective_date_start("2024-01-01")
                      .effective_date_end("2024-12-31")
                      .fields([])
                      .build()) \
        .build()

    # 发起请求
    response: QueryMultiTimelineDepartmentResponse = client.corehr.v2.department.query_multi_timeline(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.department.query_multi_timeline failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: QueryMultiTimelineDepartmentRequest = QueryMultiTimelineDepartmentRequest.builder() \
        .page_size(100) \
        .page_token("6891251722631890445") \
        .user_id_type("people_corehr_id") \
        .department_id_type("people_corehr_department_id") \
        .request_body(QueryMultiTimelineDepartmentRequestBody.builder()
                      .department_ids([])
                      .effective_date_start("2024-01-01")
                      .effective_date_end("2024-12-31")
                      .fields([])
                      .build()) \
        .build()

    # 发起请求
    response: QueryMultiTimelineDepartmentResponse = await client.corehr.v2.department.aquery_multi_timeline(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.department.aquery_multi_timeline failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
