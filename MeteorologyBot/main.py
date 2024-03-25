from telethon import TelegramClient, events, Button
from config import *
from messages import start_message
from telethon.tl.custom.message import Message

client = TelegramClient("bot_session", api_id=api_id, api_hash=api_hash)


async def state(event, id):
    markup = client.build_reply_markup(
        [
            [
                Button.inline("تهران", data="Tehran"),
                Button.inline("کهگیلویه و بویراحمد", data="KohgiluyehandBoyerAhmad"),
                Button.inline("آذربایجان شرقی", data="EastAzerbaijan"),
            ],
            [
                Button.inline("آذربایجان غربی", data="WestAzerbaijan"),
                Button.inline("اردبیل", data="Ardabil"),
                Button.inline("اصفهان", data="Isfahan"),
            ],
            [
                Button.inline("البرز", data="Alborz"),
                Button.inline("ایلام", data="Ilam"),
                Button.inline("بوشهر", data="Bushehr"),
            ],
            [
                Button.inline("چهارمحال و بختیاری", data="ChaharmahalandBakhtiari"),
                Button.inline("خراسان جنوبی", data="SouthKhorasan"),
                Button.inline("خراسان رضوی", data="RazaviKhorasan"),
            ],
            [
                Button.inline("خراسان شمالی", data="NorthKhorasan"),
                Button.inline("خوزستان", data="Khuzestan"),
                Button.inline("زنجان", data="Zanjan"),
            ],
            [
                Button.inline("سمنان", data="Semnan"),
                Button.inline("سیستان و بلوچستان", data="SistanandBaluchestan"),
                Button.inline("فارس", data="Fars"),
            ],
            [
                Button.inline("قزوین", data="Qazvin"),
                Button.inline("قم", data="Qom"),
                Button.inline("کردستان", data="Kurdistan"),
            ],
            [
                Button.inline("کرمان", data="Kerman"),
                Button.inline("کرمانشاه", data="Kermanshah"),
                Button.inline("گلستان", data="Golestan"),
            ],
            [
                Button.inline("گیلان", data="Gilan"),
                Button.inline("لرستان", data="Lorestan"),
                Button.inline("مازندران", data="Mazandaran"),
            ],
            [
                Button.inline("مرکزی", data="Markazi"),
                Button.inline("هرمزگان", data="Hormozgan"),
                Button.inline("همدان", data="Hamadan"),
            ],
            [
                Button.inline("یزد", data="Yazd"),
            ],
        ]
    )

    if id == "start":
        await client.send_message(
            entity=event.chat_id, message="لطفا استان خود را وارد کنید:", buttons=markup
        )
    else:
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text="استان خود را وارد کنید:",
            buttons=markup,
        )


@client.on(events.NewMessage(pattern=r"/start"))
async def start(event):
    text = start_message()
    text: Message = await client.send_message(
        entity=event.chat_id,
        message=text,
        parse_mode="html",
    )
    await state(event, "start")


@client.on(events.CallbackQuery)
async def city(event: Message):
    if event.data == b"Tehran":
        markup = [
            [
                Button.inline(text="تهران", data="tehran"),
                Button.inline(text="کرج", data="karaj"),
                Button.inline(text="شهریار", data="Shahriar"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"KohgiluyehandBoyerAhmad":
        markup = [
            [
                Button.inline(text="یاسوج", data="yasuj"),
                Button.inline(text="دهدشت", data="dehdasht"),
                Button.inline(text="گچسران", data="gachsaran"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"EastAzerbaijan":
        markup = [
            [
                Button.inline(text="تبریز", data="tabriz"),
                Button.inline(text="مراغه", data="maragheh"),
                Button.inline(text="مرند", data="marand"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"WestAzerbaijan":
        markup = [
            [
                Button.inline(text="ارومیه", data="urmia"),
                Button.inline(text="خوی", data="khoy"),
                Button.inline(text="مهاباد", data="mahabad"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Ardabil":
        markup = [
            [
                Button.inline(text="اردبیل", data="ardabil"),
                Button.inline(text="پارس آباد", data="parsabad"),
                Button.inline(text="خلخال", data="khalkhal"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Isfahan":
        markup = [
            [
                Button.inline(text="اصفهان", data="isfahan"),
                Button.inline(text="کاشان", data="kashan"),
                Button.inline(text="نجف آباد", data="najafabad"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Alborz":
        markup = [
            [
                Button.inline(text="کرج", data="karaj"),
                Button.inline(text="ساوجبلاغ", data="savojbolagh"),
                Button.inline(text="نظرآباد", data="nazarabad"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Ilam":
        markup = [
            [
                Button.inline(text="ایلام", data="ilam"),
                Button.inline(text="دهلران", data="dehloran"),
                Button.inline(text="ایوان", data="ivan"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Bushehr":
        markup = [
            [
                Button.inline(text="بوشهر", data="bushehr"),
                Button.inline(text="گناوه", data="ganaveh"),
                Button.inline(text="دشتستان", data="dashtestan"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"ChaharmahalandBakhtiari":
        markup = [
            [
                Button.inline(text="شهرکرد", data="shahrekord"),
                Button.inline(text="بروجن", data="borujen"),
                Button.inline(text="لردگان", data="lordegan"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"SouthKhorasan":
        markup = [
            [
                Button.inline(text="بیرجند", data="birjand"),
                Button.inline(text="قائنات", data="ghainat"),
                Button.inline(text="طبس", data="tabas"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"RazaviKhorasan":
        markup = [
            [
                Button.inline(text="مشهد", data="mashhad"),
                Button.inline(text="نیشابور", data="neyshabur"),
                Button.inline(text="تربت حیدریه ", data="torbateheydarieh"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"NorthKhorasan":
        markup = [
            [
                Button.inline(text="بجنورد", data="bojnourd"),
                Button.inline(text="شیروان", data="shirvan"),
                Button.inline(text="اسفراین", data="esfarayen"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Khuzestan":
        markup = [
            [
                Button.inline(text="اهواز", data="ahvaz"),
                Button.inline(text="آبادان", data="abadan"),
                Button.inline(text="خرمشهر", data="khorramshahr"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Zanjan":
        markup = [
            [
                Button.inline(text="زنجان", data="zanjan"),
                Button.inline(text="آبهر", data="abhar"),
                Button.inline(text="خدابنده", data="khodabandeh"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"SistanandBaluchestan":
        markup = [
            [
                Button.inline(text="زاهدان", data="Zahedan"),
                Button.inline(text="چابهار", data="Chabahar"),
                Button.inline(text="زابل", data="Zabol"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Qazvin":
        markup = [
            [
                Button.inline(text="قزوین", data="qazvin"),
                Button.inline(text="تاکستان", data="takestan"),
                Button.inline(text="آبیک", data="abiyek"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Qom":
        markup = [
            [
                Button.inline(text="قم", data="qom"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Kurdistan":
        markup = [
            [
                Button.inline(text="سنندج", data="sanandaj"),
                Button.inline(text="سقز", data="saghez"),
                Button.inline(text="بانه", data="baneh"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Kerman":
        markup = [
            [
                Button.inline(text="کرمان", data="kerman"),
                Button.inline(text="سیرجان", data="sirjan"),
                Button.inline(text="جیرفت", data="jiroft"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Kermanshah":
        markup = [
            [
                Button.inline(text="کرمانشاه", data="kermanshah"),
                Button.inline(text="اسلام آباد", data="eslamabad-e gharb"),
                Button.inline(text="سنقر", data="songhor"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Golestan":
        markup = [
            [
                Button.inline(text="گرگان", data="gorgan"),
                Button.inline(text="گنبد کاووس", data="gonbad-e kavus"),
                Button.inline(text="بندرترکمان", data="bandar torkaman"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Gilan":
        markup = [
            [
                Button.inline(text="رشت", data="rasht"),
                Button.inline(text="لاهیجان", data="lahijan"),
                Button.inline(text="بندرانزلی", data="anzali"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Lorestan":
        markup = [
            [
                Button.inline(text="خرم آباد", data="khorramabad"),
                Button.inline(text="بروجرد", data="borujerd"),
                Button.inline(text="دورود", data="dorud"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Mazandaran":
        markup = [
            [
                Button.inline(text="ساری", data="sari"),
                Button.inline(text="بابل", data="babol"),
                Button.inline(text="آمل", data="amol"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Markazi":
        markup = [
            [
                Button.inline(text="اراک", data="arak"),
                Button.inline(text="ساوه", data="saveh"),
                Button.inline(text="خمین", data="khomein"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Hormozgan":
        markup = [
            [
                Button.inline(text="بندعباس", data="bandar abbas"),
                Button.inline(text="قشم", data="qeshm"),
                Button.inline(text="میناب", data="minab"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Hamadan":
        markup = [
            [
                Button.inline(text="همدان", data="hamedan"),
                Button.inline(text="ملایر", data="malayer"),
                Button.inline(text="نهاوند", data="nahavand"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )
    if event.data == b"Yazd":
        markup = [
            [
                Button.inline(text="یزد", data="yazd"),
                Button.inline(text="میبد", data="meybod"),
                Button.inline(text="اردکان", data="ardakan"),
            ],
            [
                Button.inline(text="بازگشت", data="back"),
            ],
        ]
        await client.edit_message(
            entity=event.chat_id,
            message=event.message_id,
            text=":شهر خود را انتخاب کنید",
            buttons=markup,
        )


async def service(event, city):
    markup = [
        [Button.inline("دما", "temp"), Button.inline("وضعیت آب و هوا", "weather")],
        [
            Button.inline("زمان طلوع و غروب خورشید", "suntime"),
            Button.inline("لیست دمای تمام شهرها", "templist"),
        ],
    ]

    await client.edit_message(
        entity=event.chat_id,
        message=event.message_id,
        text="گزینه مورد نظر را انتخاب کنید :",
        buttons=markup,
    )


@client.on(events.CallbackQuery)
async def detail(event: Message):
    data = event.data.decode("utf-8")
    cities = [
        "tabriz",
        "maragheh",
        "marand",  # آذربایجان شرقی
        "urmia",
        "khoy",
        "mahabad",  # آذربایجان غربی
        "ardabil",
        "parsabad",
        "khalkhal",  # اردبیل
        "isfahan",
        "kashan",
        "najafabad",  # اصفهان
        "karaj",
        "savojbolagh",
        "nazarabad",  # البرز
        "ilam",
        "dehloran",
        "ivan",  # ایلام
        "bushehr",
        "ganaveh",
        "dashtestan",  # بوشهر
        "tehran",
        "karaj",
        "shahriar",  # تهران
        "shahrekord",
        "borujen",
        "lordegan",  # چهارمحال و بختیاری
        "birjand",
        "ghainat",
        "tabas",  # خراسان جنوبی
        "mashhad",
        "neyshabur",
        "torbat-e heydarieh",  # خراسان رضوی
        "bojnourd",
        "shirvan",
        "esfarayen",  # خراسان شمالی
        "ahvaz",
        "abadan",
        "khorramshahr",  # خوزستان
        "zanjan",
        "abhar",
        "khodabandeh",  # زنجان
        "semnan",
        "shahrood",
        "damghan",  # سمنان
        "zahedan",
        "chabahar",
        "zabol",  # سیستان و بلوچستان
        "shiraz",
        "jahrom",
        "marvdasht",  # فارس
        "qazvin",
        "takestan",
        "abiyek",  # قزوین
        "qom",  # قم
        "sanandaj",
        "saghez",
        "baneh",  # کردستان
        "kerman",
        "sirjan",
        "jiroft",  # کرمان
        "kermanshah",
        "eslamabad-e gharb",
        "songhor",  # کرمانشاه
        "yasuj",
        "dehdasht",
        "gachsaran",  # کهگیلویه و بویراحمد
        "gorgan",
        "gonbad-e kavus",
        "bandar torkaman",  # گلستان
        "rasht",
        "lahijan",
        "anzali",  # گیلان
        "khorramabad",
        "borujerd",
        "dorud",  # لرستان
        "sari",
        "babol",
        "amol",  # مازندران
        "arak",
        "saveh",
        "khomein",  # مرکزی
        "bandar abbas",
        "qeshm",
        "minab",  # هرمزگان
        "hamedan",
        "malayer",
        "nahavand",  # همدان
        "yazd",
        "meybod",
        "ardakan",  # یزد
    ]

    for i in cities:
        if data == i:
            await service(event, data)


client.start(bot_token="")
client.run_until_disconnected()
