import os

from srai_telegrambot.mode.text_mode_rag import TextModeRag
from srai_telegrambot.telegram_bot_test import TelegramBotTest


def test_text_mode_rag():

    path_dir_vectorstore = os.path.abspath(os.path.join("test", "data", "vectorstore"))
    mode = TextModeRag(path_dir_vectorstore)
    mode.register(TelegramBotTest())

    list_path_file = []
    list_path_file.append(os.path.abspath(os.path.join("test", "data", "paper_0.pdf")))
    list_path_file.append(os.path.abspath(os.path.join("test", "data", "paper_1.pdf")))
    list_path_file.append(os.path.abspath(os.path.join("test", "data", "paper_2.pdf")))

    for path_file in list_path_file:
        mode.add_path_file_pdf(path_file)
    mode.rebuild_vectorstore()
    print(mode._handle_text("test_chat", "What is the most important parameter in DCE-CT in stroke?"))
    print(mode._handle_text("test_chat", "Please elaborate?"))


if __name__ == "__main__":
    test_text_mode_rag()
