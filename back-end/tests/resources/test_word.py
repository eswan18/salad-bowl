import random
import string

import pytest

API_URL_PREFIX = '/api/v1/word'

def test_get_fails(client):
    '''
    GIVEN
        Any database state
    WHEN
        A GET request is issued to the API's word resource
    THEN
        The response is an error -- 405: Method not allowed
        There is no change in the database

    The word resource does not support GET requests.
    '''
    response = client.get(API_URL_PREFIX)
    assert response.status_code == 405

def test_post_fails_when_game_doesnt_exist(client):
    '''
    GIVEN
        The database does not contain a certain game ID
    WHEN
        A new word is posted to the API with that game ID
    THEN
        The response is an error -- 404: Not Found
        There is no change in the database

    Words are meant to be submitted to games that have already been created.
    '''
    response = client.post(API_URL_PREFIX,
                           json={'word': 'ethan', 'game_id': 'NOGAME'})
    assert response.status_code == 404

@pytest.mark.xfail()
@pytest.mark.parametrize('game_round', [1, 2, 3])
def test_post_fails_when_game_has_started(client, game_round):
    '''
    GIVEN
        The database has a certain game ID and that game is in round 1, 2, or 3
    WHEN
        A new word is posted to the API with that game ID.
    THEN
        The response is an error -- 403: Forbidden
        There is no change in the database

    Words can only be submitted before the game has begun, when the game is in
    round 0.
    '''
    assert response.status_code == 403


@pytest.mark.xfail()
def test_valid_post_succeeds(client):
    '''
    GIVEN
        The database contains a certain game ID
        That game ID is recorded as being in round 0
        That game contains no words
    WHEN
        A new word is posted to the API with that game ID
    THEN
        The response is success -- 200
        There is a new entry in the database with that word in the game ID

    Words can be added to games that exist and are in round 0, so long as the
    word doesn't already exist in that game.
    '''
    assert response.status_code == 200
