
# Telegram Notifier Pipe

A bitbucket custom pipe to send Telegram notifications.


## Usage

```bash
- pipe: docker://diogenesc/telegram-notifier-pipe:latest
  variables:
    BOT_TOKEN: XXXXXXXXXXXXXXX
    CHAT_ID: 0000000
    MESSAGE_TEXT: 'Hi!'
```


### Variables
- BOT_TOKEN (required): The token provided by BotFather
- CHAT_ID (required): Unique identifier for the target chat or username of the target channel
- MESSAGE_TEXT (required): Text of the message to be sent, 1-4096 characters after entities parsing
