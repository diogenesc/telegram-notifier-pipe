import os

from telegram import Bot

def main() -> None:
    bot = Bot(os.environ.get('TELEGRAM_BOT_TOKEN'))

    bot.send_message(chat_id=os.environ.get('TELEGRAM_CHAT_ID'), text=os.environ.get('MESSAGE_TEXT'))


if __name__ == '__main__':
    main()