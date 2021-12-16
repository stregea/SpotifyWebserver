from spotify.spotify_external_urls import SpotifyExternalURLs
from spotify.spotify_followers import SpotifyFollowers
from spotify.spotify_image import SpotifyImage


class SpotifyArtist:
    """
    Object representing an artist.
    """

    def __init__(self, json_response: dict):
        """
        Construct an Artist object from a response.

        More information about this object can be found here:
        https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist

        :param json_response: The response from the Sport
        """
        self.external_urls = SpotifyExternalURLs(json_response['external_urls'])
        self.followers = SpotifyFollowers(json_response['followers'])
        self.genres = json_response['genres']
        self.href = json_response['href']
        self.id = json_response['id']
        self.images = [SpotifyImage(image) for image in json_response['images']]
        self.name = json_response['name']
        self.popularity = json_response['popularity']
        self.type = json_response['type']
        self.uri = json_response['uri']
