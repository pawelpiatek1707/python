from flask_restful import Resource
from controllers.get_movies import get_movies

class Movies(Resource):
    def get(self):
        movies = get_movies()
        json_movies = list()
        for movie in movies:
            json_movies.append(movie.__dict__)
        return json_movies