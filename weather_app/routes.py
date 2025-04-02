from flask import jsonify, request
from flask_restful import Resource
from weather_app import app, api
from weather_app.scrapper import weather_data, today_data

class Home(Resource):
    def get(self):
        return "Welcome to Weather Backend!"

api.add_resource(Home, "/")

class WeatherData(Resource):
    def get(self):
        return jsonify(weather_data)

api.add_resource(WeatherData, "/weather")

class TodayData(Resource):
    def get(self):
        return jsonify(today_data)

api.add_resource(TodayData, "/today_weather")