# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n_names import I18nNames
from .restricted_mode_setting import RestrictedModeSetting
from .user_id import UserId


class ChatChange(object):
    _types = {
        "avatar": str,
        "name": str,
        "description": str,
        "i18n_names": I18nNames,
        "add_member_permission": str,
        "share_card_permission": str,
        "at_all_permission": str,
        "edit_permission": str,
        "membership_approval": str,
        "join_message_visibility": str,
        "leave_message_visibility": str,
        "moderation_permission": str,
        "owner_id": UserId,
        "restricted_mode_setting": RestrictedModeSetting,
        "group_message_type": str,
    }

    def __init__(self, d=None):
        self.avatar: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.i18n_names: Optional[I18nNames] = None
        self.add_member_permission: Optional[str] = None
        self.share_card_permission: Optional[str] = None
        self.at_all_permission: Optional[str] = None
        self.edit_permission: Optional[str] = None
        self.membership_approval: Optional[str] = None
        self.join_message_visibility: Optional[str] = None
        self.leave_message_visibility: Optional[str] = None
        self.moderation_permission: Optional[str] = None
        self.owner_id: Optional[UserId] = None
        self.restricted_mode_setting: Optional[RestrictedModeSetting] = None
        self.group_message_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatChangeBuilder":
        return ChatChangeBuilder()


class ChatChangeBuilder(object):
    def __init__(self) -> None:
        self._chat_change = ChatChange()

    def avatar(self, avatar: str) -> "ChatChangeBuilder":
        self._chat_change.avatar = avatar
        return self

    def name(self, name: str) -> "ChatChangeBuilder":
        self._chat_change.name = name
        return self

    def description(self, description: str) -> "ChatChangeBuilder":
        self._chat_change.description = description
        return self

    def i18n_names(self, i18n_names: I18nNames) -> "ChatChangeBuilder":
        self._chat_change.i18n_names = i18n_names
        return self

    def add_member_permission(self, add_member_permission: str) -> "ChatChangeBuilder":
        self._chat_change.add_member_permission = add_member_permission
        return self

    def share_card_permission(self, share_card_permission: str) -> "ChatChangeBuilder":
        self._chat_change.share_card_permission = share_card_permission
        return self

    def at_all_permission(self, at_all_permission: str) -> "ChatChangeBuilder":
        self._chat_change.at_all_permission = at_all_permission
        return self

    def edit_permission(self, edit_permission: str) -> "ChatChangeBuilder":
        self._chat_change.edit_permission = edit_permission
        return self

    def membership_approval(self, membership_approval: str) -> "ChatChangeBuilder":
        self._chat_change.membership_approval = membership_approval
        return self

    def join_message_visibility(self, join_message_visibility: str) -> "ChatChangeBuilder":
        self._chat_change.join_message_visibility = join_message_visibility
        return self

    def leave_message_visibility(self, leave_message_visibility: str) -> "ChatChangeBuilder":
        self._chat_change.leave_message_visibility = leave_message_visibility
        return self

    def moderation_permission(self, moderation_permission: str) -> "ChatChangeBuilder":
        self._chat_change.moderation_permission = moderation_permission
        return self

    def owner_id(self, owner_id: UserId) -> "ChatChangeBuilder":
        self._chat_change.owner_id = owner_id
        return self

    def restricted_mode_setting(self, restricted_mode_setting: RestrictedModeSetting) -> "ChatChangeBuilder":
        self._chat_change.restricted_mode_setting = restricted_mode_setting
        return self

    def group_message_type(self, group_message_type: str) -> "ChatChangeBuilder":
        self._chat_change.group_message_type = group_message_type
        return self

    def build(self) -> "ChatChange":
        return self._chat_change
