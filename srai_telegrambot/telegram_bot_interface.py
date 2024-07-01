from abc import ABC, abstractmethod


class TelegramBotInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def message_admins(self, text: str):
        raise NotImplementedError()

    @abstractmethod
    def message_chat(self, chat_id: str, text: str):
        raise NotImplementedError()
