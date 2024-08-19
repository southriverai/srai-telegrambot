import os

from srai_telegrambot.mode.text_mode_rag import TextModeRag
from srai_telegrambot.telegram_bot_test import TelegramBotTest


def test_text_mode_rag_pancan():

    path_dir_vectorstore = os.path.abspath(os.path.join("test", "data", "vectorstore_pancan"))
    mode = TextModeRag(path_dir_vectorstore)
    mode.register(TelegramBotTest())

    path_dir_data = os.path.abspath(os.path.join("..", "data"))
    list_name_file = os.listdir(path_dir_data)
    exit()
    for name_file in list_name_file:
        path_file = os.path.join(path_dir, name_file)
        mode.list_path_file_txt.append(path_file)

    mode.rebuild_vectorstore()
    print(mode._handle_text("test_chat", "What is the most important parameter in DCE-CT in stroke?"))
    print(mode._handle_text("test_chat", "Please elaborate?"))


if __name__ == "__main__":
    test_text_mode_rag_pancan()
