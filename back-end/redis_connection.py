from flask import g, current_app
from redis import Redis

HOST = 'localhost'
PORT = 6379
DB = 0

def get_redis():
    if 'db' not in g:
        url = current_app.config['REDIS_URL']
        g.db = Redis.from_url(url, decode_responses=True)
        return g.db
    else:
        return g.db
        #(host=host,
        #                port=port,
        #                db=db,
        #                decode_responses=True)
