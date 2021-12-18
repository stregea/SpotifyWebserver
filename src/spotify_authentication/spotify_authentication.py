import base64, json, requests

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/?'
SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
RESPONSE_TYPE = 'code'
HEADER = 'application/x-www-form-urlencoded'
SCOPE = 'streaming user-read-birthdate user-read-email user-read-private'
REFRESH_TOKEN = ''

PORT = "5000"
HOST = "http://localhost"
CALLBACK_URI = f'{HOST}:{PORT}/callback/'

# TOKEN_DATA will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def get_user_authorization_uri(client_id: str) -> str:
    return f'{SPOTIFY_URL_AUTH}client_id={client_id}&response_type=code&redirect_uri={CALLBACK_URI}//&scope={SCOPE}'


def get_authorization_token(code: str, client_id: str, client_secret: str, redirect_uri: str) -> list:
    body = {
        "grant_type": 'authorization_code',
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    encoded = base64.b64encode(f'{client_id}:{client_secret}'.encode('ascii'))
    headers = {"Content-Type": HEADER, "Authorization": f"Basic {encoded}"}
    post = requests.post(SPOTIFY_URL_TOKEN, params=body, headers=headers)

    print(json.loads(post.text))
    return handle_token(json.loads(post.text))


def handle_token(response) -> list:
    auth_head = {"Authorization": "Bearer {}".format(response["access_token"])}
    REFRESH_TOKEN = response["refresh_token"]
    return [response["access_token"], auth_head, response["scope"], response["expires_in"]]


def refresh_authentication():
    body = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }

    post_refresh = requests.post(SPOTIFY_URL_TOKEN, data=body, headers=HEADER)
    post_back = json.dumps(post_refresh.text)

    return handle_token(post_back)


def get_user_token(code, client_id, client_secret):
    global TOKEN_DATA
    TOKEN_DATA = get_authorization_token(code, client_id, client_secret, CALLBACK_URI)


def refresh_token(time):
    time.sleep(time)
    TOKEN_DATA = refresh_authentication()


def get_access_token():
    return TOKEN_DATA
