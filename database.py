import pymysql

# database credentials
import db_credentials
db_host = db_credentials.hostname
db_user = db_credentials.username
db_pass = db_credentials.password
db_name = 'weather'


# database functions
class Database:

    def connect(self, database=db_name):
        return pymysql.connect(host=db_host,
                               user=db_user,
                               passwd=db_pass,
                               db=database)

    def get_weather_data(self):
        connection = self.connect()
        try:
            query = 'SELECT `when`, temperature, humidity FROM dht order by `when` desc'
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchone()
                current_weather = {'when': data[0], 'temperature': data[1], 'humidity': data[2]}
            return current_weather
        except Exception as ex:
            print ex
            return {'when': 'error', 'temperature': 'error', 'humidity': 'error'}
        finally:
            connection.close()

    def rec_weather_data(self, temperature, humidity):
        connection = self.connect()
        try:
            query = 'INSERT INTO dht (`when`, temperature, humidity) VALUES (now(), %s, %s)'
            with connection.cursor() as cursor:
                cursor.execute(query, (temperature, humidity))
                connection.commit()
        except Exception as ex:
            print ex
        finally:
            connection.close()
