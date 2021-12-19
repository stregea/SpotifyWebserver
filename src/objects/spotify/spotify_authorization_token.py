import base64
import time
import requests
import json
import os

# load in the server information.
SERVER_INFORMATION = json.loads(open(os.path.abspath('data/json/spotify_credentials.json'), 'r').read())

TOKEN_URI = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = f'{SERVER_INFORMATION["http"]}://{SERVER_INFORMATION["host"]}:{SERVER_INFORMATION["port"]}/callback/'


class SpotifyAuthorizationToken:

    def __init__(self, json_response: dict):
        """
        Construct an authorization token from Spotify.
        :param json_response: The json response from the Spotify API containing information for
        a SpotifyAuthorizationToken.
        """

        # An Access Token that can be provided in subsequent calls, for example to Spotify Web API services
        self._access_token: str = json_response['access_token'] if 'access_token' in json_response else None

        # How the Access Token may be used: always “Bearer”.
        self._token_type: str = json_response['token_type'] if 'token_type' in json_response else None

        # A space-separated list of scopes which have been granted for this access_token
        self._scope: str = json_response['scope'] if 'scope' in json_response else None

        # The time period (in seconds) for which the Access Token is valid
        self._expires_in: int = json_response['expires_in'] if 'expires_in' in json_response else -1

        # A token that can be sent to the Spotify Accounts service in place of an authorization code.
        # (When the access code expires, send a POST request to the Accounts service /api/token endpoint,
        # but use this code in place of an authorization code. A new Access Token will be returned.
        # A new refresh token might be returned too.)
        self._refresh_token: str = json_response['refresh_token'] if 'refresh_token' in json_response else None

        # The time at which this token will expire.
        self._expiration_time: float = time.time() + self._expires_in

    def get_access_token(self) -> str:
        """
        Get the access token associated with this SpotifyAuthorizationToken.
        :return: The access token.
        """
        return self._access_token

    def get_token_type(self) -> str:
        """
        Get the token type associated with this SpotifyAuthorizationToken.
        :return: The token type.
        """
        return self._token_type

    def get_scope(self) -> str:
        """
        Get the scope associated with this SpotifyAuthorizationToken.
        :return: The scope.
        """
        return self._scope

    def get_refresh_token(self) -> str:
        """
        Get the refresh token associated with this SpotifyAuthorizationToken.
        :return: The refresh token.
        """
        return self._refresh_token

    def is_expired(self) -> bool:
        """
        Determine if this instance of the token is expired or not.
        :return: True if the current time is passed the expiration time, False otherwise.
        """
        current_time: float = time.time()
        return current_time >= self._expiration_time

    def refresh(self, client_id: str, client_secret) -> None:
        """
        Refresh this authorization token.
        :param client_id: The id of the client.
        :param client_secret: The secret id of the client.
        """
        b64_str: bytes = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8'))

        # Build the JSON body that will be used for a POST request.
        headers: dict = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {str(b64_str, encoding="ascii")}'
        }
        body: dict = {
            'grant_type': 'refresh_token',
            'refresh_token': f'{self._refresh_token}'
        }

        response: dict = requests.post(TOKEN_URI, data=body, headers=headers).json()

        # Update the token. Note: We do not need to update the refresh_token
        self._access_token = response['access_token'] if 'access_token' in response else None
        self._token_type = response['token_type'] if 'token_type' in response else None
        self._scope = response['scope'] if 'scope' in response else None
        self._expires_in = response['expires_in'] if 'expires_in' in response else -1
        self._expiration_time = time.time() + self._expires_in


def create_authorization_token(code: str, client_id: str, client_secret) -> SpotifyAuthorizationToken:
    """
    Create an authorization token to be used within the client-side of the Spotify API.
    :param code: An authorization code receive from the Spotify API from a successful login.
    :param client_id: The id of the client.
    :param client_secret: The secret id of the client.
    :return: An authorization token created from the Spotify API.
    """

    # Build the JSON body that will be used for a POST request.
    b64_str: bytes = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8'))
    headers: dict = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {str(b64_str, encoding="ascii")}'
    }
    body: dict = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    # Perform a POST request to exchange the code for a token
    response: dict = requests.post(TOKEN_URI, data=body, headers=headers).json()

    return SpotifyAuthorizationToken(json_response=response)
