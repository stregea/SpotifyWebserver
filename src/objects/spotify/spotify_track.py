from objects.spotify.spotify_album import SpotifyAlbum
from objects.spotify.spotify_artist import SpotifyArtist
from objects.spotify.spotify_external_ids import SpotifyExternalIDs
from objects.spotify.spotify_external_urls import SpotifyExternalURLs
from objects.spotify.spotify_restrictions import SpotifyRestrictions


class SpotifyTrack:
    """
    Class to represent a spotify track.

    More information about this object can be found here:
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track
    """

    def __init__(self, json_response):
        """
        Construct a SpotifyTrack object from a response.
        :param json_response: The response from the Spotify API.
        """

        # The album on which the track appears.
        # The album object includes a link in href to full information about the album.
        self.album: SpotifyAlbum = SpotifyAlbum(json_response['album']) if 'album' in json_response else None

        # The artists who performed the track.
        # Each artist object includes a link in href to more detailed information about the artist.
        self.artists: [SpotifyArtist] = [SpotifyArtist(artist) for artist in json_response['artists']] if 'artists' in json_response else None

        # A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code.
        self.available_markets: [str] = json_response['available_markets'] if 'available_markets' in json_response else None

        # The disc number (usually 1 unless the album consists of more than one disc).
        self.disc_number: int = json_response['disc_number'] if 'disc_number' in json_response else -1

        # The track length in milliseconds.
        self.duration_ms: int = json_response['duration_ms'] if 'duration_ms' in json_response else -1

        # Whether or not the track has explicit lyrics ( true = yes it does; false = no it does not OR unknown).
        self.explicit: bool = json_response['explicit'] if 'explicit' in json_response else False

        # Known external IDs for the track.
        self.external_ids: SpotifyExternalIDs = SpotifyExternalIDs(json_response['external_ids']) if 'external_ids' in json_response else None

        # Known external URLs for this track.
        self.external_urls: SpotifyExternalURLs = SpotifyExternalURLs(json_response['external_urls']) if 'external_urls' in json_response else None

        # A link to the Web API endpoint providing full details of the track.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # A link to the Web API endpoint providing full details of the track.
        self.id: str = json_response['id'] if 'id' in json_response else None

        # Part of the response when Track Relinking is applied. If true, the track is playable in the given market.
        # Otherwise false.
        self.is_playable: bool = json_response['is_playable'] if 'is_playable' in json_response else False

        # Part of the response when Track Relinking is applied, and the requested track has been replaced with
        # different track.
        # The track in the linked_from object contains information about the originally requested track.
        self.linked_from: SpotifyTrack = SpotifyTrack(json_response['linked_from']) if 'linked_from' in json_response and json_response['linked_from'] is not None else None

        # Included in the response when a content restriction is applied.
        self.restrictions: SpotifyRestrictions = SpotifyRestrictions(json_response['restrictions']) if 'restrictions' in json_response and json_response['restrictions'] is not None else None

        # The name of the track.
        self.name: str = json_response['name'] if 'name' in json_response else None

        # The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
        # The popularity of a track is a value between 0 and 100, with 100 being the most popular.
        # The popularity is calculated by algorithm and is based, in the most part,
        # on the total number of plays the track has had and how recent those plays are.
        # Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were
        # played a lot in the past.
        # Duplicate tracks (e.g. the same track from a single and an album) are rated independently.
        # Artist and album popularity is derived mathematically from track popularity.
        # Note: the popularity value may lag actual popularity by a few days: the value is not updated in real time.
        self.popularity: int = json_response['popularity'] if 'popularity' in json_response else None

        # A link to a 30 second preview (MP3 format) of the track. Can be null.
        self.preview_url: str = json_response['preview_url'] if 'preview_url' in json_response else None

        # The number of the track. If an album has several discs, the track number is the number on the specified disc.
        self.track_number: int = json_response['track_number'] if 'track_number' in json_response else None

        # The object type: "track".
        self.type: str = json_response['type'] if 'type' in json_response else None

        # The Spotify URI for the track.
        self.uri: str = json_response['uri'] if 'uri' in json_response else None

        # Whether or not the track is from a local file.
        self.is_local: bool = json_response['is_local'] if 'is_local' in json_response else None
