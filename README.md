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
import os
from srai_core.store.database_mongo import DatabaseMongo
from srai_core.tools_env import get_string_from_env

from srai_telegrambot.command.command_chat_id import CommandChatId
from srai_telegrambot.command.command_help import CommandHelp
from srai_telegrambot.command.command_image_tag import CommandImageTag
from srai_telegrambot.dao_telegram_bot import DaoTelegramBot
from srai_telegrambot.mode.text_mode_gpt import TextModeGpt
from srai_telegrambot.mode.text_mode_rag import TextModeRag
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
    bot.register_text_mode(TextModeGpt("you are a chatbot"), False)

    path_dir_vectorstore = os.path.abspath(os.path.join("test", "data", "vectorstore"))
    bot.register_text_mode(TextModeRag(path_dir_vectorstore), True)
    # start bot
    bot.main()
```
### How to build a voice interface to chatgpt
Below is code for a voice interface to chatgpt

```python
from srai_core.store.database_mongo import DatabaseMongo
from srai_core.tools_env import get_string_from_env

from srai_telegrambot.command.command_chat_id import CommandChatId
from srai_telegrambot.command.command_help import CommandHelp
from srai_telegrambot.command.command_image_tag import CommandImageTag
from srai_telegrambot.dao_telegram_bot import DaoTelegramBot
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
    bot.register_voice_mode(VoiceModeGpt("You are a chatbot. Never respond in more that three sentences"), True)


    # start bot
    bot.main()
```


### How to build a RAG telegram bot vectorstore
Below is code for a rag telegram bot

```python
import os

from srai_telegrambot.mode.text_mode_rag import TextModeRag
from srai_telegrambot.telegram_bot_test import TelegramBotTest

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
```


## Changelog
### 0.17.2
- Made the bot explicitly threaded so it can run as part of a bigger program
### 0.17.0
- Added voice support
- Removed inate vectorstore FAISS

### 0.16.0
- Added RAG text mode
- Moved memory databases to core lib