import json

from src.objects.spotify.spotify_external_urls import SpotifyExternalURLs
from src.objects.spotify.spotify_followers import SpotifyFollowers
from src.objects.spotify.spotify_image import SpotifyImage


class SpotifyUser:
    """
    Class that will represent a signed-in user from the Spotify API.
    """

    def __init__(self, json_response: dict):
        """
        Construct a user from a response.
        :param json_response: The json response from the Spotify API.
        """

        # The name displayed on the user's profile. null if not available.
        self.display_name: str = json_response['display_name'] if 'display_name' in json_response else None

        # Known external URLs for this user.
        self.external_urls: SpotifyExternalURLs = SpotifyExternalURLs(json_response['external_urls']) if 'external_urls' in json_response and json_response['external_urls'] is not None else None

        # Information about the followers of the user.
        self.followers: SpotifyFollowers = SpotifyFollowers(json_response['followers']) if 'followers' in json_response and json_response['followers'] is not None else None

        # A link to the Web API endpoint for this user.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # The Spotify user ID for the user.
        self.id: str = json_response['id'] if 'id' in json_response else None

        # The user's profile image.
        self.images: [SpotifyImage] = [SpotifyImage(image) for image in json_response['images']] if 'images' in json_response and json_response['images'] is not None else []

        # The object type: "user"
        self.type: str = json_response['type'] if 'type' in json_response else None

        # The Spotify URI for the user.
        self.uri: str = json_response['uri'] if 'uri' in json_response else None

    def to_json(self) -> str:
        """
        Convert this user to a JSON representation.
        :return: A JSON representation of a user.
        """
        return json.dumps(self, default=lambda o: o.__dict__)
