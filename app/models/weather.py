#This file defines weather model.
class Weather:
    def __init__(self, city, temperature, humidity, wind_speed, description):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.description = description

    def to_dict(self):
        return {
            'city': self.city,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'wind_speed': self.wind_speed,
            'description': self.description
        }
