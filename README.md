# srai-telegrambot
A library that makes it easier to build ai powered telegram bots

# install
pip install srai-telegrambot

## get your token
get your telegrambot token from the botfather as described here https://core.telegram.org/bots/tutorial

## usage
This is how i use the bot:
I rely on mongo db to save messages there are other options!
You can also implement your own version of dao telegrambot.
I will add a in-memory database that i use for testing in the near future

```python
from srai_core.store.database_mongo import DatabaseMongo
from srai_core.tools_env import get_string_from_env

from srai_telegrambot.command.command_chat_id import CommandChatId
from srai_telegrambot.command.command_help import CommandHelp
from srai_telegrambot.command.command_image_tag import CommandImageTag
from srai_telegrambot.dao_telegram_bot import DaoTelegramBot
from srai_telegrambot.mode.text_mode_gpt import TextModeGpt
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
    bot.register_text_mode(TextModeGpt("you are a chatbot"), True)

    # start bot
    bot.main()
```

## Changelog

0.15.0
- added in memory database
- added default release option