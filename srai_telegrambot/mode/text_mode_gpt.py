from srai_openai.client_openai_chatgpt import ClientOpenaiChatgpt

from srai_telegrambot.mode.text_mode_base import TextModeBase


class TextModeGpt(TextModeBase):

    def __init__(self, system_message_content: str):
        super().__init__("text_mode_gpt")
        self.client = ClientOpenaiChatgpt()
        self.system_message_content = system_message_content

    def _handle_text(self, prompt: str) -> str:
        return self.client.prompt_default(self.system_message_content, prompt)
