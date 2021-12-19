import flask
from flask import Flask, redirect, render_template, request
import os
import json
from src.objects.spotify.spotify_user import SpotifyUser
from src.objects.spotify.spotify_current_user import SpotifyCurrentUser, get_current_user
from src.objects.spotify.spotify_authorization_token import create_authorization_token, SpotifyAuthorizationToken
import urllib.parse

# load in the server information.
SERVER_INFORMATION = json.loads(open(os.path.abspath('data/json/spotify_credentials.json'), 'r').read())

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

SPOTIFY_USERS: dict[str: [SpotifyUser, SpotifyAuthorizationToken]] = {}

client_id = SERVER_INFORMATION['client_id']
client_secret = SERVER_INFORMATION['client_secret']

spotify_url_authorize = 'https://accounts.spotify.com/authorize/?'
encoded_redirect = urllib.parse.quote(f"https://{SERVER_INFORMATION['host']}:{SERVER_INFORMATION['port']}/callback/")


@app.route('/')
@app.route('/index')
def index():  # put application's code here

    # check to determine if the session user is currently in the dictionary of users.
    try:
        # Get the current session_user's id.
        session_user_id = json.loads(flask.session['current_user'])['id']

        # Update the session user's authentication token if it's expired.
        if SPOTIFY_USERS[session_user_id][1].is_expired():
            SPOTIFY_USERS[session_user_id][1].refresh(client_id=client_id, client_secret=client_secret)

        return render_template(
            'index.html',
            session_user_information=SPOTIFY_USERS[json.loads(flask.session['current_user'])['id']],
            user_json=json.loads(flask.session['current_user']),
            total_users=len(SPOTIFY_USERS)
        )
    except KeyError:
        # If not, take user to sign-in page to get access to a code that will be used to request an access token.
        response_type = 'code'
        scope = 'streaming%20user-read-email%20user-read-private'
        state = '123'  # make random later

        redirect_uri = f'{spotify_url_authorize}client_id={client_id}&redirect_uri={encoded_redirect}&scope={scope}&response_type={response_type}&state={state}'
        return redirect(redirect_uri)


@app.route('/callback/')
def callback_for_login():
    # have user sign-in here, may need a call-back page to store the session user information here.

    # get the Authorization code from Spotify API
    authorize = request.args.get('authorize')
    error = request.args.get('error')
    code = request.args.get('code')
    state = request.args.get('state')

    if code:
        # Create access token.
        token: SpotifyAuthorizationToken = create_authorization_token(code, client_id, client_secret)

        # Create the current user.
        current_user: SpotifyCurrentUser = get_current_user(token, client_id, client_secret)

        # Set the current user as the session user
        flask.session['current_user'] = current_user.to_json()

        # Add user to the current dictionary of users.
        SPOTIFY_USERS[current_user.id]: [SpotifyCurrentUser, SpotifyAuthorizationToken] = [current_user, token]

        # redirect user to home page.
        return redirect('/')
    elif error:
        # redirect to a sorry page?
        print("User hit 'cancel' for user access.")
        pass
    elif authorize:
        # get and set access token for the current session user
        print("second call back")
        pass
    return 'callback'


if __name__ == '__main__':
    context = (os.path.abspath(SERVER_INFORMATION['ssl_cert']), os.path.abspath(SERVER_INFORMATION['ssl_key']))
    app.run(host="0.0.0.0", port=SERVER_INFORMATION['port'], ssl_context=context)
