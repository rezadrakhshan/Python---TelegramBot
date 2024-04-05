import requests
from datetime import *

nowtimes = datetime.now()

hour = nowtimes.hour

def Markazitemp(data):
    if data == "arak":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=34.0949&longitude=49.6981&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر اراک :</b>
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
    if data == "saveh":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=35.0213&longitude=50.3566&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر ساوه:</b>
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
    if data == "khomein":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=33.6389&longitude=50.08&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر خمین:</b>
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
