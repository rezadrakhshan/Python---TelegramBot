import requests

URL = 'https://api.open-meteo.com/v1/forecast?latitude=35.8327&longitude=50.9915&hourly=temperature_2m&timezone=Europe%2FMoscow'

location = "delhi technologicaluniversity"

PARAM = {'address':location}

info = requests.get(url=URL,params=PARAM)

data = info.json()

temps = data["hourly"]["temperature_2m"]