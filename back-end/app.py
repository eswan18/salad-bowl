import redis
from flask import Flask, request
from flask_restful import Api

from models import User

API_VERSION = '1'
API_URL_PREFIX = f'/api/v{API_VERSION}'

app = Flask(__name__)
api = Api(app)

r = redis.Redis(host='localhost',
                port=6379,
                db=0,
                decode_responses=True)

api.add_resource(User, f'{API_URL_PREFIX}/<string:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
