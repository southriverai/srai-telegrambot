from srai_telegrambot.mode.text_mode_gpt import TextModeGpt
from srai_telegrambot.telegram_bot_test import TelegramBotTest


def test_gpt():
    mode = TextModeGpt("you are a chatbot")
    mode.register(TelegramBotTest())
    print(mode._handle_text("test_chat", "Hi"))
    print(mode._handle_text("test_chat", "Please call me John"))
    print(mode._handle_text("test_chat", "What is my name?"))


if __name__ == "__main__":
    test_gpt()
