from objects.spotify.spotify_external_urls import SpotifyExternalURLs
from objects.spotify.spotify_followers import SpotifyFollowers
from objects.spotify.spotify_image import SpotifyImage
from objects.spotify.spotify_tracks import SpotifyTracks
from objects.spotify.spotify_user import SpotifyUser


class SpotifyPlaylist:
    """
    Class to represent a spotify playlist.

    More information about this object can be found here:
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist
    """

    def __init__(self, json_response: dict):
        """
        Construct a SpotifyPlaylist object from a response.
        :param json_response: The response from the Spotify API.
        """

        # True if the owner allows other users to modify the playlist.
        self.collaborative: bool = json_response['collaborative'] if 'collaborative' in json_response else False

        # The playlist description. Only returned for modified, verified playlists, otherwise null.
        self.description: str = json_response['description'] if 'description' in json_response else None

        # Known external URLs for this playlist.
        self.external_urls: SpotifyExternalURLs = SpotifyExternalURLs(json_response['external_urls']) if 'external_urls' in json_response else None

        # Information about the followers of the playlist.
        self.followers: SpotifyFollowers = SpotifyFollowers(json_response['followers']) if 'followers' in json_response else None

        # A link to the Web API endpoint providing full details of the playlist.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # The Spotify ID for the playlist.
        self.id: str = json_response['id'] if 'id' in json_response else None

        # Images for the playlist. The array may be empty or contain up to three images.
        # The images are returned by size in descending order.
        # See Working with Playlists (https://developer.spotify.com/documentation/general/guides/working-with-playlists/).
        # Note: If returned, the source URL for the image (url) is temporary and will expire in less than a day.
        self.images: [SpotifyImage] = [SpotifyImage(image) for image in json_response['images']] if 'images' in json_response else []

        # The name of the playlist.
        self.name: str = json_response['name'] if 'name' in json_response else None

        # The user who owns the playlist
        self.owner: SpotifyUser = SpotifyUser(json_response['owner']) if 'owner' in json_response else None

        # The playlist's public/private status: true the playlist is public, false the playlist is private,
        # null the playlist status is not relevant.
        # For more about public/private status, see Working with Playlists (https://developer.spotify.com/documentation/general/guides/working-with-playlists/).
        self.public: bool = json_response['public'] if 'public' in json_response else False

        # The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version
        self.snapshot_id: str = json_response['snapshot_id'] if 'snapshot_id' in json_response else None

        # The tracks of the playlist.
        self.tracks: SpotifyTracks = SpotifyTracks(json_response['tracks']) if 'tracks' in json_response else None

        # The object type: "playlist"
        self.type: str = json_response['type'] if 'type' in json_response else None

        # The Spotify URI for the playlist.
        self.uri: str = json_response['uri'] if 'uri' in json_response else None
