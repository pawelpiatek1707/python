from flask_restful import Resource
from flask import jsonify
from controllers.get_movies import get_movies
from controllers.transform_to_json import transform_to_json

class Movies(Resource):
    def get(self):
        movies = get_movies()
        json_movies = list()
        for movie in movies:
            json_movies.append(movie.__dict__)
        return json_movies