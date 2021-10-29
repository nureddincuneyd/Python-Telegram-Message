from telethon import TelegramClient, events, sync
import time
import configparser

parser = configparser.ConfigParser()
parser.read("config.txt")

print("Telegram API Defined")
api_id = parser.get("config", "TelApi_id")
api_hash = parser.get("config", "TelApi_hash")
telChnlURL = parser.get("config", "TelChnlLink")



client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()

# Terminal Output {          Signed in successfully as [TelegramUserName]            }

