from database import Database

debug = False

if debug:
    import dht_emu as Adafruit_DHT
else:
    import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if (humidity is not None) and (temperature is not None):
    db = Database()
    db.rec_weather_data(temperature,humidity)
else:
    print 'Error reading data from sensor'
