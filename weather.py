from database import Database
from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

db = Database()


@app.route('/')
def get_weather():
    weather_data = db.get_weather_data()
    mytime = time.strftime('%A %B, %d %Y %H:%M:%S')
    return render_template('index.html', weather = weather_data, servertime = mytime)


if __name__ == '__main__':
    app.run()

