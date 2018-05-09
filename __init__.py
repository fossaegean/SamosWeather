from database import Database
from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

db = Database()


@app.route('/')
def get_weather():
    weather_data = db.get_weather_data()
    tm = time.strftime('%H:%M')
    return render_template('index.html', weather = weather_data, now = tm)


if __name__ == '__main__':
    app.run()
