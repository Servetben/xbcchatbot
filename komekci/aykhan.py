
from telethon import TelegramClient

# Config məlumatları

# Telegram Client (Telethon)
API_ID = "21122885"
API_HASH = "08324eb4d401d75c4b66fe4c94b88ef3"
bot_token = "6797602758:AAHcEyta6x0g4FTt1JZ0MKbqzHdXOGfWV70"

# Nermin
Nermin = TelegramClient('Nermin', API_ID, API_HASH).start(bot_token=bot_token)
