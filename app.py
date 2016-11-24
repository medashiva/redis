from flask import Flask, jsonify
import os
from datetime import timedelta
import datetime
import redis

app = Flask("redis")

print("datainapp",dir(app))

@app.route("/")
def index():
	
    session_dict = {'id': 1, 'name': 'shiva'}
    redis_db.set('forgot_session', session_dict)
    print(redis_db.keys())
    return "hi"


@app.route("/redis")
def redises():
    redis_db.expireat('forgot_session', datetime.datetime.now() + timedelta(minutes=1))
    redis_db.expireat('full stack', datetime.datetime.now() + timedelta(minutes=1))
    print(redis_db.exists('forgot_session'))
    if redis_db.exists('forgot_session'):
        return "expire"
    else:
        return "Not Yet"


if __name__ == "__main__":
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    app.run(port=15420)
