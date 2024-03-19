from telethon import TelegramClient, events, Button
from config import *
from messages import start_message

client = TelegramClient("bot_session", api_id=api_id, api_hash=api_hash)


@client.on(events.NewMessage(pattern=r"/start"))
async def start(event):
    text = start_message()
    markup = client.build_reply_markup(
        [
        [
            Button.inline("دما",data="temperature"),
            Button.inline("راهنما",data="help"),
        ],
        [
            Button.inline("درباره ما",data="about"),
            Button.inline("حمایت از ما",data="donate"),
        ],
        ]
    )
    await client.send_message(
        entity=event.chat_id,
        message=text,
        parse_mode="html",
        buttons=markup,
    )

@client.on(events.CallbackQuery)
async def callback_query(event):
    if event.data == b"help":
        await client.send_message(entity=event.chat_id,message="راهنما")
    if event.data == b"temperature":
        await client.send_message(entity=event.chat_id,message="دما")
    if event.data == b"about":
        await client.send_message(entity=event.chat_id,message="درباره ربات")
    if event.data == b"donate":
        await client.send_message(entity=event.chat_id,message="حمایت از ما")



client.start(bot_token="")
client.run_until_disconnected()
