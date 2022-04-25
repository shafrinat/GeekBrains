# Зарегистрироваться на https://openweathermap.org/api и написать функцию, которая получает погоду в данный
# момент для города, название которого получается через input. https://openweathermap.org/current

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
key = "OPENWEATHERMAP_KEY"
API_key = os.environ[key]
SAVE_FORECAST_PATH = "forecast.json"


def make_url(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
    return url


def make_forecast(url):
    response = requests.get(url).json()
    return response


def save_forecast(forecast, path):
    with open(path, "w") as f:
        json.dump(forecast, f, indent=2)


def pipeline(path):
    cityname = input("Input city name: ")
    url = make_url(cityname)
    forecast = make_forecast(url)
    save_forecast(forecast, path)


pipeline(SAVE_FORECAST_PATH)
