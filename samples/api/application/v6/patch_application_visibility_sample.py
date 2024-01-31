# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.application.v6 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchApplicationVisibilityRequest = PatchApplicationVisibilityRequest.builder() \
        .app_id("cli_9b445f5258795107") \
        .department_id_type("open_department_id") \
        .user_id_type("open_id") \
        .request_body(PatchApplicationVisibilityRequestBody.builder()
                      .add_visible_list(AppVisibilityIdList.builder().build())
                      .del_visible_list(AppVisibilityIdList.builder().build())
                      .add_invisible_list(AppVisibilityIdList.builder().build())
                      .del_invisible_list(AppVisibilityIdList.builder().build())
                      .is_visible_to_all(False)
                      .build()) \
        .build()

    # 发起请求
    response: PatchApplicationVisibilityResponse = client.application.v6.application_visibility.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application_visibility.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PatchApplicationVisibilityRequest = PatchApplicationVisibilityRequest.builder() \
        .app_id("cli_9b445f5258795107") \
        .department_id_type("open_department_id") \
        .user_id_type("open_id") \
        .request_body(PatchApplicationVisibilityRequestBody.builder()
                      .add_visible_list(AppVisibilityIdList.builder().build())
                      .del_visible_list(AppVisibilityIdList.builder().build())
                      .add_invisible_list(AppVisibilityIdList.builder().build())
                      .del_invisible_list(AppVisibilityIdList.builder().build())
                      .is_visible_to_all(False)
                      .build()) \
        .build()

    # 发起请求
    response: PatchApplicationVisibilityResponse = await client.application.v6.application_visibility.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application_visibility.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
