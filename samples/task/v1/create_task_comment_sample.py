# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateTaskCommentRequest = CreateTaskCommentRequest.builder() \
        .task_id("83912691-2e43-47fc-94a4-d512e03984fa") \
        .user_id_type("user_id") \
        .request_body(Comment.builder()
                      .content("举杯邀明月，对影成三人")
                      .parent_id("6937231762296684564")
                      .create_milli_time("1657075055135")
                      .rich_content("举杯邀明月，对影成三人<at id=7058204817822318612></at>")
                      .build()) \
        .build()

    # 发起请求
    response: CreateTaskCommentResponse = client.task.v1.task_comment.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v1.task_comment.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()