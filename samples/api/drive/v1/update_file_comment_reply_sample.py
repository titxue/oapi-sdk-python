# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: UpdateFileCommentReplyRequest = UpdateFileCommentReplyRequest.builder() \
        .file_token("doccnHh7U87HOFpii5u5G*****") \
        .comment_id("6916106822734578184") \
        .reply_id("6916106822734594568") \
        .file_type("doc") \
        .user_id_type("user_id") \
        .request_body(UpdateFileCommentReplyRequestBody.builder()
                      .content(ReplyContent.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: UpdateFileCommentReplyResponse = client.drive.v1.file_comment_reply.update(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file_comment_reply.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: UpdateFileCommentReplyRequest = UpdateFileCommentReplyRequest.builder() \
        .file_token("doccnHh7U87HOFpii5u5G*****") \
        .comment_id("6916106822734578184") \
        .reply_id("6916106822734594568") \
        .file_type("doc") \
        .user_id_type("user_id") \
        .request_body(UpdateFileCommentReplyRequestBody.builder()
                      .content(ReplyContent.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: UpdateFileCommentReplyResponse = await client.drive.v1.file_comment_reply.aupdate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file_comment_reply.aupdate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
