from flask import request
from flask_restful import Resource

from .identifiers import random_id 

class Word(Resource):

    def __init__(self, redis):
        self.redis = redis

    def post(self):
        '''Submit a new word.'''
        data = request.json
        if data is None:
            return {'error': 'No JSON payload'}, 400
        word, game_id = data['word'], data['game_id']
        # Be sure that game exists and hasn't begun (so is in round 0).
        game_round = self.redis.get(f'game:{game_id}')
        if game_round is None:
            return {'error': f'No such game_id {game_id}'}, 404
        elif game_round in ['1', '2', '3']:
            return {'error': f'Game has already begun'}, 403
        elif game_round != '0':
            # Any other value for game_round would be unexpected
            msg = 'Unexpected game_round in database'
            raise ValueError(msg)
        round_key = f'round:{game_id}-0'
        # Check if the word has already been submitted.
        if self.redis.sismember(round_key, word):
            return {'error': f'Duplicate word'}, 409
        # Assuming the game and word are valid, add the word to the DB.
        self.redis.sadd(round_key, word)
        return {'game_id': game_id, 'round': 0, 'word': word}

    def delete(self):
        return
