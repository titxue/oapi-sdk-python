# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.aily.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateAilySessionAilyMessageRequest = CreateAilySessionAilyMessageRequest.builder() \
        .aily_session_id("session_4dfunz7sp1g8m") \
        .request_body(CreateAilySessionAilyMessageRequestBody.builder()
                      .idempotent_id("idempotent_id_1")
                      .content_type("MDX")
                      .content("你好")
                      .file_ids([])
                      .quote_message_id("message_4de9bpg70qskh")
                      .mentions([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateAilySessionAilyMessageResponse = client.aily.v1.aily_session_aily_message.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.aily.v1.aily_session_aily_message.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateAilySessionAilyMessageRequest = CreateAilySessionAilyMessageRequest.builder() \
        .aily_session_id("session_4dfunz7sp1g8m") \
        .request_body(CreateAilySessionAilyMessageRequestBody.builder()
                      .idempotent_id("idempotent_id_1")
                      .content_type("MDX")
                      .content("你好")
                      .file_ids([])
                      .quote_message_id("message_4de9bpg70qskh")
                      .mentions([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateAilySessionAilyMessageResponse = await client.aily.v1.aily_session_aily_message.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.aily.v1.aily_session_aily_message.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()