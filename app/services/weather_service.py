# app/services/weather_service.py

import requests
from app.models.weather import Weather
from app.utils.cache import SimpleCache

class WeatherService:
    def __init__(self):
        self.api_key = '2b1b3c4389b5475aa2c145524241108'
        self.base_url = 'http://api.weatherapi.com/v1/current.json'
        self.cache = SimpleCache()

    def fetch_weather(self, city):
        cached_data = self.cache.get(city)
        if cached_data:
            return cached_data

        params = {
            'q': city,
            'key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        
        print(f"Response Status: {response.status_code}")
        print(f"Response Content: {response.text}")

        if response.status_code != 200:
            return {'error': 'Failed to fetch weather data'}
        
        data = response.json()
        weather = Weather(
            city=data['location']['name'],
            temperature=data['current']['temp_c'],
            humidity=data['current']['humidity'],
            wind_speed=data['current']['wind_kph'],
            description=data['current']['condition']['text']
        )
        self.cache.set(city, weather.to_dict())
        return weather.to_dict()
