# srai-telegrambot
A library that makes it easier to build ai powered telegram bots

# install
pip install srai-telegrambot

## usage
This is how i use the bot
'''python

from srai_core.store.database_mongo import DatabaseMongo
from srai_core.tools_env import get_string_from_env

from srai_telegrambot.command.command_chat_id import CommandChatId
from srai_telegrambot.command.command_help import CommandHelp
from srai_telegrambot.command.command_image_tag import CommandImageTag
from srai_telegrambot.dao_telegram_bot import DaoTelegramBot
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

    # start bot
    bot.main()
'''