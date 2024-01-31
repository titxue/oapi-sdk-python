# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchJobLevelRequest = PatchJobLevelRequest.builder() \
        .job_level_id("1616161616") \
        .client_token("12454646") \
        .request_body(JobLevel.builder()
                      .level_order(9999)
                      .code("VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=")
                      .name([])
                      .description([])
                      .active(True)
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchJobLevelResponse = client.corehr.v1.job_level.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.job_level.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PatchJobLevelRequest = PatchJobLevelRequest.builder() \
        .job_level_id("1616161616") \
        .client_token("12454646") \
        .request_body(JobLevel.builder()
                      .level_order(9999)
                      .code("VQzo/BSonp8l6PmcZ+VlDhkd2595LMkhyBAGX6HAlCY=")
                      .name([])
                      .description([])
                      .active(True)
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchJobLevelResponse = await client.corehr.v1.job_level.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.job_level.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
