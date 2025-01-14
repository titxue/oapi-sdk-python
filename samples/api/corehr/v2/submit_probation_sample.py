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
    request: SubmitProbationRequest = SubmitProbationRequest.builder() \
        .client_token("6822122262122064111") \
        .user_id_type("open_id") \
        .request_body(SubmitProbationRequestBody.builder()
                      .employment_id("7140964208476371111")
                      .conversion_mode(1)
                      .actual_probation_end_date("2022-05-20")
                      .submission_type("system")
                      .initiator_id("7140964208476371111")
                      .notes("符合预期")
                      .self_review("符合预期")
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: SubmitProbationResponse = client.corehr.v2.probation.submit(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.probation.submit failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: SubmitProbationRequest = SubmitProbationRequest.builder() \
        .client_token("6822122262122064111") \
        .user_id_type("open_id") \
        .request_body(SubmitProbationRequestBody.builder()
                      .employment_id("7140964208476371111")
                      .conversion_mode(1)
                      .actual_probation_end_date("2022-05-20")
                      .submission_type("system")
                      .initiator_id("7140964208476371111")
                      .notes("符合预期")
                      .self_review("符合预期")
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: SubmitProbationResponse = await client.corehr.v2.probation.asubmit(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.probation.asubmit failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
