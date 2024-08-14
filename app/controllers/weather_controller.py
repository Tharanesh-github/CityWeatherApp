#This file contains the route and controller logic for fetching weather data
from flask import Blueprint, request, jsonify
from app.services.weather_service import WeatherService

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_service = WeatherService()
    weather_data = weather_service.fetch_weather(city)
    
    if 'error' in weather_data:
        return jsonify(weather_data), 400
    
    return jsonify(weather_data)
