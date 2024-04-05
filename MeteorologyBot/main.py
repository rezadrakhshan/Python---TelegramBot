from telethon import TelegramClient, events, Button
from config import *
from messages import start_message
from telethon.tl.custom.message import Message
import s
# from state.Alborz.req import *
# from state.Ardabil.req import *
# from state.Bushehr.req import *
# from state.ChaharmahalandBakhtiari.req import *
# from state.EastAzerbaijan.req import *
# from state.Fars.req import *
# from state.Gilan.req import *
# from state.Golestan.req import *
# from state.Hamadan.req import *
# from state.Hormozgan.req import *
# from state.Ilam.req import *
# from state.Isfahan.req import *
# from state.Kerman.req import *
import mysql.connector
from data import state, cities_dict
import s.Alborz
import s.Alborz.req
import s.Ardabil
import s.Ardabil.req
import s.Bushehr
import s.Bushehr.req
import s.ChaharmahalandBakhtiari
import s.ChaharmahalandBakhtiari.req
import s.EastAzerbaijan
import s.EastAzerbaijan.req
import s.Fars
import s.Fars.req
import s.Gilan
import s.Gilan.req
import s.Golestan
import s.Golestan.req
import s.Hamadan
import s.Hamadan.req
import s.Hormozgan
import s.Hormozgan.req
import s.Ilam
import s.Ilam.req
import s.Isfahan
import s.Isfahan.req
import s.Kermanshah
import s.Kermanshah.req


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
                text = s.Alborz.req.alborztemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Ardabil":
                text = s.Ardabil.req.ardabiltemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Bushehr":
                text = s.Bushehr.req.bushehrtemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Chaharmahal and Bakhtiari":
                text = s.ChaharmahalandBakhtiari.req.ChaharmahalandBakhtiaritemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "East Azerbaijan":
                text = s.EastAzerbaijan.req.EastAzerbaijantemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Fars":
                text = s.Fars.req.Farstemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Gilan":
                text = s.Gilan.req.Gilantemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Golestan":
                text = s.Golestan.req.Golestantemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Hamedan":
                text = s.Hamadan.req.Hamadantemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Hormozgan":
                text = s.Hormozgan.req.Hormozgantemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Ilam":
                text = s.Ilam.req.Ilamtemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Isfahan":
                text = s.Isfahan.req.Isfahantemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )
            elif user_state_format == "Kermanshah":
                text = s.Kermanshah.req.Kermanshahtemp(user_city_format)
                await client.edit_message(
                    event.chat_id, event.message_id, text, parse_mode="html"
                )


client.start(bot_token="")
client.run_until_disconnected()
