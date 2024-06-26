import requests
from datetime import *

nowtimes = datetime.now()

hour = nowtimes.hour

def alborztemp(data):
    if data == "karaj":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=35.8327&longitude=50.9915&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر کرج:</b>
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
    if data == "nazrabad":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=35.9541&longitude=50.6061&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر نظر آباد:</b>
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
    if data == "taleqan":
        URL = "https://api.open-meteo.com/v1/forecast?latitude=36.1745&longitude=50.7691&hourly=temperature_2m"
        location = "delhi technologicaluniversity"
        PARAM = {"adress": location}
        info = requests.get(url=URL, params=PARAM)
        data = info.json()
        temps = data["hourly"]["temperature_2m"]
        return f"""<b>وضعیت دما در شهر طالقان:</b>
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
