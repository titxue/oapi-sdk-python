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
    request: CreateJobRequirementRequest = CreateJobRequirementRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("open_department_id") \
        .job_level_id_type("people_admin_job_level_id") \
        .job_family_id_type("people_admin_job_category_id") \
        .employee_type_id_type("people_admin_employee_type_id") \
        .request_body(JobRequirement.builder()
                      .short_code("xx1")
                      .name("test")
                      .display_progress(1)
                      .head_count(11)
                      .recruitment_type_id("1618209327096")
                      .employee_type_id("6807409776231254285")
                      .max_level_id("123")
                      .min_level_id("11")
                      .sequence_id("111")
                      .category(1)
                      .department_id("1111")
                      .recruiter_id_list([])
                      .jr_hiring_manager_id_list([])
                      .direct_leader_id_list([])
                      .start_time("1625729379000")
                      .deadline("1625729379000")
                      .priority(1)
                      .required_degree(1)
                      .max_salary("123")
                      .min_salary("11")
                      .address_id("11")
                      .description("11")
                      .customized_data_list([])
                      .process_type(1)
                      .job_type_id("6930815272790114324")
                      .build()) \
        .build()

    # 发起请求
    response: CreateJobRequirementResponse = client.hire.v1.job_requirement.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.job_requirement.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
