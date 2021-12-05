from flask_restful import Resource
from controllers.get_tags import get_tags

class Tags(Resource):
    def get(self):
        tags = get_tags()
        json_tags = list()
        for tag in tags:
            json_tags.append(tag.__dict__)
        return json_tags