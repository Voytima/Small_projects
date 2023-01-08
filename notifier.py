import datetime
import time
import requests
from plyer import notification

weather = None
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/105.0.0.0 Safari/537.36"}

params = {'q': 'Minsk',
          'appid': '9b8df2f38280ffbbc6803dd4cb6233e3'}

url = "https://api.openweathermap.org/data/2.5/weather"

try:
    response = requests.get(url, headers=headers, params=params)
except:
    print("Please! Check your internet connection")

if weather is not None:
    data = weather.json()['Success']

    while True:
        notification.notify(
            title="Weather Stats on {}".format(datetime.date.today()),
            message=f"In city {data.get('name')} temperature is {round(data.get('main').get('temp') - 273.15, 2)} "
                    f"grad Celsius and humidity is {data.get('main').get('humidity')}",
            app_icon="Paomedia-Small-N-Flat-Bell.ico",
            timeout=50
        )
        time.sleep(60 * 60 * 4)