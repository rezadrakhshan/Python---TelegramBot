import requests

URL = 'https://api.open-meteo.com/v1/forecast?latitude=29.6103&longitude=52.5311&hourly=temperature_2m'

location = "delhi technologicaluniversity"

PARAM = {'address':location}

info = requests.get(url=URL,params=PARAM)

data = info.json()

temps = data["hourly"]["temperature_2m"]