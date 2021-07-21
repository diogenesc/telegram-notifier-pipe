import os

from telegram import Bot

def main() -> None:
    bot = Bot(os.environ.get('BOT_TOKEN'))

    bot.send_message(chat_id=os.environ.get('CHAT_ID'), text=os.environ.get('MESSAGE_TEXT'))


if __name__ == '__main__':
    main()