from flask import request
from flask_restful import Resource

from .identifiers import random_id 
from .redis_connection import redis_connection as redis

class Game(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        '''Start a new game'''
        game_id = random_id()
        # Make sure that ID isn't in the database -- repick until a new one is
        # found.
        while redis.exists(f'game:{game_id}'):
            game_id = random_id()
        # Merge the game_id (list of characters) into a single string.
        game_id = ''.join(game_id)
        return {'game_id': game_id}

    def delete(self):
        return
