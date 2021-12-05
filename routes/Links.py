from flask_restful import Resource
from controllers.get_links import get_links

class Links(Resource):
    def get(self):
        links = get_links()
        json_links = list()
        for link in links:
            json_links.append(link.__dict__)
        return json_links