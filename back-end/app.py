import redis
from flask import Flask, Blueprint
from flask_restful import Api

from resources import User, Game, Word

API_VERSION = '1'
API_URL_PREFIX = f'/api/v{API_VERSION}'

app = Flask(__name__)
api_bp = Blueprint('api', __name__, url_prefix=API_URL_PREFIX)
api = Api(api_bp)

api.add_resource(User, '/user/<string:user_id>')
api.add_resource(Game, '/game', '/game/<string:game_id>')
api.add_resource(Word, '/word')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
