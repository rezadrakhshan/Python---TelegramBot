
state = {
    "آذربایجان شرقی": "East Azerbaijan",
    "آذربایجان غربی": "West Azerbaijan",
    "اردبیل": "Ardabil",
    "اصفهان": "Isfahan",
    "البرز": "Alborz",
    "ایلام": "Ilam",
    "بوشهر": "Bushehr",
    "تهران": "Tehran",
    "چهارمحال و بختیاری": "Chaharmahal and Bakhtiari",
    "خراسان جنوبی": "South Khorasan",
    "خراسان رضوی": "Razavi Khorasan", 
    "خراسان شمالی": "North Khorasan",
    "خوزستان": "Khuzestan",
    "زنجان": "Zanjan",
    "سمنان": "Semnan",
    "سیستان و بلوچستان": "Sistan and Baluchestan",
    "فارس": "Fars",
    "قزوین": "Qazvin",
    "قم": "Qom",
    "کردستان": "Kurdistan",
    "کرمان": "Kerman",
    "کرمانشاه": "Kermanshah",
    "کهگیلویه و بویراحمد": "Kohgiluyeh and Boyer-Ahmad",
    "گلستان": "Golestan",
    "گیلان": "Gilan",
    "لرستان": "Lorestan",
    "مازندران": "Mazandaran",
    "مرکزی": "Markazi",
    "هرمزگان": "Hormozgan",
    "همدان": "Hamedan",
    "یزد": "Yazd",
}

# Creating a dictionary for all provinces of Iran and adding a few cities for each in the requested format.

cities_dict = {
    "East Azerbaijan": [
        ("تبریز", "tabriz"),
        ("ارومیه", "urmia"),
        ("مراغه", "maragheh"),
    ],
    "West Azerbaijan": [("ارومیه", "urmia"), ("خوی", "khoy"), ("مهاباد", "mahabad")],
    "Ardabil": [
        ("اردبیل", "ardabil"),
        ("مشگین شهر", "meshgin shahr"),
        ("پارس آباد", "parsabad"),
    ],
    "Isfahan": [("اصفهان", "isfahan"), ("کاشان", "kashan"), ("نجف آباد", "najafabad")],
    "Alborz": [("کرج", "karaj"), ("نظرآباد", "nazrabad"), ("طالقان", "taleqan")],
    "Ilam": [("ایلام", "ilam"), ("دهلران", "dehloran"), ("ایوان", "ivan")],
    "Bushehr": [("بوشهر", "bushehr"), ("برازجان", "borazjan"), ("خورموج", "khormoj")],
    "Tehran": [("تهران", "tehran"), ("شهریار", "shahriar"), ("پرند", "parand")],
    "Chaharmahal and Bakhtiari": [
        ("شهرکرد", "shahrekord"),
        ("بروجن", "borujen"),
        ("لردگان", "lordegan"),
    ],
    "South Khorasan": [
        ("بیرجند", "birjand"),
        ("قائنات", "ghaenat"),
        ("فردوس", "ferdows"),
    ],
    "Razavi Khorasan": [
        ("مشهد", "mashhad"),
        ("نیشابور", "neyshabur"),
        ("سبزوار", "sabzevar"),
    ],
    "North Khorasan": [
        ("بجنورد", "bojnurd"),
        ("اسفراین", "esfarayen"),
        ("شیروان", "shirvan"),
    ],
    "Khuzestan": [("اهواز", "ahvaz"), ("آبادان", "abadan"), ("خرمشهر", "khorramshahr")],
    "Zanjan": [("زنجان", "zanjan"), ("ابهر", "abhar"), ("خدابنده", "khodabandeh")],
    "Semnan": [("سمنان", "semnan"), ("شاهرود", "shahroud"), ("دامغان", "damghan")],
    "Sistan and Baluchestan": [
        ("زاهدان", "zahedan"),
        ("چابهار", "chabahar"),
        ("ایرانشهر", "iranshahr"),
    ],
    "Fars": [("شیراز", "shiraz"), ("جهرم", "jahrom"), ("مرودشت", "marvdasht")],
    "Qazvin": [("قزوین", "qazvin"), ("تاکستان", "takestan"), ("البرز", "alborz")],
    "Qom": [("قم", "qom"), ("کاهک", "kahak"), ("جعفریه", "jafariyeh")],
    "Kurdistan": [("سنندج", "sanandaj"), ("مریوان", "marivan"), ("بانه", "baneh")],
    "Kerman": [("کرمان", "kerman"), ("سیرجان", "sirjan"), ("رفسنجان", "rafsanjan")],
    "Kermanshah": [
        ("کرمانشاه", "kermanshah"),
        ("اسلام آباد غرب", "islamabad-e gharb"),
        ("سنقر", "saghez"),
    ],
    "Kohgiluyeh and Boyer-Ahmad": [
        ("یاسوج", "yasuj"),
        ("گچساران", "gachsaran"),
        ("دهدشت", "dehdasht"),
    ],
    "Golestan": [
        ("گرگان", "gorgan"),
        ("گنبد کاووس", "gonbad-e kavus"),
        ("بندر ترکمان", "bandar torkaman"),
    ],
    "Gilan": [("رشت", "rasht"), ("لاهیجان", "lahijan"), ("بند انزلی", "anzali")],
    "Lorestan": [
        ("خرم آباد", "khorramabad"),
        ("بروجرد", "borujerd"),
        ("دورود", "dorud"),
    ],
    "Mazandaran": [("ساری", "sari"), ("بابل", "babol"), ("آمل", "amol")],
    "Markazi": [("اراک", "arak"), ("ساوه", "saveh"), ("خمین", "khomein")],
    "Hormozgan": [("بندر عباس", "bandar abbas"), ("قشم", "qeshm"), ("میناب", "minab")],
    "Hamedan": [("همدان", "hamedan"), ("ملایر", "malayer"), ("نهاوند", "nahavand")],
    "Yazd": [("یزد", "yazd"), ("میبد", "meybod"), ("اردکان", "ardakan")],
}




