import requests
from datetime import *

nowtimes = datetime.now()

hour = nowtimes.hour

def Lorestantemp(data):
    if data == "khorramabad":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=33.4878&longitude=48.3558&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر خرم آباد:</b>
 دما هم اکنون = <code>{temps[hour]}</code> درجه سانتی‌گراد
<b>دما در ساعت های مختلف:</b>
۰۰:۰۰ = {temps[0]}
۰۱:۰۰ = {temps[1]}
۰۲:۰۰ = {temps[2]}
۰۳:۰۰ = {temps[3]}
 ۰۴:۰۰ = {temps[4]}
 ۰۵:۰۰ = {temps[5]}
 ۰۶:۰۰ = {temps[6]}
 ۰۷:۰۰ = {temps[7]}
۰۸:۰۰ = {temps[7]}
۰۹:۰۰ = {temps[9]}
۱۰:۰۰ = {temps[10]}
۱۱:۰۰ = {temps[11]}
۱۲:۰۰ = {temps[12]}
۱۳:۰۰ = {temps[13]}
۱۴:۰۰ = {temps[14]}
۱۵:۰۰ = {temps[15]}
۱۶:۰۰ = {temps[16]}
۱۷:۰۰ = {temps[17]}
۱۸:۰۰ = {temps[18]}
۱۹:۰۰ = {temps[19]}
۲۰:۰۰ = {temps[20]}
۲۱:۰۰ = {temps[21]}
۲۲:۰۰ = {temps[22]}
۲۳:۰۰ = {temps[23]}


⚠️<i>توجه: این آمار برای امروز می‌باشد!!</i>
    """ 
    if data == "borujerd":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=33.8973&longitude=48.7516&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر بروجرد:</b>
 دما هم اکنون = <code>{temps[hour]}</code> درجه سانتی‌گراد
<b>دما در ساعت های مختلف:</b>
۰۰:۰۰ = {temps[0]}
۰۱:۰۰ = {temps[1]}
۰۲:۰۰ = {temps[2]}
۰۳:۰۰ = {temps[3]}
 ۰۴:۰۰ = {temps[4]}
 ۰۵:۰۰ = {temps[5]}
 ۰۶:۰۰ = {temps[6]}
 ۰۷:۰۰ = {temps[7]}
۰۸:۰۰ = {temps[7]}
۰۹:۰۰ = {temps[9]}
۱۰:۰۰ = {temps[10]}
۱۱:۰۰ = {temps[11]}
۱۲:۰۰ = {temps[12]}
۱۳:۰۰ = {temps[13]}
۱۴:۰۰ = {temps[14]}
۱۵:۰۰ = {temps[15]}
۱۶:۰۰ = {temps[16]}
۱۷:۰۰ = {temps[17]}
۱۸:۰۰ = {temps[18]}
۱۹:۰۰ = {temps[19]}
۲۰:۰۰ = {temps[20]}
۲۱:۰۰ = {temps[21]}
۲۲:۰۰ = {temps[22]}
۲۳:۰۰ = {temps[23]}


⚠️<i>توجه: این آمار برای امروز می‌باشد!!</i>
    """ 
    if data == "dorud":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=33.4922&longitude=49.0616&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر دورود:</b>
 دما هم اکنون = <code>{temps[hour]}</code> درجه سانتی‌گراد
<b>دما در ساعت های مختلف:</b>
۰۰:۰۰ = {temps[0]}
۰۱:۰۰ = {temps[1]}
۰۲:۰۰ = {temps[2]}
۰۳:۰۰ = {temps[3]}
 ۰۴:۰۰ = {temps[4]}
 ۰۵:۰۰ = {temps[5]}
 ۰۶:۰۰ = {temps[6]}
 ۰۷:۰۰ = {temps[7]}
۰۸:۰۰ = {temps[7]}
۰۹:۰۰ = {temps[9]}
۱۰:۰۰ = {temps[10]}
۱۱:۰۰ = {temps[11]}
۱۲:۰۰ = {temps[12]}
۱۳:۰۰ = {temps[13]}
۱۴:۰۰ = {temps[14]}
۱۵:۰۰ = {temps[15]}
۱۶:۰۰ = {temps[16]}
۱۷:۰۰ = {temps[17]}
۱۸:۰۰ = {temps[18]}
۱۹:۰۰ = {temps[19]}
۲۰:۰۰ = {temps[20]}
۲۱:۰۰ = {temps[21]}
۲۲:۰۰ = {temps[22]}
۲۳:۰۰ = {temps[23]}


⚠️<i>توجه: این آمار برای امروز می‌باشد!!</i>
    """ 
