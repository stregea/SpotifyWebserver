import base64

import flask
from flask import Flask, redirect, render_template, request
import os
import json
from objects.spotify.spotify_user import SpotifyUser
from objects.spotify.spotify_authorization_token import create_authorization_token

# load in the client id and secret id.
CLIENT_INFORMATION = json.loads(open(os.path.abspath('data/json/spotify_credentials.json'), 'r').read())

app = Flask(__name__)

SPOTIFY_USERS: dict[str: SpotifyUser] = {}  # make user id and auth token?

client_id = CLIENT_INFORMATION['client_id']
client_secret = CLIENT_INFORMATION['client_secret']
spotify_url_authorize = 'https://accounts.spotify.com/authorize/?'
encoded_redirect = 'http%3A%2F%2Flocalhost%3A5000%2Fcallback%2F'


@app.route('/')
@app.route('/index')
def index():  # put application's code here

    # check to determine if the session user is currently in the dictionary of users.
    try:
        SPOTIFY_USERS[flask.session['current_user_id']]
    except KeyError:
        # If not, take user to sign-in page to get access to a code that will be used to request an access token.
        response_type = 'code'
        scope = 'user-read-email%20user-read-private'
        state = '123'  # make random later

        redirect_uri = f'{spotify_url_authorize}client_id={client_id}&redirect_uri={encoded_redirect}&scope={scope}&response_type={response_type}&state={state}'
        return redirect(redirect_uri)

    return CLIENT_INFORMATION


# @app.route('/login')
# def login():
#     return render_template('login.html', client_information=CLIENT_INFORMATION)
#

@app.route('/callback/')
def callback():
    # have user sign-in here, may need a call-back page to store the session user information here.

    # get the Authorization code from Spotify API
    authorize = request.args.get('authorize')
    error = request.args.get('error')
    code = request.args.get('code')
    state = request.args.get('state')

    if code:
        print("first call back")

        # create access token
        token = create_authorization_token(code, client_id, client_secret)

        # need to assign token with user.
        # redirect user to home page...
        pass
    elif error:
        # redirect to a sorry page?
        pass
    elif authorize:
        # get and set access token for the current session user
        print("second call back")
        pass
    return 'callback'


if __name__ == '__main__':
    app.run()
