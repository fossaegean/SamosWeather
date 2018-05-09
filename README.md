# rpiWeather

## RaspberryPi setup

#### Install python pip:
```sh
$ sudo apt-get install python-pip -y
```

#### Install flask, pymysql, Adafruit_Python_DHT:
```sh
$ pip install flask
$ pip install pymysql
$ pip install Adafruit_Python_DHT
```

#### Set the crontab

Create a crontab
```sh
$ crontab -e
```
Set the sampling interval to 20 minutes (this will take a record every HH:00, HH:20, HH:40)
```
*/20 * * * * /usr/bin/python /path/to/weather_to_db.py
```


## Database setup

```mysql
CREATE DATABASE IF NOT EXISTS weather;
```

```mysql
CREATE TABLE IF NOT EXISTS weather.dht (`when` DATETIME, temperature TINYINT, humidity TINYINT, PRIMARY KEY (`when`));
```

## Hardware setup

Connect sensor pin 1 to RPi pin 1 (3.3V)  
Connect sensor pin 2 to RPi pin 7 (GPIO4)  
Connect sensor pin 4 to PRi pin 9 (GND)  
Connect a 10kΩ resistor between sensor pin 1 and 2 (pull-up resistor)  

For more information on DHTXX sensors refer to: [Adafruit documentation][Adafruit_DHTXX]


[Adafruit_DHTXX]: <https://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor>
