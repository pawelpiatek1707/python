from flask import Flask
from flask_restful import Resource, Api
from routes.Links import Links
from routes.Movies import Movies
from routes.Links import Links
from routes.Ratings import Ratings

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')


if __name__ == '__main__':
    app.run(debug=True)