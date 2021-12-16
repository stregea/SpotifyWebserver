from flask import Flask
import os
import json

CLIENT_INFORMATION = json.loads(open(os.path.abspath('data/json/spotify_credentials.json'), 'r').read())

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return CLIENT_INFORMATION


@app.route('/login')
def login():
    return "login here"


if __name__ == '__main__':
    app.run()
