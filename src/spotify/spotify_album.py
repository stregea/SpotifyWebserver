from spotify.spotify_artist import SpotifyArtist
from spotify.spotify_external_urls import SpotifyExternalURLs
from spotify.spotify_image import SpotifyImage


class SpotifyAlbum:
    """
    Todo
    """
    def __init__(self, json_response: dict):
        """
        Construct an album from a response.
        :param json_response: The json response from the Spotify API.
        """
        self.album_type = json_response['album_type']
        self.total_tracks = json_response['total_tracks']
        self.available_markets = json_response['available_markets']
        self.external_urls = [SpotifyExternalURLs(data) for data in json_response['external_urls']]
        self.id = json_response['id']
        self.images = [SpotifyImage(image) for image in json_response['images']]
        self.name = json_response['name']
        self.release_date = json_response['release_date']
        self.release_date_precision = json_response['release_date_precision']
        self.restrictions = json_response['restrictions']
        self.type = json_response['type']
        self.uri = json_response['uri']
        self.artists = [SpotifyArtist(artist) for artist in json_response['artists']]
        self.tracks = json_response['tracks'] #todo: create object for this