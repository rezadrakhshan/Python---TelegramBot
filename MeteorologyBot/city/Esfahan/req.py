import requests

URL = 'https://api.open-meteo.com/v1/forecast?latitude=32.6525&longitude=51.6746&hourly=temperature_2m'

location = "delhi technologicaluniversity"

PARAM = {'address':location}

info = requests.get(url=URL,params=PARAM)

data = info.json()

temps = data["hourly"]["temperature_2m"]