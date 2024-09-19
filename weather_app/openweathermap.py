import os
from dotenv import load_dotenv
import requests
load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather_by_id(city_id):
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def get_weather_by_name(city_name, country_code='CA'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data