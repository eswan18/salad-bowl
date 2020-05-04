from flask import request
from flask_restful import Resource

from common.redis_connection import redis_connection as redis
from common.identifiers import random_id

class Game(Resource):

    def get(self, game_id):
        '''Get the current round of a given game.'''
        game_round = redis.get(f'game:{game_id}')
        if game_round is not None:
            return {'game_id': game_id, 'round': game_round}
        else:
            return {'error': f'game_id {game_id} does not exist'}, 404

    def post(self):
        '''Start a new game'''
        game_id = random_id()
        # Make sure that ID isn't in the database -- repick until a new one is
        # found.
        while redis.exists(f'game:{game_id}'):
            game_id = random_id()
        # Merge the game_id (list of characters) into a single string.
        game_id = ''.join(game_id)
        # Update Redis with that game, and note it as being in round 0 (meaning
        # it hasn't begun).
        redis.set(f'game:{game_id}', 0)
        return {'game_id': game_id}
