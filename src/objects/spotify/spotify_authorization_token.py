import base64
import time
import requests

TOKEN_URI = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = 'http://localhost:5000/callback/'


class SpotifyAuthorizationToken:

    def __init__(self, json_response: dict):
        """
        Construct an authorization token from Spotify.
        :param json_response: The json response from the Spotify API containing information for
        a SpotifyAuthorizationToken.
        """

        # An Access Token that can be provided in subsequent calls, for example to Spotify Web API services
        self.access_token: str = json_response['access_token'] if 'access_token' in json_response else None

        # How the Access Token may be used: always “Bearer”.
        self.token_type: str = json_response['token_type'] if 'token_type' in json_response else None

        # A space-separated list of scopes which have been granted for this access_token
        self.scope: str = json_response['scope'] if 'scope' in json_response else None

        # The time period (in seconds) for which the Access Token is valid
        self.expires_in: int = json_response['expires_in'] if 'expires_in' in json_response else -1

        # A token that can be sent to the Spotify Accounts service in place of an authorization code.
        # (When the access code expires, send a POST request to the Accounts service /api/token endpoint,
        # but use this code in place of an authorization code. A new Access Token will be returned.
        # A new refresh token might be returned too.)
        self.refresh_token: str = json_response['refresh_token'] if 'refresh_token' in json_response else None

        # The time at which this token will expire.
        self.__expiration_time: float = time.time() + self.expires_in

    def is_expired(self) -> bool:
        """
        Determine if this instance of the token is expired or not.
        :return: True if the current time is passed the expiration time, False otherwise.
        """
        return time.time() >= self.__expiration_time

    def update_token(self, client_id: str, client_secret):
        b64_str = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8'))

        # Build the JSON body that will be used for a POST request.
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {str(b64_str, encoding="ascii")}'
        }
        body = {
            'grant_type': 'refresh_token',
            'refresh_token': f'{self.refresh_token}'
        }

        json_response = requests.post(TOKEN_URI, data=body, headers=headers).json()

        # Update the token. Note: We do not need to update the refresh_token
        self.access_token = json_response['access_token'] if 'access_token' in json_response else None
        self.token_type = json_response['token_type'] if 'token_type' in json_response else None
        self.scope = json_response['scope'] if 'scope' in json_response else None
        self.expires_in = json_response['expires_in'] if 'expires_in' in json_response else -1
        self.__expiration_time = time.time() + self.expires_in


def create_authorization_token(code: str, client_id: str, client_secret) -> SpotifyAuthorizationToken:
    """
    Create an authorization token to be used within the client-side of the Spotify API.
    :param code: An authorization code receive from the Spotify API from a successful login.
    :param client_id: The id of the client.
    :param client_secret: The secret id of the client.
    :return: An authorization token created from the Spotify API.
    """

    # Build the JSON body that will be used for a POST request.
    b64_str = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8'))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {str(b64_str, encoding="ascii")}'
    }
    body = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    # Perform a POST request to exchange the code for a token
    response = requests.post(TOKEN_URI, data=body, headers=headers)

    # return a constructed SpotifyAuthorizationToken
    return SpotifyAuthorizationToken(json_response=response.json())
