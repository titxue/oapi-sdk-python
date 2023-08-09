# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: RemoveTasklistTaskRequest = RemoveTasklistTaskRequest.builder() \
        .task_guid("d300a75f-c56a-4be9-80d1-e47653028ceb") \
        .user_id_type("open_id") \
        .request_body(RemoveTasklistTaskRequestBody.builder()
                      .tasklist_guid("d300a75f-c56a-4be9-80d1-e47653028ceb")
                      .build()) \
        .build()

    # 发起请求
    response: RemoveTasklistTaskResponse = client.task.v2.task.remove_tasklist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.task.remove_tasklist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()