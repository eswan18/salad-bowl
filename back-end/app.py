import redis
from flask import Flask, request
from flask_restful import Api

from models import User, Game

API_VERSION = '1'
API_URL_PREFIX = f'/api/v{API_VERSION}'

app = Flask(__name__)
api = Api(app)

api.add_resource(User, f'{API_URL_PREFIX}/user/<int:user_id>')
api.add_resource(Game, f'{API_URL_PREFIX}/game')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
