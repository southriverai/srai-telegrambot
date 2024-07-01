from srai_telegrambot.mode.text_mode_gpt import TextModeGpt


def test_gpt():
    mode = TextModeGpt("you are a chatbot")
    print(mode._handle_text("Hi"))


if __name__ == "__main__":
    test_gpt()
