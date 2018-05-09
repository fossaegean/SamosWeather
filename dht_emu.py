import json
import urllib2

LOCATION = 'id=256492'  # Samos
API_KEY = 'fbb8f37978c6c3340fdb9b41c0f4a8a6'  # Please register for an API key
WEATHER_API = 'http://api.openweathermap.org/data/2.5/weather?' + LOCATION + '&units=metric&appid=' + API_KEY


DHT11 = 11
DHT22 = 22


def read_retry(sensor, pin):
    print WEATHER_API
    data = urllib2.urlopen(WEATHER_API).read()
    temperature = json.loads(data)['main']['temp']
    humidity = json.loads(data)['main']['humidity']
    return humidity, temperature
