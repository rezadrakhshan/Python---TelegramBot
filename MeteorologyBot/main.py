from telethon import TelegramClient, events
from config import *

client = TelegramClient("bot_session", api_id=api_id, api_hash=api_hash)

@client.on(events.NewMessage(pattern=r"/start"))
async def start(event):
    await client.send_message(entity=event.chat_id,message="""به ربات هواشناسی ما خوش آمدید! 🌈

ما در اینجا هستیم تا آخرین و دقیق‌ترین اطلاعات هواشناسی را در اختیار شما قرار دهیم. شما می‌توانید با وارد کردن نام شهر یا منطقه خود، آب و هوای کنونی، پیش‌بینی‌های کوتاه‌مدت و بلندمدت را دریافت کنید. ☀️🌧

علاوه بر این، ما امکانات دیگری نظیر نمایش زمان طلوع و غروب آفتاب، رطوبت، سرعت باد و بیشتر را فراهم آورده‌ایم. می‌توانید از این اطلاعات برای برنامه‌ریزی فعالیت‌های روزانه خود استفاده کنید. 🌦💨

برای شروع، کافی است نام شهر یا منطقه خود را ارسال کنید. اگر نیاز به کمک داشتید، می‌توانید هر زمان که خواستید با نوشتن "راهنما" راهنمایی دریافت کنید.

با تشکر از انتخاب شما. امیدواریم تجربه‌ای دلپذیر با ما داشته باشید! 🌟

<b>Made by:<a href="https://github.com/rezadrakhshan/" style="text-decoration: none;">RezaDerakhshan</a></b>""",parse_mode='html')


client.start(bot_token="7110386237:AAGhkfozqIeoPd_e6giviMtHT-5eNv6Qs2Q")
client.run_until_disconnected()

