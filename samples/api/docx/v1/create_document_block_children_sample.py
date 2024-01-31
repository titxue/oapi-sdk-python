# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.docx.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateDocumentBlockChildrenRequest = CreateDocumentBlockChildrenRequest.builder() \
        .document_id("doxcnePuYufKa49ISjhD8Ih0ikh") \
        .block_id("doxcnO6UW6wAw2qIcYf4hZpFIth") \
        .document_revision_id(-1) \
        .client_token("fe599b60-450f-46ff-b2ef-9f6675625b97") \
        .user_id_type("user_id") \
        .request_body(CreateDocumentBlockChildrenRequestBody.builder()
                      .children([])
                      .index(-1)
                      .build()) \
        .build()

    # 发起请求
    response: CreateDocumentBlockChildrenResponse = client.docx.v1.document_block_children.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.docx.v1.document_block_children.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateDocumentBlockChildrenRequest = CreateDocumentBlockChildrenRequest.builder() \
        .document_id("doxcnePuYufKa49ISjhD8Ih0ikh") \
        .block_id("doxcnO6UW6wAw2qIcYf4hZpFIth") \
        .document_revision_id(-1) \
        .client_token("fe599b60-450f-46ff-b2ef-9f6675625b97") \
        .user_id_type("user_id") \
        .request_body(CreateDocumentBlockChildrenRequestBody.builder()
                      .children([])
                      .index(-1)
                      .build()) \
        .build()

    # 发起请求
    response: CreateDocumentBlockChildrenResponse = await client.docx.v1.document_block_children.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.docx.v1.document_block_children.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
