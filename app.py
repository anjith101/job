from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        api_key = "c048d46cbd48a21a01434f89363af3be"

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric')

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)