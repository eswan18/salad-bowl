from app import app as _app
import pytest

TEST_REDIS_URL = 'redis://localhost:6379/1'

@pytest.fixture
def app():
    return _app

@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    app.config['REDIS_URL'] = TEST_REDIS_URL
    with app.test_client() as client:
        yield client
