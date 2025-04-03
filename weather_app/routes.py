from flask import jsonify, request
from flask_restful import Resource
from weather_app import app, api
from weather_app.models import WeatherForecast, TodayWeather

class Home(Resource):
    def get(self):
        return "Welcome to Weather Backend!"

api.add_resource(Home, "/")

class WeatherForecastResource(Resource):
    def get(self):
        forecasts = WeatherForecast.query.all()
        result = []
        for forecast in forecasts:
            result.append({
                'day':forecast.day,
                'high_temp': forecast.high_temp,
                'low_temp': forecast.low_temp,
                'condition': forecast.condition,
                'rain_percentage': forecast.rain_percentage,
                'timestamp': forecast.timestamp
            })
        return jsonify(result)

api.add_resource(WeatherForecastResource, '/weather')

class TodayWeatherResource(Resource):
    def get(self):
        today_weather = TodayWeather.query.first()
        if today_weather:
            return {
                'day': today_weather.day,
                'sunrise': today_weather.sunrise,
                'sunset': today_weather.sunset,
                'highest_temp': today_weather.highest_temp,
                'lowest_temp': today_weather.lowest_temp,
                'wind_speed': today_weather.wind_speed,
                'humidity': today_weather.humidity,
                'dew_point': today_weather.dew_point,
                'pressure': today_weather.pressure,
                'uv_index': today_weather.uv_index,
                'visibility': today_weather.visibility,
                'moon_phase': today_weather.moon_phase
            }
        else:
            return "No data available for today's weather", 404

api.add_resource(TodayWeatherResource,'/today_weather')