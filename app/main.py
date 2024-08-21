from srai_core.store.database_mongo import DatabaseMongo
from srai_core.tools_env import get_string_from_env

from srai_telegrambot.command.command_chat_id import CommandChatId
from srai_telegrambot.command.command_help import CommandHelp
from srai_telegrambot.command.command_image_tag import CommandImageTag
from srai_telegrambot.dao_telegram_bot import DaoTelegramBot
from srai_telegrambot.mode.text_mode_gpt import TextModeGpt
from srai_telegrambot.mode.voice_mode_gpt import VoiceModeGpt
from srai_telegrambot.telegram_bot import TelegramBot

if __name__ == "__main__":
    telegram_token = get_string_from_env("SRAI_TELEGRAM_TOKEN")
    connection_string = get_string_from_env("MONGODB_CONNECTION_STRING")
    telegram_root_id = get_string_from_env(
        "TELEGRAM_ROOT_ID"
    )  # this is my user id and it gives me admin rights in the bot

    database_mongo = DatabaseMongo("database_telegrambot", connection_string)
    dao_telegram_bot = DaoTelegramBot(database_mongo)
    bot = TelegramBot(
        token=telegram_token,
        dao_telegram_bot=dao_telegram_bot,
    )

    bot.register_admin(telegram_root_id)

    # register commands
    bot.register_command(CommandHelp())
    bot.register_command(CommandChatId())
    bot.register_command(CommandImageTag())
    bot.register_text_mode(TextModeGpt("You are a chatbot"), True)
    bot.register_voice_mode(VoiceModeGpt("You are a chatbot. Never respond in more that three sentences"), True)

    # start bot
    bot.start()
