try:
    import configparser
    from forex_python.converter import CurrencyRates
    import cryptocompare as cryp
except:
    print("Python forex_python, configparser or cryptocompare library not installed!")

try:
    from telethon import TelegramClient, events, sync
    from telethon.tl.functions.messages import ImportChatInviteRequest
    import asyncio
except:
    print("Telethon not installed!")

parser = configparser.ConfigParser()
parser.read("config.txt")

cryp.cryptocompare._set_api_key_parameter('YOUR_API_KEY')
currentRate = CurrencyRates()

print("Telegram API Defined")
api_id = parser.get("config", "TelApi_id")
api_hash = parser.get("config", "TelApi_hash")
#telChnlURL = parser.get("config", "TelChnlLink")


client = TelegramClient('anon', api_id, api_hash)
client.start()


@client.on(events.NewMessage)
async def my_event_handler(event):
    if '!USD/TRY' in event.raw_text:
        await event.reply(str(currentRate.get_rate('USD','TRY')))
    if '!BTC' in event.raw_text:
        await event.reply(str(cryp.get_price('BTC', currency='USD')))
    if '!ETH' in event.raw_text:
        await event.reply(str(cryp.get_price('ETH', currency='USD')))
    if '!COMP' in event.raw_text:
        await event.reply(str(cryp.get_price('COMP', currency='USD')))
    


client.run_until_disconnected()

