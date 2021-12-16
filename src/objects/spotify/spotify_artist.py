from objects.spotify.spotify_external_urls import SpotifyExternalURLs
from objects.spotify.spotify_followers import SpotifyFollowers
from objects.spotify.spotify_image import SpotifyImage


class SpotifyArtist:
    """
    Class to represent an artist.

    More information about this object can be found here:
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist
    """

    def __init__(self, json_response: dict):
        """
        Construct an Artist object from a response.
        :param json_response: The response from the Spotify API.
        """
        # Known external URLs for this artist.
        self.external_urls: SpotifyExternalURLs = SpotifyExternalURLs(json_response['external_urls'])

        # Information about the followers of the artist.
        self.followers: SpotifyFollowers = SpotifyFollowers(json_response['followers'])

        # A list of the genres the artist is associated with. If not yet classified, the array is empty.
        self.genres: [str] = json_response['genres'] if 'genres' in json_response else []

        # A link to the Web API endpoint providing full details of the artist.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # A link to the Web API endpoint providing full details of the artist.
        self.id: str = json_response['id'] if 'id' in json_response else None

        # Images of the artist in various sizes, the widest first.
        self.images: [SpotifyImage] = [SpotifyImage(image) for image in json_response['images']]

        # The name of the artist.
        self.name: str = json_response['name'] if 'name' in json_response else None

        # The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular.
        # The artist's popularity is calculated from the popularity of all the artist's tracks.
        self.popularity: int = json_response['popularity'] if 'popularity' in json_response else -1

        # The objects type.
        self.type: str = json_response['type'] if 'type' in json_response else None

        # The Spotify URI for the artist.
        self.uri: str = json_response['uri'] if 'uri' in json_response else None
