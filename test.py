import requests
import json

city = "Indianapolis"
country = "US"

api_key = "c048d46cbd48a21a01434f89363af3be"

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric')

weather_data = weather_url.json()