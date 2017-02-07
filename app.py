from flask import Flask, jsonify
import redis
import json

app = Flask("redistest")


@app.route("/")
def index():
    
    #value to save in redis 
    value_to_set = "shiva"
    #set value to key
    redis_db.set('name', value_to_set)   
    return json.dumps(redis_db.keys())



if __name__ == "__main__":
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    app.run(port=15420)
