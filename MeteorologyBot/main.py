from telethon import TelegramClient, events, Button
from config import *
from messages import start_message
from telethon.tl.custom.message import Message
from state.Alborz.req import *
import mysql.connector

db = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = db.cursor()


client = TelegramClient("bot_session", api_id=api_id, api_hash=api_hash)


@client.on(events.NewMessage(pattern=r"/start"))
async def start(event: Message):
    text = start_message()
    try:
        cursor.execute("INSERT INTO user (ID, state, city) VALUES (%s, %s, %s);", (str(event.chat_id), 'test', 'test'))
        db.commit()
        await client.send_message(entity=event.chat_id,message="خوش آمدی کاربر جدید")
    except:
        await client.send_message(entity=event.chat_id,message="خوش آمدی کاربر قدیمی")





@client.on(events.CallbackQuery)
async def detail(event: Message):
    data = event.data.decode("utf-8")


client.start(bot_token="")
client.run_until_disconnected()
