# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .app_ability_bot_i18n import AppAbilityBotI18n


class AppAbilityBot(object):
    _types = {
        "enable": bool,
        "message_card_callback_url": str,
        "i18ns": List[AppAbilityBotI18n],
    }

    def __init__(self, d=None):
        self.enable: Optional[bool] = None
        self.message_card_callback_url: Optional[str] = None
        self.i18ns: Optional[List[AppAbilityBotI18n]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppAbilityBotBuilder":
        return AppAbilityBotBuilder()


class AppAbilityBotBuilder(object):
    def __init__(self) -> None:
        self._app_ability_bot = AppAbilityBot()

    def enable(self, enable: bool) -> "AppAbilityBotBuilder":
        self._app_ability_bot.enable = enable
        return self

    def message_card_callback_url(self, message_card_callback_url: str) -> "AppAbilityBotBuilder":
        self._app_ability_bot.message_card_callback_url = message_card_callback_url
        return self

    def i18ns(self, i18ns: List[AppAbilityBotI18n]) -> "AppAbilityBotBuilder":
        self._app_ability_bot.i18ns = i18ns
        return self

    def build(self) -> "AppAbilityBot":
        return self._app_ability_bot
