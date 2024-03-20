from telethon import TelegramClient, events, Button
from config import *
from messages import start_message
from telethon.tl.custom.message import Message
from city.Tehran import req as tehranreq
from city.Tehran import timee as tehrantime
from city.Karaj import req as karajreq
from city.Karaj import timee as karajtime

client = TelegramClient("bot_session", api_id=api_id, api_hash=api_hash)


@client.on(events.NewMessage(pattern=r"/start"))
async def start(event):
    text = start_message()
    markup = client.build_reply_markup(
        [
            [
                Button.inline("دما", data="temperature"),
                Button.inline("راهنما", data="help"),
            ],
            [
                Button.inline("درباره ما", data="about"),
                Button.inline("حمایت از ما", data="donate"),
            ],
        ]
    )
    text: Message = await client.send_message(
        entity=event.chat_id,
        message=text,
        parse_mode="html",
        buttons=markup,
    )


@client.on(events.CallbackQuery)
async def callback_query(event):
    if event.data == b"help":
        await client.send_message(entity=event.chat_id, message="راهنما")
    if event.data == b"temperature":
        markup = client.build_reply_markup(
            [
                [
                    Button.inline("تهران", data="Tehran"),
                    Button.inline("اصفهان", data="Esfahan"),
                    Button.inline("شیراز", data="Shiraz"),
                ],
                [
                    Button.inline("مشهد", data="Mashhad"),
                    Button.inline("تبریز", data="Tabriz"),
                    Button.inline("اهواز", data="Ahvaz"),
                ],
                [
                    Button.inline("کرمانشاه", data="Kermanshah"),
                    Button.inline("قم", data="Qom"),
                    Button.inline("کرج", data="Karaj"),
                ],
                [
                    Button.inline("اراک", data="Arak"),
                    Button.inline("قزوین", data="Qazvin"),
                    Button.inline("سنندج", data="Sanandaj"),
                ],
                [
                    Button.inline("زاهدان", data="Zahedan"),
                    Button.inline("همدان", data="Hamedan"),
                    Button.inline("ارومیه", data="Urmia"),
                ],
                [
                    Button.inline("رشت", data="Rasht"),
                    Button.inline("یزد", data="Yazd"),
                    Button.inline("اردبیل", data="Ardabil "),
                ],
                [
                    Button.inline("کرمان", data="Kerman"),
                    Button.inline("بندرعباس", data="BandarAbbas"),
                ],
                [
                    Button.inline("بازگشت", data="back"),
                ],
            ]
        )
        await client.edit_message(
            event.chat_id,
            event.message_id,
            text="شهر مورد نظر را انتخاب کنید :",
            buttons=markup,
        )
    if event.data == b"about":
        await client.send_message(entity=event.chat_id, message="درباره ربات")
    if event.data == b"donate":
        await client.send_message(entity=event.chat_id, message="حمایت از ما")


@client.on(events.CallbackQuery)
async def temperature(event):
    if event.data == b"Tehran":
        temp = str(tehranreq.temps[tehrantime.hour])
        await client.edit_message(event.chat_id, event.message_id, text=temp)
    if event.data == b"Karaj":
        temp = str(karajreq.temps[karajtime.hour])
        await client.edit_message(event.chat_id, event.message_id, text=temp)



client.start(bot_token="")
client.run_until_disconnected()
