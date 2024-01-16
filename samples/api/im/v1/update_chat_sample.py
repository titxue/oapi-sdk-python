# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: UpdateChatRequest = UpdateChatRequest.builder() \
        .chat_id("oc_a0553eda9014c201e6969b478895c230") \
        .user_id_type("user_id") \
        .request_body(UpdateChatRequestBody.builder()
                      .avatar("default-avatar_44ae0ca3-e140-494b-956f-78091e348435")
                      .name("群聊")
                      .description("测试群描述")
                      .i18n_names(I18nNames.builder().build())
                      .add_member_permission("all_members")
                      .share_card_permission("allowed")
                      .at_all_permission("all_members")
                      .edit_permission("all_members")
                      .owner_id("4d7a3c6g")
                      .join_message_visibility("only_owner")
                      .leave_message_visibility("only_owner")
                      .membership_approval("no_approval_required")
                      .restricted_mode_setting(RestrictedModeSetting.builder().build())
                      .chat_type("private")
                      .group_message_type("chat")
                      .urgent_setting("all_members")
                      .video_conference_setting("all_members")
                      .build()) \
        .build()

    # 发起请求
    response: UpdateChatResponse = client.im.v1.chat.update(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.chat.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
