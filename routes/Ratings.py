from flask_restful import Resource
from controllers.get_ratings import get_ratings

class Ratings(Resource):
    def get(self):
        ratings = get_ratings()
        json_ratings = list()
        for rating in ratings:
            json_ratings.append(rating.__dict__)
        return json_ratings