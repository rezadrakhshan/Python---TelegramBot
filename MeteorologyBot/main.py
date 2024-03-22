from telethon import TelegramClient, events, Button
from config import *
from messages import start_message
from telethon.tl.custom.message import Message
from city.Tehran.messages import msg as tehran
from city.Karaj.messages import msg as karaj
from city.Esfahan.messages import msg as esfahan
from city.Shiraz.messages import msg as shiraz

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
    markup = client.build_reply_markup([Button.inline(text="بازگشت", data="back")])
    if event.data == b"back":
        await client.delete_messages(entity=event.chat_id,message_ids=event.message_id)
        await start(event) 
    if event.data == b"Tehran":
        await client.edit_message(
            entity=event.chat_id, 
            message=event.message_id,
            text=tehran,
            parse_mode="html",
            buttons=markup,
        )
    if event.data == b"Karaj":
        await client.edit_message(
            entity=event.chat_id, 
            message=event.message_id,
            text=karaj,
            parse_mode="html",
            buttons=markup,
        )
    if event.data == b"Esfahan":
        await client.edit_message(
            entity=event.chat_id, 
            message=event.message_id,
            text=esfahan,
            parse_mode="html",
            buttons=markup,
        )
    if event.data == b"Shiraz":
        await client.edit_message(
            entity=event.chat_id, 
            message=event.message_id,
            text=shiraz,
            parse_mode="html",
            buttons=markup,
        )


client.start(bot_token="")
client.run_until_disconnected()
