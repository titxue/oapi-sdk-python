# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateTripartiteAgreementRequest = CreateTripartiteAgreementRequest.builder() \
        .request_body(TripartiteAgreementInfo.builder()
                      .application_id("6930815272790114325")
                      .state(1)
                      .create_time("1698292282660")
                      .build()) \
        .build()

    # 发起请求
    response: CreateTripartiteAgreementResponse = client.hire.v1.tripartite_agreement.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.tripartite_agreement.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateTripartiteAgreementRequest = CreateTripartiteAgreementRequest.builder() \
        .request_body(TripartiteAgreementInfo.builder()
                      .application_id("6930815272790114325")
                      .state(1)
                      .create_time("1698292282660")
                      .build()) \
        .build()

    # 发起请求
    response: CreateTripartiteAgreementResponse = await client.hire.v1.tripartite_agreement.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.tripartite_agreement.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
