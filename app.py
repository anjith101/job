#import frameworks and libreries
from flask import Flask, render_template, request
import requests
import json
#create flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def result():

    city = request.form['city']
    api_key = "c048d46cbd48a21a01434f89363af3be"

    weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric')

    weather_data = weather_url.json()


    return render_template("result.html",weather = weather_data)


if __name__ == '__main__':
    app.run(debug=True)