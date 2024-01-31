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
    request: CreatePreHireRequest = CreatePreHireRequest.builder() \
        .request_body(PrehireCreate.builder()
                      .basic_info(BasicInfo.builder().build())
                      .offer_info(OfferInfo.builder().build())
                      .education_info([])
                      .work_experience([])
                      .ats_application_id("7140946969586010376")
                      .build()) \
        .build()

    # 发起请求
    response: CreatePreHireResponse = client.corehr.v2.pre_hire.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.pre_hire.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreatePreHireRequest = CreatePreHireRequest.builder() \
        .request_body(PrehireCreate.builder()
                      .basic_info(BasicInfo.builder().build())
                      .offer_info(OfferInfo.builder().build())
                      .education_info([])
                      .work_experience([])
                      .ats_application_id("7140946969586010376")
                      .build()) \
        .build()

    # 发起请求
    response: CreatePreHireResponse = await client.corehr.v2.pre_hire.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.pre_hire.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
