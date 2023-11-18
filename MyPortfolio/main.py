import telebot


bot = telebot.TeleBot("6071743808:AAFVtY4XHF5cwYOAy06dR53mnpzoDcjiwR4")

lan = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
lan.add("persian", "english")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "hi there")
    bot.send_message(
        message.chat.id, "please select language to continue", reply_markup=lan
    )


perchoices = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
perchoices.add("درباره من", "گیت هاب", "لینکدین", "ارتباط با من")

enchoices = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
enchoices.add("about me", "github", "linkedin", "contact me")

github = telebot.types.InlineKeyboardButton(
    "گیت هاب", url="https://github.com/rezadrakhshan"
)
markup = telebot.types.InlineKeyboardMarkup()
markup.add(github)

engithub = telebot.types.InlineKeyboardButton(
    "Git Hub", url="https://github.com/rezadrakhshan"
)
engmarkup = telebot.types.InlineKeyboardMarkup()
engmarkup.add(engithub)

linkedin = telebot.types.InlineKeyboardButton(
    "لینکدین", url="https://www.linkedin.com/in/seyedrezadrakhshan/"
)
linkmark = telebot.types.InlineKeyboardMarkup()
linkmark.add(linkedin)

englinkedin = telebot.types.InlineKeyboardButton(
    "Linkedin", url="https://www.linkedin.com/in/seyedrezadrakhshan/"
)
englinkmark = telebot.types.InlineKeyboardMarkup()
englinkmark.add(englinkedin)


@bot.message_handler()
def persian(message):
    if message.text == "persian":
        msg = bot.send_message(
            message.chat.id, "گزینه خود را انتخاب کنید.", reply_markup=perchoices
        )
        bot.register_next_step_handler(msg, command)
    elif message.text == "english":
        msg = bot.send_message(
            message.chat.id, "select your choice.", reply_markup=enchoices
        )
        bot.register_next_step_handler(msg, command)


@bot.message_handler(func=lambda m: True)
def command(message):
    # persian
    if message.text == "درباره من":
        msg = bot.send_message(
            message.chat.id,
            """سلام
من سید رضا درخشان اهل کشور ایران و شهر تهران هستم. دانش اموز سال یازدهم رشته کامپیوتر که حدود یک سال است برنامه نویسی رو شروع کردم و در حال حاضر در سطح جونیور هستم. 
در این یک سال با زبان برنامه نویسی پایتون و فریمورک های django و fastapi کار کرده ام. 
من دارای توانایی هایی از جمله توانایی حل مسائل و همچنین کار در تیم هستم. 
در این یک سال با انجام پروژه های مختلف توانسته ام تجربه زیادی به دست آورم و با مشکلات و چالش های مختلفی که در طول این پروژه ها برایم پیش آمده بود، مقابله کنم. 
با توجه به تجربه های خود و مهارت هایی که دارم مطمئن هستم که میتوانم در یک تیم به عنوان برنامه نویس جونیور عملکردی مفید داشته باشم.""",
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "گیت هاب":
        msg = bot.send_message(
            message.chat.id, "فالو و استار فراموش نشه", reply_markup=markup
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "لینکدین":
        msg = bot.send_message(
            message.chat.id, "در لینکدین با من در ارتباط باشید.", reply_markup=linkmark
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "ارتباط با من":
        msg = bot.send_message(
            message.chat.id,
            """اگر هرگونه سوال,انتقاد یا پیشنهادی دارید میتوانید از طریق راه های زیر با من در ارتباط باشید.
شماره تلفن : ٠٩٣٧١٣٩۴٢۴٩
ایمیل : srdrakhshan@gmail.com
دیسکورد : imreza#3197
تلگرام :@LAREZA""",
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "about me":
        msg = bot.send_message(
            message.chat.id,
            """Hello
I am Seyed Reza Derakhshan from Iran and Tehran. I am an 11th year computer student who started programming about a year ago and I am currently at the junior level.
In this one year, I have worked with Python programming language and Django and Fastapi frameworks.
I have the ability to solve problems as well as work in a team.
In this one year, by doing various projects, I have been able to gain a lot of experience and deal with various problems and challenges that came to me during these projects.
Considering my experience and the skills I have, I am sure that I can have a useful function in a team as a junior programmer.""",
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "github":
        msg = bot.send_message(
            message.chat.id, "Do not forget to follow and star", reply_markup=engmarkup
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "linkedin":
        msg = bot.send_message(
            message.chat.id, "shoot me a message on Linkedin", reply_markup=englinkmark
        )
        bot.register_next_step_handler(msg, command)
    if message.text == "contact me":
        msg = bot.send_message(
            message.chat.id,
            """If you have any questions, criticisms or suggestions, you can contact me through the following ways.
Phone number : +98 937 139 4249
Email : srdrakhshan@gmail.com
Discord : imreza#3197
Telegram : @LAREZA""",
        )
        bot.register_next_step_handler(msg, command)


bot.infinity_polling()
