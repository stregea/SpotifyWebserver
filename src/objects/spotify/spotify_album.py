from objects.spotify.spotify_artist import SpotifyArtist
from objects.spotify.spotify_external_urls import SpotifyExternalURLs
from objects.spotify.spotify_image import SpotifyImage
from objects.spotify.spotify_restrictions import SpotifyRestrictions
from objects.spotify.spotify_tracks import SpotifyTracks


class SpotifyAlbum:
    """
    Class to represent an album.

    More information about this object can be found here:
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album
    """
    def __init__(self, json_response: dict):
        """
        Construct an album from a response.
        :param json_response: The json response from the Spotify API.
        """

        # The type of the album.
        self.album_type: str = json_response['album_type'] if 'album_type' in json_response else None

        # The number of tracks on the album.
        self.total_tracks: int = json_response['total_tracks'] if 'total_tracks' in json_response else -1

        # The markets in which the album is available: ISO 3166-1 alpha-2 country codes.
        # NOTE: an album is considered available in a market when at least 1 of its tracks is available in that market.
        self.available_markets: [str] = json_response['available_markets'] if 'available_markets' in json_response else []

        # Known external URLs for this album.
        self.external_urls: [SpotifyExternalURLs] = [SpotifyExternalURLs(data) for data in json_response['external_urls']] if 'external_urls' in json_response else []

        # A link to the Web API endpoint providing full details of the album.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # The Spotify ID for the album.
        self.id: str = json_response['id'] if 'id' in json_response else None

        # The name of the album. In case of an album takedown, the value may be an empty string.
        self.images: [SpotifyImage] = [SpotifyImage(image) for image in json_response['images']] if 'images' in json_response else []

        # The name of the album. In case of an album takedown, the value may be an empty string.
        self.name: str = json_response['name'] if 'name' in json_response else None

        # The name of the album. In case of an album takedown, the value may be an empty string.
        self.release_date: str = json_response['release_date'] if 'release_date' in json_response else None

        # The precision with which release_date value is known.
        self.release_date_precision: str = json_response['release_date_precision'] if 'release_date_precision' in json_response else None

        # Included in the response when a content restriction is applied.
        self.restrictions: SpotifyRestrictions = SpotifyRestrictions(json_response['restrictions'])

        # The object type.
        self.type: str = json_response['type'] if 'type' in json_response else None

        # The Spotify URI for the album.
        self.uri: str = json_response['uri'] if 'uri' in json_response else None

        # The artists of the album.
        # Each artist object includes a link in href to more detailed information about the artist.
        self.artists: [SpotifyArtist] = [SpotifyArtist(artist) for artist in json_response['artists']] if 'artists' in json_response else []

        # The tracks of the album.
        self.tracks: SpotifyTracks = SpotifyTracks(json_response['tracks'])
