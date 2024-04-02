from telethon import TelegramClient, events, Button
from config import *
from messages import start_message
from telethon.tl.custom.message import Message
from state.Alborz.req import *
from state.Ardabil.req import *
import mysql.connector
from data import state, cities_dict


db = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = db.cursor()


client = TelegramClient("bot_session", api_id=api_id, api_hash=api_hash)

buttons = []
temp_buttons = []

for province_name, province_name_en in state.items():
    temp_buttons.append(Button.inline(province_name, data=province_name_en))
    if len(temp_buttons) == 3:
        buttons.append(temp_buttons)
        temp_buttons = []

if temp_buttons:
    buttons.append(temp_buttons)


@client.on(events.NewMessage(pattern=r"/start"))
async def start(event: Message):
    text = start_message()
    markup = [[Button.url("Made By Derakhshan", "https://github.com/rezadrakhshan")]]
    try:
        cursor.execute(
            "INSERT INTO user (ID, state, city) VALUES (%s, %s, %s);",
            (str(event.chat_id), "test", "test"),
        )
        db.commit()
        await client.send_message(entity=event.chat_id, message=text, buttons=markup)
        await client.send_message(
            entity=event.chat_id, message="استان خود را انتخاب کنید:", buttons=buttons
        )
    except:
        await client.send_message(entity=event.chat_id, message=text, buttons=markup)
        await client.send_message(
            entity=event.chat_id, message="استان خود را انتخاب کنید", buttons=buttons
        )


@client.on(events.CallbackQuery)
async def call_back_state(event: Message):
    data = event.data.decode("utf-8")
    for i, j in state.items():
        if data == j:
            try:
                cursor.execute(
                    "UPDATE user SET state = %s WHERE ID = %s;",
                    (str(data), str(event.chat_id)),
                )
                db.commit()
                city = cities_dict[data]
                button = [
                    Button.inline(name, data=english_name)
                    for name, english_name in city
                ]
                await client.edit_message(
                    event.chat_id,
                    event.message_id,
                    text="شهر خود را انتخاب کنید:",
                    buttons=button,
                )
            except:
                await client.edit_message(event.chat_id, event.message_id, text="خطا")


@client.on(events.CallbackQuery)
async def call_back_city(event: Message):
    data = event.data.decode("utf-8")
    button = [
        [
            Button.inline("دما", data="temp"),
        ]
    ]
    for i in cities_dict.values():
        for j, z in i:
            if data == z:
                cursor.execute(
                    "UPDATE user SET city = %s WHERE ID = %s;",
                    (str(data), str(event.chat_id)),
                )
                db.commit()
                await client.edit_message(
                    event.chat_id,
                    event.message_id,
                    text="گزینه خود را انتخاب کنید: ",
                    buttons=button,
                )
            # except:
            #     await client.edit_message(
            #         event.chat_id, event.message_id, text="خطا"
            #     )


@client.on(events.CallbackQuery)
async def call_back_service(event: Message):
    query = "SELECT state FROM user WHERE ID = %s"
    cursor.execute(query, (str(event.chat_id),))
    user_state = cursor.fetchone()
    user_state_format = str(user_state[0])
    city = "SELECT city FROM user WHERE ID = %s"
    cursor.execute(city, (str(event.chat_id),))
    user_city = cursor.fetchone()
    user_city_format = str(user_city[0])
    match event.data:
        case b"temp":
            if user_state_format == "Alborz":
                text = alborz(user_city_format)
                await client.edit_message(event.chat_id,event.message_id,text,parse_mode="html")
            if user_state_format == "Ardabil":
                text = ardabil(user_city_format)
                await client.edit_message(event.chat_id,event.message_id,text,parse_mode="html")



client.start(bot_token="")
client.run_until_disconnected()
