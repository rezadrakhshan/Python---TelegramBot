#bot id in telegram = https://t.me/blahman_bot
import telebot

bot = telebot.TeleBot("6602525887:AAHDXzjr-IPyrJ0UB8oeAXxK7__sc8DH3hc")


second_button = telebot.types.InlineKeyboardButton("button 2", url="https://www.itgeared.com/how-to-stop-telegram-auto-download/")
markup = telebot.types.InlineKeyboardMarkup()
markup.add(second_button)


@bot.message_handler(commands=['start'])
def sender(message):
    bot.send_message(message.chat.id,"Hi there",reply_markup=markup)  

key = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key.add("register","two","three")

@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(message,"what can i do",reply_markup=key)



@bot.message_handler(func= lambda m:True)
def info(message):
    if message.text == "register":
        msg = bot.send_message(message.chat.id,"enter your name")
        bot.register_next_step_handler(msg, name)

def name(message):
    global nm
    nm = message.text
    msg = bot.send_message(message.chat.id,"enter your age")
    bot.register_next_step_handler(msg, age)

def age(message):
    global ag
    ag = message.text
    msg = bot.send_message(message.chat.id,"enter your height")
    bot.register_next_step_handler(msg, height)

def height(message):
    hg = message.text
    bot.send_message(message.chat.id,f"your name:{nm}\nyour age:{ag}\nyour height:{hg}")

bot.infinity_polling()