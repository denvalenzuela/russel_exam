from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Hello World!'


class Maps(Resource):
    def __init__(self):
        self.__url = "https://maps.googleapis.com/maps"
        self.__resource = {
            'search': '/api/place/textsearch/json',
            'photo': '/api/place/photo',
            'nearby': '/api/place/nearbysearch/json'
        }

    def get(self, keyword=""):        
        # need api key for google api
        url = self.__url + self.__resource.get(keyword, "")
        
        res = requests.get(url)
        retval = res.json()

        res = requests.get(url)
        retval = res.json()
        return retval

    def post(self):
        res = { 
            'id' : id,
            'status': 'Success',
            'total_count': 0
        }
        
        return res, 200

    def put(self):
        res = { 
            'id' : id,
            'status': 'Success',
            'total_count': 0
        }
        
        return res, 200

    def delete(self, id=0):
        res = { 
            'id' : id,
            'status': 'Success',
            'total_count': 0
        }
        
        return res, 200

api.add_resource(Maps, '/v1/maps', endpoint='map_get_post')
api.add_resource(Maps, '/v1/maps/<keyword>', endpoint='map_get_single') 

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)

