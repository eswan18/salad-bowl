from flask import request
from flask_restful import Resource

class User(Resource):
    def get(self, user_id):
        return {'hello': 'world'}

    def put(self, user_id):
        return request.form['data']
    
    def post(self, user_id):
        return

    def delete(self, user_id):
        return
