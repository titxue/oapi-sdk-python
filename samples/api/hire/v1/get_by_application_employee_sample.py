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
    request: GetByApplicationEmployeeRequest = GetByApplicationEmployeeRequest.builder() \
        .application_id("123") \
        .user_id_type("open_id") \
        .department_id_type("people_admin_department_id") \
        .job_level_id_type("people_admin_job_level_id") \
        .job_family_id_type("people_admin_job_category_id") \
        .employee_type_id_type("people_admin_employee_type_id") \
        .build()

    # 发起请求
    response: GetByApplicationEmployeeResponse = client.hire.v1.employee.get_by_application(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.employee.get_by_application failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
