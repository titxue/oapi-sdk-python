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
    request: BatchGetEmployeesJobDataRequest = BatchGetEmployeesJobDataRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("people_corehr_department_id") \
        .request_body(BatchGetEmployeesJobDataRequestBody.builder()
                      .employment_ids([])
                      .get_all_version(False)
                      .effective_date_start("2020-01-01")
                      .effective_date_end("2020-01-01")
                      .data_date("2020-01-01")
                      .build()) \
        .build()

    # 发起请求
    response: BatchGetEmployeesJobDataResponse = client.corehr.v2.employees_job_data.batch_get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.employees_job_data.batch_get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: BatchGetEmployeesJobDataRequest = BatchGetEmployeesJobDataRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("people_corehr_department_id") \
        .request_body(BatchGetEmployeesJobDataRequestBody.builder()
                      .employment_ids([])
                      .get_all_version(False)
                      .effective_date_start("2020-01-01")
                      .effective_date_end("2020-01-01")
                      .data_date("2020-01-01")
                      .build()) \
        .build()

    # 发起请求
    response: BatchGetEmployeesJobDataResponse = await client.corehr.v2.employees_job_data.abatch_get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.employees_job_data.abatch_get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
