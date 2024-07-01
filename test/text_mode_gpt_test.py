from srai_core.store.bytes_store_base import BytesStoreBase
from srai_core.store.database_base import DatabaseBase
from srai_core.store.document_store_base import DocumentStoreBase

from srai_telegrambot.dao_telegram_bot import DaoTelegramBot
from srai_telegrambot.mode.text_mode_gpt import TextModeGpt
from srai_telegrambot.telegram_bot_interface import TelegramBotInterface


class DocumentStoreMemory(DocumentStoreBase):
    def __init__(self):
        self.dict_document = {}

    def save_document(self, document_id: str, document: dict):
        self.dict_document[document_id] = document

    def load_document(self, document_id: str) -> dict:
        return self.dict_document[document_id]

    def delete_document(self, document_id: str):
        del self.dict_document[document_id]

    def exists_document(self, document_id: str) -> bool:
        return document_id in self.dict_document

    def load_document_all(self) -> dict:
        return self.dict_document

    def count_document(self) -> int:
        return len(self.dict_document)


class BytesStoreMemory(BytesStoreBase):
    def __init__(self):
        self.dict_bytes = {}

    def save_bytes(self, bytes_id: str, bytes: bytes):
        self.dict_bytes[bytes_id] = bytes

    def load_bytes(self, bytes_id: str) -> bytes:
        return self.dict_bytes[bytes_id]

    def delete_bytes(self, bytes_id: str):
        del self.dict_bytes[bytes_id]

    def exists_bytes(self, bytes_id: str) -> bool:
        return bytes_id in self.dict_bytes

    def load_bytes_all(self) -> dict:
        return self.dict_bytes

    def count_bytes(self) -> int:
        return len(self.dict_bytes)


class DatabaseMemory(DatabaseBase):
    def __init__(self):
        pass

    def get_document_store(self, name: str) -> DocumentStoreBase:
        return DocumentStoreMemory()

    def get_bytes_store(self, collection_name: str) -> BytesStoreBase:
        return BytesStoreMemory()


class TelegramBotTest(TelegramBotInterface):
    def __init__(self):
        self.dao_telegram_bot = DaoTelegramBot(DatabaseMemory())

    def message_admins(self, text: str):
        print(text)

    def message_chat(self, chat_id: str, text: str):
        print(text)

    def get_dao(self):
        return self.dao_telegram_bot


def test_gpt():
    mode = TextModeGpt("you are a chatbot")
    mode.register(TelegramBotTest())
    print(mode._handle_text("test_chat", "Hi"))
    print(mode._handle_text("test_chat", "Please call me John"))
    print(mode._handle_text("test_chat", "What is my name?"))


if __name__ == "__main__":
    test_gpt()
