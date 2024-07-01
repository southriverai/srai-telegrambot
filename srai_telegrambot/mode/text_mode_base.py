from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext

from srai_telegrambot.telegram_bot_interface import TelegramBotInterface


class TextModeBase(ABC):

    def __init__(self, text_mode_name: str) -> None:
        self.text_mode_name = text_mode_name
        self.telegram_bot: TelegramBotInterface = None  # type: ignore

    def register(self, telegram_bot: TelegramBotInterface) -> None:
        if telegram_bot is None:
            raise ValueError("telegram_bot cannot be None")
        self.telegram_bot = telegram_bot

    def handle_text(self, update: Update, context: CallbackContext):
        message = self._handle_text(update.message.text)
        update.message.reply_text(message)

    @abstractmethod
    def _handle_text(self, text: str) -> str:
        raise NotImplementedError()
