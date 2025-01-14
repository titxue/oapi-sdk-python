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
    request: CreateByResumeWebsiteDeliveryRequest = CreateByResumeWebsiteDeliveryRequest.builder() \
        .website_id("1618209327096") \
        .user_id_type("open_id") \
        .request_body(WebsiteDelivery.builder()
                      .job_post_id("6960663240925956636")
                      .resume(WebsiteDeliveryResume.builder().build())
                      .user_id("6960663240925956634")
                      .application_preferred_city_code_list([])
                      .channel_id("6891560630172518670")
                      .build()) \
        .build()

    # 发起请求
    response: CreateByResumeWebsiteDeliveryResponse = client.hire.v1.website_delivery.create_by_resume(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.website_delivery.create_by_resume failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateByResumeWebsiteDeliveryRequest = CreateByResumeWebsiteDeliveryRequest.builder() \
        .website_id("1618209327096") \
        .user_id_type("open_id") \
        .request_body(WebsiteDelivery.builder()
                      .job_post_id("6960663240925956636")
                      .resume(WebsiteDeliveryResume.builder().build())
                      .user_id("6960663240925956634")
                      .application_preferred_city_code_list([])
                      .channel_id("6891560630172518670")
                      .build()) \
        .build()

    # 发起请求
    response: CreateByResumeWebsiteDeliveryResponse = await client.hire.v1.website_delivery.acreate_by_resume(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.website_delivery.acreate_by_resume failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
