from flask import jsonify, request
from flask_restful import Resource
from weather_app import app, api

class Home(Resource):
    def get(self):
        return "Welcome to Weather Backend!"

api.add_resource(Home, "/")